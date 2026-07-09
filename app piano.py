import tkinter as tk
import winsound as ws

def handle_click_sol():
    ws.Beep(392, 1000)
def handle_click_la():
    ws.Beep(440, 1000)
def handle_click_si():
    ws.Beep(492, 1000)
def handle_click_fa():
    ws.Beep(349, 1000)
def handle_click_mi():
    ws.Beep(330, 1000)
def handle_click_re():
    ws.Beep(293, 1000)
def handle_click_do():
    ws.Beep(261, 1000)
def handle_click_doS():
    ws.Beep(277, 1000)
def handle_click_reS():
    ws.Beep(311, 1000)
def handle_click_faS():
    ws.Beep(369, 1000)
def handle_click_solS():
    ws.Beep(415, 1000)
def handle_click_laS():
    ws.Beep(466, 1000)


root = tk.Tk()
root.title("Piano")
root.geometry("310x210")
root.configure(bg="#637469")

label = tk.Label(root,
    text="This is a piano",
    bg="black", 
    fg="white",
    padx=10,
    pady=10,
)

label.grid(row=0, column=3, columnspan=3, padx= 10, pady= 10)

button_do = tk.Button(
    root,
    text="Do",
    command=handle_click_do,
    fg="white",
    bg="blue",
    padx=10,
    pady=20,
)

button_do.grid(row= 2, column= 1, padx= 1, pady=5)

button_doS = tk.Button(
    root,
    text= "Do#",
    command=handle_click_doS,
    fg="white",
    bg="blue",
    padx=10,
    pady=20

)

button_doS.grid(row=1, column=1, columnspan=2, padx=1)

button_re = tk.Button(
    root,
    text="Re",
    command=handle_click_re,
    fg="white",
    bg="blue",
    padx=10,
    pady=20,
)

button_re.grid(row= 2,column= 2, padx=1, pady=5)

button_reS= tk.Button(
    root,
    command=handle_click_reS,
    text="Re#",
    fg="white",
    bg="blue",
    padx=10,
    pady=20
)

button_reS.grid(row=1, column=2, columnspan=2, padx=1)

button_mi = tk.Button(
    root,
    text="Mi",
    command=handle_click_mi,
    fg="white",
    bg="blue",
    padx=10,
    pady=20
)

button_mi.grid(row= 2, column=3, padx=1, pady=5)

button_fa = tk.Button(
    root,
    text= "Fa",
    command=handle_click_fa,
    fg="white",
    bg="blue",
    padx=10,
    pady=20,
)

button_fa.grid(row=2, column=4, padx=1, pady=5)

button_faS = tk.Button(
    root,
    command=handle_click_faS,
    text="Fa#",
    fg="white",
    bg="blue",
    padx=10,
    pady=20,
)

button_faS.grid(row=1, column=4, columnspan=2, padx=1, pady=5)

button_sol = tk.Button(
    root,
    text="Sol",
    command=handle_click_sol,
    fg="white",
    bg="blue",
    padx=10,
    pady=20,
)

button_sol.grid(row=2, column=5, padx=1, pady=5)

button_la = tk.Button(
    root, 
    text="La", 
    command=handle_click_la,
    fg="white",     
    bg="blue",
    padx=10,
    pady=20,
)

button_la.grid(row= 2, column=6, padx=1, pady=5)

button_si = tk.Button(
    root,
    text="Si",
    command=handle_click_si,
    fg="white",
    bg="blue",
    padx=10,
    pady=20
)

button_si.grid(row=2, column=7, padx=1, pady=5)


root.mainloop()
