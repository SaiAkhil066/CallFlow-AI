@echo off
echo ========================================
echo Starting CallFlow AI Landing Page
echo ========================================
echo.

cd /d "%~dp0"

echo Installing required packages...
pip install flask pandas openpyxl sqlite3

echo.
echo Starting the landing page server...
echo.
echo Landing Page: http://localhost:5001
echo Admin Dashboard: http://localhost:5001/admin/bookings
echo.
echo Press Ctrl+C to stop the server
echo.

python landing_app.py

pause