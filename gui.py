from tkinter import *

def lock(): # Lockscreen
  window = Tk()
  root = Tk()
  window.title('Lock Screen')
  window.geometry("600x400")
  
  lbl1 = Label(window, text="Password")
  
  t1 = Entry()
  
  lbl1.place(x=110, y=50)
  t1.place(x=200, y=50)
  root.withdraw()
  lbl5 = Label(window, text = "Warning! Password Hardcoded.") # Warning that should be removed when the issue is solved.
  lbl5.place(x = 100, y = 150
  
  def submit(): 
    password = t1.get()
    secret = "123" #THIS IS A PASSWORD HARDCODED INTO THE PROGRAM! PLEASE REPLACE THIS WITH A .ENV KEY ASAP!
    
    if password == secret: # Gets rid of any text if password is correct
      lbl4 = Label(window, text = "")
      lbl4.place(x = 200, y = 100)
      passwordYes()
  
    elif password == "": # If password is empty
      lbl2 = Label(window, text = "Password Missing!")
      lbl2.place(x = 200, y = 100)
    elif password != secret: # If password is wrong
      lbl3 = Label(window, text = "Wrong Password!")
      lbl3.place(x = 200, y = 100)
  
  def passwordYes():
    window.destroy() # Destroys lockscreen when correct password is entered
    mainscreen() # Opens up the mainscreen
    
  b1 = Button(window, text='Enter', command=submit) # Runs submit() function when pressed
  
  b1.place(x=390, y=46)
  
  window.mainloop()

def mainscreen():
  """A screen that just has a button to run the program."""
  window = Tk()
  root = Tk()
  window.title('Main Window')
  window.geometry("600x400")
  root.withdraw()
  
  def runMain():
    import main # Seems sus but it works. If there are any future problems with main.py it might be because of this import statement. Just saying.
  
  b1 = Button(window, text='Run!', command=runMain) # Runs the import runMain() function
  
  b1.place(x=200, y=100)
  
  window.mainloop()
lock()
