#!/bin/bash

echo "Installing Tailwind CSS..."

# Verificar si Node.js está instalado
if ! command -v node &> /dev/null
then
    echo "Node.js no está instalado. Por favor, instala Node.js primero."
    exit 1
fi

# Inicializar npm y instalar Tailwind CSS
npm install -D tailwindcss
npx tailwindcss init
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css

echo "Tailwind CSS installation and configuration complete."
