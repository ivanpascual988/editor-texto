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
        self.tachado = ttk.Button(self, text="abc", width=5, style="Tachado.TButton", command=self.poner_quitar_tachado)
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

        # Obtengo las etiquetas del texto seleccionado
        etiqueta_texto = (self.texto.tag_names(inicio_texto))

        # Si tiene la etiqueta bold la eliminamos
        if "bold" in etiqueta_texto:
            self.texto.tag_remove("bold", inicio_texto, fin_texto)
        # Si no tiene la etiqueta la añadimos
        else:
            self.texto.tag_add("bold", inicio_texto, fin_texto)   # Si es la primera vez, le añade la etiqueta
            self.texto.tag_configure("bold", font=("Arial", 10, "bold"))
        
    
    def poner_quitar_cursiva(self):
        """
        Funcion para comprobar si el texto seleccionado esta en cursiva o no.
        Si esta en cursiva lo quita y si no esta en cursiva, lo pone en cursiva
        """
        # Obtengo el texto seleccionado
        inicio_texto = self.texto.index(tk.SEL_FIRST)
        fin_texto =  self.texto.index(tk.SEL_LAST)

        # Obtengo las etiquetas del texto seleccionado
        etiqueta_texto = (self.texto.tag_names(inicio_texto))

        # Si tiene la etiqueta italic la eliminamos
        if "italic" in etiqueta_texto:
            self.texto.tag_remove("italic", inicio_texto, fin_texto)
        # Si no tiene la etiqueta la añadimos
        else:
            self.texto.tag_add("italic", inicio_texto, fin_texto)  
            self.texto.tag_configure("italic", font=("Arial", 10, "italic"))
        
    def poner_quitar_subrayado(self):
        """
        Funcion para comprobar si el texto seleccionado esta subrayado o no.
        Si esta subrayado lo quita y si no esta subrayado, lo subraya
        """
        # Obtengo el texto seleccionado
        inicio_texto = self.texto.index(tk.SEL_FIRST)
        fin_texto =  self.texto.index(tk.SEL_LAST)

        # Obtenemos las etiquetas del texto seleccionado
        etiqueta_texto = self.texto.tag_names(inicio_texto)

        # Si tiene la etiqueta se la eliminamos
        if "underline" in etiqueta_texto:
            self.texto.tag_remove("underline", inicio_texto, fin_texto)
        # Si no tiene la etiqueta la añadimos
        else:
            self.texto.tag_add("underline", inicio_texto, fin_texto)
            self.texto.tag_configure("underline", underline=True)   # Configuramos la etiqueta para que esta subrayado

    def poner_quitar_tachado(self):
        """
        Funcion para comprobar si el texto seleccionado esta tachado o no.
        Si esta tachado lo quita y si no esta tachado, lo tacha
        """
        # Obtengo el texto seleccionado
        inicio_texto = self.texto.index(tk.SEL_FIRST)
        fin_texto =  self.texto.index(tk.SEL_LAST)

        # Compruebo si esta subrayado o no
        etiqueta_texto = self.texto.tag_names(inicio_texto)

        # Si tiene la etiqueta se la eliminamos
        if "overstrike" in etiqueta_texto:
            self.texto.tag_remove("overstrike", inicio_texto, fin_texto)
        # Si no tiene la etiqueta la añadimos
        else:
            self.texto.tag_add("overstrike", inicio_texto, fin_texto)
            self.texto.tag_configure("overstrike", overstrike=True)    # Configuramos la etiqueta para que esta tachado

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()