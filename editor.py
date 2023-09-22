"""
Editor de texto que simula a cualquier editor de texto

@Author Iván Pascual
"""

# Importamos las bibliotecas 
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de texto") # Titulo de la app
        self.window_definition()

    def window_definition(self):
        """
        Defino la ventana al completo de la app
        """
        # Estilo del boton negrita
        n = ttk.Style()
        n.configure("Negrita.TButton", foreground="black", font=("Arial", 10, "bold"))
        # Botón poner en negrita el texto
        self.negrita = ttk.Button(self, text="N", width=5, style="Negrita.TButton")
        self.negrita.place(x=50, y=10)

        # Estilo del boton cursiva
        k = ttk.Style()
        k.configure("Cursiva.TButton", foreground="black", font=("Arial", 10, "italic"))
        # Botón para poner en cursiva el texto
        self.cursiva = ttk.Button(self, text="K", width=5, style="Cursiva.TButton")
        self.cursiva.place(x=100, y=10)

        # Estilo del boton subrayado
        s = ttk.Style()
        s.configure("Subrayado.TButton", foreground="black", font=("Arial", 10))
        # Botón para subrayar el texto
        self.subrayado = ttk.Button(self, text="S", width=5, style="Subrayado.TButton")
        self.subrayado.configure(underline=False) # Añadimos el subrayado a la "S"
        self.subrayado.place(x=150, y=10)

        # Estilo del boton tachar
        t = ttk.Style()
        t.configure("Tachado.TButton", foreground="black", font=("Arial", 10, "overstrike"))
        # Botón para tachar el texto
        self.tachado = ttk.Button(self, text="abc", width=5, style="Tachado.TButton")
        self.tachado.place(x=200, y=10)

        # Botón poner abrir un archivo de texto
        self.abrir = ttk.Button(self, text="Abrir archivo")
        self.abrir.place(x=500, y=10)

        # Botón guardar el texto escrito
        self.save = ttk.Button(self, text="Guardar archivo")
        self.save.place(x=600, y=10)

        # Área de entrada de texto para el usuario
        self.input_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=20, width=80)
        self.input_text.pack(pady=50, padx=50)

app = TextEditor()
app.mainloop()