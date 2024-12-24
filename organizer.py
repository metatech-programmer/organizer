import ctypes
import sys
import shutil
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import platform
import subprocess

currentRoute = os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    """Obtiene la ruta absoluta de los recursos."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def formatRoute(route):
    clean = ""
    for caracter in route:
        if caracter == '\\':
            clean = clean + '/'
        else:
            clean = clean + caracter

    return clean

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        global currentRoute
        currentRoute = formatRoute(folder_path)
        route_label.config(text=currentRoute)
        enable_buttons()  # Habilitar botones

def rename_if_duplicate(destination, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(destination, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

def create_directory(path):
    """Crea un directorio si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files():
    currentFolder = formatRoute(currentRoute) + '/'
    organized_files = os.path.join(currentFolder, 'archivos_organizados')
    unknown_files = os.path.join(organized_files, 'desconocidos')  # Carpeta para archivos desconocidos
    folders = os.path.join(organized_files, 'folders')  # Carpeta para carpetas existentes

    # Crear carpetas organizadas
    create_directory(organized_files)
    create_directory(unknown_files)  # Crear carpeta de desconocidos
    create_directory(folders)  # Crear carpeta para carpetas existentes

    # Crear subcarpetas para organización
    subfolders = ['imagenes', 'audios', 'videos', 'powerpoints', 'programas', "rar's", 'word', 'txt', 'pdf', 'excel', 'programing', 'adobe']
    for subfolder in subfolders:
        create_directory(os.path.join(organized_files, subfolder))

    print("Iniciando organización...")
    total_files = len(os.listdir(currentFolder))
    progress_bar["maximum"] = total_files  # Establecer el máximo de la barra de progreso
    progress_bar["value"] = 0  # Reiniciar la barra de progreso

    for index, filename in enumerate(os.listdir(currentFolder)):
        try:
            name, extension = os.path.splitext(filename)
            full_path = os.path.join(currentFolder, filename)

            if os.path.isdir(full_path):
                # Verificar que no sea la carpeta de archivos organizados
                if full_path != organized_files:
                    # Mover carpetas existentes a la carpeta "folders"
                    shutil.move(full_path, os.path.join(folders, filename))
                continue  # Saltar al siguiente archivo

            # Clasificación de archivos
            if extension in [".jpg", ".jpeg", ".png", ".gif", ".ico", ".webp", ".bmp", ".tiff", ".raw", ".exif", ".heif", ".avif", ".svg", ".ico", ".jfif", ".pjpeg", ".pjp", ".webp", ".tiff", ".tif", ".psd", ".eps", ".ai", ".indd", ".svgz", ".ai", ".indd", ".svgz"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'imagenes'), filename)
                os.rename(full_path, os.path.join(organized_files, 'imagenes', new_filename))

            elif extension in [".mp3", ".wav", ".flac", ".aac", ".m4a", ".wma", ".ogg", ".opus", ".alac", ".aiff", ".dsd", ".m3u", ".m3u8", ".m4a", ".wma", ".ape", ".cda", ".aac", ".aiff", ".dsd", ".m3u", ".m3u8", ".m4a", ".wma", ".ape", ".cda"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'audios'), filename)
                os.rename(full_path, os.path.join(organized_files, 'audios', new_filename))

            elif extension in [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".m4v", ".mpg", ".mp2", ".mpe", ".mpv", ".ogv", ".ogg", ".qt", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".m4v", ".mpg", ".mp2", ".mpe", ".mpv", ".ogv", ".ogg", ".qt", ".mkv"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'videos'), filename)
                os.rename(full_path, os.path.join(organized_files, 'videos', new_filename))

            elif extension in [".ppt", ".pptx", ".pps", ".ppsx", ".key", ".odp", ".odt", ".rtf", ".wps", ".doc", ".docx", ".dot", ".dotx", ".odt", ".rtf", ".wps", ".doc", ".docx", ".dot", ".dotx", ".odt", ".rtf", ".wps"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'powerpoints'), filename)
                os.rename(full_path, os.path.join(organized_files, 'powerpoints', new_filename))

            elif extension in [".exe", ".dmg", ".app", ".deb", ".rpm", ".msi", ".bat", ".sh", ".iso", ".torrent", ".apk", ".jar", ".rmskin", ".appinstaller", ".msu", ".run", ".xps", ".apk", ".jar", ".rmskin", ".appinstaller", ".msu", ".run", ".xps"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'programas'), filename)
                os.rename(full_path, os.path.join(organized_files, 'programas', new_filename))

            elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".ace", ".cab", ".lzh", ".lha", ".arj", ".zoo", ".iso", ".xz", ".ace", ".cab", ".lzh", ".lha", ".arj", ".zoo", ".iso"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, "rar's"), filename)
                os.rename(full_path, os.path.join(organized_files, "rar's", new_filename))

            elif extension in [".doc", ".docx", ".dot", ".dotx", ".odt", ".rtf", ".wps", ".gan", ".key", ".odp", ".odt", ".rtf", ".wps", ".doc", ".docx", ".dot", ".dotx", ".odt", ".rtf", ".wps", ".gan", ".key", ".odp", ".odt", ".rtf", ".wps"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'word'), filename)
                os.rename(full_path, os.path.join(organized_files, 'word', new_filename))

            elif extension in [".txt", ".md", ".rtf", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".wps", ".key", ".odp", ".odt", ".rtf", ".wps", ".doc", ".docx", ".odt", ".rtf", ".wps", ".key", ".odp", ".odt", ".rtf", ".wps", ]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'txt'), filename)
                os.rename(full_path, os.path.join(organized_files, 'txt', new_filename))

            elif extension in [".pdf", ".PDF", ".xps", ".ps", ".ai", ".indd", ".ae", ".fla", ".xd", ".svg", ".dng", ".idml", ".muse", ".swf", ".cpt", ".ait", ".psd", ".eps", ".pdf", ".PDF", ".xps", ".ps", ".ai", ".indd", ".ae", ".fla", ".xd", ".svg", ".dng", ".idml", ".muse", ".swf", ".cpt", ".ait", ".psd", ".eps"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'pdf'), filename)
                os.rename(full_path, os.path.join(organized_files, 'pdf', new_filename))

            elif extension in [".xls", ".xlsx", ".xlsm", ".xlsb", ".ods",".ots", ".csv", ".tsv", ".sxc", ".sxi", ".ods", ".ots", ".csv", ".tsv", ".sxc", ".sxi", ".ods", ".ots", ".csv", ".tsv", ".sxc", ".sxi"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'excel'), filename)
                os.rename(full_path, os.path.join(organized_files, 'excel', new_filename))

            elif extension in [".ai", ".indd", ".ae", ".fla", ".xd", ".svg", ".dng", ".idml", ".muse", ".swf", ".cpt", ".ait", ".psd", ".eps", ".ai", ".indd", ".ae", ".fla", ".xd", ".svg", ".dng", ".idml", ".muse", ".swf", ".cpt", ".ait", ".psd", ".eps"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'adobe'), filename)
                os.rename(full_path, os.path.join(organized_files, 'adobe', new_filename))

            elif extension in [".c", ".cpp", ".java", ".js", ".html", ".py", ".css", ".php", ".rb", ".pl", ".swift", ".go", ".ts", ".lua", ".vb", ".scala", ".r", ".sql", ".xml", ".json", ".yaml", ".ini", ".cfg","c", ".cpp", ".java", ".js", ".html", ".py", ".css", ".php", ".rb", ".pl", ".swift", ".go", ".ts", ".lua", ".vb", ".scala", ".r", ".sql", ".xml", ".json", ".yaml", ".ini", ".cfg", "c++", "c#", "java", "python", "javascript", "html", "php", "ruby", "perl", "swift", "go", "typescript", "lua", "visual basic", "scala", "r", "sql", "xml", "json", "yaml", "ini", "config"]:
                new_filename = rename_if_duplicate(os.path.join(organized_files, 'programing'), filename)
                os.rename(full_path, os.path.join(organized_files, 'programing', new_filename))

            else:
                # Mover archivos desconocidos a la carpeta "desconocidos"
                shutil.move(full_path, os.path.join(unknown_files, filename))

            # Actualizar la barra de progreso
            progress_bar["value"] += 1

        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar {filename}: {e}")

    messagebox.showinfo("Finalizado", "La organización de archivos se completó con éxito.")
    open_folder(organized_files)  # Abre la carpeta organizada

    # Eliminar carpetas vacías
    delete_empty_folders(organized_files)

