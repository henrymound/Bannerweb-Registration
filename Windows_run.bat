@echo off
set curpath=%~d0%~p0

echo %curpath%

pushd %curpath%\Dist
C:\Python27\python Midd_Script.py

popd
pause
=======
pause
