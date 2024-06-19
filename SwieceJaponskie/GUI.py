import tkinter as tk
from tkinter import ttk
from logic import download_data, change_structure, find_match, draw_plot_candles

def fetch_and_draw():
    symbol = symbol_entry.get()
    interval = interval_entry.get()
    limit = limit_entry.get()
    try:
        candles = download_data(symbol, interval, limit)
        formatted_candles = change_structure(candles)
        last_ten = formatted_candles[-10:]
        match = find_match(formatted_candles[:-10], last_ten)
        draw_plot_candles(f"{symbol} {interval} Last 10 Candles", last_ten)
        draw_plot_candles(f"{symbol} {interval} Match", match)
    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title('Market Data Visualization')
root.geometry("200x200")

frame = tk.Frame(root, bg='#ffffff')
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

tk.Label(frame, text="Symbol:").grid(row=0, column=0, sticky='w')
symbol_entry = tk.Entry(frame)
symbol_entry.grid(row=0, column=1, sticky='ew')

tk.Label(frame, text="Interval:").grid(row=1, column=0, sticky='w')
interval_entry = tk.Entry(frame)
interval_entry.grid(row=1, column=1, sticky='ew')

tk.Label(frame, text="Limit:").grid(row=2, column=0, sticky='w')
limit_entry = tk.Entry(frame)
limit_entry.grid(row=2, column=1, sticky='ew')

fetch_button = tk.Button(frame, text="Upload Data", command=fetch_and_draw)
fetch_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
