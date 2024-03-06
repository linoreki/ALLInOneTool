import subprocess
import time
import os 
import platform

# Function to execute shell commands
def execute(command: str):
    return subprocess.run(command.split(" "))

# ASCII art representing the script's theme
hacker_art = """
 █████╗ ██╗     ██╗           ██╗███╗   ██╗       ██████╗ ███╗   ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██║     ██║           ██║████╗  ██║      ██╔═══██╗████╗  ██║██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████║██║     ██║     █████╗██║██╔██╗ ██║█████╗██║   ██║██╔██╗ ██║█████╗         ██║   ██║   ██║██║   ██║██║     
██╔══██║██║     ██║     ╚════╝██║██║╚██╗██║╚════╝██║   ██║██║╚██╗██║██╔══╝         ██║   ██║   ██║██║   ██║██║     
██║  ██║███████╗███████╗      ██║██║ ╚████║      ╚██████╔╝██║ ╚████║███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝      ╚═╝╚═╝  ╚═══╝       ╚═════╝ ╚═╝  ╚═══╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

"""

# Function to install Metasploit on Linux
def install_msfconsole():
    execute("sudo apt install ruby")
    execute("sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresql postgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev ruby -y")
    execute("git clone https://github.com/rapid7/metasploit-framework.git")
    os.chdir(f"{os.getcwd()}/metasploit-framework/")
    execute("sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'")
    execute("sudo gem install bundler -v 2.4.22")
    execute("sudo apt-get install ruby-full build-essential")
    execute("bundle install")
    execute("sudo gem install mini_portile2 -v 2.8.4")
    execute("sudo service postgresql start")
    execute("msfdb init")

# Function to install a set of applications on Linux
def install_simple():
    execute("sudo apt update")
    execute("sudo gem install wpscan")
    execute("sudo snap install searchsploit")
    execute("sudo apt install nmap -y")
    execute("sudo snap install metasploit-framework")

# Function to install applications on Linux
def install_linux():
    install_simple()

# Function to install applications based on the operating system
def install_applications():
    sistema = platform.system()
    if sistema == "Linux":
        install_linux()

# Function to execute WPScan on a specified URL
def execute_application_1():
    url = input("Enter the URL you want to scan: ")
    execute(f"wpscan --url {url}")

# Function to execute SearchSploit
def execute_application_2():
    execute("searchsploit")

# Function to print Nmap help
def execute_application_3():
    execute("nmap -help")

# Function to start MSFConsole
def execute_application_4():
    execute("msfconsole")

# Function for the main execution menu
def execution_menu():
    execute("clear")
    print(hacker_art)  
    print("Welcome to the Hacker Menu:")
    print("1. WPScan")
    print("2. SearchSploit")
    print("3. Nmap")
    print("4. Metasploit")
    print("5. Exit")
    
    option = int(input("Please choose an option (1-5): "))  
    if option == 1:
        execute_application_1()
    elif option == 2:
        execute_application_2()
    elif option == 3:
        execute_application_3()
    elif option == 4:
        execute_application_4()
    elif option == 5:
        print("Goodbye!")
        time.sleep(2)
        exit()
    elif option >= 5:
        print("Incorrect option. Please choose a valid option.")
        execution_menu()

# Main function for the script
def main():
    print(hacker_art)
    print("Welcome to the Hacker Menu:")
    print("1. Install ALL applications")
    print("2. Install Metasploit (complex installation)")
    print("3. Execution Menu")
    print("4. Exit")

    option = int(input("Please choose an option (1-4): "))

    if option == 1:
        install_applications()
    elif option == 2:
        install_msfconsole()
    elif option == 3:
        execution_menu()
    elif option == 4:
        print("Goodbye!")
        time.sleep(2)
        exit()
    elif option >= 4:
        print("Incorrect option. Please choose a valid option.")
        main()

# Entry point of the script
if __name__ == "__main__":
    main()
