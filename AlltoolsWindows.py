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
    print("Instalando Ruby...")
    execute("choco install ruby -y")

    print("Instalando MSFConsole...")
    execute("choco install metasploit-framework -y")

    print("Iniciando PostgreSQL...")
    execute("Start-Service postgresql-x64-13")

def instalar_simple():
    print("Instalando WPScan...")
    execute("gem install wpscan")
    execute("wpscan --update --disable-tls-checks")

    print("Instalando SearchSploit...")
    execute("gem install searchsploit")

    print("Instalando Nmap...")
    execute("choco install nmap -y")

def instalar_windows():
    instalar_simple()
    instalar_msfconsole()

def instalar_aplicaciones():
    sistema = platform.system()
    if sistema == "Windows":
        instalar_windows()
    else:
        print("El sistema operativo no es compatible con este script.")

def ejecutar_aplicacion_1():
    Url = input("ingrese la url la cual quieres vulnerar: ")
    execute(f"wpscan --url {Url} --random-user-agent --disable-tls-checks")

def ejecutar_aplicacion_2():
    execute("searchsploit")

def ejecutar_aplicacion_3():
    ip = input("ingrese la ip cual quieres investigar: ")
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

def main():
    print(hacker_art)
    print("Bienvenido al Menú Hacker:")
    print("1. Instalar todas las aplicaciones")
    print("2. Instalar Metasploit")
    print("3. Menú de ejecución")
    print("4. Salir")
    print("5.instalar gem (necesario para instalar aplicaciones)")
    
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
        main()

if __name__ == "__main__":
    main()
