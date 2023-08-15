import os
import sys

os.system("git add .")
os.system(f"git commit -am {sys.argv[1]}")
os.system("git push origin main")