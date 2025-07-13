#!/usr/bin/env python3
import subprocess

# Ejecuta el flujo: mapper -> sort -> reducer
command = "type input.txt | python mapper.py | sort | python reducer.py"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

# Imprime la salida
for line in process.stdout:
    print(line.decode().strip())