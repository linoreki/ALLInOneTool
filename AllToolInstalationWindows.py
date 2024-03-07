import subprocess
import time

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


    #execute("choco source add -n=rapid7 -s=\"https://www.rapid7.com/metasploit-framework-download/\"")
    #execute("choco install metasploit-framework")

    execute("git clone https://github.com/rapid7/metasploit-framework.git")
    print("sigue las instrucciones del github")
    url33 = "https://github.com/rapid7/metasploit-framework"
    webbrowser.open(url33)           
    #os.chdir(f"{os.getcwd()}\\metasploit-framework\\")
    #execute("sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'")

    #execute("msfdb init")

def instalar_simple():
    
    print("instalando choco")
    execute("@powershell -NoProfile -ExecutionPolicy unrestricted -Command \"iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))\" && SET PATH=%PATH%;%ALLUSERSPROFILE%chocolateybin")
    #reinicio de terminal
    print("Instalando Ruby...")
    execute("choco install ruby -y")
    execute("winget install --id Git.Git -e --source winget")
    #reinicio de terminal
    print("Instalando Nmap...")
    execute("choco install nmap")   
    # print("Instalando WPScan...") 
    # execute("ridk install")
    # execute("ridk exec pacman -S mingw-w64-x86_64-make")
    # execute("gem update --system")
    # execute("gem sources")
    # execute("gem install wpscan --platform ruby")
    # print("Instalando SearchSploit...")
    # execute("gem install searchsploit")

def instalar_aplicaciones():
        instalar_simple()
        instalar_msfconsole()

def ejecutar_aplicacion_1():
    Url = input("Ingrese la URL que desea vulnerar: ")
    execute(f"wpscan --url {Url} --random-user-agent --disable-tls-checks")


def menu_ejecucion():

    print(hacker_art) 

    print("Bienvenido al Menú Hacker:")
    print("1. Nmap")
    print("2. Salir")
    
    opcion = int(input("Por favor, elige una opción (1-5): "))  

    if opcion == 1:
        ejecutar_aplicacion_1()
    elif opcion == 2:
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