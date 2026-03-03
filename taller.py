import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque


class VelourLuxeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Velour Luxe Logistics 💖🎀")
        self.root.geometry("960x540")
        self.root.configure(bg="#FFF5F8")

        # ===== Data Structures =====
        self.orders_queue = deque()   # FIFO
        self.truck_stack = []         # LIFO

        self.categories = ["Accessories 🎀", "Makeup 💄",
                           "Shoes 👠", "Dresses 👗", "Handbags 👜"]

        self.setup_styles()
        self.create_widgets()
        self.refresh()

    # =========================
    # STYLE CONFIGURATION
    # =========================
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.ROSE_LIGHT = "#FCE4EC"
        self.ROSE_SOFT = "#F8BBD0"
        self.ROSE_MEDIUM = "#F06292"
        self.ROSE_STRONG = "#C2185B"
        self.ROSE_DARK = "#880E4F"
        self.WHITE = "#FFFFFF"

        self.style.configure("TFrame", background="#FFF5F8")
        self.style.configure("TLabel",
                             background="#FFF5F8",
                             foreground=self.ROSE_DARK,
                             font=("Segoe UI", 10))
        self.style.configure("TEntry", padding=6)
        self.style.configure("TCombobox", padding=6)

    # =========================
    # UI CREATION
    # =========================
    def create_widgets(self):

        # Header
        header = tk.Label(self.root,
                          text="💖 Velour Luxe Logistics 🎀",
                          bg=self.ROSE_STRONG,
                          fg="white",
                          font=("Georgia", 26, "bold"),
                          pady=18)
        header.pack(fill="x")

        self.main = ttk.Frame(self.root, padding=20)
        self.main.pack(fill="both", expand=True)

        self.main.columnconfigure((0, 1, 2), weight=1)
        self.main.rowconfigure(4, weight=1)

        # Variables
        self.order_id_var = tk.StringVar()
        self.client_var = tk.StringVar()
        self.category_var = tk.StringVar(value=self.categories[0])

        # Inputs
        ttk.Label(self.main, text="Order ID 💌").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.main, textvariable=self.order_id_var).grid(row=1, column=0, sticky="ew", padx=8)

        ttk.Label(self.main, text="Client Name 💕").grid(row=0, column=1, sticky="w")
        ttk.Entry(self.main, textvariable=self.client_var).grid(row=1, column=1, sticky="ew", padx=8)

        ttk.Label(self.main, text="Category 🎀").grid(row=0, column=2, sticky="w")
        ttk.Combobox(self.main,
                     textvariable=self.category_var,
                     values=self.categories,
                     state="readonly").grid(row=1, column=2, sticky="ew", padx=8)

        # Buttons
        buttons = ttk.Frame(self.main)
        buttons.grid(row=2, column=0, columnspan=3, sticky="ew", pady=20)
        buttons.columnconfigure((0, 1, 2), weight=1)

        tk.Button(buttons,
                  text="Add Order 💖",
                  bg=self.ROSE_MEDIUM,
                  fg="white",
                  font=("Segoe UI", 10, "bold"),
                  relief="flat",
                  command=self.add_order).grid(row=0, column=0, sticky="ew", padx=8)

        tk.Button(buttons,
                  text="Process Order 🚚🎀",
                  bg=self.ROSE_SOFT,
                  fg=self.ROSE_DARK,
                  font=("Segoe UI", 10, "bold"),
                  relief="flat",
                  command=self.process_next).grid(row=0, column=1, sticky="ew", padx=8)

        tk.Button(buttons,
                  text="Deliver Order 💝",
                  bg=self.ROSE_STRONG,
                  fg="white",
                  font=("Segoe UI", 10, "bold"),
                  relief="flat",
                  command=self.deliver_next).grid(row=0, column=2, sticky="ew", padx=8)

        # Lists
        ttk.Label(self.main, text="Orders Queue (FIFO) 💗").grid(row=3, column=0, sticky="w")

        self.queue_list = tk.Listbox(self.main,
                                     bg=self.WHITE,
                                     fg=self.ROSE_DARK,
                                     font=("Segoe UI", 10),
                                     highlightbackground=self.ROSE_SOFT,
                                     highlightthickness=2,
                                     borderwidth=0)
        self.queue_list.grid(row=4, column=0, sticky="nsew", padx=8, pady=8)

        ttk.Label(self.main, text="Truck Stack (LIFO) 🎀").grid(row=3, column=1, sticky="w")

        self.truck_list = tk.Listbox(self.main,
                                     bg=self.ROSE_LIGHT,
                                     fg=self.ROSE_DARK,
                                     font=("Segoe UI", 10),
                                     highlightbackground=self.ROSE_MEDIUM,
                                     highlightthickness=2,
                                     borderwidth=0)
        self.truck_list.grid(row=4, column=1, sticky="nsew", padx=8, pady=8)

    # =========================
    # LOGIC METHODS
    # =========================
    def refresh(self):
        self.queue_list.delete(0, tk.END)
        for o in list(self.orders_queue):
            self.queue_list.insert(tk.END, o)

        self.truck_list.delete(0, tk.END)
        for o in self.truck_stack:
            self.truck_list.insert(tk.END, o)

    def add_order(self):
        order_id = self.order_id_var.get().strip()
        client = self.client_var.get().strip()
        category = self.category_var.get().strip()

        if not order_id or not client:
            messagebox.showwarning("Missing Data 💔",
                                   "Order ID and Client Name are required.")
            return

        self.orders_queue.append(f"{order_id} | {client} | {category}")
        self.order_id_var.set("")
        self.client_var.set("")
        self.refresh()

    def process_next(self):
        if not self.orders_queue:
            messagebox.showinfo("Queue Empty 💕", "No orders to process.")
            return

        order = self.orders_queue.popleft()
        self.truck_stack.append(order)

        messagebox.showinfo("Processed 💖",
                            f"Order loaded to truck:\n{order}")
        self.refresh()

    def deliver_next(self):
        if not self.truck_stack:
            messagebox.showinfo("Truck Empty 🎀",
                                "No packages to deliver.")
            return

        order = self.truck_stack.pop()
        messagebox.showinfo("Delivered 💝",
                            f"Order delivered:\n{order}")
        self.refresh()


# =========================
# RUN APPLICATION
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = VelourLuxeApp(root)
    root.mainloop()