import subprocess
import time
import os

def execute(command: str):
    """
    Execute a shell command.

    Args:
        command (str): The command to execute.

    Returns:
        CompletedProcess: An object representing the result of the completed process.
    """
    return subprocess.run(command, shell=True)


hacker_art = """
  _   _      _ _         __        __         _     _ _ 
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\__,_(_)
                      |/                                
"""

def install_msfconsole():
    """
    Install MSFConsole and its dependencies.
    """
    print("Installing MSFConsole...")

    execute("sudo apt-get install git -y")
    execute("sudo apt-get install build-essential zlib1g zlib1g-dev libxml2 libxml2-dev libxslt-dev locate libreadline6-dev libcurl4-openssl-dev git-core autoconf curl postgresqlpostgresql-contrib libpq-dev libapr1 libaprutil1 libsvn1 libpcap-dev ruby -y")
    execute("git clone https://github.com/rapid7/metasploit-framework.git")
    os.chdir(f"{os.getcwd()}/metasploit-framework/")
    execute("sudo bash -c 'for MSF in $(ls msf*) do ln -s /usr/local/src/metasploit-framework/$MSF /usr/local/bin/$MSF'")
    execute("sudo gem install bundler -v 2.4.22")
    execute("sudo apt-get install ruby-full build-essential -y")
    execute("sudo bundle install")
    execute("sudo gem install pg -v '1.5.4' --source 'https://rubygems.org/'")
    execute("sudo gem install mini_portile2 -v 2.8.4")
    execute("sudo service postgresql start")

    execute("msfdb init")

def install_simple():
    """
    Install required packages based on the selected Linux distribution.
    """
    system = input("Which distribution are you using? 1. Debian 2. Ubuntu 3. RedHat (if none of these, try Ubuntu)")

    if system == "1":
        install_all()
        execute("sudo apt install dirmngr ca-certificates gnupg")
        execute("sudo gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF")
        execute("echo \"deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/debian stable-buster main\" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list")
        execute("sudo apt update")
        execute("sudo apt install mono-devel")
        execute("apt-get install postgresql-12")
        msf_verification()
    elif system == "2":
        install_all()
        execute("sudo apt install ca-certificates gnupg")
        execute("sudo gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF")
        execute("echo \"deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable-focal main\" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list")
        execute("sudo apt update")
        execute("sudo apt install mono-devel")
        execute("sudo sh -c 'echo \"deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main\" > /etc/apt/sources.list.d/pgdg.list'")
        execute("wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -")
        execute("sudo apt-get update")
        execute("sudo apt-get -y install postgresql")
        msf_verification()
    elif system == "3":
        install_all()
        execute("yum install postgresql-server")
        execute("dnf install postgresql-server")
        execute("sudo apt install ca-certificates gnupg")
        execute("sudo gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF")
        execute("echo \"deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable-focal main\" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list")
        execute("sudo apt update")
        execute("sudo apt install mono-devel")
        msf_verification()
    else:
        print("Please enter a valid option.")
        install_simple()


def msf_verification():
    """
    Check if there was an error with MSFConsole installation and reinstall if needed.
    """
    msfsi = input("Did you encounter any errors with msfconsole? (Y/N)").lower()
    if msfsi == "y":
        install_msfconsole()
    else:
        menu()

def install_all():
    """
    Install Ruby, Nmap, WPScan, SearchSploit, and Metasploit.
    """
    print("Installing Ruby...")
    execute("sudo apt install ruby -y")
    print("Installing Nmap...")
    execute("sudo apt install nmap -y")
    print("Installing WPScan...")
    execute("sudo gem install wpscan")
    execute("sudo apt install wpscan -y")
    print("Installing SearchSploit...")
    execute("sudo snap install searchsploit")
    execute("sudo git clone https://github.com/Muxutruk2/ahaikatu")
    print("Installing Msfconsole")
    execute("sudo snap install metasploit-framework")


def install_applications():
    install_simple()


def run_application_1():
    """
    Execute WPScan application.
    """
    Url = input("Enter the URL you want to scan for vulnerabilities: ")
    execute(f"wpscan --url {Url} --random-user-agent --disable-tls-checks")


def run_application_2():
    """
    Execute SearchSploit application.
    """
    vulnerability = input("Enter the vulnerability you want to search for: ")
    execute(f"searchsploit {vulnerability}")
    execution = input("Select the vulnerability you want to view: ")
    execute(f"searchsploit -x {execution}")


def run_application_3():
    """
    Execute SearchSploit application.
    """
    ip = input("Enter the IP address you want to investigate: ")
    execute(f"nmap -p- --open {ip} -sS --min-rate 5000 -v -n -Pn")


def run_application_4():
    """
    Execute Metasploit application.
    """
    execute("sudo msfconsole")


def run_application_5():
    """
    Execute custom application.
    """
    os.chdir(f"{os.getcwd()}/ahaikatu/")
    execute("sudo bash ahaikatu.sh")


def execution_menu():
    """
    Display and execute applications from the execution menu.
    """
    print(hacker_art)
    print("Welcome to the Hacker Menu:")
    print("1. WPScan")
    print("2. SearchSploit")
    print("3. Nmap")
    print("4. Metasploit")
    print("5. Create Virus")
    print("6. Exit")

    option = int(input("Please choose an option (1-6): "))

    if option == 1:
        run_application_1()
    elif option == 2:
        run_application_2()
    elif option == 3:
        run_application_3()
    elif option == 4:
        run_application_4()
    elif option == 5:
        run_application_5()
    elif option == 6:
        print("Goodbye!")
        time.sleep(2)
        exit()
    else:
        print("Incorrect option. Please choose a valid option.")
        execution_menu()


def menu():
    """
    Display and execute options from the main menu.
    """
    print(hacker_art)
    print("Welcome to the Hacker Menu:")
    print("1. Install all applications")
    print("2. Install Metasploit")
    print("3. Execution menu")
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
    else:
        print("Incorrect option. Please choose a valid option.")
        menu()


def main():
    """
    Display and execute options from the main menu.
    """
    menu()


if __name__ == "__main__":
    main()