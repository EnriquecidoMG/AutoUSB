import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser
import shutil

def list_drives():
    """Lists available drives on the system, excluding the main disk."""
    drives = []
    for letter in "DEFGHIJKLMNOPQRSTUVWXYZ": 
        if os.path.exists(f"{letter}:"):
            drives.append(f"{letter}:")
    return drives

def create_autorun():
    drive = combobox_drive.get()
    icon_path = entry_icon.get().strip()
    new_name = entry_name.get().strip()
    start_file_path = entry_start_file.get().strip()

    if not drive:
        messagebox.showerror("Error", "Please select a USB drive.")
        return

    
    icon_name = ''
    if icon_path:
        icon_file_name = os.path.basename(icon_path)
        destination_icon_path = os.path.join(drive, icon_file_name)

        try:
            shutil.copy(icon_path, destination_icon_path)
            icon_name = icon_file_name
        except Exception as e:
            messagebox.showerror("Error", f"Could not copy the icon: {e}")
            return

    
    start_file_name = ''
    if start_file_path:
        start_file_name = os.path.basename(start_file_path)
        destination_start_file_path = os.path.join(drive, start_file_name)

        try:
            shutil.copy(start_file_path, destination_start_file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not copy the start file: {e}")
            return

    autorun_content = f"""[Autorun]
Icon={icon_name}
Label={new_name if new_name else ''}
Open={start_file_name if start_file_name else ''}
; This autorun.inf file was made with 'AutoUSB' (a program made by EnriquecidoMG)
"""

    autorun_path = os.path.join(drive, "autorun.inf")

    try:
        with open(autorun_path, "w") as f:
            f.write(autorun_content)
        messagebox.showinfo("Success", f"The autorun.inf file has been created at {autorun_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not create the file: {e}")

def show_help():
    help_text = (
        "Instructions:\n\n"
        "1. Select the USB drive from the list.\n"
        "2. Optional: Enter the new name for the drive.\n"
        "3. Optional: Click 'Select Icon' to choose a .ico file.\n"
        "4. Optional: Click 'Select Start File' to choose an executable, image, or video file.\n"
        "5. Click 'Create autorun.inf' to generate the file.\n\n"
        "Note: If you encounter issues with the help section in the app, check the documentation provided on GitHub for troubleshooting tips."
    )
    messagebox.showinfo("Help", help_text)

def select_icon():
    icon_file = filedialog.askopenfilename(
        title="Select Icon",
        filetypes=[("Icon Files", "*.ico"), ("All Files", "*.*")]
    )
    if icon_file:
        entry_icon.delete(0, tk.END)  
        entry_icon.insert(0, icon_file)  

def select_start_file():
    start_file = filedialog.askopenfilename(
        title="Select Start File",
        filetypes=[
            ("Executable Files", "*.exe"),
            ("Images", "*.jpg;*.jpeg;*.png;*.gif"),
            ("Videos", "*.mp4;*.avi;*.mov;*.mkv"),
            ("All Files", "*.*")
        ]
    )
    if start_file:
        entry_start_file.delete(0, tk.END)  
        entry_start_file.insert(0, start_file)  

def open_github():
    webbrowser.open("https://github.com/EnriquecidoMG/AutoUSB")  


window = ThemedTk()
window.get_themes()  
window.set_theme("arc")  

window.title("AutoUSB: a USB autorun Generator")


window.iconbitmap("./icon.ico")  


window_width = 400
window_height = 400
window.geometry(f"{window_width}x{window_height}")


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"+{x}+{y}")


window.resizable(False, False)


title = tk.Label(window, text="AutoUSB", font=("Helvetica", 18, "bold"))
title.pack(pady=10)


frame_drive = tk.Frame(window)
frame_drive.pack(pady=5)
label_drive = tk.Label(frame_drive, text="Select USB Drive:")
label_drive.pack(side=tk.LEFT, padx=5)


combobox_drive = ttk.Combobox(frame_drive, values=list_drives(), state="readonly")
combobox_drive.pack(side=tk.LEFT)


frame_name = tk.Frame(window)
frame_name.pack(pady=5)
label_name = tk.Label(frame_name, text="New drive name (optional):")
label_name.pack(side=tk.LEFT, padx=5)
entry_name = tk.Entry(frame_name, width=20)
entry_name.pack(side=tk.LEFT)


frame_icon = tk.Frame(window)
frame_icon.pack(pady=5)
label_icon = tk.Label(frame_icon, text="Icon file (optional):")
label_icon.pack(side=tk.LEFT, padx=5)
entry_icon = tk.Entry(frame_icon, width=20)
entry_icon.pack(side=tk.LEFT)


button_select_icon = ttk.Button(frame_icon, text="Select", command=select_icon)
button_select_icon.pack(side=tk.LEFT, padx=5)


frame_start_file = tk.Frame(window)
frame_start_file.pack(pady=5)
label_start_file = tk.Label(frame_start_file, text="Start file (optional):")
label_start_file.pack(side=tk.LEFT, padx=5)
entry_start_file = tk.Entry(frame_start_file, width=20)
entry_start_file.pack(side=tk.LEFT)


button_select_start_file = ttk.Button(frame_start_file, text="Select", command=select_start_file)
button_select_start_file.pack(side=tk.LEFT, padx=5)


frame_button = tk.Frame(window)
frame_button.pack(pady=20)
button_create = ttk.Button(frame_button, text="Create autorun.inf", command=create_autorun)
button_create.pack(side=tk.LEFT, padx=5)

button_help = ttk.Button(frame_button, text="Help", command=show_help)
button_help.pack(side=tk.LEFT, padx=5)


button_github = ttk.Button(window, text="Visit my GitHub", command=open_github)
button_github.pack(side=tk.BOTTOM, pady=10)


window.mainloop()
