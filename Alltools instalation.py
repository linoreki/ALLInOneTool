import subprocess
import time
import os 
import platform

def execute(command:str):
    return subprocess.run(command.split(" "))

hacker_art = """
  _   _      _ _         __        __         _     _ _ 
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\__,_(_)
                      |/                                
"""


def instalar_msfconsole():
    subprocess.run(["sudo apt install ruby"])
    subprocess.run(["sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresqlpostgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev ruby -y"])
    subprocess.run(["git clone https://github.com/rapid7/metasploit-framework.git"])
    os.chdir(f"{os.getcwd()}/metasploit-framework/")
    subprocess.run(["sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'"])
    subprocess.run(["sudo gem install bundler -v 2.4.22"])
    subprocess.run(["sudo apt-get install ruby-full build-essential"])
    subprocess.run(["bundle install"])
    subprocess.run(["sudo gem install mini_portile2 -v 2.8.4"])
    subprocess.run(["sudo service postgresql start"])
    subprocess.run([ "msfdb init"])


def instalar_simple():
    subprocess.run(["sudo apt update"])
    subprocess.run(["sudo gem install wpscan"])
    subprocess.run(["sudo snap install searchsploit"])
    subprocess.run(["sudo apt install nmap -y"])
    subprocess.run(["sudo snap install metasploit-framework"])


def instalar_linux():
    instalar_simple()

def instalar_windows():

def instalar_aplicaciones():

    sistema = platform.system()
    if sistema == "Linux":
        instalar_linux()

def ejecutar_aplicacion_1():
    
    subprocess.run(["wpscan -hh"])

def ejecutar_aplicacion_2():
    
    subprocess.run(["searchsploit"])

def ejecutar_aplicacion_3():
    
    subprocess.run(["nmap -help"])

def ejecutar_aplicacion_4():
    
    subprocess.run(["msfconsole"])



def menu():
   
    print(hacker_art)
    
    print("Bienvenido al Menú Hacker:")
    print("1. Instalar TODAS las aplicación 1")
    print("2. instalar metasploit (era compleja)")
    print("3. Ejecutar aplicación 1")
    print("4. Ejecutar aplicación 2")
    print("5. Ejecutar aplicación 3")
    print("6. Ejecutar aplicación 4")
    print("7. Salir")

    opcion = int(input("Por favor, elige una opción (1-7): "))

    
    if opcion == 1:
        instalar_aplicaciones()
        return
    
    if opcion == 2:
        instalar_msfconsole()
        return
    
    elif opcion == 3:
        ejecutar_aplicacion_1()
        return
    
    elif opcion == 4:
        ejecutar_aplicacion_2()
        return
    
    elif opcion == 5:
        ejecutar_aplicacion_3()
        return
    
    elif opcion == 6:
        ejecutar_aplicacion_4()
        return
    
    elif opcion == 7:
        print("¡Hasta luego!")
        time.sleep(2)
        exit()
    
    elif opcion >= 7:
        print("opcion incorrecta por favor inserte un valor permitido")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()