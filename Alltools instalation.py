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
    execute("sudo apt install ruby")
    execute("sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresqlpostgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev ruby -y")
    execute("git clone https://github.com/rapid7/metasploit-framework.git")
    os.chdir(f"{os.getcwd()}/metasploit-framework/")
    execute("sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'")
    execute("sudo gem install bundler -v 2.4.22")
    execute("sudo apt-get install ruby-full build-essential")
    execute("bundle install")
    execute("sudo gem install mini_portile2 -v 2.8.4")
    execute("sudo service postgresql start")
    execute( "msfdb init")


def instalar_simple():
    execute("sudo apt update")
    execute("sudo gem install wpscan")
    execute("sudo snap install searchsploit")
    execute("sudo apt install nmap -y")
    execute("sudo snap install metasploit-framework")


def instalar_linux():
    instalar_simple()

def instalar_windows():

def instalar_aplicaciones():
    sistema = platform.system()
    if sistema == "Linux":
        instalar_linux()
    elif sistema == "Windows":
    instalar_windows()

    else:
        print("El sistema operativo no es compatible con este script.")

def ejecutar_aplicacion_1():
    Url = input("ingrese la url la cual quieres vulnerar: ")
    execute(f"wpscan --url {Url}")
    

def ejecutar_aplicacion_2():
    
    execute("searchsploit")

def ejecutar_aplicacion_3():
    ip = input("ingrese la ip cual quieres investigar: ")
    execute(f"nmap -p- --open {ip} -sS --min-rate 5000 -v -n -Pn")

def ejecutar_aplicacion_4():
    
    execute("msfconsole")

def menu_ejecuccion():

    execute("clear")
    print(hacker_art)  
    print("Bienvenido al Menú Hacker:")
    print("1. wpscan ")
    print("2. searchsploit ")
    print("3. nmap")
    print("4. metasploit")
    print("5. Salir")
    
    opcion = int(input("Por favor, elige una opción (1-5): "))  
    if opcion == 1:
        ejecutar_aplicacion_1()
        return
    
    elif opcion == 2:
        ejecutar_aplicacion_2()
        return
    
    elif opcion == 3:
        ejecutar_aplicacion_3
        return
        
    elif opcion == 4:
        ejecutar_aplicacion_4
        return
    
    elif opcion == 5:
        print("¡Hasta luego!")
        time.sleep(2)
        exit()
    elif opcion >= 5:
        print("opcion incorrecta por favor inserte un valor permitido")
        menu_ejecuccion

def menu():
   
    print(hacker_art)
    
    print("Bienvenido al Menú Hacker:")
    print("1. Instalar TODAS las aplicación")
    print("2. instalar metasploit (era compleja)")
    print("3. Menu de ejecucion")
    print("4. Salir")

    opcion = int(input("Por favor, elige una opción (1-4): "))

    
    if opcion == 1:
        instalar_aplicaciones()
        return
    
    if opcion == 2:
        instalar_msfconsole()
        return
    
    elif opcion == 3:
        menu_ejecuccion()
        return
    
    elif opcion == 4:
        print("¡Hasta luego!")
        time.sleep(2)
        exit()
    
    elif opcion >= 4:
        print("opcion incorrecta por favor inserte un valor permitido")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()