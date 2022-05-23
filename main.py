from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates


root = Tk()
root.title('DwB App - Currency Conversion')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x400")

# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# Add our Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# Disable 2nd tab
my_notebook.tab(1, state='disabled')

#######################
# CURRENCY STUFF
#######################
def lock():
	if not home_entry.get() or not conversion_entry.get():
		messagebox.showwarning("WARNING!", "You Didn't Fill Out All The Fields")	
	else:
		# Disable entry boxes
		home_entry.config(state="disabled")
		conversion_entry.config(state="disabled")
		# Enable tab
		my_notebook.tab(1, state='normal')
		# Change Tab Field
		amount_label.config(text=f'Amount of {home_entry.get().upper()} To Convert To {conversion_entry.get().upper()}')
		converted_label.config(text=f'Equals This Many {conversion_entry.get().upper()}')
		convert_button.config(text=f'Convert From {home_entry.get().upper()}')
def unlock():
	# Enable entry boxes
	home_entry.config(state="normal")
	conversion_entry.config(state="normal")
	# Disable Tab
	my_notebook.tab(1, state='disabled')


home = LabelFrame(currency_frame, text="Your Home Currency")
home.pack(pady=20)

# Home currency entry box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)



# Convert To Entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)


# Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create Buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)


#######################
# CONVERSION STUFF
#######################
def convert():
	try:
		# Clear Converted Entry Box
		converted_entry.delete(0, END)

		# Convert > proses hitungan disini 
		moneyFrom = home_entry.get().upper()
		moneyTo = conversion_entry.get().upper()
		amount = amount_entry.get()

		c = CurrencyRates()
		result = c.convert(moneyFrom,moneyTo,int(amount))
		result = round(result,2)

		# update entry box > tambahkan hasil hitungan disini
		converted_entry.insert(0, f'{moneyTo}= {result}')
	except ValueError:
		messagebox.showwarning('WARNING!', 'Please enter the amount value!')


def clear():
	amount_entry.delete(0, END)
	converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text="Amount To Conver")
amount_label.pack(pady=20)

# Entry Box For Amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# Fake Label for spacing
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()


root.mainloop()