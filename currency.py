from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates


root = Tk()
root.title('DwB App - Currency Conversion')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x650")

# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=580)
helper_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
helper_frame.pack(fill="both", expand=1)

# Add our Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(helper_frame, text="Help")


#######################
# CURRENCY STUFF
#######################


# Home Currency labelFrame
home = LabelFrame(currency_frame, text="Your Home Currency", font=("batmanForeverAlternate", 11))
home.pack(pady=20)
# Home currency entry box
home_entry = Entry(home, font=("Engravers MT", 24))
home_entry.pack(pady=10, padx=10)

# Conversion Currency labelFrame
conversion = LabelFrame(currency_frame, text="Conversion Currency", font=("batmanForeverAlternate", 11))
conversion.pack(pady=20)
# Convert_To Entry box
conversion_entry = Entry(conversion, font=("Engravers MT", 24))
conversion_entry.pack(pady=10, padx=10)

# amount labelFrame
label_amount = LabelFrame(currency_frame, text="Amount To Convert", font=("batmanForeverAlternate", 11))
label_amount.pack(pady=20)
# amount Entry box
amount_entry = Entry(label_amount, font=("Times New Roman", 24))
amount_entry.pack(pady=10, padx=10)




root.mainloop()