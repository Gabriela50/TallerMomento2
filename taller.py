import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque

# ===== Data Structures =====
orders_queue = deque()   # FIFO
truck_stack = []         # LIFO

#  Fashion Categories
categories = ["Accessories ", "Makeup ", "Shoes ", "Dresses ", "Handbags "]


def refresh():
    queue_list.delete(0, tk.END)
    for o in list(orders_queue):
        queue_list.insert(tk.END, o)

    truck_list.delete(0, tk.END)
    for o in truck_stack:
        truck_list.insert(tk.END, o)


def add_order():
    order_id = order_id_var.get().strip()
    client = client_var.get().strip()
    category = category_var.get().strip()

    if not order_id or not client:
        messagebox.showwarning("Missing Data ", "Order ID and Client Name are required.")
        return

    orders_queue.append(f"{order_id} | {client} | {category}")
    order_id_var.set("")
    client_var.set("")
    refresh()


def process_next():
    if not orders_queue:
        messagebox.showinfo("Queue Empty 💕", "No orders to process.")
        return

    order = orders_queue.popleft()
    truck_stack.append(order)

    messagebox.showinfo("Processed 💖", f"Order loaded to truck:\n{order}")
    refresh()


def deliver_next():
    if not truck_stack:
        messagebox.showinfo("Truck Empty 🎀", "No packages to deliver.")
        return

    order = truck_stack.pop()
    messagebox.showinfo("Delivered 💝", f"Order delivered:\n{order}")
    refresh()


# ===== GUI Elegant Feminine Corporate Style =====
root = tk.Tk()
root.title("Velour Luxe Logistics 💖🎀")
root.geometry("960x540")
root.configure(bg="#FFF5F8")

style = ttk.Style()
style.theme_use("clam")

# 💗 Elegant Pink Palette
ROSE_LIGHT = "#FCE4EC"
ROSE_SOFT = "#F8BBD0"
ROSE_MEDIUM = "#F06292"
ROSE_STRONG = "#C2185B"
ROSE_DARK = "#880E4F"
WHITE = "#FFFFFF"

style.configure("TFrame", background="#FFF5F8")
style.configure("TLabel",
                background="#FFF5F8",
                foreground=ROSE_DARK,
                font=("Segoe UI", 10))
style.configure("TEntry", padding=6)
style.configure("TCombobox", padding=6)

main = ttk.Frame(root, padding=20)
main.pack(fill="both", expand=True)

main.columnconfigure((0, 1, 2), weight=1)
main.rowconfigure(4, weight=1)

# ===== Header =====
header = tk.Label(root,
                  text="💖 Velour Luxe Logistics 🎀",
                  bg=ROSE_STRONG,
                  fg="white",
                  font=("Segoe UI", 20, "bold"),
                  pady=15)
header.pack(fill="x")

# Variables
order_id_var = tk.StringVar()
client_var = tk.StringVar()
category_var = tk.StringVar(value="Accessories 🎀")

# ===== Inputs =====
ttk.Label(main, text="Order ID 💌").grid(row=0, column=0, sticky="w")
ttk.Entry(main, textvariable=order_id_var).grid(row=1, column=0, sticky="ew", padx=8)

ttk.Label(main, text="Client Name 💕").grid(row=0, column=1, sticky="w")
ttk.Entry(main, textvariable=client_var).grid(row=1, column=1, sticky="ew", padx=8)

ttk.Label(main, text="Category 🎀").grid(row=0, column=2, sticky="w")
ttk.Combobox(main, textvariable=category_var, values=categories, state="readonly")\
    .grid(row=1, column=2, sticky="ew", padx=8)

# ===== Buttons =====
buttons = ttk.Frame(main)
buttons.grid(row=2, column=0, columnspan=3, sticky="ew", pady=20)
buttons.columnconfigure((0, 1, 2), weight=1)

btn_add = tk.Button(buttons,
                    text="Add Order 💖",
                    bg=ROSE_MEDIUM,
                    fg="white",
                    activebackground=ROSE_STRONG,
                    font=("Segoe UI", 10, "bold"),
                    relief="flat",
                    command=add_order)
btn_add.grid(row=0, column=0, sticky="ew", padx=8)

btn_process = tk.Button(buttons,
                        text="Process Order 🚚🎀",
                        bg=ROSE_SOFT,
                        fg=ROSE_DARK,
                        activebackground=ROSE_MEDIUM,
                        font=("Segoe UI", 10, "bold"),
                        relief="flat",
                        command=process_next)
btn_process.grid(row=0, column=1, sticky="ew", padx=8)

btn_deliver = tk.Button(buttons,
                        text="Deliver Order 💝",
                        bg=ROSE_STRONG,
                        fg="white",
                        activebackground=ROSE_DARK,
                        font=("Segoe UI", 10, "bold"),
                        relief="flat",
                        command=deliver_next)
btn_deliver.grid(row=0, column=2, sticky="ew", padx=8)

# ===== Lists =====
ttk.Label(main, text="Orders Queue  💗").grid(row=3, column=0, sticky="w")

queue_list = tk.Listbox(main,
                        bg=WHITE,
                        fg=ROSE_DARK,
                        font=("Segoe UI", 10),
                        highlightbackground=ROSE_SOFT,
                        highlightthickness=2,
                        borderwidth=0)
queue_list.grid(row=4, column=0, sticky="nsew", padx=8, pady=8)

ttk.Label(main, text="Truck Stack  🎀").grid(row=3, column=1, sticky="w")

truck_list = tk.Listbox(main,
                        bg=ROSE_LIGHT,
                        fg=ROSE_DARK,
                        font=("Segoe UI", 10),
                        highlightbackground=ROSE_MEDIUM,
                        highlightthickness=2,
                        borderwidth=0)
truck_list.grid(row=4, column=1, sticky="nsew", padx=8, pady=8)

refresh()
root.mainloop()