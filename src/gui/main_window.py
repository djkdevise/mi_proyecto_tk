import tkinter as tk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")
        self.root.geometry("350x450")  # Ajustar tamaño de la ventana

        # Widget de entrada
        self.entry = tk.Entry(self.root, font=("Arial", 24))  # Ajustar tamaño de la fuente
        self.entry.grid(row=0, column=0, columnspan=3)  # Colocar en la primera fila y ocupar tres columnas
        self.entry.bind("<Return>", self.calculate)  # Asociar tecla "Enter" con la función calculate

        # Marco para los botones
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=1, column=0, columnspan=3)  # Colocar en la segunda fila y ocupar tres columnas

        # Crear botones
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", lambda: self.add_digit(7)),
            ("8", lambda: self.add_digit(8)),
            ("9", lambda: self.add_digit(9)),
            ("+", lambda: self.add_operator("+")),
            ("4", lambda: self.add_digit(4)),
            ("5", lambda: self.add_digit(5)),
            ("6", lambda: self.add_digit(6)),
            ("-", lambda: self.add_operator("-")),
            ("1", lambda: self.add_digit(1)),
            ("2", lambda: self.add_digit(2)),
            ("3", lambda: self.add_digit(3)),
            ("*", lambda: self.add_operator("*")),
            ("0", lambda: self.add_digit(0)),
            ("C", self.clear_entry),
            ("=", self.calculate),
            ("/", lambda: self.add_operator("/")),
        ]

        row = 0
        column = 0
        for btn_text, command in buttons:
            btn = tk.Button(self.buttons_frame, text=btn_text, command=command, width=10, height=3)  # Ajustar tamaño de los botones
            btn.grid(row=row, column=column)  # Organizar en la cuadrícula
            column += 1
            if column == 3:  # Pasar a la siguiente fila después de tres columnas
                column = 0
                row += 1

    def add_digit(self, digit):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + str(digit))

    def add_operator(self, operator):
        current_text = self.entry.get()
        last_char = current_text[-1] if current_text else ""

        if last_char not in ["+", "-", "*", "/"]:
            self.entry.insert(tk.END, operator)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate(self, event=None):  # Agregar argumento opcional para el evento
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()
