@echo off
title DL Training & DeepVision AI Studio
echo =========================================================================
echo    🚀 Deep Learning Training & DeepVision AI Studio Hub
echo =========================================================================
echo.
echo Starting Streamlit web application (app.py)...
python -m streamlit run app.py
if errorlevel 1 (
    streamlit run app.py
)
pause
