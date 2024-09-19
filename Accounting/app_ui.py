import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Accounting App")
        self.geometry("800x500")
        self.config(bg="#f0f0f0")

        self.sidebar = tk.Frame(self, bg="#333", width=200, height=500)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.product_button = tk.Button(self.sidebar, text="محصولات", command=self.product_page, bg="#4CAF50",
                                        fg="#fff", font=("Arial", 12), width=10, height=2, bd=0, relief="ridge",justify='right')
        self.product_button.pack(pady=20)

        self.sales_button = tk.Button(self.sidebar, text="Sales", command=self.sales_page, bg="#03A9F4", fg="#fff",
                                      font=("Arial", 12), width=10, height=2, bd=0, relief="ridge")
        self.sales_button.pack(pady=20)

        self.management_button = tk.Button(self.sidebar, text="Management", command=self.management_page, bg="#FF9800",
                                           fg="#fff", font=("Arial", 12), width=10, height=2, bd=0, relief="ridge")
        self.management_button.pack(pady=20)

        self.content_frame = tk.Frame(self, bg="#f0f0f0", width=600, height=500)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def product_page(self):
        self.title("صفحه محصولات")
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self, bg="#f0f0f0", width=600, height=500)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.product_label = tk.Label(self.content_frame, text="Products Page", font=("Arial", 24), bg="#f0f0f0")
        self.product_label.pack(pady=20)

        self.product_tree = ttk.Treeview(self.content_frame,
                                         columns=("Product ID", "Product Name", "Quantity", "Price"))
        self.product_tree.pack(pady=20)

        self.product_tree.heading("#0", text="Product")
        self.product_tree.heading("Product ID", text="ID")
        self.product_tree.heading("Product Name", text="Name")
        self.product_tree.heading("Quantity", text="Quantity")
        self.product_tree.heading("Price", text="Price")

        self.product_tree.insert("", "end", values=("1", "Product 1", "10", "100.00"))
        self.product_tree.insert("", "end", values=("2", "Product 2", "20", "200.00"))
        self.product_tree.insert("", "end", values=("3", "Product 3", "30", "300.00"))

    def sales_page(self):
        self.title("Sales Page")
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self, bg="#f0f0f0", width=600, height=500)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.sales_label = tk.Label(self.content_frame, text="Sales Page", font=("Arial", 24), bg="#f0f0f0")
        self.sales_label.pack(pady=20)

        self.sales_tree = ttk.Treeview(self.content_frame,
                                       columns=("Sale ID", "Product ID", "Quantity", "Date", "Total"))
        self.sales_tree.pack(pady=20)

        self.sales_tree.heading("#0", text="Sale")
        self.sales_tree.heading("Sale ID", text="ID")
        self.sales_tree.heading("Product ID", text="Product ID")
        self.sales_tree.heading("Quantity", text="Quantity")
        self.sales_tree.heading("Date", text="Date")
        self.sales_tree.heading("Total", text="Total")

        self.sales_tree.insert("", "end", values=("1", "1", "5", "2022-01-01", "500.00"))
        self.sales_tree.insert("", "end", values=("2", "2", "10", "2022-01-05", "1000.00"))
        self.sales_tree.insert("", "end", values=("3", "3", "15", "2022-01-10", "1500.00"))


    def management_page(self):
        self.title("Management Page")
        self.content_frame.destroy()
        self.content_frame = tk.Frame(self, bg="#f0f0f0", width=600, height=500)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.management_label = tk.Label(self.content_frame, text="Management Page", font=("Arial", 24), bg="#f0f0f0")
        self.management_label.pack(pady=20)

        self.management_tree = ttk.Treeview(self.content_frame, columns=("Employee ID", "Name", "Role", "Salary"))
        self.management_tree.pack(pady=20)

        self.management_tree.heading("#0", text="Employee")
        self.management_tree.heading("Employee ID", text="ID")
        self.management_tree.heading("Name", text="Name")
        self.management_tree.heading("Role", text="Role")
        self.management_tree.heading("Salary", text="Salary")

        self.management_tree.insert("", "end", values=("1", "John Doe", "Manager", "5000.00"))
        self.management_tree.insert("", "end", values=("2", "Jane Doe", "Accountant", "4000.00"))
        self.management_tree.insert("", "end", values=("3", "Bob Smith", "Salesman", "3000.00"))


if __name__ == "__main__":
    app = Application()
    app.mainloop()
