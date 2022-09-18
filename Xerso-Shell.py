import subprocess
import webbrowser
import platform
import socket
import time
import sys
import os

path = "C:/"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Xerso-Shell [Version 1.01]")

def pings():
    host = input("Enter Website to Ping : ")
    number = input("Enter How Many Times to Ping: ")

    def ping(host):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, number, host]
        return subprocess.call(command)
    print(ping(host))

def local():
    print("Your Local IPS Is: " + host_ip)
    print("Your Desktop Name Is: " + host_name)

def date():
    print("The Local Date Is: " + time.strftime("%m/%d/%Y"))

def ls():
    dir_list = os.listdir()
    print(dir_list)

def lsdir():
    file = input("Enter The Direct File Path To Read: ")
    try:
        dir_list2 = os.scandir(file)
        print("Files and directories in '", file, "':")
        print(dir_list2)
    except FileNotFoundError:
        print(f'there is no directory named: "{file}"')

def echo():
    echo = input("What Do You Want Me To Echo: ")
    print(echo)


def tasklist():
    os.system("tasklist")

def cmd():
    os.system('start cmd')   

def info():
    print('Xerso-Shell [version 1.01]')
    print('Made by Xerso. (anyone is allowed to use the source)')

def explorer():
    subprocess.Popen('explorer')

def tree():
    os.system("tree")

def pwd():
    dir=os.getcwd()
    print(dir)

def cd():
    dir=input("directory to cd : ")
    if dir == "":
        print("Please specify the directory name the directory name.") 
    else:
        os.chdir(dir)

def cdback():
    os.chdir('..')

def mkdir():
    new_dir=input('Enter the name of new directory')
    os.mkdir(new_dir)

def web():
        def _find_default_browser():
            if sys.platform == 'win32':
                import winreg
                userchoice = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.html\UserChoice")
                browserId = winreg.QueryValueEx(userchoice, 'ProgId')[0]
                command_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, browserId + r"\shell\open\command")
                full_command = winreg.QueryValueEx(command_key, '')[0]
                command = full_command[1:full_command.index('"', 1)].replace('\\', '/')
                return command
            else:
                raise NotImplementedError('Unsupported platfom')


        def open_new():
            command = _find_default_browser()
            subprocess.Popen([command])
        open_new()

def fail():
    raise Exception("Explosions!")

commands = dict()

def init():
    commands['ping'] = pings
    commands['local'] = local
    commands['date'] = date
    commands['ls'] = ls
    commands['ls -a'] = lsdir
    commands['echo'] = echo
    commands['tasklist'] = tasklist
    commands['cmd'] = cmd
    commands['info'] = info
    commands['explorer'] = explorer
    commands['pwd'] = pwd
    commands['cd'] = cd
    commands['cd ..'] = cdback
    commands['mkdir'] = mkdir
    commands['help'] = help
    commands['web'] = web
    commands['fail'] = fail
    commands['tree'] = tree
    

def main():
    while True:
        code=(input("~> ").strip())
        if code in commands:
            try:
                commands[code]()
            except BaseException:
                print(f'A error occured while running "{code}"')
        else:
            print(f'{code}: No such command', 'valid comands are', sep='\n')


if __name__ == '__main__':
    init()
    main()


