
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import openpyxl

# Function to save sales data to a file
def save_sales_data():
    with open('sales_data.txt', 'w') as file:
        for product, details in sales_data.items():
            amount = details["amount"]
            delivery_date = details["delivery_date"]
            customer_name = details["customer_name"]
            customer_address = details["customer_address"]
            cost_price = details["cost_price"]
            selling_price = details["selling_price"]
            quantity = details["quantity"]
            tentative_business = details["tentative_business"]
            file.write(f"{product},{amount},{delivery_date},{customer_name}|{customer_address},{cost_price},{selling_price},{quantity},{tentative_business}\n")

# Function to add a new sale
def add_sale():
    product = product_entry.get()
    amount = int(amount_entry.get())
    delivery_date = delivery_date_entry.get()
    customer_name = customer_name_entry.get()
    customer_address = customer_address_entry.get()
    cost_price = float(cost_price_entry.get())
    selling_price = float(selling_price_entry.get())
    quantity = int(quantity_entry.get())
    tentative_business = tentative_business_entry.get()
    
    if product and amount > 0 and delivery_date and customer_name and customer_address and cost_price >= 0 and selling_price >= 0 and quantity > 0:
        if product in sales_data:
            sales_data[product]["amount"] += amount
        else:
            sales_data[product] = {
                "amount": amount,
                "delivery_date": delivery_date,
                "customer_name": customer_name,
                "customer_address": customer_address,
                "cost_price": cost_price,
                "selling_price": selling_price,
                "quantity": quantity,
                "tentative_business": tentative_business
            }
        update_display()
        save_sales_data()
        messagebox.showinfo("Success", f"Sale of {amount} units of {product} added.")
    else:
        messagebox.showerror("Error", "Please enter valid data in all fields.")

# Function to clear the input fields
def clear_fields():
    product_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    delivery_date_entry.delete(0, tk.END)
    customer_name_entry.delete(0, tk.END)
    customer_address_entry.delete(0, tk.END)
    cost_price_entry.delete(0, tk.END)
    selling_price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    tentative_business_entry.delete(0, tk.END)

# Function to confirm and exit the application
def exit_app():
    response = messagebox.askyesno("Exit", "Do you want to save and exit?")
    if response:
        save_sales_data()
        root.destroy()

# Initialize an empty dictionary to store sales data
sales_data = {}

# Load existing sales data from a file if it exists
if os.path.exists('sales_data.txt'):
    with open('sales_data.txt', 'r') as file:
        for line in file:
            product, amount, delivery_date, customer_info, cost_price, selling_price, quantity, tentative_business = line.strip().split(',')
            customer_name, customer_address = customer_info.split('|')
            sales_data[product] = {
                "amount": int(amount),
                "delivery_date": delivery_date,
                "customer_name": customer_name,
                "customer_address": customer_address,
                "cost_price": float(cost_price),
                "selling_price": float(selling_price),
                "quantity": int(quantity),
                "tentative_business": tentative_business
            }

# Function to save sales data to a file
def save_sales_data():
    with open('sales_data.txt', 'w') as file:
        for product, details in sales_data.items():
            amount = details["amount"]
            delivery_date = details["delivery_date"]
            customer_name = details["customer_name"]
            customer_address = details["customer_address"]
            cost_price = details["cost_price"]
            selling_price = details["selling_price"]
            quantity = details["quantity"]
            tentative_business = details["tentative_business"]
            file.write(f"{product},{amount},{delivery_date},{customer_name}|{customer_address},{cost_price},{selling_price},{quantity},{tentative_business}\n")

# Function to add a new sale
def add_sale():
    product = product_entry.get()
    amount = int(amount_entry.get())
    delivery_date = delivery_date_entry.get()
    customer_name = customer_name_entry.get()
    customer_address = customer_address_entry.get()
    cost_price = float(cost_price_entry.get())
    selling_price = float(selling_price_entry.get())
    quantity = int(quantity_entry.get())
    tentative_business = tentative_business_entry.get()
    
    if product and amount > 0 and delivery_date and customer_name and customer_address and cost_price >= 0 and selling_price >= 0 and quantity > 0:
        if product in sales_data:
            sales_data[product]["amount"] += amount
        else:
            sales_data[product] = {
                "amount": amount,
                "delivery_date": delivery_date,
                "customer_name": customer_name,
                "customer_address": customer_address,
                "cost_price": cost_price,
                "selling_price": selling_price,
                "quantity": quantity,
                "tentative_business": tentative_business
            }
        update_display()
        save_sales_data()
        messagebox.showinfo("Success", f"Sale of {amount} units of {product} added.")
    else:
        messagebox.showerror("Error", "Please enter valid data in all fields.")

# Function to clear the input fields
def clear_fields():
    product_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    delivery_date_entry.delete(0, tk.END)
    customer_name_entry.delete(0, tk.END)
    customer_address_entry.delete(0, tk.END)
    cost_price_entry.delete(0, tk.END)
    selling_price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    tentative_business_entry.delete(0, tk.END)

# Function to confirm and exit the application
def exit_app():
    response = messagebox.askyesno("Exit", "Do you want to save and exit?")
    if response:
        save_sales_data()
        root.destroy()

