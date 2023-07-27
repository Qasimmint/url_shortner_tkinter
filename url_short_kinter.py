from tkinter import *
from tkinter import messagebox
import pyshorteners as ps, pyperclip as clip

root = Tk()
root.title("Python's URL shorter")
root.iconbitmap(r"C:\Users\qk633\Downloads\url.png")
root.configure(background="white")
root.geometry("1300x500")
root.columnconfigure(0, weight=1)

# FONTS
head_font = ("Helvetica", 35)
text_font  = ("Verdana", 18)

def copyURL():
    try:
        clip.copy(short_url)
        messagebox.showinfo("Info 🥳", "Link is successfully copied")

    except Exception as e:
        messagebox.showerror("Error ❌", f"{e} occurred. Try again or enter the valid URL")

def cutURL():
    global short_url
    shortner = ps.Shortener()
    short_url = shortner.osdb.short(shortner_frame.get())
    show_lbl = Label(root, text=f"Shortened URL: {short_url}", font=text_font, bg='white', fg='green')
    show_lbl.grid(row=4, column=0, columnspan=3, pady=(10, 3))
    copy_btn = Button(root, text="Copy URL 📄", fg='white', bg='green', padx=20, pady=8, font=text_font, cursor='hand1', state=NORMAL,  command=copyURL)
    copy_btn.grid(row=5, column=0, columnspan=3, pady=(15, 0))

def cleanBox():
        shortner_frame.delete(0, END)        
            

head = Label(root, text="Python URL Shortner ✂️", font=head_font, fg="black", bg="white")
head.grid(row=0, column=0, columnspan=2, pady=(50, 10), sticky='ns')

shortner_frame = Entry(root, width=60, fg='black', bg='white', font=text_font, bd=6, borderwidth=2)
shortner_frame.config(fg="skyblue")
shortner_frame.grid(row=1, column=0, columnspan=2, pady=(50, 10))

del_btn = Button(root, text="Clean 🧹", fg='black', bg='cyan', padx=15, pady=6, font=text_font, cursor='hand1', command=cleanBox)
del_btn.grid(row=1, column=1, columnspan=1,  pady=(50, 5), padx=(10, 28), sticky='s')

short_btn = Button(root, text="Cut URL...✂️", fg='white', bg='black', padx=20, pady=8, font=text_font, cursor='hand1', command=cutURL)
short_btn.grid(row=2, column=0, columnspan=2, pady=(30, 5))

copy_btn = Button(root, text="Copy URL 📄", fg='white', bg='green', padx=20, pady=8, font=text_font, cursor='hand1', state=DISABLED, command=copyURL)
copy_btn.grid(row=5, column=0, columnspan=3, pady=(15, 0))

root.mainloop()
