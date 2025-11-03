import os 
import subprocess
import time

def banner(): 
    banner = """


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠆⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⡇⠀⠀⠀⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠹⣆⠀⢠⠃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⡏⠀⠘⡼⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡈⠓⢾⠀⣧⡀⠀⠀⠀⠀⠀⣤⣤⣴⣶⣦⢤⣄⡀⠀⠀⢸⠀⣧⠀⠀⢧⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣦⣼⠀⡿⡏⠙⠲⠤⣀⡀⠀⠈⠙⣆⠈⠓⣄⠙⢢⡀⠈⣆⠘⢇⠀⠸⡇⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⠀⢸⣹⡀⠠⣀⠀⠉⠙⠲⢄⡈⣆⠀⠈⢣⡀⢱⣄⣸⢦⣤⣑⢄⡇⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠘⣇⢻⣶⣌⠙⢦⡀⠀⠀⠉⠺⢦⠀⠨⡇⠀⠙⣶⣉⣴⠛⠻⠱⣄⠀⢱⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣖⣉⣇⠀⠸⡄⠹⣌⠳⣦⡙⢶⣄⠀⠀⠀⠙⢆⣟⠀⡸⠫⢿⡜⣆⠀⠀⠘⢆⠈⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠽⣿⠀⠀⠹⡄⠈⢧⡈⠻⣆⠙⣧⣀⠀⠀⠀⠹⣄⡀⠀⡜⠳⣘⡄⠀⠀⠘⣇⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣛⠛⠛⠿⣦⡀⠀⠙⢤⠀⠱⣦⢽⣧⡈⢻⡇⠀⠀⢀⣹⣏⣼⡁⠀⢙⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡇⠀⠀⢳⡳⣀⠀⠀⢳⡄⠈⢷⣌⣷⣠⡿⣿⣫⣿⣾⣿⣄⠀⡴⠋⠙⠳⣶⣶⢬⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣯⣤⣤⣤⣤⣷⡈⢷⣦⡀⠙⢦⠀⣈⠛⢿⣾⣿⠋⢁⠔⠚⠻⢟⠣⠀⠔⠉⠙⢮⣙⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⠿⢭⡉⠀⠀⠀⠈⠉⠙⠛⣿⣦⡉⢿⣦⣌⢣⡈⢷⡀⡼⢿⡄⠈⠀⡠⠒⠚⠳⢄⠀⢀⠖⠙⢿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠁⠀⠀⣠⣇⣠⣤⣤⣤⣤⡴⠚⢉⣿⣿⣦⡈⠙⣷⣽⣄⣿⠃⠀⠙⢷⣼⡁⠀⡀⠐⠒⠯⣉⠀⢠⠴⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣴⡿⠛⠋⠉⠁⠉⢹⠟⠀⠀⠀⣠⣽⣿⣷⡀⠸⠿⢿⡇⠀⠀⠀⠀⢹⣷⣦⣇⠀⢀⠘⠙⠛⡇⠀⠸⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣯⣅⠀⠀⠀⠀⣀⡴⠋⠀⠐⠒⠉⠉⠉⠛⣿⣷⣄⡀⢸⣧⠀⠀⠀⠀⠀⢻⣿⣿⣿⣾⠀⠀⠀⠀⡄⠀⡇⠈⣧⠀⠀⠀
⠀⠀⠀⢀⠟⠁⠀⣸⣠⡴⠾⢿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠨⢟⣛⣿⡟⠉⢳⣄⠀⠀⠀⠀⢻⡈⠉⠻⣷⣀⠀⠀⢸⣼⣇⣧⡿⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠞⠋⠀⠀⢠⠞⠀⠀⠀⠀⢀⣠⠤⢔⣾⣿⠿⠛⢿⢹⠁⠀⠀⠙⢷⡄⠀⠀⠀⠙⠻⣿⣿⡟⣟⠛⠁⣿⠀⣿⠁⠀⠀⠀
⠀⠀⠀⣰⠟⠁⠀⡀⢀⣠⠏⠀⠀⠀⣠⠖⠋⣠⣾⡟⠛⣧⠀⠀⠘⢿⡄⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠈⢿⣇⠹⠀⠀⢸⡀⣿⠀⠀⠀⠀
⠀⠀⢰⣏⣄⠀⣠⣶⢿⠏⠀⠀⠀⠞⠁⣠⣾⡿⡏⠀⠀⠈⠳⣄⣀⣀⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⢦⠀⠀⠘⢇⢹⠀⠀⠀⠀
⠀⠀⡿⠁⣰⡾⠛⠂⡜⠀⠀⠀⠀⢀⣼⡿⠃⠘⢳⡀⠀⠀⢠⠋⠳⢄⡀⠙⢦⣀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠙⠾⠀⠀⠀⠈⠋⣇⠀⠀⠀
⠀⠀⠁⣼⠛⠀⠀⣺⠃⠀⠀⠀⢀⣾⡟⣷⠀⠀⠀⠙⠒⠒⠚⢷⠖⠋⢉⡿⠋⠉⠓⢦⣄⠸⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀
⠀⠀⣸⠃⠀⢀⣴⡇⠀⠀⠀⢀⣾⡟⠉⠉⢧⡀⠀⠀⠘⣆⣀⠤⢷⣶⠟⠀⠀⠀⠀⠀⠈⠱⣄⠉⠳⢤⡀⠀⠀⠀⢰⡎⠉⠲⠄⢹⠲⡄
⠀⠀⣧⠞⣧⣾⢿⠁⠀⠀⠀⣼⡿⡁⠀⠀⠀⠈⠹⡟⠛⠙⣆⡤⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠙⢦⡀⠀⢀⣿⣄⠀⠀⠀⠀⢸
⠀⢸⠃⣰⡟⠁⣾⠀⠀⠀⢸⣿⣤⠧⣄⠀⠀⠀⢀⣱⠤⠒⠁⢠⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣵⡄⢻⠀⠸⡻⣿⣄⣤⠀⠀⡼
⠀⠉⢸⡟⠀⠀⡿⠀⠀⠀⣿⡇⠀⠀⠀⠉⢹⡏⠉⠈⣷⠤⠴⣿⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⠀⢧⡀⠀⠾⠀⠀⢸⢠⠇
⠀⠀⡿⠁⠀⠀⡇⠀⠀⢰⡟⢱⣄⠀⠀⠀⠀⢣⠤⠚⠁⠀⢰⣿⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⣄⡉⠳⢦⣀⡤⣾⡟⠀
⠀⢸⣇⡤⠤⣄⡇⠀⠀⣿⡏⠉⠈⠙⠒⡖⠒⠉⢷⡀⠀⣠⢾⡟⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠉⢻⠖⠋⠀⠀
⠀⣼⠏⠀⢀⣿⡇⠀⢀⣿⡀⠀⠀⠀⠀⠙⣆⣀⠴⠋⠉⠑⢾⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⠀⢀⣿⠏⣇⠀⢸⣿⢑⡤⣀⣀⣀⡴⠛⣇⠀⠀⠀⢀⣼⡇⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⡏⠀⣧⠀⣼⡿⠉⠀⠈⠉⢧⡀⠀⢈⡷⠒⠒⠫⣼⡇⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣠⢦⣿⠀⣿⣧⠀⠀⠀⠀⠀⢉⣞⠉⠀⠀⠀⠀⢸⣧⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠁⢸⣿⢰⣿⣏⡳⠤⣤⡤⠖⠉⠘⢦⡀⠀⠀⣠⡾⣿⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠋⠀⡞⣿⢸⣿⠀⠀⠀⠈⠣⡀⠀⢀⣠⠛⠉⠉⠉⠓⣿⡄⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠇⡿⢸⣿⡄⠀⠀⠀⠀⢈⣽⡋⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣠⡇⢸⣿⠿⠓⠦⢶⡛⠉⠀⠙⠢⣤⣀⣀⣀⡤⣿⣿⡄⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⢻⡇⣸⡇⠀⠀⠀⠀⠳⡀⠀⢀⡴⠛⠀⠀⠀⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠃⣿⡇⠀⠀⠀⠀⠀⢈⣿⣏⠀⠀⠀⠀⠀⠀⠀⢸⠿⣷⡀⠀⠀⠀⠀⠀⠈⠛⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡇⠀⣿⣿⣦⣤⣤⣶⠟⠁⠈⠈⠳⢤⣀⣀⣀⡤⠴⠚⠚⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⠁⢸⣿⢟⠩⠃⠈⢧⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢶⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡿⠀⣾⡇⠀⠀⠀⠀⠈⢧⡀⠀⡰⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⢿⣷⣄⠀⠀⠀⠀⠀⠀⣀⣀⣀⡠⠤⣴⣻⡄⠀⠀⠀⠀
⠀⣠⣴⡏⠀⢰⣿⣧⡀⠀⠀⠀⠀⠀⣹⠿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡰⠯⠤⠤⠜⠛⠙⠓⠒⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠴⠁⠸⢤⠴⠟⠛⠙⠛⠶⣶⡴⠖⠊⠁⠀⠙⠲⢤⣄⣀⣀⣀⣤⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣴⡤⠴⠚⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

NAME: INFINITE
DESCRIPTION: Tool designed for the detection of Userland / LKM rootkits.
AUTHOR: cphx_
"""
    print(banner)



