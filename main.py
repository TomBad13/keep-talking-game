import sys,subprocess

if len(sys.argv) > 1:
    mode = sys.argv[1]    
    fils = sys.argv[2]
    if mode == "1":
        subprocess.run(["python", "Console.py", fils])
    elif mode == "2":
        subprocess.run(["python", "GUI.py", fils])
