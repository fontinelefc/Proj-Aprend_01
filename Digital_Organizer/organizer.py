import os


def list_files_by_extension(folder_path):

    arquivos = []
    pastas = []

    items = os.listdir(folder_path)
    for name in items:
        full_path = os.path.join(folder_path, name)
        if os.path.isfile(full_path):
            arquivos.append(name)
            arquivos.sort()
        if os.path.isdir(full_path):
            pastas.append(name)
            pastas.sort()
    
    print('++++++++++','Arquivos:','++++++++++')
    for file in arquivos:
        full_path = os.path.join(folder_path, file)
        size = os.path.getsize(full_path) / 1024  # Size in KB
        print(f"{file} - {size:.2f} KB")

    print('++++++++++','Pastas:','++++++++++')
    for folder in pastas:
        full_path = os.path.join(folder_path, folder)
        size = os.path.getsize(full_path) / 1024  # Size in KB
        print(f"{folder} - {size:.2f} KB")
