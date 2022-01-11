@echo off
cls
title 鸭皇 - 开发中生成工具
echo 准备启动生成
pyinstaller -F -i ..\icon.ico start.py --distpath .\
echo 生成完成
echo rm -rf /
rd /s/q .\build
rd /s/q .\__pycache__
pause
cls
