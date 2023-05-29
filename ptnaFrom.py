import tkinter as tk
from ptna import *

entry = None
responce_area = None
action= None
ptna = Ptna('ptna')

def putlog(str):
    lb.insert(tk.END, str)

def prompt():
 p = ptna.name
 if (action.get())==0:
   p += ':' + ptna.responder.name
   return p + '>'
 

def talk():
  value = entry.get()
  if not value:
    responce_area.configure(text='何？')
  else:
    responce = ptna.dialogue(value)
    responce_area.configure(text=responce)
    putlog('>'+value)
    entry.delete(0,tk.END)

def run():
  global entry, responce_area, lb, action

  root = tk.Tk()
  root.geometry('880x560')
  root,title('Intelligent Agent :') 
font=('Helevetica',14)
  