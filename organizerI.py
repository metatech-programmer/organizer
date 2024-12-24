import ctypes
import sys
import shutil
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog

currentRoute = os.path.dirname(os.path.abspath(__file__))


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


def organize_files():
    currentFolder = formatRoute(currentRoute) + '/'

    organized_files = currentFolder + 'archivos_organizados'
    organized_filesImages = organized_files + '/imagenes'
    organized_filesSongs = organized_files + '/audios'
    organized_filesVideos = organized_files + '/videos'
    organized_filesPoint = organized_files + '/powerpoints'
    organized_filesPrograms = organized_files + '/programas'
    organized_filesRar = organized_files + "/rar's"
    organized_filesWord = organized_files + '/word'
    organized_filesTxt = organized_files + '/txt'
    organized_filesPdf = organized_files + '/pdf'
    organized_filesExcel = organized_files + '/excel'
    organized_filesPrograming = organized_files + '/programing'
    organized_filesAdobe = organized_files + '/adobe'
    organized_filesOthers = organized_files + '/otros'

    if not os.path.exists(organized_files):
        os.mkdir(organized_files)
    if not os.path.exists(organized_filesImages):
        os.mkdir(organized_filesImages)
    if not os.path.exists(organized_filesSongs):
        os.mkdir(organized_filesSongs)
    if not os.path.exists(organized_filesVideos):
        os.mkdir(organized_filesVideos)
    if not os.path.exists(organized_filesPoint):
        os.mkdir(organized_filesPoint)
    if not os.path.exists(organized_filesPrograms):
        os.mkdir(organized_filesPrograms)
    if not os.path.exists(organized_filesRar):
        os.mkdir(organized_filesRar)
    if not os.path.exists(organized_filesWord):
        os.mkdir(organized_filesWord)
    if not os.path.exists(organized_filesTxt):
        os.mkdir(organized_filesTxt)
    if not os.path.exists(organized_filesPdf):
        os.mkdir(organized_filesPdf)
    if not os.path.exists(organized_filesExcel):
        os.mkdir(organized_filesExcel)
    if not os.path.exists(organized_filesPrograming):
        os.mkdir(organized_filesPrograming)
    if not os.path.exists(organized_filesAdobe):
        os.mkdir(organized_filesAdobe)
    if not os.path.exists(organized_filesOthers):
        os.mkdir(organized_filesOthers)


    print("running")
    for filename in os.listdir(currentFolder):
        name, extension = os.path.splitext(currentFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".gif", ".ico", ".webp", ".bmp", ".tiff", ".raw", ".exif", ".heif",
                         ".bat", ".bpg", ".ppm", ".pgm", ".pbm", ".pnm", ".hdr", ".jxr", ".jpx", ".wdp", ".hdp", ".j2k",
                         ".jp2", ".jpm", ".jxr", ".jxl", ".avif"]:
            picture = Image.open(currentFolder + filename)
            picture.save(organized_filesImages + '/' + "compressed_" + filename, optimized=True, quality=100)
            os.remove(currentFolder + filename)

        elif extension in [".mp3", ".wav", ".flac", ".aac", ".m4a", ".wma", ".ogg", ".opus", ".alac", ".aiff", ".dsd",
                           ".mid", ".midi", ".amr", ".ape", ".ac3", ".mp2", ".mka", ".pcm"]:
            os.rename(currentFolder + filename, organized_filesSongs + '/' + filename)

        elif extension in [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".m4v", ".mpg",
                           ".rm", ".swf", ".vob", ".ts", ".m2ts", ".mts", ".ogv", ".mxf", ".divx"]:
            os.rename(currentFolder + filename, organized_filesVideos + '/' + filename)

        elif extension in [".ppt", ".pptx", ".pps", ".ppsx", ".pot", ".potx"]:
            os.rename(currentFolder + filename, organized_filesPoint + '/' + filename)
        elif extension in [".exe", ".dmg", ".app", ".deb", ".rpm", ".msi", ".bat", ".sh", ".iso", ".torrent",".apk", ".jar", ".rmskin",".appinstaller"]:
            os.rename(currentFolder + filename, organized_filesPrograms + '/' + filename)

        elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"]:
            os.rename(currentFolder + filename, organized_filesRar + '/' + filename)

        elif extension in [".doc", ".docx", ".dot", ".dotx",".DOC",".DOCX"]:
            os.rename(currentFolder + filename, organized_filesWord + '/' + filename)

        elif extension in [".txt",".md"]:
            os.rename(currentFolder + filename, organized_filesTxt + '/' + filename)

        elif extension in [".pdf",".PDF"]:
            os.rename(currentFolder + filename, organized_filesPdf + '/' + filename)

        elif extension in [".xls", ".xlsx", ".xlsm", ".xlsb", ".xlk",".XLS"]:
            os.rename(currentFolder + filename, organized_filesExcel + '/' + filename)

        elif extension in [".ai", ".indd", ".ae", ".fla", ".xd", ".svg", ".dng", ".idml", ".muse", ".swf", ".cpt", ".ait"]:
            os.rename(currentFolder + filename, organized_filesAdobe + '/' + filename)
    
        elif extension in [".c", ".cpp", ".java", ".js", ".htm","py", ".html", ".pdb", ".pdm", ".nbm", ".css", ".php", ".asp",
                           ".rb", ".pl", ".swift", ".go", ".ts", ".lua", ".vb", ".scala", ".perl", ".r", ".matlab",
                           ".sql", ".shell", ".bat", ".powershell", ".xml", ".json", ".yaml", ".ini", ".cfg", ".h",
                           ".hpp", ".cs", ".vb", ".as", ".asm", ".coffee", ".dart", ".ejs", ".groovy", ".less", ".scss",".py"]:
            os.rename(currentFolder + filename, organized_filesPrograming + '/' + filename)      

        else:
            # Mover la carpeta a la carpeta "otros"
            if os.path.isdir(currentFolder + filename) and filename != "archivos_organizados":
                shutil.move(currentFolder + filename, organized_filesOthers + '/' + filename)
            else:
                 route_label.config(text="Finalizo la organización, revisa tú carpeta")
                

   
    # Eliminar carpetas vacías
    delete_empty_folders(organized_files)


def delete_empty_folders(organized_files):
    for folder_name in os.listdir(organized_files):
        folder_path = os.path.join(organized_files, folder_name)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)


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
        root.iconbitmap('./assets/icon.ico')

        # Configurar el fondo de la ventana
        background_image = Image.open('./assets/compressed_compressed_fondo.png')
        background_image = background_image.resize((400, 200), Image.ANTIALIAS)
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(root, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        root.geometry("300x200")
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

        # Botón para ejecutar la organización de archivos
        organize_button = tk.Button(root, text="Organizar archivos", command=organize_files, bg="green", fg="white", padx=10, pady=5)
        organize_button.pack(pady=10)

        root.mainloop()
