"""
Script to initialize the database tables
"""

import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from sqlmodel import SQLModel
from config.database import engine
from models.user import User
from models.todo import Todo

def create_tables():
    """Create all database tables"""
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()