def delete_empty_folders(path):
    """Elimina carpetas vacías de manera recursiva."""
    # Recorre todos los elementos en la carpeta actual
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            # Llamada recursiva para eliminar carpetas vacías en subcarpetas
            delete_empty_folders(folder_path)
            # Si la carpeta está vacía después de eliminar subcarpetas, la elimina
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def analyze_and_delete_empty_folders():
    """Analiza y elimina carpetas vacías en la ruta dada."""
    if currentRoute:
        delete_empty_folders(currentRoute)
        messagebox.showinfo("Finalizado", "Se han eliminado todas las carpetas vacías.")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna ruta.")

def open_folder(path):
    """Abre la carpeta organizada según el sistema operativo."""
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", path])
    else:
        messagebox.showerror("Error", "Sistema operativo no soportado.")

if __name__ == '__main__':
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        print("run")
    else:
        print("run")
        # Crear la interfaz gráfica
        root = tk.Tk()
        root.title("Organizador de archivos")

        # Establecer un icono personalizado
        root.iconbitmap(resource_path('./assets/armario.ico'))

        # Configurar el fondo de la ventana
        background_image = Image.open(resource_path('./assets/compressed_compressed_fondo.png'))
        background_image = background_image.resize((400, 200), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(root, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        root.geometry("400x200")
        root.resizable(False, False)  # Deshabilitar el redimensionamiento de la ventana

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (200 // 2)

        # Establecer la geometría de la ventana para que aparezca centrada
        root.geometry(f"400x200+{x}+{y}")

        # Etiqueta para mostrar la ruta seleccionada
        route_label = tk.Label(root, text="Seleccione la ruta que organizara", wraplength=300)
        route_label.pack(pady=20)

        # Botón para seleccionar la ruta
        select_button = tk.Button(root, text="Seleccionar ruta", command=select_folder, bg="blue", fg="white", padx=10, pady=5)
        select_button.pack()

        # Crear un Frame para centrar los botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Botones para organizar archivos y eliminar carpetas vacías (inicialmente deshabilitados)
        organize_button = tk.Button(button_frame, text="Organizar archivos", command=organize_files, bg="gray", fg="white", padx=10, pady=5, state=tk.DISABLED)
        delete_empty_folders_button = tk.Button(button_frame, text="Eliminar carpetas vacías", command=analyze_and_delete_empty_folders, bg="gray", fg="white", padx=10, pady=5, state=tk.DISABLED)

        # Colocar los botones uno al lado del otro
        organize_button.pack(side=tk.LEFT, padx=10)
        delete_empty_folders_button.pack(side=tk.LEFT, padx=10)

        # Barra de progreso
        progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        progress_bar.pack(pady=20)

        # Función para habilitar botones después de seleccionar la ruta
        def enable_buttons():
            select_button.config(text="Seleccionar otra ruta", bg="blue", fg="white")
            organize_button.config(state=tk.NORMAL, bg="green")
            delete_empty_folders_button.config(state=tk.NORMAL, bg="red")

        root.mainloop()
