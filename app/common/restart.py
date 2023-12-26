from os import getcwd, getpid, system

def rebootApp():
    current_dir = getcwd()
    system("cd " + current_dir + f" && python demo.py --reboot --pid={getpid()}") # For Debug
    system("cd " + current_dir + f" && start /b RIT_ToolKit.exe --reboot --pid={getpid()}") # For Release