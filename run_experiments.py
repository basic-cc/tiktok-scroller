import tkinter as tk
from scripts.window_scroller import prepare_windows, scroll_all_windows

def on_scroll():
    prepare_windows()
    scroll_all_windows()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TikTok Scroller")
    root.geometry("200x100")

    scroll_button = tk.Button(root, text="Scroll", command=on_scroll)
    scroll_button.pack(expand=True)

    root.mainloop()
