import platform
import AlltoolsLinux
import AlltoolsWindows

def main():
    system = platform.system()
    if system == "Linux":
        AlltoolsLinux.main()
    if system == "Windows":
        AlltoolsWindows.main()

if __name__ == "__main__":
    main()