# System State
pkgs = ["questa"]
files = ["readme.txt"]
u = "guest"
path = "" 

def pyfetch():
    print("O O O O O O LyWebs v1")
    print(" O O O O O  Mem: 64kB")
    print("O O O O O O S: 16MB")
    print(" O O O O O  OS: v1.0")
    print("O O O O O O")

def readme():
    print("""
Lynux Webs is a Linux 
distribution made
entirely with Python.")
It simulates a Linux
terminal, where you
can type commands.""")     

def linux():
    global u, path
    while True:
        # Shortened prompt for small screen
        p = u + "@lywebs:" + path + "$ "
        cmd = input(p)
        
        # --- Nano Logic ---
        if cmd[:5] == "nano ":
            f = cmd[5:]
            if f in files:
                print("Open: " + f)
            else:
                print("New: " + f)
                files.append(f)
            print("== NANO ==")
            input("> ") # Type text
            print("Saved.")

        # --- pwd ---
        elif cmd == "pwd":
            print("/home/" + u + path)

        # --- cd ---
        elif cmd[:3] == "cd ":
            t = cmd[3:]
            if t == ".." or t == "/":
                path = ""
            else:
                path = "/" + t

        # --- readme ---
        elif cmd == "readme":
            readme()

        elif cmd == "ls":
            print(files)
            
        elif cmd == "help":
            print("about, bee, ls, nano")
            print("pyfetch, logoff")
            print("pwd, cd, questa")

        elif cmd == "pyfetch":
            pyfetch()

        elif cmd == "about":
            print("Lynux Webs v1.0 Alpha")

        elif cmd == "bee":
            print("Pkgs:", pkgs)

        elif cmd[:12] == "bee install ":
            pkg = cmd[12:]
            if pkg in pkgs:
                print("Already there.")
            else:
                pkgs.append(pkg)
                print("Done.")

        elif cmd == "questa":
            if "questa" in pkgs:
                print("hello world")
            else:
                print("No pkg.")

        elif cmd == "logoff":
            print("Logout " + u)
            o = input("Power off?(y/n)")
            if o.lower() == "y":
                return "OFF"
            else:
                return "OUT"

        elif cmd == "":
            pass
        else:
            print("Error: " + cmd)

# --- Boot ---
while True:
    print("\nLynux Webs v1")
    u = input("Login: ")
    if u == "": u = "guest"
    print("User: " + u)
    
    sig = linux()
    if sig == "OFF":
        print("Halted.")
        break
