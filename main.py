import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if(not os.path.exists("sample.txt")):
    f = open("sample.txt",'x')
    f.write("Hello\n")
    f.close()
else:
    f = open("sample.txt",'a')
    f.write("Hello\n")
    f.close()