import csv
import tkinter as tk
from functools import partial
from tkinter import messagebox as mb

def ReadFile():
  with open(r".\Users.csv", encoding='utf-8', mode='a+', newline='') as file:
    content = csv.writer(file, delimiter=',', )
    allData = []
    content.writerow([entUser.get(), entPassword.get()])
  return allData

def VerifyData(user):
  print(user.get())
  allData = ReadFile()
  for r in allData:
    print(r)
  
def VerifyDigits(event, entry):
  try:
    int(entry.get())
  except:
    mb.showerror("Erro", "Insira apenas números!")
    value = entry.get()
    for i in range(len(value)):
      try:
        int(value[i])
      except:
        entry.delete(i,len(value))
        break

root = tk.Tk()
x = round((root.winfo_screenwidth() - 800)/2)
y = round((root.winfo_screenheight() - 600)/2)
root.geometry(f"{800}x{600}+{x}+{y}")
root.resizable(0, 0)
root.title("CRUD")

frame = tk.Frame(root, width=800, height=600)
frame.grid()
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=2)

lblUser = tk.Label(frame, text="Nome:")
entUser = tk.Entry(frame)
lblUser.grid(column=0, row=0, padx=5, pady=2)
entUser.grid(column=1, row=0, padx=5, pady=2)


lblPassword = tk.Label(frame, text="Senha")
entPassword = tk.Entry(frame)
entPassword.bind("<KeyRelease>", lambda event1: VerifyDigits(event=event1,entry=entPassword))
lblPassword.grid(column=0, row=1, padx=5, pady=2)
entPassword.grid(column=1, row=1, padx=5, pady=2)

btnLogin = tk.Button(frame, text="Entrar", command=partial(VerifyData, entUser))
btnLogin.grid(column=2, row=0, rowspan=2, padx=5, pady=2)

root.mainloop()