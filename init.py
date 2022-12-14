import os
import platform

system = platform.system()

os.system("git config core.hooksPath .githooks")
if system != "windows":
    os.system("chmod ug+x .githooks/*")
os.system("conda update -n base -c defaults conda -y")
os.system("python3 .githooks/_post_merge.py")
