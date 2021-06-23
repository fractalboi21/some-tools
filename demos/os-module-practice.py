import os
import sys
import shutil
import subprocess
#os.getcwd()
#os.listdir()
#os.path.isfile("/home/pi/Documents/projects/hetasalo/clues")
#os.chdir()
#os.mkdir()
#os.remove()
#os.uname()
#os.walk()
#os.system()
#os.rmdir()
#os.path.isdir()
#os.name()
#os.path.exists() – Returns True if path or directory does exists.
#os.path.isfile() – Returns True if path is File.
#os.path.isdir() - Returns True if path is Directory.
#pathlib.Path.exists()
#os.getlogin()
#os.getenv("SHELL")
#os.renames(old, new)

#sys.argv[0]
#sys.executable
#sys.exit()
#sys.platform
#sys.thread_info

from torrequest import TorRequest

with TorRequest() as tr:
  response = tr.get('http://ipecho.net/plain')
  print(response.text)
