import os
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists("sample.txt"):
    with open("sample.txt", 'x') as f:
        f.write("Hello\n")
else:
    with open("sample.txt", 'a') as f:
        f.write(f"Hello {datetime.now()}\n")