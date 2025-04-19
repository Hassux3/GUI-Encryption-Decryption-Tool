from tkinter import *
import string, os, sys
from tkinter import messagebox
alphabets = string.ascii_lowercase 

def resource_path(path):
    try:
        base_path = sys.MEIPASS2
    except Exception:
        base_path = os.path.basename(".")

    return os.path.join(path + base_path)

def encryption(plain_text, shift_key):
    cypher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_key) % 26
            cypher_text += alphabets[new_position]
        else:
            cypher_text += char
    return cypher_text

def decryption(cypher_text, shift_key):
    decrypted_text = ""
    for char in cypher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_key) % 26
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += char
    return decrypted_text

def encryption_window():
    clear()
    root.title('Encyption-Decryption Program')
    root.geometry('800x595+500+280')
    root.config(bg='black')
    root.resizable(False,False)
    title.config(text='ENCRYPTION')
    Lbl_01.config(text='Enter text for encryption:')
    Lbl_03.config(text='Encrypted text will shown here')
    submitBtn.config(command=encrypted_Submit)

    menu = Menu(root) 
    MENU = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Encryption', command=encryption_window) 
    menu.add_cascade(label='Decryption', command=decryption_window) 
 
    root.config(menu=menu)

def decryption_window():
    clear()
    root.title('Encyption-Decryption Program')
    root.geometry('800x595+500+280')
    root.config(bg='black')
    root.resizable(False,False)

    title.config(text='DECRYPTION')
    Lbl_01.config(text='Enter text for decryption:')
    Lbl_03.config(text='Decrypted text will shown here')
    submitBtn.config(command=decrypted_Submit)

    menu = Menu(root) 
    MENU = Menu(menu, tearoff=0) 
    menu.add_cascade(label='Encryption', command=encryption_window) 
    menu.add_cascade(label='Decryption', command=decryption_window) 
 
    root.config(menu=menu)


def encrypted_Submit():
    CodedtextArea.config(state='normal')
    CodedtextArea.delete(1.0,END)

    texttoEncode = textArea.get(1.0,END)
    shiftKey = shiftkeyvar.get()
    encodedText = encryption(texttoEncode,shiftKey)
    
    CodedtextArea.insert(1.0,encodedText)
    CodedtextArea.config(state='disabled')


def decrypted_Submit():
    CodedtextArea.config(state='normal')
    CodedtextArea.delete(1.0,END)

    texttoDecode = textArea.get(1.0,END)
    shiftKey = shiftkeyvar.get()
    encodedText = decryption(texttoDecode,shiftKey)

    CodedtextArea.insert(1.0,encodedText)
    CodedtextArea.config(state='disabled')

def clear():
    shiftkeyvar.set(0)
    textArea.delete(1.0,END)
    CodedtextArea.config(state='normal')
    CodedtextArea.delete(1.0,END)
    CodedtextArea.config(state='disabled')

def about():
    return messagebox.showinfo('About', 'Encryption-Decryption by Hassan Khan.')
    

if __name__ == '__main__':
    root = Tk()
    root.title('Encyption-Decryption Program')
    root.geometry('800x615+500+280')
    root.config(bg='black')
    root.resizable(False,False)

    icon_photo = PhotoImage(file=resource_path('icon.png'))
    root.iconphoto(False,icon_photo)

    title = Label(root, text='ENCRYPTION', font=('Berlin Sans FB', '50'), fg='darkorange', bg='black')
    title.pack()

    Lbl_01 = Label(root, text='Enter text for encryption:', font=('Calibri', '18'), fg='white', bg='black')
    Lbl_01.place(x=20, y=70)

    Lbl_02 = Label(root, text='Enter shift key -->', font=('Calibri', '18'), fg='white', bg='black')
    Lbl_02.place(x=480, y=70)

    shiftkeyvar = IntVar()
    shiftkeyArea = Entry(root, bg='black', fg='white', font=('Calibri', '15', 'bold'),textvariable=shiftkeyvar, justify='center',bd='5', relief=SUNKEN).place(x=680, y=65, width=100, height=40)
    
    textArea = Text(root,bg='black', fg='white', font=('Arial', '18'), bd='5', relief=SUNKEN)
    textArea.place(x=20, y=110, width=760, height=220)

    Lbl_03 = Label(root, text='Encrypted text will shown here', font=('Calibri', '14'), fg='white', bg='black')
    Lbl_03.place(x=275, y=330)

    CodedtextArea = Text(root,bg='black', fg='white', font=('Calibri', '18'), bd='5', relief=SUNKEN, state='disabled')
    CodedtextArea.place(x=20, y=360, width=760, height=170)

    submitBtn = Button(root, text='Submit',font=('Constantia', '20'), bg='black', fg='darkorange', activebackground='black', activeforeground='white', command=encrypted_Submit)
    submitBtn.place(x=80,y=545, width=200, height=40)
    
    Button(root, text='Clear',font=('Constantia', '20'), bg='black', fg='darkorange', activebackground='black', activeforeground='white', command=clear).place(x=305,y=545, width=200, height=40)
    
    Button(root, text='About',font=('Constantia', '20'), bg='black', fg='darkorange', activebackground='black', activeforeground='white', command=about).place(x=530,y=545, width=200, height=40)

    # Label(root, text='www.youtube.com/CodingWithHassan', font=('Calibri', '12'), fg='white', bg='black').place(x=530, y=560)

    menu = Menu(root)
    MENU = Menu(menu, tearoff=0)
    menu.add_cascade(label='Encryption', command=encryption_window)
    menu.add_cascade(label='Decryption', command=decryption_window)
    root.config(menu=menu)

    root.mainloop()