import subprocess
import sys

def check_installation(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", package])
    except subprocess.CalledProcessError:
        return False
    return True

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def instala_biblioteca():
    packages_to_check = ['geocoder', 'mysql-connector-python']

    for package in packages_to_check:
        if not check_installation(package):
            print(f"{package} não está instalado. Instalando...")
            install_package(package)
            print(f"{package} instalado com sucesso!")

    print("Verificação completa.")

if __name__ == "__main__":
    instala_biblioteca()
