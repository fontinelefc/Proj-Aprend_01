import os

from organizer import list_files_by_extension, print_formatted_lists

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta: ")
    arquivos, pastas = list_files_by_extension(caminho)
    print_formatted_lists(arquivos, pastas)
