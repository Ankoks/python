# coding : utf-8
import os
import sys
import psutil
import shutil
import multiprocessing

# Комментарий
print("Hello (Привет)")
#name = input("Your name: ")
#print("Hello,", name)

# PEP-8
answer = ''

while answer != 'q':
	answer = input("Lets work? (Y/N/q):")
	if answer == 'Y':
		print("What do you want to do:")
		print("1. List dirrectories")
		print("2. USER password")
		print("3. List of PIDs")
		print("4. Dublicate files")
		print("5. Dublicate choosen file")
		print("6. Delete all dublicate files from choosen directory")
		
		do = int(input("What you would choose: "))
		if do == 1:
			print(os.listdir())
		elif do == 2:
			print("Current directory name:", os.getcwd())
			print("Current os platform:", sys.platform)
			print("Current file system encoding:", sys.getfilesystemencoding())
			print("Current user login:", os.getlogin())
			print("Count CPU:", psutil.cpu_count())
		elif do == 3:
			print(psutil.pids())
		elif do == 4:
			fileList = os.listdir()
			i = 0
			while i < len(fileList):
				if os.path.isfile(fileList[i]):
					newFileName = fileList[i] + '.dublicate'
					shutil.copy(fileList[i], newFileName)
				i += 1
		elif do == 5:
			i = 0
			fileList = os.listdir();
			while i < len(fileList):
				print('[' + str(i) + '] ' + fileList[i])
				i += 1
			choosenFile = int(input("Choose number of file: "))
			
			shutil.copy(fileList[choosenFile], fileList[choosenFile] + '.dublicate')
		elif do == 6:
			directoryName = input("Please, set directory ")
			os.listdir(directoryName)
			fileList = os.listdir();
			i = 0
			while i < len(fileList):
				fullName = os.path.join(directoryName, fileList[i])
				if fullName.endswith(".dublicate"):
					os.remove(fileList[i])
				i += 1
		else:
			pass
	elif answer == 'N':
		print("Bad job")
	else:
		print("Good bye!")