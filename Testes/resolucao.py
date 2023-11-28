from tkinter import Tk, filedialog
from PIL import Image

def change_resolution(image_path, new_width, new_height):
    img = Image.open(image_path)
    img = img.resize((new_width, new_height))
    img.save("Logo_JA_50x50.png")
    print("Nova imagem criada com sucesso!")

def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    file_path = select_image()
    new_width = int(input("Digite a largura desejada da imagem: "))
    new_height = int(input("Digite a altura desejada da imagem: "))
    change_resolution(file_path, new_width, new_height)

if __name__ == "__main__":
    main()
