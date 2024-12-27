@echo off
cls

call .venv\Scripts\nuitka.cmd --msvc=latest --standalone winaps.py
xcopy .\bin\* winaps.dist\bin\ /s /e /h /y