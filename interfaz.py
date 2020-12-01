import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext,messagebox
from lexer import leerLexer1
from sintactico import reglas_sintactico

class Ventana:
    def __init__(self,root):
        root.title("Analizador sintáctico - Kotlin")
        root.configure(bg="#e7e4ee")
        root.resizable(width=False, height=False)

        # Titulo
        self.lbl_title = tk.Label(win, text="Analizador Sintáctico: KOTLIN",
                                  font=("Arial Bold", 20),height=2,width=50, bg="#5832a4", fg="white")
        self.lbl_title.grid(row = 0, column = 0, columnspan=4)

        # Scrolled text
        self.txt = scrolledtext.ScrolledText(win,width=105,height=10)
        self.txt.grid(row = 1, column = 0, columnspan=4,padx=50, pady=10)


        # Boton lexico y sintactico
        self.btn_lexico = tk.Button(win, text="Analizador léxico",command=self.lexico,font=("Arial Bold", 10), height=2,width=20, bg="#5832a4", fg="white")
        self.btn_lexico.grid(row = 2, column = 0, columnspan=2)

        self.btn_sintactico = tk.Button(win, text="Analizador sintáctico",command=self.sintactico,font=("Arial Bold", 10),height=2,width=20, bg="#5832a4", fg="white")
        self.btn_sintactico.grid(row=2, column=2, columnspan=2)


        # Muestra por pantalla análisis léxico
        self.scroll_lexico = ScrollableFrame(win)

        tk.Label(self.scroll_lexico.scrollable_frame, text="", height=20, width=60, bg='white').grid(row=3, column=0)
        self.l_lexico = tk.Label(self.scroll_lexico.scrollable_frame, text="", width=60, bg='white')
        self.l_lexico.grid(row=3, column=0)
        self.scroll_lexico.grid(row=3, column=1)

        # Muestra por pantalla análisis sintáctico
        self.scroll_sintactico = ScrollableFrame(win)

        tk.Label(self.scroll_sintactico.scrollable_frame, text="", height=20, width=60, bg='white').grid(row=3, column=2)
        self.l_sintactico = tk.Label(self.scroll_sintactico.scrollable_frame, text="",width=60,bg='white')
        self.l_sintactico.grid(row=3, column=2)
        self.scroll_sintactico.grid(row=3, column=3)

        tk.Label(win, height=2).grid(row=4)


    def lexico(self):
        try:
            texto = leerLexer1(self.txt.get("1.0", 'end'))
            str_texto = "\n".join(texto)
            self.l_lexico.config(text=str_texto)
        except:
            messagebox.showinfo(message="Debe ingresar una expresión", title="Advertencia")
    def sintactico(self):
        # try:
            sint = reglas_sintactico(self.txt.get("1.0", 'end'))
            str_texto = "\n".join(sint)
            self.l_sintactico.config(text=str_texto)
        # except:
        #     messagebox.showinfo(message="Debe ingresar una expresión", title="Advertencia")

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


win = tk.Tk()

windows = Ventana(win)
win.mainloop()