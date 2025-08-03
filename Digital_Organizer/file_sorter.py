import os
import shutil



def organize_files_by_type(folder_path):

    # Dicionário de tipos de arquivo.
    EXTENSIONS_MAP = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Áudios": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executáveis": [".exe", ".sh", ".bat", ".apk"],
    "Outros": []  # Para arquivos que não se encaixam
}
    