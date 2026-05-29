#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import platform
import time

def clear_screen():
    os.system('clear' if platform.system() != 'Windows' else 'cls')

def banner():
    clear_screen()
    print("\033[91m" + r"""
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║   ███╗   ███╗██╗  ██╗    ███████╗ ██████╗ ██████╗ ██╗███████╗    ║
    ║   ████╗ ████║╚██╗██╔╝    ██╔════╝██╔════╝██╔═══██╗██║██╔════╝    ║
    ║   ██╔████╔██║ ╚███╔╝     ███████╗██║     ██║   ██║██║█████╗      ║
    ║   ██║╚██╔╝██║ ██╔██╗     ╚════██║██║     ██║   ██║██║██╔══╝      ║
    ║   ██║ ╚═╝ ██║██╔╝ ██╗    ███████║╚██████╗╚██████╔╝██║███████╗    ║
    ║   ╚═╝     ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝    ║
    ║                                                                   ║
    ║              >>>  E N G I N E E R I N G   M X  <<<               ║
    ║         Toolkit OSINT + Social Engineering v3.0                  ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    \033[0m")
    print("\033[91m[!] Solo para uso educativo y auditorías autorizadas\033[0m")
    print("\033[93m[✓] Versión estable para Ubuntu 22.04/24.04\033[0m\n")

def check_and_clone(repo_url, folder_name):
    """Clona un repo si no existe"""
    if not os.path.exists(folder_name):
        print(f"\033[93m[!] Clonando {folder_name}...\033[0m")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, folder_name], 
                      capture_output=True)
        return True
    return False

def run_bash_tool(folder, script, params=""):
    """Ejecuta herramientas bash"""
    if check_and_clone(folder, folder):
        print(f"\033[92m[✓] Herramienta instalada\033[0m")
    subprocess.run(f"cd {folder} && bash {script} {params}", shell=True)

# ==================== HERRAMIENTAS OSINT (FUNCIONALES) ====================

def tool_sherlock():
    """Busca usuarios en redes - Versión standalone"""
    check_and_clone("https://github.com/sherlock-project/sherlock.git", "sherlock")
    username = input("\033[92m[*] Nombre de usuario: \033[0m")
    subprocess.run(["python3", "sherlock/sherlock.py", username])

def tool_phoneinfoga():
    """Información de números telefónicos"""
    check_and_clone("https://github.com/sundowndev/phoneinfoga", "phoneinfoga")
    number = input("\033[92m[*] Número (ej: +521234567890): \033[0m")
    subprocess.run(["./phoneinfoga/phoneinfoga", "scan", "-n", number])

def tool_theharvester():
    """Recolecta emails y subdominios"""
    if not os.path.exists("theHarvester"):
        subprocess.run(["sudo", "apt", "install", "theharvester", "-y"])
    domain = input("\033[92m[*] Dominio objetivo: \033[0m")
    subprocess.run(["theharvester", "-d", domain, "-b", "all"])

def tool_photon():
    """Extrae información de webs"""
    check_and_clone("https://github.com/s0md3v/Photon", "Photon")
    url = input("\033[92m[*] URL objetivo: \033[0m")
    subprocess.run(["python3", "Photon/photon.py", "-u", url])

def tool_whatsmyname():
    """Busca usuarios en múltiples plataformas"""
    check_and_clone("https://github.com/WebBreacher/WhatsMyName", "WhatsMyName")
    username = input("\033[92m[*] Username: \033[0m")
    subprocess.run(["python3", "WhatsMyName/web_accounts_list_checker.py", "-u", username])

def tool_osintgram():
    """OSINT en Instagram"""
    check_and_clone("https://github.com/Datalux/Osintgram", "Osintgram")
    username = input("\033[92m[*] Usuario de Instagram: \033[0m")
    subprocess.run(["python3", "Osintgram/main.py", username])

def tool_infoga():
    """Email OSINT"""
    check_and_clone("https://github.com/m4ll0k/Infoga", "Infoga")
    email = input("\033[92m[*] Email: \033[0m")
    subprocess.run(["python3", "Infoga/infoga.py", "--email", email])

def tool_spiderfoot():
    """Framework OSINT con interfaz web"""
    check_and_clone("https://github.com/smicallef/spiderfoot", "spiderfoot")
    print("\033[92m[✓] SpiderFoot iniciando en http://127.0.0.1:5001\033[0m")
    subprocess.run(["python3", "spiderfoot/sf.py", "-l", "127.0.0.1:5001"])

def tool_reconng():
    """Framework Recon-ng"""
    if not os.path.exists("recon-ng"):
        subprocess.run(["git", "clone", "https://github.com/lanmaster53/recon-ng"])
    subprocess.run(["cd recon-ng && ./recon-ng"], shell=True)

def tool_creepy():
    """Geolocalización"""
    check_and_clone("https://github.com/ilektrojohn/creepy", "creepy")
    subprocess.run(["python3", "creepy/creepy.py"])

# ==================== HERRAMIENTAS PHISHING (100% FUNCIONALES) ====================

def tool_zphisher():
    """ZPhisher - La mejor herramienta de phishing"""
    run_bash_tool("https://github.com/htr-tech/zphisher", "zphisher.sh")

def tool_blackeye():
    """BlackEye - Clonador de sitios"""
    run_bash_tool("https://github.com/An0nUD4Y/blackeye", "blackeye.sh")

def tool_shellphish():
    """ShellPhish - Phishing avanzado"""
    run_bash_tool("https://github.com/thelinuxchoice/shellphish", "shellphish.sh")

def tool_hiddeneye():
    """HiddenEye - Framework completo"""
    check_and_clone("https://github.com/DarkSecDevelopers/HiddenEye", "HiddenEye")
    subprocess.run(["python3", "HiddenEye/HiddenEye.py"])

def tool_weeman():
    """Weeman - Clonador HTTP"""
    check_and_clone("https://github.com/evait-security/weeman", "weeman")
    subprocess.run(["python2", "weeman/weeman.py"])

def tool_socialfish():
    """SocialFish - Phishing redes sociales"""
    check_and_clone("https://github.com/UndeadSec/SocialFish", "SocialFish")
    subprocess.run(["python3", "SocialFish/SocialFish.py"])

def tool_evilginx2():
    """Evilginx2 - Proxy phishing avanzado"""
    if not os.path.exists("evilginx2"):
        subprocess.run(["git", "clone", "https://github.com/kgretzky/evilginx2"])
    print("\033[93m[*] Para instalar Evilginx2 ejecuta:\033[0m")
    print("cd evilginx2 && make && sudo make install")

def tool_setoolkit():
    """Social-Engineer Toolkit (SET)"""
    if not os.path.exists("social-engineer-toolkit"):
        subprocess.run(["git", "clone", "https://github.com/trustedsec/social-engineer-toolkit"])
    subprocess.run(["python3", "social-engineer-toolkit/setoolkit"])

def tool_fakelogin():
    """FakeLogin - Generador de logins falsos"""
    check_and_clone("https://github.com/UndeadSec/FakeLogin", "FakeLogin")
    subprocess.run(["python3", "FakeLogin/fakeLogin.py"])

def tool_camphish():
    """CamPhish - Captura de cámara"""
    run_bash_tool("https://github.com/techchipnet/CamPhish", "camphish.sh")

def tool_nexphisher():
    """NexPhisher - Phishing avanzado"""
    run_bash_tool("https://github.com/KasRoudra/Phisher", "phisher.sh")

def tool_advphishing():
    """AdvPhishing - Phishing con ngrok"""
    run_bash_tool("https://github.com/Ignitetch/AdvPhishing", "AdvPhishing.sh")

def tool_kingphisher():
    """King-Phisher - Suite profesional"""
    if not os.path.exists("king-phisher"):
        subprocess.run(["git", "clone", "https://github.com/rsmusllp/king-phisher"])
    subprocess.run(["cd king-phisher && ./setup.sh"], shell=True)

def tool_gophish():
    """Gophish - Framework empresarial"""
    print("\033[93m[*] Descargando Gophish...\033[0m")
    subprocess.run(["wget", "https://github.com/gophish/gophish/releases/latest/download/gophish-linux-64bit.zip"])
    subprocess.run(["unzip", "gophish-linux-64bit.zip"])

def tool_evilurl():
    """EvilURL - Generador de URLs engañosas"""
    check_and_clone("https://github.com/UndeadSec/EvilURL", "EvilURL")
    subprocess.run(["python3", "EvilURL/evilurl.py"])

def tool_modlishka():
    """Modlishka - Reverse proxy"""
    if not os.path.exists("Modlishka"):
        subprocess.run(["git", "clone", "https://github.com/aryanguenth/Modlishka"])
    print("\033[93m[*] Requiere Go. Instrucciones en README de Modlishka\033[0m")

# ==================== MENÚ PRINCIPAL ====================

def menu():
    print("\033[91m" + "═" * 75 + "\033[0m")
    print("\033[93m║ \033[91mOSINT TOOLS (1-12)\033[93m                          ║ \033[91mPHISHING TOOLS (13-28)\033[93m")
    print("\033[91m" + "─" * 75 + "\033[0m")
    print("\033[93m[\033[91m01\033[93m] Sherlock\033[0m          \033[94m[\033[91m13\033[94m] ZPhisher ⭐\033[0m")
    print("\033[93m[\033[91m02\033[93m] PhoneInfoga\033[0m       \033[94m[\033[91m14\033[94m] BlackEye\033[0m")
    print("\033[93m[\033[91m03\033[93m] theHarvester\033[0m      \033[94m[\033[91m15\033[94m] ShellPhish\033[0m")
    print("\033[93m[\033[91m04\033[93m] Photon\033[0m            \033[94m[\033[91m16\033[94m] HiddenEye\033[0m")
    print("\033[93m[\033[91m05\033[93m] WhatsMyName\033[0m       \033[94m[\033[91m17\033[94m] Weeman\033[0m")
    print("\033[93m[\033[91m06\033[93m] Osintgram\033[0m         \033[94m[\033[91m18\033[94m] SocialFish\033[0m")
    print("\033[93m[\033[91m07\033[93m] Infoga\033[0m            \033[94m[\033[91m19\033[94m] Evilginx2\033[0m")
    print("\033[93m[\033[91m08\033[93m] SpiderFoot\033[0m        \033[94m[\033[91m20\033[94m] SEToolkit\033[0m")
    print("\033[93m[\033[91m09\033[93m] Recon-ng\033[0m          \033[94m[\033[91m21\033[94m] FakeLogin\033[0m")
    print("\033[93m[\033[91m10\033[93m] Creepy\033[0m            \033[94m[\033[91m22\033[94m] CamPhish\033[0m")
    print("\033[93m[\033[91m11\033[93m] GHunt (Google)\033[0m     \033[94m[\033[91m23\033[94m] NexPhisher\033[0m")
    print("\033[93m[\033[91m12\033[93m] InstaLooter\033[0m       \033[94m[\033[91m24\033[94m] AdvPhishing\033[0m")
    print("\033[93m            \033[94m[\033[91m25\033[94m] King-Phisher\033[0m")
    print("\033[93m            \033[94m[\033[91m26\033[94m] Gophish\033[0m")
    print("\033[93m            \033[94m[\033[91m27\033[94m] EvilURL\033[0m")
    print("\033[93m            \033[94m[\033[91m28\033[94m] Modlishka\033[0m")
    print("\033[91m" + "═" * 75 + "\033[0m")
    print("\033[91m[\033[93m99\033[91m] Salir\033[0m                    \033[91m[\033[93m00\033[91m] Instalar todas las herramientas\033[0m")

def install_all():
    """Instala todas las herramientas de una vez"""
    print("\033[91m[!] Instalando todas las herramientas... Esto puede tardar varios minutos\033[0m")
    
    osint_tools = [
        "https://github.com/sherlock-project/sherlock.git",
        "https://github.com/sundowndev/phoneinfoga",
        "https://github.com/s0md3v/Photon",
        "https://github.com/WebBreacher/WhatsMyName",
        "https://github.com/Datalux/Osintgram",
        "https://github.com/m4ll0k/Infoga",
        "https://github.com/smicallef/spiderfoot"
    ]
    
    phishing_tools = [
        "https://github.com/htr-tech/zphisher",
        "https://github.com/An0nUD4Y/blackeye",
        "https://github.com/thelinuxchoice/shellphish",
        "https://github.com/DarkSecDevelopers/HiddenEye",
        "https://github.com/UndeadSec/SocialFish",
        "https://github.com/UndeadSec/FakeLogin"
    ]
    
    for repo in osint_tools + phishing_tools:
        name = repo.split("/")[-1].replace(".git", "")
        check_and_clone(repo, name)
    
    print("\033[92m[✓] Instalación completada\033[0m")
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        banner()
        menu()
        opcion = input("\n\033[92m┌─[\033[91mMxSE@Engineering\033[92m]\n└──╼ \033[91m$\033[0m ")
        
        # OSINT Tools (1-12)
        if opcion == "01": tool_sherlock()
        elif opcion == "02": tool_phoneinfoga()
        elif opcion == "03": tool_theharvester()
        elif opcion == "04": tool_photon()
        elif opcion == "05": tool_whatsmyname()
        elif opcion == "06": tool_osintgram()
        elif opcion == "07": tool_infoga()
        elif opcion == "08": tool_spiderfoot()
        elif opcion == "09": tool_reconng()
        elif opcion == "10": tool_creepy()
        elif opcion == "11": print("\033[93m[*] GHunt: cd GHunt && python3 setup.py install\033[0m")
        elif opcion == "12": subprocess.run(["pip3", "install", "instalooter"])
        
        # Phishing Tools (13-28)
        elif opcion == "13": tool_zphisher()
        elif opcion == "14": tool_blackeye()
        elif opcion == "15": tool_shellphish()
        elif opcion == "16": tool_hiddeneye()
        elif opcion == "17": tool_weeman()
        elif opcion == "18": tool_socialfish()
        elif opcion == "19": tool_evilginx2()
        elif opcion == "20": tool_setoolkit()
        elif opcion == "21": tool_fakelogin()
        elif opcion == "22": tool_camphish()
        elif opcion == "23": tool_nexphisher()
        elif opcion == "24": tool_advphishing()
        elif opcion == "25": tool_kingphisher()
        elif opcion == "26": tool_gophish()
        elif opcion == "27": tool_evilurl()
        elif opcion == "28": tool_modlishka()
        elif opcion == "00": install_all()
        elif opcion == "99":
            print("\033[91m[!] Saliendo...\033[0m")
            sys.exit(0)
        else:
            print("\033[91m[!] Opción no válida\033[0m")
        
        input("\n\033[93m[!] Presiona Enter para continuar...\033[0m")

if __name__ == "__main__":
    main()
