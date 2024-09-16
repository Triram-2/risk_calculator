import tkinter as tk
from tkinter import messagebox

def calculation():
    '''
    Выводит на заготовленное место результат расчетов.
    Получает аргументы прямо через глобальную область видимости.
    
    Args:
        entry_point (float): Точка входа.
        stop_loss (float): Стоп-лосс.
        deposit(float): Депозит.
        shoulder(float): Плечо.
        risk_menegment(float): Риск-менеджмент(% от депозита, который можно потерять за сделку.)
    
    Return:
        Выводит на заготовленное место результат расчетов.
    '''
    try:
        entry_point = float(input_entry_point.get())
        stop_loss = float(input_stop_loss.get())
        deposit = float(input_deposit.get())
        shoulder = float(input_shoulder.get())
        risk_menegment = float(input_risk_menegment.get())
        
        if deposit == 0:
            messagebox.showerror("Ошибка", "Если у Вас депозит 0, Вы не можете зайти в сделку!")
            return
        
        ub = 1 - stop_loss / entry_point
        ub = f'{ub:.3f}'
        ub = float(ub)
        lot_size = (((deposit * (risk_menegment / 100)) / (ub)) / entry_point) * shoulder
        for_output.config(text=f"В сделку следует заходить на: {lot_size:.4f} единиц.")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")

# Создание графического интерфейса.
root = tk.Tk()

root.title("Калькулятор Риска")

tk.Label(root, text="Точка входа:").grid(row=0, column=0)
input_entry_point = tk.Entry(root)
input_entry_point.grid(row=0, column=1)

tk.Label(root, text="Стоп лосс:").grid(row=1, column=0)
input_stop_loss = tk.Entry(root)
input_stop_loss.grid(row=1, column=1)

tk.Label(root, text="Депозит:").grid(row=2, column=0)
input_deposit = tk.Entry(root)
input_deposit.grid(row=2, column=1)

tk.Label(root, text="Плечо(если спот - введите 1):").grid(row=3, column=0)
input_shoulder = tk.Entry(root)
input_shoulder.grid(row=3, column=1)

tk.Label(root, text="Риск менеджмент(рекомендую 1 или 3%):").grid(row=4, column=0)
input_risk_menegment = tk.Entry(root)
input_risk_menegment.grid(row=4, column=1)

calculation_button = tk.Button(root, text="Рассчитать", command=calculation)
calculation_button.grid(row=5, columnspan=2)

for_output = tk.Label(root, text="")
for_output.grid(row=6, columnspan=2)

# Запуск.
root.mainloop()