def userland_krux(): 
    try:
        # strace /bin/ls |grep "openat(AT_FDCWD)"
        os.system("sudo apt install strace -y")
        time.sleep(1)
        strace = os.system("strace /bin/ls |grep 'openat(AT_FDCWD)' > strace_output.txt")
        print("[*] Strace correctamente ejecutado.")
    except Exception as e: 
        print("ERROR")

    
    try: 
        # ldd /bin/ls |grep ".so"
        possible_module_name = input("[*] Posible nombre de el .so?: ")
        so_module = os.system(f"ldd /bin/ls |grep {possible_module_name}")
        print(f"[*] Resultado de el posible modulo userland: {so_module}")
    
    except Exception as e: 
        print("ERROR")

    
    try: 
        # ps aux |grep server
        detect_server_krux = subprocess.getoutput("ps aux |grep server")
        # Miraremos tambien por sshd
        sshd_detect = subprocess.getoutput("ps aux |grep sshd")
        print(f"[*] Server de Krux: {detect_server_krux}")
        print(f"[*] Deteccion de sshd (posible server): {sshd_detect}") # Se mira sshd por posible ocultacion de nombre de el proceso verdadero

    except Exception as e: 
        print("ERROR")

    
    try:
        # netstat -an |grep 8181
        # Es algo inutil ya que Krux se apoya de Singularity lkm para ocultar conexiones, pero aun así lo pondremos 
        first_netstat = subprocess.getoutput("netstat -an |grep 8181")
        second_netstat = subprocess.getoutput("netstat -an |grep 8081")
        print(f"[*] Netstat en el puerto 8181 (krux userland rk): {first_netstat}")
        print(f"[*] Netstat en el puerto 8081 (singularity lkm rk): {second_netstat}")
    except Exception as e: 
        print("ERROR")




