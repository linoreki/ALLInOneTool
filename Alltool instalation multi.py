import subprocess
import time
import os 
import platform
import webbrowser

def execute(command:str):
    return subprocess.run(command, shell=True)

hacker_art = """
  _   _      _ _         __        __         _     _ _ 
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\__,_(_)
                      |/                                
"""

def instalar_msfconsole():
    print("Instalando MSFConsole...")
    execute("choco install metasploit-framework -y") if platform.system() == "Windows" else execute("sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresqlpostgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev ruby -y")
    execute("git clone https://github.com/rapid7/metasploit-framework.git")
    os.chdir(f"{os.getcwd()}/metasploit-framework/")
    execute("sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'")
    execute("sudo gem install bundler -v 2.4.22") if platform.system() == "Linux" else None
    execute("sudo apt-get install ruby-full build-essential") if platform.system() == "Linux" else None
    execute("bundle install") if platform.system() == "Linux" else None
    execute("sudo gem install mini_portile2 -v 2.8.4") if platform.system() == "Linux" else None
    execute("sudo service postgresql start") if platform.system() == "Linux" else None
    execute( "msfdb init")

def instalar_simple():
    sistema = platform.system()
    print("Instalando Ruby...")
    if sistema == "Windows":
        execute("choco install ruby -y")
    elif sistema == "Linux":
        execute("sudo apt install ruby -y")


    print("Instalando WPScan...")
    execute("gem install wpscan")
    execute("wpscan --update --disable-tls-checks")

    print("Instalando SearchSploit...")
    execute("gem install searchsploit")

    print("Instalando Nmap...")
    execute("choco install nmap -y") if platform.system() == "Windows" else execute("sudo apt install nmap -y")

def instalar_aplicaciones():
    sistema = platform.system()
    if sistema == "Linux":
        instalar_simple()
        instalar_msfconsole()
    elif sistema == "Windows":
        instalar_simple()
        instalar_msfconsole()

def ejecutar_aplicacion_1():
    Url = input("Ingrese la URL que desea vulnerar: ")
    execute(f"wpscan --url {Url} --random-user-agent --disable-tls-checks")

def ejecutar_aplicacion_2():
    execute("searchsploit")

def ejecutar_aplicacion_3():
    ip = input("Ingrese la IP que desea investigar: ")
    execute(f"nmap -p- --open {ip} -sS --min-rate 5000 -v -n -Pn")

def ejecutar_aplicacion_4():
    execute("msfconsole")

def menu_ejecucion():
    print(hacker_art)  
    print("Bienvenido al Menú Hacker:")
    print("1. WPScan")
    print("2. SearchSploit")
    print("3. Nmap")
    print("4. Metasploit")
    print("5. Salir")
    
    opcion = int(input("Por favor, elige una opción (1-5): "))  

    if opcion == 1:
        ejecutar_aplicacion_1()
    elif opcion == 2:
        ejecutar_aplicacion_2()
    elif opcion == 3:
        ejecutar_aplicacion_3()
    elif opcion == 4:
        ejecutar_aplicacion_4()
    elif opcion == 5:
        print("¡Hasta luego!")
        time.sleep(2)
        exit()
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")
        menu_ejecucion()

def menu():
    print(hacker_art)
    print("Bienvenido al Menú Hacker:")
    print("1. Instalar todas las aplicaciones")
    print("2. Instalar Metasploit")
    print("3. Menú de ejecución")
    print("4. Salir")
    print("5. Instalar gem manualmente")
    
    opcion = int(input("Por favor, elige una opción (1-5): "))

    if opcion == 1:
        instalar_aplicaciones()
    elif opcion == 2:
        instalar_msfconsole()
    elif opcion == 3:
        menu_ejecucion()
    elif opcion == 4:
        print("¡Hasta luego!")
        time.sleep(2)
        exit()
    elif opcion == 5:
        url = "https://rubyinstaller.org/"
        webbrowser.open(url)
        time.sleep(2)
        exit() 
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")
        menu()

def main():
    menu()
    
if __name__ == "__main__":
    main()
    sistema = platform.system()