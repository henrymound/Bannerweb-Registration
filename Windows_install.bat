@echo off
set curpath=%~d0%~p0

echo %curpath%

pushd %curpath%\Dist

@ msiexec.exe /i .\python-2.7.8.msi /QN /L*V "C:\Temp\msilog.log"
Start python-2.7.8.msi
echo Press enter when done installing python
pause

C:\Python27\python.exe ez_install_setup.py

C:\Python27\Scripts\easy_install.exe mechanize
C:\Python27\python Midd_Script.py

popd 
pause