import tkinter as tk

root = tk.Tk()
root.title("Interface")

button = tk.Button(root, text="Cliquez ici !")
button.pack()

root.minsize(1920, 1080)
root.geometry("1920x1080")
root.mainloop()
