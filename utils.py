import os
import platform

def limpar_tela():
    """
    Limpa o terminal, independentemente do sistema operacional.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')