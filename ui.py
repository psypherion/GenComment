import tkinter as tk
from tkinter import filedialog

class FolderSelectorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Selector UI")

        # Label and entry for folder name
        self.label = tk.Label(root, text="Enter Folder Name:")
        self.label.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        # Button to select the folder
        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack()

        # Variable to store the selected folder name
        self.folder_name = tk.StringVar()

    def select_folder(self):
        folder_name = filedialog.askdirectory()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, folder_name)
        self.folder_name.set(folder_name)
        self.root.destroy()  # Close the UI immediately after selecting the folder

    def get_selected_folder(self):
        return self.folder_name.get()

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderSelectorUI(root)
    root.mainloop()
    selected_folder = app.get_selected_folder()
    print("Selected Folder:", selected_folder)
