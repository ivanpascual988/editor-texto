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
        self.title("Editor de texto by Ivan Pascual") # Titulo de la app
        self.window_definition()
        self.etiqueta_texto = []

    def window_definition(self):
        """
        Defino la ventana al completo de la app
        """
        # Estilo del boton negrita
        n = ttk.Style()
        n.configure("Negrita.TButton", foreground="black", font=("Arial", 10, "bold"))
        # Botón poner en negrita el texto
        self.negrita = ttk.Button(self, text="N", width=5, style="Negrita.TButton", command=self.poner_quitar_negrita)
        self.negrita.place(x=50, y=10)

        # Estilo del boton cursiva
        k = ttk.Style()
        k.configure("Cursiva.TButton", foreground="black", font=("Arial", 10, "italic"))
        # Botón para poner en cursiva el texto
        self.cursiva = ttk.Button(self, text="K", width=5, style="Cursiva.TButton", command=self.poner_quitar_cursiva)
        self.cursiva.place(x=100, y=10)

        # Estilo del boton subrayado
        s = ttk.Style()
        s.configure("Subrayado.TButton", foreground="black", font=("Arial", 10))
        # Botón para subrayar el texto
        self.subrayado = ttk.Button(self, text="S", width=5, style="Subrayado.TButton", command=self.poner_quitar_subrayado)
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
        self.abrir.place(x=420, y=10)

        # Botón guardar el texto escrito
        self.guardar = ttk.Button(self, text="Guardar archivo")
        self.guardar.place(x=520, y=10)

        # Área de entrada de texto para el usuario
        self.texto = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=20, width=80, font=("Arial", 10))
        self.texto.pack(pady=50, padx=50)
    
    def poner_quitar_negrita(self):
        """
        Funcion para comprobar si el texto seleccionado esta en negrita o no.
        Si esta en negrita lo quita y si no esta en negrita, lo pone en negrita
        """
        # Obtengo el texto seleccionado
        inicio_texto = self.texto.index(tk.SEL_FIRST)
        fin_texto =  self.texto.index(tk.SEL_LAST)

        # Compruebo si esta subrayado o no
        etiqueta_texto = (self.texto.tag_names(inicio_texto))
        print(etiqueta_texto)

        # Si el texto seleccionado está subrayado, lo quita
        if "negrita" in etiqueta_texto:
            self.texto.tag_remove("negrita", inicio_texto, fin_texto)
            self.etiqueta_texto.remove("negrita")
        # Si no esta subrayado, lo subraya
        else:
            self.etiqueta_texto.append("negrita")     
            self.texto.tag_add("negrita", inicio_texto, fin_texto)   # Si es la primera vez, le añade la etiqueta
            if "cursiva" in self.etiqueta_texto:
                self.texto.tag_configure("negrita", font=("Arial", 10, "bold", "italic"))
            else:
                self.texto.tag_configure("negrita", font=("Arial", 10, "bold"))
        print(self.etiqueta_texto)
    
    def poner_quitar_cursiva(self):
        """
        Funcion para comprobar si el texto seleccionado esta en cursiva o no.
        Si esta en cursiva lo quita y si no esta en cursiva, lo pone en cursiva
        """
        # Obtengo el texto seleccionado
        inicio_texto = self.texto.index(tk.SEL_FIRST)
        fin_texto =  self.texto.index(tk.SEL_LAST)

        # Compruebo si esta subrayado o no
        etiqueta_texto = (self.texto.tag_names(inicio_texto))
        print(etiqueta_texto)

        # Si el texto seleccionado está subrayado, lo quita
        if "cursiva" in etiqueta_texto:
            self.texto.tag_remove("cursiva", inicio_texto, fin_texto)
            self.etiqueta_texto.remove("cursiva")
        # Si no esta subrayado, lo subraya
        else:
            self.etiqueta_texto.append("cursiva")
            self.texto.tag_add("cursiva", inicio_texto, fin_texto)  # Si es la primera vez, le añade la etiqueta
            if "negrita" in self.etiqueta_texto:
                self.texto.tag_configure("cursiva", font=("Arial", 10, "bold", "italic"))
            else:
                self.texto.tag_configure("cursiva", font=("Arial", 10, "italic"))
        print(self.etiqueta_texto)

    def poner_quitar_subrayado(self):
        """
        Funcion para comprobar si el texto seleccionado esta subrayado o no.
        Si esta subrayado lo quita y si no esta subrayado, lo subraya
        """
        # Obtengo el texto seleccionado
        inicio_texto = self.texto.index(tk.SEL_FIRST)
        fin_texto =  self.texto.index(tk.SEL_LAST)

        # Compruebo si esta subrayado o no
        etiqueta_texto = self.texto.tag_names(inicio_texto)

        # Si el texto seleccionado está subrayado, lo quita
        if "subrayado" in etiqueta_texto:
            self.texto.tag_remove("subrayado", inicio_texto, fin_texto)
        else:
            # Si es la primera vez, le añade la etiqueta
            # Si no esta subrayado, lo subraya
            self.texto.tag_add("subrayado", inicio_texto, fin_texto)
            self.texto.tag_configure("subrayado", underline=True)

app = TextEditor()
app.mainloop()