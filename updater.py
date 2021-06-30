import requests
import os
import sty
from sty import bg, ef, fg
import time

VER = "1.0.0"
GITHUBVERLINK = "https://raw.githubusercontent.com/eternadox/Python-Script-Updater/main/version.txt" # Raw github version here
GITHUBSCRIPT = "https://raw.githubusercontent.com/eternadox/Python-Script-Updater/main/script.py" # Raw github script here
SCRIPTNAME = "script" # script name

githubversion = requests.get(GITHUBVERLINK).text
githubfile = requests.get(GITHUBSCRIPT).text

def latestversioncheck():
    if (githubversion == VER):
        return True
    else:
        return False

print(f"{fg.white}[{fg.li_green}*{fg.white}] Checking if latest version...")
if (latestversioncheck() == True):
 print(f"{fg.white}[{fg.yellow}!{fg.white}] Version is latest!")
 os.system(f"python3 {SCRIPTNAME}.py")
else:
  print(f"{fg.white}[{fg.yellow}!{fg.white}] Version is outdated! Updating...")
  f = open(SCRIPTNAME + '.py', 'w')
  f.write(githubfile)
  f.close()
  os.system(f"python3 {SCRIPTNAME}.py")
