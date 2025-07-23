import os

def get_folder_size(folder_path):
    total_size = 0
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            total_size += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total_size += get_folder_size(full_path)
    return total_size # Size in bytes

def list_files_by_extension(folder_path):

    arquivos = []
    pastas = []

    items = os.listdir(folder_path)
    for name in items:
        full_path = os.path.join(folder_path, name)
        if os.path.isfile(full_path):
            size_bytes = os.path.getsize(full_path)
            arquivos.append((name, size_bytes))
        elif os.path.isdir(full_path):
            size_bytes = get_folder_size(full_path)
            pastas.append((name, size_bytes))

    arquivos.sort(key=lambda x: x[0].lower())
    pastas.sort(key=lambda x: x[0].lower())
    return arquivos, pastas

def print_formatted_lists(arquivos, pastas):
    def format_size(size_bytes):
        if size_bytes >= 1024**3:
            return f"{size_bytes / (1024**3):.2f} GB"
        elif size_bytes >= 1024**2:
            return f"{size_bytes / (1024**2):.2f} MB"
        elif size_bytes >= 1024:
            return f"{size_bytes / 1024:.2f} KB"
        else:
            return f"{size_bytes:.2f} Bytes"

    print("++++++++++ Arquivos ++++++++++")
    for name, total_size in arquivos:
        print(f"{name} - {format_size(total_size)}")

    print("++++++++++ Pastas ++++++++++")
    for name, total_size in pastas:
        print(f"{name} - {format_size(total_size)}")