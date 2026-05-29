#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import importlib.util
import pkgutil
import platform

def clear_screen():
    os.system('clear' if platform.system() != 'Windows' else 'cls')

def check_and_install(package, pip_name=None):
    if pip_name is None:
        pip_name = package
    if importlib.util.find_spec(package) is None:
        print(f"\033[93m[!] Instalando {package}...\033[0m")
        subprocess.run([sys.executable, "-m", "pip", "install", pip_name], capture_output=True)
        return False
    return True

def run_python_tool(module_name, function_name, *args):
    try:
        module = __import__(module_name)
        if hasattr(module, function_name):
            func = getattr(module, function_name)
            func(*args)
        else:
            print(f"\033[91m[!] Función {function_name} no encontrada\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")

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
    ║         Toolkit OSINT + Social Engineering v2.0                  ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    \033[0m")
    print("\033[91m[!] Solo para uso educativo y auditorías autorizadas\033[0m\n")

# ==================== HERRAMIENTAS QUE SÍ JALAN ====================

def tool_sherlock():
    """Busca usuarios en redes sociales"""
    check_and_install("sherlock_project", "sherlock-project")
    username = input("\033[92m[*] Nombre de usuario: \033[0m")
    subprocess.run([sys.executable, "-m", "sherlock", username])

def tool_holehe():
    """Verifica emails en sitios web"""
    check_and_install("holehe", "holehe")
    email = input("\033[92m[*] Email a verificar: \033[0m")
    from holehe import core
    core.holehe([email])

def tool_phoneinfoga():
    """Información de números telefónicos"""
    if not os.path.exists("phoneinfoga"):
        subprocess.run(["git", "clone", "https://github.com/sundowndev/phoneinfoga"])
    number = input("\033[92m[*] Número (ej: +521234567890): \033[0m")
    subprocess.run(["./phoneinfoga/phoneinfoga", "scan", "-n", number])

def tool_theharvester():
    """Recolecta emails, subdominios, etc"""
    subprocess.run(["theharvester", "-h"] if os.system("which theharvester") == 0 
                   else ["sudo", "apt", "install", "theharvester", "-y"])

def tool_photon():
    """Extrae información de webs"""
    if not os.path.exists("Photon"):
        subprocess.run(["git", "clone", "https://github.com/s0md3v/Photon"])
    url = input("\033[92m[*] URL objetivo: \033[0m")
    subprocess.run(["python3", "Photon/photon.py", "-u", url])

def tool_zphisher():
    """Phishing con 30+ templates (la más chingona)"""
    if not os.path.exists("zphisher"):
        subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher"])
    subprocess.run(["bash", "zphisher/zphisher.sh"])

def tool_blackeye():
    """Clonador de páginas para phishing"""
    if not os.path.exists("blackeye"):
        subprocess.run(["git", "clone", "https://github.com/An0nUD4Y/blackeye"])
    subprocess.run(["bash", "blackeye/blackeye.sh"])

def tool_shellphish():
    """Otra herramienta de phishing"""
    if not os.path.exists("shellphish"):
        subprocess.run(["git", "clone", "https://github.com/thelinuxchoice/shellphish"])
    subprocess.run(["bash", "shellphish/shellphish.sh"])

def tool_hiddeneye():
    """Framework completo de phishing"""
    if not os.path.exists("HiddenEye"):
        subprocess.run(["git", "clone", "https://github.com/DarkSecDevelopers/HiddenEye"])
    subprocess.run(["python3", "HiddenEye/HiddenEye.py"])

def tool_weeman():
    """Clonador HTTP simple pero efectivo"""
    if not os.path.exists("weeman"):
        subprocess.run(["git", "clone", "https://github.com/evait-security/weeman"])
    subprocess.run(["python2", "weeman/weeman.py"])

def tool_socialfish():
    """Phishing para redes sociales"""
    if not os.path.exists("SocialFish"):
        subprocess.run(["git", "clone", "https://github.com/UndeadSec/SocialFish"])
    subprocess.run(["python3", "SocialFish/SocialFish.py"])

def tool_whatsmyname():
    """Usuarios en múltiples plataformas"""
    if not os.path.exists("WhatsMyName"):
        subprocess.run(["git", "clone", "https://github.com/WebBreacher/WhatsMyName"])
    username = input("\033[92m[*] Username: \033[0m")
    subprocess.run(["python3", "WhatsMyName/web_accounts_list_checker.py", "-u", username])

def tool_osintgram():
    """OSINT en Instagram"""
    if not os.path.exists("Osintgram"):
        subprocess.run(["git", "clone", "https://github.com/Datalux/Osintgram"])
    username = input("\033[92m[*] Usuario de Instagram: \033[0m")
    subprocess.run(["python3", "Osintgram/main.py", username])

def tool_infoga():
    """Email OSINT avanzado"""
    if not os.path.exists("Infoga"):
        subprocess.run(["git", "clone", "https://github.com/m4ll0k/Infoga"])
    email = input("\033[92m[*] Email: \033[0m")
    subprocess.run(["python3", "Infoga/infoga.py", "--email", email])

def tool_twint():
    """Scraper de Twitter sin API"""
    check_and_install("twint", "twint")
    username = input("\033[92m[*] Usuario de Twitter: \033[0m")
    subprocess.run([sys.executable, "-m", "twint", "-u", username])

def tool_creepy():
    """Geolocalización a partir de redes"""
    if not os.path.exists("creepy"):
        subprocess.run(["git", "clone", "https://github.com/ilektrojohn/creepy"])
    subprocess.run(["python3", "creepy/creepy.py"])

def tool_spiderfoot():
    """Automatización OSINT con web UI"""
    if not os.path.exists("spiderfoot"):
        subprocess.run(["git", "clone", "https://github.com/smicallef/spiderfoot"])
    subprocess.run(["python3", "spiderfoot/sf.py", "-l", "127.0.0.1:5001"])
    print("\033[92m[*] SpiderFoot corriendo en http://127.0.0.1:5001\033[0m")

def tool_evilginx2():
    """Proxy phishing avanzado (requiere Go)"""
    if not os.path.exists("evilginx2"):
        subprocess.run(["git", "clone", "https://github.com/kgretzky/evilginx2"])
    print("\033[93m[*] Instrucciones: cd evilginx2 && make && sudo make install\033[0m")

def tool_setoolkit():
    """Social-Engineer Toolkit (la OG)"""
    if not os.path.exists("social-engineer-toolkit"):
        subprocess.run(["git", "clone", "https://github.com/trustedsec/social-engineer-toolkit"])
    subprocess.run(["python3", "social-engineer-toolkit/setoolkit"])

# ==================== MENÚ PRINCIPAL ====================

def menu():
    print("\033[91m" + "═" * 70 + "\033[0m")
    print("\033[93m║ \033[91mOSINT TOOLS\033[93m                                ║ \033[91mPHISHING TOOLS\033[93m")
    print("\033[91m" + "─" * 70 + "\033[0m")
    print("\033[93m[\033[91m01\033[93m] Sherlock\033[0m          \033[94m[\033[91m17\033[94m] ZPhisher (TOP)\033[0m")
    print("\033[93m[\033[91m02\033[93m] Holehe\033[0m             \033[94m[\033[91m18\033[94m] BlackEye\033[0m")
    print("\033[93m[\033[91m03\033[93m] PhoneInfoga\033[0m        \033[94m[\033[91m19\033[94m] ShellPhish\033[0m")
    print("\033[93m[\033[91m04\033[93m] theHarvester\033[0m       \033[94m[\033[91m20\033[94m] HiddenEye\033[0m")
    print("\033[93m[\033[91m05\033[93m] Photon\033[0m              \033[94m[\033[91m21\033[94m] Weeman\033[0m")
    print("\033[93m[\033[91m06\033[93m] WhatsMyName\033[0m        \033[94m[\033[91m22\033[94m] SocialFish\033[0m")
    print("\033[93m[\033[91m07\033[93m] Osintgram\033[0m          \033[94m[\033[91m23\033[94m] Evilginx2\033[0m")
    print("\033[93m[\033[91m08\033[93m] Infoga\033[0m             \033[94m[\033[91m24\033[94m] SET (Social-Engineer)\033[0m")
    print("\033[93m[\033[91m09\033[93m] Twint (Twitter)\033[0m     \033[94m[\033[91m25\033[94m] FakeLogin\033[0m")
    print("\033[93m[\033[91m10\033[93m] Creepy (Geo)\033[0m        \033[94m[\033[91m26\033[94m] AdvPhishing\033[0m")
    print("\033[93m[\033[91m11\033[93m] SpiderFoot\033[0m         \033[94m[\033[91m27\033[94m] King-Phisher\033[0m")
    print("\033[93m[\033[91m12\033[93m] Recon-ng\033[0m           \033[94m[\033[91m28\033[94m] Gophish\033[0m")
    print("\033[93m[\033[91m13\033[93m] Maltego\033[0m            \033[94m[\033[91m29\033[94m] Modlishka\033[0m")
    print("\033[93m[\033[91m14\033[93m] GHunt (Google)\033[0m      \033[94m[\033[91m30\033[94m] EvilURL\033[0m")
    print("\033[93m[\033[91m15\033[93m] InstaLooter\033[0m        \033[94m[\033[91m31\033[94m] NexPhisher\033[0m")
    print("\033[93m[\033[91m16\033[93m] Facebook OSINT\033[0m      \033[94m[\033[91m32\033[94m] CamPhish\033[0m")
    print("\033[91m" + "═" * 70 + "\033[0m")
    print("\033[91m[\033[93m99\033[91m] Salir\033[0m                    \033[91m[\033[93m00\033[91m] Instalar todo\033[0m")

def install_all():
    print("\033[91m[!] Instalando todas las herramientas... Esto puede tardar\033[0m")
    tools_to_clone = [
        "https://github.com/htr-tech/zphisher",
        "https://github.com/An0nUD4Y/blackeye",
        "https://github.com/thelinuxchoice/shellphish",
        "https://github.com/DarkSecDevelopers/HiddenEye",
        "https://github.com/sundowndev/phoneinfoga",
        "https://github.com/s0md3v/Photon",
        "https://github.com/WebBreacher/WhatsMyName",
        "https://github.com/Datalux/Osintgram",
        "https://github.com/m4ll0k/Infoga"
    ]
    for repo in tools_to_clone:
        name = repo.split("/")[-1]
        if not os.path.exists(name):
            subprocess.run(["git", "clone", repo])
    subprocess.run([sys.executable, "-m", "pip", "install", "sherlock-project", "holehe", "twint"])
    print("\033[92m[✓] Instalación completada\033[0m")

def main():
    while True:
        banner()
        menu()
        opcion = input("\n\033[92m┌─[\033[91mMxSE@Engineering\033[92m]\n└──╼ \033[91m$\033[0m ")
        
        # OSINT (1-16)
        if opcion == "01": tool_sherlock()
        elif opcion == "02": tool_holehe()
        elif opcion == "03": tool_phoneinfoga()
        elif opcion == "04": tool_theharvester()
        elif opcion == "05": tool_photon()
        elif opcion == "06": tool_whatsmyname()
        elif opcion == "07": tool_osintgram()
        elif opcion == "08": tool_infoga()
        elif opcion == "09": tool_twint()
        elif opcion == "10": tool_creepy()
        elif opcion == "11": tool_spiderfoot()
        elif opcion == "12": print("\033[93m[*] Ejecuta: cd recon-ng && ./recon-ng\033[0m")
        elif opcion == "13": print("\033[93m[*] Maltego: https://www.maltego.com/download/\033[0m")
        elif opcion == "14": print("\033[93m[*] GHunt: cd GHunt && python3 setup.py install\033[0m")
        elif opcion == "15": subprocess.run(["pip3", "install", "instalooter"])
        elif opcion == "16": print("\033[93m[*] Facebook OSINT: https://github.com/harismuneer/Ultimate-Facebook-Scraper\033[0m")
        
        # Phishing (17-32)
        elif opcion == "17": tool_zphisher()
        elif opcion == "18": tool_blackeye()
        elif opcion == "19": tool_shellphish()
        elif opcion == "20": tool_hiddeneye()
        elif opcion == "21": tool_weeman()
        elif opcion == "22": tool_socialfish()
        elif opcion == "23": tool_evilginx2()
        elif opcion == "24": tool_setoolkit()
        elif opcion == "25": print("\033[93m[*] FakeLogin: git clone https://github.com/UndeadSec/FakeLogin\033[0m")
        elif opcion == "26": print("\033[93m[*] AdvPhishing: git clone https://github.com/Ignitetch/AdvPhishing\033[0m")
        elif opcion == "27": print("\033[93m[*] King-Phisher: git clone https://github.com/rsmusllp/king-phisher\033[0m")
        elif opcion == "28": print("\033[93m[*] Gophish: https://getgophish.com/\033[0m")
        elif opcion == "29": print("\033[93m[*] Modlishka: git clone https://github.com/aryanguenth/Modlishka\033[0m")
        elif opcion == "30": print("\033[93m[*] EvilURL: git clone https://github.com/UndeadSec/EvilURL\033[0m")
        elif opcion == "31": print("\033[93m[*] NexPhisher: git clone https://github.com/KasRoudra/Phisher\033[0m")
        elif opcion == "32": print("\033[93m[*] CamPhish: git clone https://github.com/techchipnet/CamPhish\033[0m")
        elif opcion == "00": install_all()
        elif opcion == "99":
            print("\033[91m[!] Saliendo...\033[0m")
            sys.exit(0)
        else:
            print("\033[91m[!] Opción no válida\033[0m")
        
        input("\n\033[93m[!] Presiona Enter para continuar...\033[0m")

if __name__ == "__main__":
    main()
