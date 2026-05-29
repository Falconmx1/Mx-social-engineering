#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
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
    ║         Toolkit OSINT + Social Engineering v1.0                  ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    \033[0m")
    print("\033[91m[!] Solo para uso educativo y audits autorizadas\033[0m\n")

def menu():
    print("\033[91m" + "═" * 70 + "\033[0m")
    print("\033[93m[\033[91m01\033[93m] Sherlock (Usuarios redes)\033[0m     \033[94m[\033[91m17\033[94m] Phishing Generator\033[0m")
    print("\033[93m[\033[91m02\033[93m] Holehe (Email rastreo)\033[0m        \033[94m[\033[91m18\033[94m] BlackEye (Clonación)\033[0m")
    print("\033[93m[\033[91m03\033[93m] theHarvester (Emails/Doms)\033[0m     \033[94m[\033[91m19\033[94m] ShellPhish\033[0m")
    print("\033[93m[\033[91m04\033[93m] Photon (Info web)\033[0m              \033[94m[\033[91m20\033[94m] HiddenEye\033[0m")
    print("\033[93m[\033[91m05\033[93m] Recon-ng\033[0m                       \033[94m[\033[91m21\033[94m] Weeman\033[0m")
    print("\033[93m[\033[91m06\033[93m] Maltego (Transformas)\033[0m           \033[94m[\033[91m22\033[94m] SocialFish\033[0m")
    print("\033[93m[\033[91m07\033[93m] SpiderFoot\033[0m                     \033[94m[\033[91m23\033[94m] NextPhishing\033[0m")
    print("\033[93m[\033[91m08\033[93m] Creepy (Geolocación)\033[0m            \033[94m[\033[91m24\033[94m] FakeLogin\033[0m")
    print("\033[93m[\033[91m09\033[93m] WhatsMyName\033[0m                    \033[94m[\033[91m25\033[94m] Zphisher\033[0m")
    print("\033[93m[\033[91m10\033[93m] Twint (Twitter scraper)\033[0m         \033[94m[\033[91m26\033[94m] AdvPhishing\033[0m")
    print("\033[93m[\033[91m11\033[93m] InstaLooter\033[0m                    \033[94m[\033[91m27\033[94m] King-Phisher\033[0m")
    print("\033[93m[\033[91m12\033[93m] Facebook OSINT\033[0m                 \033[94m[\033[91m28\033[94m] Gophish\033[0m")
    print("\033[93m[\033[91m13\033[93m] GHunt (Google accs)\033[0m             \033[94m[\033[91m29\033[94m] Evilginx2\033[0m")
    print("\033[93m[\033[91m14\033[93m] PhoneInfoga\033[0m                    \033[94m[\033[91m30\033[94m] Modlishka\033[0m")
    print("\033[93m[\033[91m15\033[93m] Infoga (Email OSINT)\033[0m            \033[94m[\033[91m31\033[94m] Social-Engineer Toolkit\033[0m")
    print("\033[93m[\033[91m16\033[93m] Osintgram\033[0m                      \033[94m[\033[91m32\033[94m] EvilURL\033[0m")
    print("\033[91m" + "═" * 70 + "\033[0m")
    print("\033[91m[\033[93m99\033[91m] Salir\033[0m")

def run_tool(tool_name, install_cmd, run_cmd):
    print(f"\033[93m[!] Ejecutando {tool_name}...\033[0m")
    if not os.path.exists(f"/usr/bin/{tool_name.lower()}"):
        print(f"\033[91m[!] {tool_name} no instalado. Instalando...\033[0m")
        os.system(install_cmd)
    os.system(run_cmd)
    input("\n\033[93m[!] Presiona Enter para continuar...\033[0m")

def main():
    while True:
        banner()
        menu()
        opcion = input("\n\033[92m┌─[\033[91mMxSE@Engineering\033[92m]\n└──╼ \033[91m$\033[0m ")
        
        # OSINT Tools (1-16)
        if opcion == "01":
            os.system("sherlock --help || pip install sherlock && sherlock")
        elif opcion == "02":
            os.system("holehe --help || pip install holehe && holehe")
        elif opcion == "03":
            os.system("theHarvester -h || apt install theharvester -y && theharvester")
        elif opcion == "04":
            os.system("photon -h || git clone https://github.com/s0md3v/Photon && cd Photon && python3 photon.py")
        elif opcion == "05":
            os.system("recon-ng || git clone https://github.com/lanmaster53/recon-ng && cd recon-ng && ./recon-ng")
        elif opcion == "06":
            os.system("maltego || echo 'Descarga desde: https://www.maltego.com/download/'")
        elif opcion == "07":
            os.system("spiderfoot -h || git clone https://github.com/smicallef/spiderfoot && cd spiderfoot && python3 sf.py")
        elif opcion == "08":
            os.system("creepy -h || git clone https://github.com/ilektrojohn/creepy && cd creepy && python3 creepy.py")
        elif opcion == "09":
            os.system("whatsmyname || git clone https://github.com/WebBreacher/WhatsMyName && cd WhatsMyName && python3 web_accounts_list_checker.py")
        elif opcion == "10":
            os.system("twint -h || pip install twint && twint")
        elif opcion == "11":
            os.system("instalooter || pip3 install instalooter && instalooter")
        elif opcion == "12":
            os.system("echo 'Usa: https://github.com/harismuneer/Ultimate-Facebook-Scraper'")
        elif opcion == "13":
            os.system("ghunt -h || git clone https://github.com/mxrch/GHunt && cd GHunt && python3 setup.py install")
        elif opcion == "14":
            os.system("phoneinfoga -h || git clone https://github.com/sundowndev/phoneinfoga && cd phoneinfoga && ./phoneinfoga")
        elif opcion == "15":
            os.system("infoga -h || git clone https://github.com/m4ll0k/Infoga && cd Infoga && python3 infoga.py")
        elif opcion == "16":
            os.system("osintgram -h || git clone https://github.com/Datalux/Osintgram && cd Osintgram && python3 main.py")
        
        # Phishing/Social Eng Tools (17-32)
        elif opcion == "17":
            os.system("git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
        elif opcion == "18":
            os.system("git clone https://github.com/An0nUD4Y/blackeye && cd blackeye && bash blackeye.sh")
        elif opcion == "19":
            os.system("git clone https://github.com/thelinuxchoice/shellphish && cd shellphish && bash shellphish.sh")
        elif opcion == "20":
            os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye && cd HiddenEye && python3 HiddenEye.py")
        elif opcion == "21":
            os.system("git clone https://github.com/evait-security/weeman && cd weeman && python2 weeman.py")
        elif opcion == "22":
            os.system("git clone https://github.com/Lucksi/Mr.Holmes && cd Mr.Holmes && bash Mr.Holmes.sh")
        elif opcion == "23":
            os.system("git clone https://github.com/KasRoudra/Phisher && cd Phisher && bash phisher.sh")
        elif opcion == "24":
            os.system("git clone https://github.com/UndeadSec/FakeLogin && cd FakeLogin && python3 fakeLogin.py")
        elif opcion == "25":
            os.system("git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
        elif opcion == "26":
            os.system("git clone https://github.com/Ignitetch/AdvPhishing && cd AdvPhishing && bash AdvPhishing.sh")
        elif opcion == "27":
            os.system("git clone https://github.com/rsmusllp/king-phisher && cd king-phisher && ./setup.sh")
        elif opcion == "28":
            os.system("echo 'Gophish: https://getgophish.com/' && wget https://github.com/gophish/gophish/releases/latest/download/gophish-linux-64bit.zip")
        elif opcion == "29":
            os.system("git clone https://github.com/kgretzky/evilginx2 && cd evilginx2 && make && sudo make install")
        elif opcion == "30":
            os.system("git clone https://github.com/aryanguenth/Modlishka && cd Modlishka && go build")
        elif opcion == "31":
            os.system("git clone https://github.com/trustedsec/social-engineer-toolkit && cd social-engineer-toolkit && python setup.py")
        elif opcion == "32":
            os.system("git clone https://github.com/UndeadSec/EvilURL && cd EvilURL && python3 evilurl.py")
        
        elif opcion == "99":
            print("\033[91m[!] Saliendo...\033[0m")
            sys.exit(0)
        else:
            print("\033[91m[!] Opción no válida\033[0m")
            input("Presiona Enter...")

if __name__ == "__main__":
    main()
