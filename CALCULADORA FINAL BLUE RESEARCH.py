import tkinter as tk
from tkinter import messagebox
def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Estamos aquí para ayudarte a realizar los cálculos de las ecuaciones aprendidas en las lecciones de sistema respiratorio y sistema cardiovascular. Si tienes algún problema, puedes llamar al 29384744 para comunicarte con un asesor.")

ventana = tk.Tk()
ventana.title("Calculadora Blue Research")
ventana.geometry("600x400")
ventana.configure(bg="#E1F1FF")

titulo = tk.Label(ventana, text="Calculadora Blue Research", font=("Times New Roman", 72), fg="black", bg="#E1F1FF")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="Estamos aquí para ayudarte a realizar los cálculos de las ecuaciones aprendidas en las lecciones de sistema respiratorio y sistema cardiovascular.", font=("Times New Roman", 14), fg="black", bg="#E1F1FF")
subtitulo.pack(pady=10)

frame_botones = tk.Frame(ventana, bg="#E1F1FF")
frame_botones.pack(pady=10)

btn_ecuaciones_cardiovascular = tk.Button(frame_botones, text="Ecuaciones de Cardiovascular")
btn_ecuaciones_cardiovascular.pack(side="left", padx=10)

btn_ecuaciones_respiratorio = tk.Button(frame_botones, text="Ecuaciones de Respiratorio")
btn_ecuaciones_respiratorio.pack(side="left", padx=10)

btn_ayuda = tk.Button(frame_botones, text="Ayuda", command=mostrar_ayuda)
btn_ayuda.pack(side="left", padx=10)

def calcular_flujo():
    try:
        delta_p = float(entry_delta_p.get())
        resistencia = float(entry_resistencia.get())
        flujo = delta_p / resistencia
        label_resultado['text'] = f"El flujo de gas es: {flujo:.2f}"
    except ValueError:
        label_resultado['text'] = "Por favor, ingresa valores numéricos válidos."

def calcular_capacidad_residual():
    try:
        volumen_residual = float(entry_volumen_residual.get())
        volumen_espiratorio_reserva = float(entry_volumen_espiratorio_reserva.get())
        capacidad_residual = volumen_residual + volumen_espiratorio_reserva
        label_resultado['text'] = f"La capacidad residual funcional es: {capacidad_residual:.2f} mL"
    except ValueError:
        label_resultado['text'] = "Por favor, ingresa valores numéricos válidos."

def calcular_capacidad_inspiratoria():
    try:
        volumen_inspiratorio_reserva = float(entry_volumen_inspiratorio_reserva.get())
        volumen_tidal = float(entry_volumen_tidal.get())
        capacidad_inspiratoria = volumen_inspiratorio_reserva + volumen_tidal
        label_resultado['text'] = f"La capacidad inspiratoria es: {capacidad_inspiratoria:.2f} mL"
    except ValueError:
        label_resultado['text'] = "Por favor, ingresa valores numéricos válidos."

def calcular_capacidad_vital():
    try:
        volumen_espiratorio_reserva = float(entry_volumen_espiratorio_reserva.get())
        volumen_tidal = float(entry_volumen_tidal.get())
        volumen_inspiratorio_reserva = float(entry_volumen_inspiratorio_reserva.get())
        capacidad_vital = volumen_espiratorio_reserva + volumen_tidal + volumen_inspiratorio_reserva
        label_resultado['text'] = f"La capacidad vital es: {capacidad_vital:.2f} mL"
    except ValueError:
        label_resultado['text'] = "Por favor, ingresa valores numéricos válidos."

def calcular_capacidad_pulmonar_total():
    try:
        volumen_residual = float(entry_volumen_residual.get())
        volumen_espiratorio_reserva = float(entry_volumen_espiratorio_reserva.get())
        volumen_inspiratorio_reserva = float(entry_volumen_inspiratorio_reserva.get())
        volumen_tidal = float(entry_volumen_tidal.get())
        capacidad_pulmonar_total = volumen_residual + volumen_espiratorio_reserva + volumen_inspiratorio_reserva + volumen_tidal
        label_resultado['text'] = f"La capacidad pulmonar total es: {capacidad_pulmonar_total:.2f} mL"
    except ValueError:
        label_resultado['text'] = "Por favor, ingresa valores numéricos válidos."
