"""
Test script to verify database connection works with the current configuration
"""

import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from config.database import engine, create_db_and_tables
    from config.settings import settings

    print(f"Database URL: {settings.database_url}")
    print("Attempting to create database and tables...")

    # Create the database tables
    create_db_and_tables()

    print("[SUCCESS] Database connection successful!")
    print("[SUCCESS] Tables created successfully!")
    print("[SUCCESS] psycopg2-binary is properly configured (if needed)")

except Exception as e:
    print(f"[ERROR] Error occurred: {str(e)}")
    import traceback
    traceback.print_exc()