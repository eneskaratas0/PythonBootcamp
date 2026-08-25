import tkinter as tk


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
    except ValueError:
        result_label.config(text="Lütfen geçerli bir kilo girin.")
        return

    try:
        height_cm = float(height_entry.get())
    except ValueError:
        result_label.config(text="Lütfen geçerli bir boy girin.")
        return

    if not (2 <= weight <= 300):
        result_label.config(text="Kilo 2-300 kg arasında olmalı.")
        return

    if not (30 <= height_cm <= 250):
        result_label.config(text="Boy 30-250 cm arasında olmalı.")
        return

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Zayıf"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Fazla Kilolu"
    else:
        category = "Obez"

    result_label.config(text=f"BMI: {bmi:.2f} ({category})")


window = tk.Tk()
window.title("BMI Hesaplayıcı")
window.geometry("300x220")

tk.Label(window, text="BMI Hesaplayıcı", font=("Arial", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=10
)

tk.Label(window, text="Kilo (kg):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Boy (cm):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1, padx=10, pady=5)

weight_entry.bind("<Return>", lambda event: calculate_bmi())
height_entry.bind("<Return>", lambda event: calculate_bmi())

tk.Button(window, text="Hesapla", command=calculate_bmi).grid(
    row=3, column=0, columnspan=2, pady=10
)

result_label = tk.Label(window, text="", font=("Arial", 11))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