def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Seleccione el tipo de cálculos que desea realizar. Nuestra calculadora está para apoyar su aprendizaje.")
    ventana = tk.Tk()
    ventana.title("Calculadora de Blue Research")
    ventana.geometry("600x400")
    ventana.configure(bg="#E1F1FF")
    titulo = tk.Label(ventana, text="Bienvenido a la Calculadora de Blue Research", font=("Times New Roman", 24, "bold"), fg="black", bg="#E1F1FF")
    titulo.pack(pady=20)
    subtitulo = tk.Label(ventana, text="¿En qué podemos ayudarte?", font=("Times New Roman", 16, "bold"), fg="black", bg="#E1F1FF")
    subtitulo.pack(pady=10)
    ventana = tk.Tk()
    ventana.title("Calculadora Blue Research")
    ventana.geometry("600x400")
    ventana.configure(bg="#ADD8E6")


    # Create the labels and entries for the first calculation
label_delta_p = tk.Label(ventana, text="Delta P:")
label_delta_p.pack()
entry_delta_p = tk.Entry(ventana)
entry_delta_p.pack()

label_resistencia = tk.Label(ventana, text="Resistencia:")
label_resistencia.pack()
entry_resistencia = tk.Entry(ventana)
entry_resistencia.pack()

    # Create the button for calculating the first calculation
button_calcular_flujo = tk.Button(ventana, text="Calcular Flujo", command=calcular_flujo)
button_calcular_flujo.pack()

    # Create the labels and entries for the second calculation
label_volumen_residual = tk.Label(ventana, text="Volumen Residual:")
label_volumen_residual.pack()
entry_volumen_residual = tk.Entry(ventana)
entry_volumen_residual.pack()

label_volumen_espiratorio_reserva = tk.Label(ventana, text="Volumen Espiratorio de Reserva:")
label_volumen_espiratorio_reserva.pack()
entry_volumen_espiratorio_reserva = tk.Entry(ventana)
entry_volumen_espiratorio_reserva.pack()

    # Create the button for calculating the second calculation
button_calcular_capacidad_residual = tk.Button(ventana, text="Calcular Capacidad Residual", command=calcular_capacidad_residual)
button_calcular_capacidad_residual.pack()

    # Create the labels and entries for the third calculation
label_volumen_inspiratorio_reserva = tk.Label(ventana, text="Volumen Inspiratorio de Reserva:")
label_volumen_inspiratorio_reserva.pack()
entry_volumen_inspiratorio_reserva = tk.Entry(ventana)
entry_volumen_inspiratorio_reserva.pack()

label_volumen_tidal = tk.Label(ventana, text="Volumen Tidal:")
label_volumen_tidal.pack()
entry_volumen_tidal = tk.Entry(ventana)
entry_volumen_tidal.pack()

    # Create the button for calculating the third calculation
button_calcular_capacidad_inspiratoria = tk.Button(ventana, text="Calcular Capacidad Inspiratoria", command=calcular_capacidad_inspiratoria)
button_calcular_capacidad_inspiratoria.pack()

    # Create the labels and entries for the fourth calculation
label_volumen_espiratorio_reserva_2 = tk.Label(ventana, text="Volumen Espiratorio de Reserva:")
label_volumen_espiratorio_reserva_2.pack()
entry_volumen_espiratorio_reserva_2 = tk.Entry(ventana)
entry_volumen_espiratorio_reserva_2.pack()

    # Create the button for calculating the fourth calculation
button_calcular_capacidad_vital = tk.Button(ventana, text="Calcular Capacidad Vital", command=calcular_capacidad_vital)
button_calcular_capacidad_vital.pack()

    # Create the labels and entries for the fifth calculation
label_volumen_residual_2 = tk.Label(ventana, text="Volumen Residual:")
label_volumen_residual_2.pack()
entry_volumen_residual_2 = tk.Entry(ventana)
entry_volumen_residual_2.pack()

    # Create the button for calculating the fifth calculation
button_calcular_capacidad_pulmonar_total = tk.Button(ventana, text="Calcular Capacidad Pulmonar Total", command=calcular_capacidad_pulmonar_total)
button_calcular_capacidad_pulmonar_total.pack()

    # Create the label for displaying the results
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

    # Create the menu bar
menu_bar = tk.Menu(ventana)
ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Mostrar ayuda", command=mostrar_ayuda)
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

    # Configure the menu bar
ventana.config(menu=menu_bar)

        

ventana.mainloop()




