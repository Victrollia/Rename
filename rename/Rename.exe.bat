@ECHO OFF
if exist upload\ (
	echo Please add images to upload folder
) else (
	md upload
)
if exist processed\ (
	echo: 
) else (
	md processed
)
python rename.py
pause
