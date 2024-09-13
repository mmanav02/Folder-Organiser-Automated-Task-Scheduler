@echo off

REM Define paths
set SCRIPT_PATH=D:\Code\Projects\Folder_Organizer\SortItOut.py

REM Create task to run the Python script every minute
schtasks /create /tn "SortItOut" /tr %SCRIPT_PATH% /sc minute /mo 1 /rl highest /f