echo off
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
REM Set dir to where this batch file is started from
cd /d "%~dp0"
python MassyTools.py
exit