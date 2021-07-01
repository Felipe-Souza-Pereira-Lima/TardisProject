# Building dependences
from os import system, chdir, getcwd
from time import sleep as wait
import socket

# Informations
bits = 16
org = "0x800-1x300"

# Host informations
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Kernel:
    def __init__(self):
        self.__version__ = "1.0"
        self.__license__ = "Apache License 2.0"
        self.SubVersion = "version 1.0"
        self.CompileProgramFramework = 'pyinstaller --noconfirm --onefile --console --icon "C:/Users/eplim/Tenaya/os/usr/bin/text_x_python_24589.ico" --name "Kernel.exe"  "C:/Users/eplim/TardisOS/kernel.py"'
            
        self.consoleApplication()
    def InputShellCommand(self):
        system(f'echo ┌─────────[\033[32m%username%@{hostname}\033[m] {getcwd()}')
        command = str(input(f'└─$\033[m ')).strip()
        return command

    def ProgramFinish(self):
        exit()
    def tty(self):
        self.echo("{}:/dev/cons0".format(org))
        return 0
    def echo(self):
        print(self)
        return 0
    def cygwinDisk(self, path):
        try:
            chdir(path)
        except FileNotFoundError:
            print("Shell: {}: Cannot acess this diretory!".format(path))
            return 1
        else:
            return 0
    def CodeActionType(self, filename):
        try:
            a = open(filename, "rt").read()
            a.close()
        except FileNotFoundError:
            print("Shell: {}: FileNotFoundError!")
            return 1
        else:
            with open(filename, "rt") as fileContent:
                print(fileContent.read())
            fileContent.close()
            return 0
    def PrintHostSettings(self):
        print(f"""Software Loopback Interface 1
                    Link encap: Local loopback
                    inet addr: {host} Mask: 255.0.0.0
                    MTU: 1500 Speed:1073,74 Mbps
                    Admin status:UP Oper status:OPERATIONAL
                    RX packets:0 dropped:0 errors:0 unkown:0
                    TX packets:0 dropped:0 errors:0 txqueuelen:0

                Qualcomm Atheros QCA9377 Wireless Network Adapter
                    Link encap: IEEE 802.11 HWaddr: 5C-C9-D3-8D-23-9D
                    inet addr: {host} Mask: 255.255.255.0
                    MTU: 1500 Speed:108,30 Mbps
                    Admin status:UP Oper status:OPERATIONAL
                    RX packets:154204 dropped:0 errors:0 unkown:0
                    TX packets:106105 dropped:0 errors:0 txqueuelen:0""")
        return 0
    def PrintHostName(self):
        print(hostname)
        return 0
    def PrintPath(self):
        print(getcwd())
        return 0
    def getHelpCommand(self):
        print("shutdown                     tty")
        print("cat [filename]               connect [host]:[port]")
        print("hostname                     ifconfig")
        print("echo [String to print]       pwd")
        print("version")


    def consoleApplication(self):
        while True:
            try:
                cmd = self.InputShellCommand()  
                try:
                    with open("{}.exe".format(cmd), "rb") as test:
                        test.close()
                except FileNotFoundError:
                    if cmd == "":
                        print()
                        continue
                    elif cmd == "shutdown":
                        break
                    elif cmd == "tty": 
                        self.tty()
                    elif cmd.startswith("echo"):
                        cmd = cmd.replace("echo ", "")
                        cmd = cmd.replace("echo", "")
                        self.echo(cmd)
                    elif cmd.startswith("cd"):
                        cmd = cmd.replace("cd ", "")
                        cmd = cmd.replace("cd", "")
                        self.cygwinDisk(cmd)
                    elif cmd.startswith("cat"):
                        cmd = cmd.replace("cat ", "")
                        cmd = cmd.replace("cat", "")
                        self.CodeActionType(cmd)
                    elif cmd.startswith("connect"):
                        cmd = cmd.split()
                        try:
                            command = cmd[0]
                            connect_host = cmd[1]
                            connect_port = cmd[2]
                        except:
                            print("Shell: no completed arguments!")
                        else:
                            try:
                                s.connect((connect_host, connect_port))
                            except:
                                print("Shell: Cannot to connect ({}:{})".format(connect_host, connect_port))
                            else:
                                while True:
                                    try:
                                        a = input("> ").strip()
                                        s.sendall(a.decode())
                                    except KeyboardInterrupt:
                                        print("Shell: Connection closed!")
                                        break
                    elif cmd == "hostname":
                        self.PrintHostName()
                    elif cmd == "ifconfig":                   
                        self.PrintHostSettings()
                    elif cmd == "help": 
                        self.getHelpCommand()
                    elif cmd == "pwd":
                        self.PrintPath()
                    elif cmd == "compile":
                        system(self.CompileProgramFramework)
                    elif cmd == "version":
                        print(self.__version__)
                        print(self.SubVersion)

                    else:
                        print("Shell: {}: Unknow Command!")
                else:
                    system("{}.exe".format(cmd))
            except KeyboardInterrupt:
                break
            else:
                print("")
core = Kernel()
core.ProgramFinish()