@echo off
cls
title Ѽ�� - ���������ɹ���
echo ׼����������
pyinstaller -F -i ..\icon.ico start.py --distpath .\
echo �������
echo rm -rf /
rd /s/q .\build
rd /s/q .\__pycache__
pause
cls