# Function to update the display
def update_display():
    sales_text.delete(1.0, tk.END)
    total_revenue = 0
    for product, details in sales_data.items():
        amount = details["amount"]
        delivery_date = details["delivery_date"]
        customer_name = details["customer_name"]
        customer_address = details["customer_address"]
        cost_price = details["cost_price"]
        selling_price = details["selling_price"]
        quantity = details["quantity"]
        tentative_business = details["tentative_business"]
        sales_text.insert(tk.END, f"Product: {product}\nAmount: {amount} units\nDelivery Date: {delivery_date}\nCustomer Name: {customer_name}\nCustomer Address: {customer_address}\nCost Price: ${cost_price:.2f}\nSelling Price: ${selling_price:.2f}\nQuantity: {quantity}\nTentative Business: {tentative_business}\n\n")
        total_revenue += amount
    sales_text.insert(tk.END, f"Total Revenue: ${total_revenue}")
    total_revenue_label.config(text=f"Total Revenue: ${total_revenue}")

# Create the main window
root = tk.Tk()
root.title("Sales Tracker - TRB TECHNOLOGIES GURGAON BRANCH")  # Adding organizer name

# Organizer Label
organizer_label = tk.Label(root, text="TRB TECHNOLOGIES GURGAON", font=("Helvetica", 16, "bold"))
organizer_label.pack()

# Frame for Product Details
product_frame = tk.LabelFrame(root, text="Product Details")
product_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Product
product_label = tk.Label(product_frame, text="Product:")
product_label.pack(side="left")

product_entry = tk.Entry(product_frame)
product_entry.pack(side="left")

# Amount
amount_label = tk.Label(product_frame, text="Amount:")
amount_label.pack(side="left")

amount_entry = tk.Entry(product_frame)
amount_entry.pack(side="left")

# Delivery Date
delivery_date_label = tk.Label(product_frame, text="Delivery Date:")
delivery_date_label.pack(side="left")

delivery_date_entry = tk.Entry(product_frame)
delivery_date_entry.pack(side="left")

# Customer Name
customer_name_label = tk.Label(product_frame, text="Customer Name:")
customer_name_label.pack(side="left")

customer_name_entry = tk.Entry(product_frame)
customer_name_entry.pack(side="left")

# Customer Address
customer_address_label = tk.Label(product_frame, text="Customer Address:")
customer_address_label.pack(side="left")

customer_address_entry = tk.Entry(product_frame)
customer_address_entry.pack(side="left")

# Cost Price
cost_price_label = tk.Label(product_frame, text="Cost Price:")
cost_price_label.pack(side="left")

cost_price_entry = tk.Entry(product_frame)
cost_price_entry.pack(side="left")

# Selling Price
selling_price_label = tk.Label(product_frame, text="Selling Price:")
selling_price_label.pack(side="left")

selling_price_entry = tk.Entry(product_frame)
selling_price_entry.pack(side="left")

# Quantity
quantity_label = tk.Label(product_frame, text="Quantity:")
quantity_label.pack(side="left")

quantity_entry = tk.Entry(product_frame)
quantity_entry.pack(side="left")

# Tentative Business
tentative_business_label = tk.Label(product_frame, text="Tentative Business:")
tentative_business_label.pack(side="left")

tentative_business_entry = tk.Entry(product_frame)
tentative_business_entry.pack(side="left")

# Function to update the display
def update_display():
    sales_text.delete(1.0, tk.END)
    total_revenue = 0
    total_profit = 0
    
    for product, details in sales_data.items():
        amount = details["amount"]
        delivery_date = details["delivery_date"]
        customer_name = details["customer_name"]
        customer_address = details["customer_address"]
        cost_price = details["cost_price"]
        selling_price = details["selling_price"]
        quantity = details["quantity"]
        tentative_business = details["tentative_business"]
        
        # Calculate profit/loss
        profit_loss = (selling_price - cost_price) * amount
        total_revenue += amount
        total_profit += profit_loss
        
        sales_text.insert(tk.END, f"Product: {product}\nAmount: {amount} units\nDelivery Date: {delivery_date}\nCustomer Name: {customer_name}\nCustomer Address: {customer_address}\nCost Price: ${cost_price:.2f}\nSelling Price: ${selling_price:.2f}\nQuantity: {quantity}\nTentative Business: {tentative_business}\nProfit/Loss: ${profit_loss:.2f}\n\n")
    
    sales_text.insert(tk.END, f"Total Revenue: ${total_revenue}\n")
    sales_text.insert(tk.END, f"Total Profit/Loss: ${total_profit:.2f}")
    total_revenue_label.config(text=f"Total Revenue: ${total_revenue}")
    total_profit_label.config(text=f"Total Profit/Loss: ${total_profit:.2f}")


# Add Sale Button
add_button = tk.Button(root, text="Add Sale", command=add_sale)
add_button.pack(pady=10)

# Frame for Sales Data Display
sales_frame = tk.LabelFrame(root, text="Sales Data")
sales_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Total Revenue Label
total_revenue_label = tk.Label(sales_frame, text="Total Revenue:")
total_revenue_label.pack()

# Text Display for Sales Data
sales_text = tk.Text(sales_frame)
sales_text.pack()

# Total Profit Label
total_profit_label = tk.Label(sales_frame, text="Total Profit:")
total_profit_label.pack()

# Save to Excel Button
save_excel_button = tk.Button(root, text="Save to Excel", command=save_to_excel)
save_excel_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Save and Exit", command=exit_app)
exit_button.pack(pady=10)

# Start the main loop
root.mainloop()

