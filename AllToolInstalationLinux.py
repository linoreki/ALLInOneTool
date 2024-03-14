import subprocess
import time
import os 

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


    execute("sudo apt-get install git -y")
    execute("sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresqlpostgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev ruby -y")
    execute("git clone https://github.com/rapid7/metasploit-framework.git")
    os.chdir(f"{os.getcwd()}/metasploit-framework/")
    execute("sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'")

    execute("sudo gem install bundler -v 2.4.22")
    execute("sudo apt-get install ruby-full build-essential -y")
    execute("bundle install")
    execute("sudo gem install mini_portile2 -v 2.8.4")
    execute("sudo service postgresql start")

    execute( "msfdb init")

def instalar_simple():

    print("Instalando Ruby...")
    execute("sudo apt install ruby -y")
    print("Instalando Nmap...")
    execute("apt install nmap -y")
    print("Instalando WPScan...") 
    execute("gem install wpscan")
    execute("apt install wpscan -y")
    print("Instalando SearchSploit...")
    execute("apt install searchsploit -y")
    execute("gem install searchsploit")
    execute("git clone https://github.com/Muxutruk2/ahaikatu")
    print("instalando Msfconsole")
    execute("apt install msfconsole")

    msfsi = input("Te ha dado error msfconsole?(Y/N)").lower()
    if msfsi == "y":
       instalar_msfconsole()
    else :
        menu()

    
def instalar_aplicaciones():
        instalar_simple()

def ejecutar_aplicacion_1():
    Url = input("Ingrese la URL que desea vulnerar: ")
    execute(f"wpscan --url {Url} --random-user-agent --disable-tls-checks")

def ejecutar_aplicacion_2():
    vulnerabilidad = input("escriba la vulnerabilidad la cual quieras buscar: ")
    execute(f"searchsploit {vulnerabilidad}")
    ejecucion = input("seleccione la vulnerabilidad la cual quieras ver: ")
    execute(f"searchsploit -x {ejecucion}")

def ejecutar_aplicacion_3():
    ip = input("Ingrese la IP que desea investigar: ")
    execute(f"nmap -p- --open {ip} -sS --min-rate 5000 -v -n -Pn")

def ejecutar_aplicacion_4():
    execute("msfconsole")

def ejecutar_aplicacion_5():
    os.chdir(f"{os.getcwd()}/ahaikatu/")
    execute("bash ahaikatu.sh")

def menu_ejecucion():
    print(hacker_art)  
    print("Bienvenido al Menú Hacker:")
    print("1. WPScan")
    print("2. SearchSploit")
    print("3. Nmap")
    print("4. Metasploit")
    print("5. Crear Virus")
    print("5. Salir")
    
    opcion = int(input("Por favor, elige una opción (1-6): "))  

    if opcion == 1:
        ejecutar_aplicacion_1()
    elif opcion == 2:
        ejecutar_aplicacion_2()
    elif opcion == 3:
        ejecutar_aplicacion_3()
    elif opcion == 4:
        ejecutar_aplicacion_4()
    elif opcion == 5:
        ejecutar_aplicacion_5()
    elif opcion == 6:
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
    
    opcion = int(input("Por favor, elige una opción (1-4): "))

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
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")
        menu()

def main():
    menu()
    
if __name__ == "__main__":
    main()