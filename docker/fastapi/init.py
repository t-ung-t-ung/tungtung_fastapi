import os
from pathlib import Path

os.system("docker rm -f tungtung_fastapi")
os.system("docker build -f Dockerfile -t tungtung:first .")

os.system(f"docker run -d -p 8000:8000 -v {Path.cwd().parent.parent}:/workspace --name tungtung_fastapi --restart unless-stopped tungtung:first")
