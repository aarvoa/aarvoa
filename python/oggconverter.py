import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread


def choose_file():
    source = filedialog.askopenfilename(
        title="Choose an M4A file",
        filetypes=[("M4A audio", "*.m4a"), ("All files", "*.*")]
    )
    if not source:
        return

    destination = filedialog.asksaveasfilename(
        title="Save OGG file",
        defaultextension=".ogg",
        initialfile="converted.ogg",
        filetypes=[("OGG audio", "*.ogg")]
    )
    if not destination:
        return

    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        messagebox.showerror(
            "FFmpeg missing",
            "Install FFmpeg and add its bin folder to PATH, "
            "then restart this program."
        )
        return

    button.config(state="disabled")
    status.config(text="Converting…")

    Thread(
        target=convert,
        args=(ffmpeg, source, destination),
        daemon=True
    ).start()


def convert(ffmpeg, source, destination):
    try:
        result = subprocess.run(
            [
                ffmpeg,
                "-y",
                "-i", source,
                "-vn",
                "-c:a", "libvorbis",
                "-q:a", "5",
                "-ac", "1",
                destination
            ],
            capture_output=True,
            text=True,
            errors="replace"
        )
        error = result.stderr if result.returncode else None
    except Exception as exc:
        error = str(exc)

    root.after(0, finished, error)


def finished(error):
    button.config(state="normal")

    if error:
        status.config(text="Conversion failed")
        messagebox.showerror("Error", error)
    else:
        status.config(text="Done! OGG saved ✅")
        messagebox.showinfo("Success", "Your OGG file is ready!")


root = tk.Tk()
root.title("M4A → OGG")
root.geometry("360x200")
root.resizable(False, False)
root.configure(bg="#171923")

tk.Label(
    root,
    text="M4A → OGG",
    font=("Segoe UI", 22, "bold"),
    bg="#171923",
    fg="white"
).pack(pady=(22, 15))

button = tk.Button(
    root,
    text="Choose M4A",
    command=choose_file,
    font=("Segoe UI", 12),
    bg="#7289da",
    fg="white",
    relief="flat",
    padx=25,
    pady=8
)
button.pack()

status = tk.Label(
    root,
    text="Choose a file to start",
    bg="#171923",
    fg="#b8becf"
)
status.pack(pady=15)

root.mainloop()