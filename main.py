import subprocess
import time
import os.path

def execute(command:str):
    return subprocess.run(command.split(" "))

hacker_art = """
  _   _      _ _         __        __         _     _ _ 
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\___(_)
                      |/                                
"""


def installApplication():
    
    execute(["sudo gem install wpscan"])
    execute(["sudo snap install searchsploit"])
    execute(["sudo apt install nmap -y"])
    execute(["sudo""apt""install""ruby"])
    execute(["sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresql postgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev""ruby -y"])
    
    execute(["git clone https://github.com/rapid7/metasploit-framework.git"])
    os.chdir(f"{os.getcwd()}/metasploit-framework/")

    execute(["sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'"])
    execute(["sudo""gem install bundler -v 2.4.22"])
    execute(["sudo""apt-get install ruby-full build-essential"])
    execute(["bundle install"])
    execute(["git""config --global --add safe.directory /home/aimar/Escritorio/metasploit-framework"])
    execute(["sudo gem install""mini_portile2""-v 2.8.4"])
    execute(["sudo service postgresql start"])
    execute([ "msfdb init"])

    # execute(["wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run"])
    # execute(["sudo chmod +x ./metasploit-latest-linux-x64-installer.run"])
    # execute(["./metasploit-latest-linux-x64-installer.run"])

def executeApplication1():
    
    execute(["wpscan -hh"])

def executeApplication2():
    
    execute(["searchsploit"])

def executeApplication3():
    
    execute(["nmap -help"])

def executeApplication4():
    
    execute(["msfconsole"])

def main():
    print(hacker_art)
    
    print("Bienvenido al Menú Hacker:")
    print("1. Instalar TODAS las aplicación 1")
    print("2. Ejecutar aplicación 1")
    print("3. Ejecutar aplicación 2")
    print("4. Ejecutar aplicación 3")
    print("5. Ejecutar aplicación 4")
    print("6. Salir")

    option = int(input("Please, select an option (1-6): "))

    if option == 1:
        installApplication()
        return

    elif option == 2:
        executeApplication1()
        return
    
    elif option == 3:
        executeApplication2()
        return
    
    elif option == 4:
        executeApplication3()
        return
    
    elif option == 5:
        executeApplication4()
        return
    
    elif option == 6:
        print("Bye bye!")
        time.sleep(2)
        exit()
    
    print("Incorrect option")
    main()

if __name__ == "__main__":
    main()