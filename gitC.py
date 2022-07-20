import os
import sys


print("git commit -a -m")
print("git log -p")
print("git diff")
print("git diff --staged")
print("git status")

def check_reboot():
    """Return True if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok")
    sys.exit(0)
main()

##REVERTIR CAMBIOS EN GIT

##git checkout se utiliza para revertir cambios, 
# antes de que se realicen en etapas

## git checkout nombreArchivo
git checkout gitC.py
##Los comentarios no se revierten

##MODIFICANDO COMMITS

# commit --amend
#permite mostrar el mensaje detallado 
# y te muestra toda la information del commit

##Debe de evitarse amend comment para los casos
#  de que el repositorio ya es publico.

git commit --ammend
