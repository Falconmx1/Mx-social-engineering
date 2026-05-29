#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[91m" + r"""
    ╔═══════════════════════════════════════════════╗
    ║   ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗██╗  ██╗   ║
    ║   ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝██║  ██║   ║
    ║   █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║███████╗███████║   ║
    ║   ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║╚════██║██╔══██║   ║
    ║   ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████║██║  ██║   ║
    ║   ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ║
    ║                                                           ║
    ║           >>>  Engineering Mx  <<<                       ║
    ║       Toolkit OSINT + Social Engineering v1.0            ║
    ╚═══════════════════════════════════════════════════════════╝
    \033[0m")
    print("\033[91m[!] Solo para uso educativo y audits autorizadas\033[0m\n")

def menu():
    print("\033[91m" + "═" * 55 + "\033[0m")
    print("\033[93m[01] Sherlock\033[0m      \033[94m[17] Phishing Generator\033[0m")
    print("\033[93m[02] Holehe\033[0m         \033[94m[18] Cam Phish\033[0m")
    # ... (agrega las 32 herramientas aquí)
    print("\033[91m" + "═" * 55 + "\033[0m")
    print("\033[91m[99] Salir\033[0m")

def main():
    while True:
        banner()
        menu()
        opcion = input("\n\033[92mMxSE@\033[0m\033[91m~\033[0m$ ")
        if opcion == "99":
            sys.exit(0)
        # Llamar a las herramientas según opción

if __name__ == "__main__":
    main()
