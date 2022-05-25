from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

from dataCurrency import idCurrency


root = Tk()
root.title('DwB App / Currency Converter')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x680")

#ganti logo app
logo = PhotoImage(file="logoTukar.png")
root.iconphoto(True, logo)

# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=630)
helper_frame = Frame(my_notebook, width=480, height=630)

currency_frame.pack(fill="both", expand=1)
helper_frame.pack(fill="both", expand=1)

# Add our Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(helper_frame, text="Help")


#######################
# CURRENCY STUFF
#######################


def tukar():
    lepas()
    beforeMoneyFrom = home_entry.get().upper()
    BeforeMoneyTo = conversion_entry.get().upper()

    home_entry.delete(0, END)
    conversion_entry.delete(0, END)

    afterMoneyFrom = BeforeMoneyTo
    afterMoneyTo = beforeMoneyFrom

    home_entry.insert(0, afterMoneyFrom)
    conversion_entry.insert(0, afterMoneyTo)

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
home.pack(pady=16)
# Home currency entry box
home_entry = Entry(home, font=("Engravers MT", 10))
home_entry.pack(pady=15, padx=10)

tuker_img = PhotoImage(file="logoTukar.png")
tukerButton = Button(currency_frame, image=tuker_img, command=tukar)
tukerButton.pack(pady=5)

# Conversion Currency labelFrame
conversion = LabelFrame(currency_frame, text="Mata Uang Tujuan", font=("Times New Roman", 14))
conversion.pack(pady=12)
# Convert_To Entry box
conversion_entry = Entry(conversion, font=("Engravers MT", 10))
conversion_entry.pack(pady=15, padx=10)

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
            messagebox.showwarning('Terdapat Masalah!', 'Hal yg harus diperhatikan :\n1. koneksi internet anda\n2. mata uang yg anda masukan.\n\nLihat menu "help" untuk melihat singkatan mata uang\nyang anda butuhkan.')


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
convert_button.config(font=("Verdana Bold Italic", 12))
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


#######################
# HELP STUFF 
#######################


header = Label(helper_frame,text="Have Some Problem?", font=("Stencil", 15))
header.pack(pady=15)

contact = Frame(helper_frame)
contact.pack(pady=5)
me = Label(contact, text="Contact me at instagram :", font=("Freestyle Script", 15))
me.grid(row=0,column=0)
ig = Label(contact, text=" @mngdms_22", font=("Harrington", 14))
ig.grid(row=0,column=1)

currHelp = Label(helper_frame,text="~ List of Currency", font=("Elephant Italic", 14))
currHelp.pack(pady=20, anchor="nw")

##################################

main_frame = Frame(helper_frame)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scroll.pack(side=RIGHT, fill=Y)


my_canvas.configure(yscrollcommand=my_scroll.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
# Gulir pake Mouse
def on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 50)), "units")
# Gulir pake Mouse
my_canvas.bind_all("<MouseWheel>", on_mouse_wheel) 


second_frame = Frame(my_canvas)


my_canvas.create_window((0,0), window=second_frame, anchor="n")


for k in idCurrency.keys():
    Label(second_frame,text=f"{k}\t=\t{idCurrency[k]} ", font=("Stika Banner Regular", 14)).pack(pady=2, anchor="nw")


# Fake Label for spacing
spacer = Label(helper_frame, text="")
spacer.pack(pady=2.5)



root.mainloop()