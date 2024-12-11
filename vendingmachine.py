import tkinter as tk
from tkinter import messagebox

# Item catalog with prices and quantities available
items = {
    'Soda': {'price': 20, 'quantity': 10},
    'Chips': {'price': 10, 'quantity': 8},
    'Candy': {'price': 5, 'quantity': 15},
    'Juice': {'price': 20, 'quantity': 5},
    'Water': {'price': 15, 'quantity': 20}
}

# Function to calculate total price of selected items
def calculate_total(selected_items):
    total = 0
    for item in selected_items:
        total += items[item]['price']
    return total

# Function to handle the purchase process (display selected items and refresh quantities)
def purchase_items():
    selected_items = []
    for item, var in item_vars.items():
        if var.get() == 1 and items[item]['quantity'] > 0:
            selected_items.append(item)
            # Decrease quantity for the selected item
            items[item]['quantity'] -= 1

    if not selected_items:
        messagebox.showwarning("No Selection", "Please select at least one item to purchase.")
        return
    
    # Calculate total price for selected items
    total_price = calculate_total(selected_items)

    # Display the selected items and their total price
    messagebox.showinfo("Purchase Successful", f"You purchased: {', '.join(selected_items)}\nTotal price: Rupees {total_price:.2f}")

    # Refresh the window to update available quantities
    refresh_window()

# Function to refresh the window and update the items' quantities and selections
def refresh_window():
    for widget in app.winfo_children():
        widget.destroy()  # Destroy all widgets (except the window)

    # Recreate the window contents
    create_widgets()

# Function to create the widgets for the window
def create_widgets():
    # Title label
    title_label = tk.Label(app, text="Vending Machine", font=("Arial", 20), bg="antiquewhite", fg="black")
    title_label.pack(pady=10)

    # Creating checkbuttons for each item with quantity information and space between items
    global item_vars
    item_vars = {}
    for item, details in items.items():
        var = tk.IntVar()
        item_vars[item] = var

        item_frame = tk.Frame(app, bg="antiquewhite")
        item_label = tk.Label(item_frame, text=f"{item} - Rupees {details['price']} (Available: {details['quantity']})", 
                              font=("Arial", 12), bg="antiquewhite", fg="black")
        item_check = tk.Checkbutton(item_frame, text=f"Select {item}", variable=var, font=("Arial", 12), bg="antiquewhite", fg="black")
        
        item_label.pack(anchor="w", padx=20)
        item_check.pack(anchor="w", padx=20, pady=5)
        
        item_frame.pack(pady=5)  # Add space between each item frame

    # Purchase button
    purchase_button = tk.Button(app, text="Purchase", font=("Arial", 14), command=purchase_items, bg="green", fg="white")
    purchase_button.pack(pady=20)

# Creating the main application window
app = tk.Tk()
app.title("Vending Machine")
app.geometry("500x500")  # Adjusted size for centering
app.config(bg="antiquewhite")

# Centering the window on the screen
window_width = 500
window_height = 500
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
app.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

# Initial widget creation
create_widgets()

# Run the application
app.mainloop()
