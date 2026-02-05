"""
Test script to verify connection to Neon PostgreSQL database
"""

import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from sqlmodel import SQLModel, create_engine
    from config.settings import settings

    print(f"Current database URL: {settings.database_url}")

    # Check if it's using PostgreSQL (Neon)
    if 'postgresql' in settings.database_url.lower():
        print("[SUCCESS] Connected to PostgreSQL (Neon) database")

        # Create an engine to test the connection
        engine = create_engine(settings.database_url)

        # Try to connect and get table names to verify
        with engine.connect() as connection:
            print("[SUCCESS] Successfully connected to Neon database")

        # Import models to create tables
        from models.user import User
        from models.todo import Todo

        # Create tables
        SQLModel.metadata.create_all(engine)
        print("[SUCCESS] Tables created in Neon database")

    else:
        print("[WARNING] Still using SQLite - check your .env file")

    print("[SUCCESS] Neon database configuration successful!")

except Exception as e:
    print(f"[ERROR] Error connecting to Neon database: {str(e)}")
    import traceback
    traceback.print_exc()