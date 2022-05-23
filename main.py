from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates


root = Tk()
root.title('DwB App / Currency Converter')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x650")

# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=615)
helper_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
helper_frame.pack(fill="both", expand=1)

# Add our Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(helper_frame, text="Help")


#######################
# CURRENCY STUFF
#######################


def tetapkan():
    if not home_entry.get() or not conversion_entry.get() :
        messagebox.showwarning("Warning!", "Harus mengisi kedua inputan di atas !")
    else:
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        # mengubah tulisan pada tabel amount
        label_amount.config(text=f'Jumlah dari {home_entry.get().upper()} yg akan di ubah ke {conversion_entry.get().upper()}')


def lepas():
	# Enable entry boxes
	home_entry.config(state="normal")
	conversion_entry.config(state="normal")
	# Disable Tab
	label_amount.config(text=" Amount To Convert ")



# Home Currency labelFrame
home = LabelFrame(currency_frame, text=" Mata Uang Kamu ", font=("Times New Roman", 14))
home.pack(pady=20)
# Home currency entry box
home_entry = Entry(home, font=("Engravers MT", 10))
home_entry.pack(pady=10, padx=10)

# Conversion Currency labelFrame
conversion = LabelFrame(currency_frame, text="Mata Uang Tujuan", font=("Times New Roman", 14))
conversion.pack(pady=20)
# Convert_To Entry box
conversion_entry = Entry(conversion, font=("Engravers MT", 10))
conversion_entry.pack(pady=10, padx=10)

# Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)
# Create Buttons
tetapkan_button = Button(button_frame, text="Tetapkan", command=tetapkan)
tetapkan_button.grid(row=0, column=0, padx=10)
lepas_button = Button(button_frame, text="Lepas", command=lepas)
lepas_button.grid(row=0, column=1, padx=10)


#######################
# CONVERSION STUFF
#######################


def convert():
    if not home_entry.get() or not conversion_entry.get() :
        messagebox.showwarning("Warning!", "Harus mengisi semua inputan di atas !")
    else:
        try:

            # Clear Converted Entry Box
            converted_entry.delete(0, END)

            # mengambil dan menaruh data pada variabel
            moneyFrom = home_entry.get().upper()
            moneyTo = conversion_entry.get().upper()
            amount = amount_entry.get()
            # Proses Hitungan
            c = CurrencyRates()
            result = c.convert(moneyFrom,moneyTo,int(amount))
            result = round(result,2)

            # update entry box > tambahkan hasil hitungan disini
            converted_entry.insert(0, f'{moneyTo}= {result}')

        except ValueError:
            messagebox.showwarning('Warning!', 'Masukan jumlah uang anda !')
        except:
            messagebox.showwarning('Ada Kesalahan', 'Aplikasi ini membutuhkan saluran internet,\nKarena data nya di proses secara real-time.')


def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


# amount labelFrame
label_amount = LabelFrame(currency_frame, text=" Jumlah yg Akan di Ubah ", font=("Times New Roman", 14))
label_amount.pack(pady=20)
# amount Entry box
amount_entry = Entry(label_amount, font=('Helvetica', 24))
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(label_amount, text="Convert!", command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(currency_frame, text="Hasil : ", font=("batmanForeverAlternate", 12))
converted_label.pack(pady=10)
# Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(currency_frame, text="Clear", command=clear)
clear_button.pack(pady=3)

# Fake Label for spacing
spacer = Label(currency_frame, text="")
spacer.pack(pady=1.5)


root.mainloop()