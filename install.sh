#!/bin/bash

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${RED}"
cat << "EOF"
    ╔═══════════════════════════════════════════╗
    ║   Instalando Mx Social Engineering...    ║
    ║        ¡Prepárate para el poder!         ║
    ╚═══════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y pip
sudo apt install python3 python3-pip git -y

# Instalar dependencias Python
pip3 install -r requirements.txt

# Instalar herramientas adicionales
sudo apt install theharvester maltego recon-ng spiderfoot -y

# Clonar herramientas de phishing (opcional)
git clone https://github.com/htr-tech/zphisher.git
git clone https://github.com/An0nUD4Y/blackeye.git

echo -e "${GREEN}[✓] Instalación completada. Ejecuta: python3 mxse.py${NC}"
