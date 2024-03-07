import subprocess
import time
import os 
import platform
import webbrowser

# Function to execute shell commands
def execute(command: str):
    return subprocess.run(command, shell=True)

# ASCII art representing the script's theme
hacker_art = """
 █████╗ ██╗     ██╗           ██╗███╗   ██╗       ██████╗ ███╗   ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██║     ██║           ██║████╗  ██║      ██╔═══██╗████╗  ██║██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████║██║     ██║     █████╗██║██╔██╗ ██║█████╗██║   ██║██╔██╗ ██║█████╗         ██║   ██║   ██║██║   ██║██║     
██╔══██║██║     ██║     ╚════╝██║██║╚██╗██║╚════╝██║   ██║██║╚██╗██║██╔══╝         ██║   ██║   ██║██║   ██║██║     
██║  ██║███████╗███████╗      ██║██║ ╚████║      ╚██████╔╝██║ ╚████║███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚══════╝      ╚═╝╚═╝  ╚═══╝       ╚═════╝ ╚═╝  ╚═══╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

"""

# Function to install Metasploit on Windows
def install_msfconsole():
    print("Installing Ruby...")
    execute("choco install ruby -y")

    print("Installing MSFConsole...")
    execute("choco install metasploit-framework -y")

    print("Starting PostgreSQL...")
    execute("Start-Service postgresql-x64-13")

# Function to install a set of applications on Windows
def install_simple():
    print("Installing WPScan...")
    execute("gem install wpscan")
    execute("wpscan --update --disable-tls-checks")

    print("Installing SearchSploit...")
    execute("gem install searchsploit")

    print("Installing Nmap...")
    execute("choco install nmap -y")

# Function to install applications on Windows
def install_windows():
    install_simple()
    install_msfconsole()

# Function to install applications based on the operating system
def install_applications():
    system = platform.system()
    if system == "Windows":
        install_windows()
    else:
        print("The operating system is not compatible with this script.")

# Function to execute WPScan on a specified URL
def execute_application_1():
    url = input("Enter the URL you want to scan: ")
    execute(f"wpscan --url {url} --random-user-agent --disable-tls-checks")

# Function to execute SearchSploit
def execute_application_2():
    execute("searchsploit")

# Function to execute Nmap on a specified IP
def execute_application_3():
    ip = input("Enter the IP you want to investigate: ")
    execute(f"nmap -p- --open {ip} -sS --min-rate 5000 -v -n -Pn")

# Function to execute MSFConsole
def execute_application_4():
    execute("msfconsole")

# Function for the main execution menu
def execution_menu():
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
    else:
        print("Incorrect option. Please choose a valid option.")
        execution_menu()

# Main function for the script
def main():
    print(hacker_art)
    print("Welcome to the Hacker Menu:")
    print("1. Install all applications")
    print("2. Install Metasploit")
    print("3. Execution Menu")
    print("4. Exit")
    print("5. Install gem (required for installing applications)")
    
    option = int(input("Please choose an option (1-5): "))

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
    elif option == 5:
        url = "https://rubyinstaller.org/"
        url2 = "https://www.youtube.com/watch?v=dB16MQWUU4o"
        webbrowser.open(url)
        webbrowser.open(url2)
        time.sleep(2)
        exit() 
       
    else:
        print("Incorrect option. Please choose a valid option.")
        main()

# Entry point of the script
if __name__ == "__main__":
    main()
