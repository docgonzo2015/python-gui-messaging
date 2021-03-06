
Label(text="Rename:").rcgrid(0,0,sticky=E)
Label("OldName",bg="yellow").rcgrid(0,1,sticky=W)
Label(text ="New name:"),rcgrid(1,0,sticky=E)
Entry("NewName").rcgrid(1,1,columnspan=2)
Button("Cancel",text="Quit").rcgrid(2,1,sticky=E)
Button("OK",text="OK").rcgrid(2,2)

### CODE ===================================================

def do_rename(name=widget("NewName"),cont = container()):
    cont.unlayout() # hide the RenameFrame
    renameElement(name.mydata[0],name.mydata[1],name.get())
    send('SHOW_SELECTION_UPDATE') # refresh show selection - sufficient, because the widget didn't change, only the name for accessing it

# on OK button press and on Return key in NewName Entry perform rename
widget("OK").do_command(do_rename)
widget("NewName").do_event("<Return>",do_rename)
widget("Cancel").do_command(lambda cont = container(): cont.unlayout())

def show_frame(msg,oldname = widget("OldName"), newname = widget("NewName"), cont = container()):
    if msg[1] == -1: oldname.config(text=msg[0])
    else: oldname.config(text=msg[0]+" [" +str(msg[1])+"]") # show the old name and index in Label OldName
    newname.delete(0,END) # prepare an empty Entry for the user input
    newname.insert(0,msg[0])
    newname.mydata=msg # store old name and index in mydata of the Entry widget
    cont.pack() # show the RenameFrame
    newname.focus_set() # and focus the entry

do_receive('RENAME_WIDGET',show_frame,wishMessage=True)
do_receive('SELECTION_CHANGED',lambda cont = container(): cont.unlayout())

### ========================================================
