import os
from datetime import datetime
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists("README.md"):
    with open("README.md", 'x') as f:
        f.write("Hello\n")
else:
    with open("README.md", 'a') as f:
        f.write(f"Hello {datetime.now()}\n")