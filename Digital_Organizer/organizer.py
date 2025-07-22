import os

def get_folder_size(folder_path):
    total_size = 0
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            total_size += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total_size += get_folder_size(full_path)
    return total_size / (1024*1024) # Size in MB

def list_files_by_extension(folder_path):

    arquivos = []
    pastas = []

    items = os.listdir(folder_path)
    for name in items:
        full_path = os.path.join(folder_path, name)
        if os.path.isfile(full_path):
            size_mb = os.path.getsize(full_path) / (1024*1024)
            arquivos.append((name, size_mb))
        elif os.path.isdir(full_path):
            size_mb = get_folder_size(full_path)
            pastas.append((name, size_mb))

    arquivos.sort(key=lambda x: x[0].lower())
    pastas.sort(key=lambda x: x[0].lower())
    return arquivos, pastas

def print_formatted_lists(arquivos, pastas):
    print("++++++++++ Arquivos ++++++++++")
    for name, total_size in arquivos:
        print(f"{name} - {total_size:.2f} MB")

    print("++++++++++ Pastas ++++++++++")
    for name, total_size in pastas:
        print(f"{name} - {total_size:.2f} MB")