@echo off
echo Organizing project structure...

REM Create backend directory
if not exist "backend" mkdir backend
echo Created backend directory

REM Move backend-related files
if exist "src" (
    if not exist "backend\src" mkdir "backend\src"
    robocopy "src" "backend\src" /E /MOVE
    rmdir "src"
)
if exist "requirements.txt" move "requirements.txt" "backend\"
if exist "requirements-dev.txt" move "requirements-dev.txt" "backend\"
if exist "tests" (
    robocopy "tests" "backend\tests" /E /MOVE
    rmdir "tests"
)
if exist "README.md" (
    REM Check if this README is for backend
    findstr /C:"FastAPI\|backend\|SQLModel\|Todo" "README.md" >nul
    if not errorlevel 1 move "README.md" "backend\"
)
if exist "initialize_db.py" move "initialize_db.py" "backend\"
if exist "test_db_connection.py" move "test_db_connection.py" "backend\"
if exist "test_psycopg2.py" move "test_psycopg2.py" "backend\"
if exist "todo_app.db" move "todo_app.db" "backend\"

REM Create frontend directory
if not exist "frontend" mkdir frontend
echo Created frontend directory

REM Move frontend-related files
if exist "package.json" move "package.json" "frontend\"
if exist "package-lock.json" move "package-lock.json" "frontend\"
if exist "next.config.js" move "next.config.js" "frontend\"
if exist "next-env.d.ts" move "next-env.d.ts" "frontend\"
if exist "postcss.config.js" move "postcss.config.js" "frontend\"
if exist "tailwind.config.js" move "tailwind.config.js" "frontend\"
if exist "tsconfig.json" move "tsconfig.json" "frontend\"
if exist "src" robocopy "src" "frontend\src" /E /MOVE
if exist "srctypes" robocopy "srctypes" "frontend\srctypes" /E /MOVE
if exist ".env" move ".env" "frontend\"
if exist ".gitignore" move ".gitignore" "frontend\"
if exist "node_modules" robocopy "node_modules" "frontend\node_modules" /E /MOVE
if exist ".next" robocopy ".next" "frontend\.next" /E /MOVE
if exist "specs" robocopy "specs" "frontend\specs" /E /MOVE
if exist "history" robocopy "history" "frontend\history" /E /MOVE
if exist "tasks.md" move "tasks.md" "frontend\"
if exist ".specify" robocopy ".specify" "frontend\.specify" /E /MOVE
if exist ".cloud" robocopy ".cloud" "frontend\.cloud" /E /MOVE
if exist "CLAUDE.md" move "CLAUDE.md" "frontend\"

REM Create root package.json
echo {
echo   "name": "fullstack-todo-app",
echo   "version": "1.0.0",
echo   "description": "Full-stack todo application with separate frontend and backend",
echo   "scripts": {
echo     "dev": "concurrently \"npm run dev:frontend\" \"npm run dev:backend\"",
echo     "dev:frontend": "cd frontend && npm run dev",
echo     "dev:backend": "cd backend && python -m uvicorn src.main:app --reload --port 8000",
echo     "build": "npm run build:frontend && npm run build:backend",
echo     "build:frontend": "cd frontend && npm run build",
echo     "build:backend": "echo 'Backend build not needed'",
echo     "start": "concurrently \"npm run start:frontend\" \"npm run start:backend\"",
echo     "start:frontend": "cd frontend && npm start",
echo     "start:backend": "cd backend && python -m uvicorn src.main:app --host 0.0.0.0 --port 8000"
echo   },
echo   "devDependencies": {
echo     "concurrently": "^8.2.0"
echo   }
echo } > package.json
echo Created root package.json

REM Create root README
echo # Full Stack Todo Application > README.md
echo. >> README.md
echo This is a full-stack todo application with separate frontend and backend components. >> README.md
echo. >> README.md
echo ## Project Structure >> README.md
echo. >> README.md
echo ``` >> README.md
echo ├── backend/          # FastAPI backend >> README.md
echo ^|   ├── src/          # Backend source code >> README.md
echo ^|   ├── requirements.txt >> README.md
echo ^|   └── ... >> README.md
echo ├── frontend/         # Next.js frontend >> README.md
echo ^|   ├── src/ >> README.md
echo ^|   ├── package.json >> README.md
echo ^|   └── ... >> README.md
echo └── README.md >> README.md
echo ``` >> README.md
echo. >> README.md
echo ## Setup Instructions >> README.md
echo. >> README.md
echo 1. **Backend Setup**: >> README.md
echo    ^```bash >> README.md
echo    cd backend >> README.md
echo    pip install -r requirements.txt >> README.md
echo    python initialize_db.py >> README.md
echo    ^``` >> README.md
echo. >> README.md
echo 2. **Frontend Setup**: >> README.md
echo    ^```bash >> README.md
echo    cd frontend >> README.md
echo    npm install >> README.md
echo    ^``` >> README.md
echo. >> README.md
echo ## Running the Application >> README.md
echo. >> README.md
echo ### Option 1: Run separately >> README.md
echo - **Backend**: `cd backend ^&^& uvicorn src.main:app --reload --port 8000` >> README.md
echo - **Frontend**: `cd frontend ^&^& npm run dev` >> README.md
echo. >> README.md
echo ### Option 2: Run together ^(from root^) >> README.md
echo ^```bash >> README.md
echo npm install >> README.md
echo npm run dev >> README.md
echo ^``` >> README.md
echo. >> README.md
echo ## Environment Variables >> README.md
echo. >> README.md
echo ### Backend ^(.env in backend/^) >> README.md
echo ^``` >> README.md
echo DATABASE_URL=sqlite:///./todo_app.db >> README.md
echo AUTH_SECRET=your-secret-key >> README.md
echo FRONTEND_URL=http://localhost:3000 >> README.md
echo ^``` >> README.md
echo. >> README.md
echo ### Frontend ^(.env in frontend/^) >> README.md
echo ^``` >> README.md
echo NEXT_PUBLIC_API_URL=http://localhost:8000 >> README.md
echo ^``` >> README.md
echo. >> README.md
echo Created root README.md

echo.
echo Project structure organized successfully!
echo.
echo Next steps:
echo 1. Check the new structure in the backend/ and frontend/ directories
echo 2. Update environment variables in both directories
echo 3. Run 'npm install' in the root directory
echo 4. Run 'npm run dev' to start both servers