def lkm_detect(): 
    try: 
        # Detect via MAGIC=mtz bash (prives)
        recomendation = """
The command will be executed with the user's assistance.Depending on the result, the system could be infected by an LKM Rootkit.
There are 2 possible results.

1 - That when we execute it, it spawns a new bash with root permissions. (Possible Rk)
2 - Let it run but stay in the same bash with the same permissions. (No rk)

----- INSTRUCTION ------

Base yourself on what comes out after executing the command.

"""
        print(recomendation)
        answer = input("[*] Do you want execute the command?: ")
        if answer == "Yes":
            os.system("MAGIC=mtz bash")
        else: 
            print("[*] Privilege escalation detection rejected.")
    except Exception as e: 
        print("[*] Error.")

    



    try: 
        # Detect via dmesg
        result1 = subprocess.getoutput("dmesg |grep 'singularity'") # Es necesario usar subprocess.getoutput() para no obtener de resultado un numero entero como: 256 o 0
        result2 = subprocess.getoutput("dmesg |grep 'diamorphine'")
        result3 = subprocess.getoutput("dmesg |grep '.ko'")
        print(f"[*] Results of dmesg: {result1}, {result2}, {result3}")  
        answer = input("[*] Do you want grep for syscalls, ioctl etc.. in dmesg?: ")
        if answer == "Yes": 
            output = subprocess.getoutput("dmesg |grep 'syscall'")
            output2 = subprocess.getoutput("dmesg |grep 'ioctl'")
            output3 = subprocess.getoutput("dmesg |grep '__x64_sys'")
            print(f"[*] Syscalls output: {output}\n")
            print(f"[*] IOCTL output: {output2}\n")
            print(f"[*] Symbol of Kernel (__x64_sys) output: {output3}\n")
            print("[*] Syscalls, ioctls communicating, and connections may possibly be intercepted. (POSSIBLE LKM RK)")
        else: 
            print("[-] Operation failed.")

    except Exception as e: 
        print(f"Error: {e}")


    except Exception as e: 
        print("ERROR")          




    try: 
        # Detect via /proc/modules 
        modules_charged = subprocess.getoutput("cat /proc/modules")
        print(f"[*] Modules charged in the system: {modules_charged}")
    except Exception as e: 
        print("ERROR")





    try: 
        # Detect via /sys/kernel/tracing/touched_functions
        with open("/sys/kernel/tracing/touched_functions", "r") as file: 
            content = file.read() 

        print(f"[*] Touched functions: {content}") # Tambien podemos filtrar por syscalls posiblemente hookeadas
    except Exception as e: 
        print("[*] Error.")


