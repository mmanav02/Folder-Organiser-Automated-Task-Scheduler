@echo off

REM Delete the Scheduled task named "SortItOut"
schtasks /delete /tn "SortItOut" /f