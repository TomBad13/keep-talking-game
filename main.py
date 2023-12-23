import sys,subprocess

if len(sys.argv) > 1:
    mode = sys.argv[1]    
    fils = sys.argv[2]
    if mode == "1":
        print("Mode terminal choisi, veuillez choisir votre nombre de fils")
        subprocess.run(["python", "Console.py", fils])
    elif mode == "2":
        print("Mode terminal choisi, veuillez choisir votre nombre de fils")
        subprocess.run(["python", "GUI.py", fils])