# Posible implementacion de nitara2 | MODTRACER



def ftrace_disable(): 
    # We gonna disable ftrace for make ftrace rootkit uselesss
    # This method can fail on some lkm rootkits for his hooks
    try: 
        os.system("echo 0 > /proc/sys/kernel/ftrace_enabled")
        print("[*] Ftrace disabled.")
    except Exception as e: 
        print(f"Error: {e}")

    
    time.sleep(2)

    try:
        with open("/proc/sys/kernel/ftrace_enabled", "w") as f: 
            value = 0
            f.write(value)

        print("[*] Ftrace disabled 2.")

    except Exception as e: 
        print("[*] Error.")


    try: 
        # Another method using pwrite() syscall
        with open("bypass.c", "w") as file: 
            code = """

#include <unistd.h>
#define _XOPEN_SOURCE 500
#include <stdio.h>
#include <sys/syscall.h>
#include <stdlib.h>
#include <fcntl.h> // Necesaria para open()


int main() {
    int fd = open("/proc/sys/kernel/ftrace_enabled", O_WRONLY); 
    if (fd == NULL) {
        printf("ERROR AL ABRIR");
    }

    pwrite(fd, "0", 1, 0)
    // "0" contenido a escribir
    // 1 <- numero de bytes a escribir
    // 0 <- OFFSET

    close(fd); 
    return 0; 
}


"""
        file.write(code)
    
    except Exception as e:
        print("[*] Error")

    
    print("[*] Bypass for ftrace hooks generated.") 
    
    time.sleep(1) # delay

    try:
        path_to_bypass = input("[*] PATH TO BYPASS.C: ")
        compilation_command = f"gcc -o bypass {path_to_bypass}"
        os.system(compilation_command)
        print("[*] Successful compilation.")
    except Exception as e: 
        print("[*] Error.")


    time.sleep(1) # delay

    answer = input("[*] Do you want execute the bypass?: ")
    if answer == "Yes": 
        print("[*] Executing ...")
        time.sleep(1)
        os.system("./bypass")
        print("[*] Check: /proc/sys/kernel/ftrace_enabled")        
    else: 
        print("[*] Operation Failed.")


    



def main(): 
    # Userland rootkit (krux)
    banner()
    time.sleep(1)



    answer = input("[*] Do you want to scan for Krux (userland rk)?: ")
    if answer == "Yes": 
        userland_krux()

    time.sleep(2)


    # LKM DETECT AND FTRACE DISABLE
    answer2 = input("[*] Do you want to scan for LKMs rootkits?: ")
    if answer2 == "Yes":
        lkm_detect() 
        time.sleep(2)
        ftrace_disable = input("[*] Do you want to disable ftrace for make ftrace rk useless?: ")
        if ftrace_disable == "Yes": 
            ftrace_disable()




if __name__ == '__main__': 
    main()