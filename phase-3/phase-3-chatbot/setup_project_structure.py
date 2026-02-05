import os
import shutil
from pathlib import Path

def organize_project():
    """
    Organize the project into proper frontend and backend structures
    """
    print("Organizing project structure...")

    # Current directory is phase-2
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")

    # Create backend directory if it doesn't exist
    backend_dir = current_dir / "backend"
    if not backend_dir.exists():
        backend_dir.mkdir(exist_ok=True)
        print(f"Created: {backend_dir}")

    # Move existing backend files to backend directory
    backend_files = [
        "src", "requirements.txt", "requirements-dev.txt",
        "tests", "README.md", "initialize_db.py",
        "test_db_connection.py", "test_psycopg2.py", "todo_app.db"
    ]

    for file in backend_files:
        source = current_dir / file
        dest = backend_dir / file
        if source.exists():
            if dest.exists() and dest.is_dir():
                # If destination exists and is a directory, merge contents
                for item in source.iterdir():
                    item.rename(dest / item.name)
                source.rmdir()
            else:
                source.rename(dest)
            print(f"Moved {file} to backend/")

    # Create frontend directory
    frontend_dir = current_dir / "frontend"
    if not frontend_dir.exists():
        frontend_dir.mkdir(exist_ok=True)
        print(f"Created: {frontend_dir}")

    # Move frontend-related files to frontend directory
    frontend_files = [
        "package.json", "package-lock.json", "next.config.js",
        "next-env.d.ts", "postcss.config.js", "tailwind.config.js",
        "tsconfig.json", "src", "srctypes", ".env", ".gitignore",
        "node_modules", ".next", "README.md", "specs", "history",
        "tasks.md", ".specify", ".cloud", "CLAUDE.md"
    ]

    for file in frontend_files:
        source = current_dir / file
        dest = frontend_dir / file
        if source.exists():
            if dest.exists() and dest.is_dir():
                # If destination exists and is a directory, merge contents
                for item in source.iterdir():
                    item.rename(dest / item.name)
                source.rmdir()
            else:
                source.rename(dest)
            print(f"Moved {file} to frontend/")

    # Create a new root package.json that can manage both
    root_package_json = current_dir / "package.json"
    if not root_package_json.exists():
        root_package_content = {
            "name": "fullstack-todo-app",
            "version": "1.0.0",
            "description": "Full-stack todo application with separate frontend and backend",
            "scripts": {
                "dev": "concurrently \"npm run dev:frontend\" \"npm run dev:backend\"",
                "dev:frontend": "cd frontend && npm run dev",
                "dev:backend": "cd backend && python -m uvicorn src.main:app --reload --port 8000",
                "build": "npm run build:frontend && npm run build:backend",
                "build:frontend": "cd frontend && npm run build",
                "build:backend": "echo 'Backend build not needed'",
                "start": "concurrently \"npm run start:frontend\" \"npm run start:backend\"",
                "start:frontend": "cd frontend && npm start",
                "start:backend": "cd backend && python -m uvicorn src.main:app --host 0.0.0.0 --port 8000"
            },
            "devDependencies": {
                "concurrently": "^8.2.0"
            },
            "workspaces": [
                "frontend",
                "backend"
            ]
        }

        import json
        with open(root_package_json, 'w') as f:
            json.dump(root_package_content, f, indent=2)
        print("Created root package.json with scripts for managing both frontend and backend")

    # Create a root README
    root_readme = current_dir / "README.md"
    if not root_readme.exists():
        readme_content = """# Full Stack Todo Application

This is a full-stack todo application with separate frontend and backend components.

## Project Structure

```
├── backend/          # FastAPI backend
│   ├── src/          # Backend source code
│   ├── requirements.txt
│   └── ...
├── frontend/         # Next.js frontend
│   ├── src/
│   ├── package.json
│   └── ...
└── README.md
```

## Setup Instructions

1. **Backend Setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python initialize_db.py
   ```

2. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   ```

## Running the Application

### Option 1: Run separately
- **Backend**: `cd backend && uvicorn src.main:app --reload --port 8000`
- **Frontend**: `cd frontend && npm run dev`

### Option 2: Run together (from root)
```bash
npm install
npm run dev
```

## Environment Variables

### Backend (.env in backend/)
```
DATABASE_URL=sqlite:///./todo_app.db
AUTH_SECRET=your-secret-key
FRONTEND_URL=http://localhost:3000
```

### Frontend (.env in frontend/)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```
"""
        with open(root_readme, 'w') as f:
            f.write(readme_content)
        print("Created root README.md")

    print("\nProject structure organized successfully!")
    print("\nNext steps:")
    print("1. Check the new structure in the backend/ and frontend/ directories")
    print("2. Update environment variables in both directories")
    print("3. Run 'npm install' in the root directory")
    print("4. Run 'npm run dev' to start both servers")

if __name__ == "__main__":
    organize_project()