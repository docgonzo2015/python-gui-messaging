def main(parent):

### CODE ===================================================

	Lock()

	# -------------- receiver for message 'SHOW_SELECTION' ----------------------------------

	def button_select(selection):
		if widget_exists(selection._widget): setSelection(selection)
		send("SELECTION_CHANGED")
	
	def highlight_on(mebutton,widget):
		confdict = widget.getconfdict()
		mebutton.mydata=(confdict["relief"],confdict["highlightthickness"],confdict["highlightbackground"])
		widget.config(relief="solid",highlightthickness=1,highlightbackground="blue")

	def highlight_off(mebutton,widget):
		widget.config(relief=mebutton.mydata[0],highlightthickness=mebutton.mydata[1],highlightbackground=mebutton.mydata[2])

	def do_button_command(selection,button_press=button_select,hili_on = highlight_on,hili_off = highlight_off):
		do_command(button_press,selection)
		widget = selection._widget
		if widget.hasConfig and widget_exists(widget) and not widget.getconfig("highlightthickness") == "":
			do_event("<Button-1>",hili_on,widget,True)
			do_event("<ButtonRelease-1>",hili_off,widget,True)

	def for_a_name(row,name,entry,selection,button_command = do_button_command):
		current_this = None
		Button(text=name) # create a button, text is the name of the widget
		button_command(Create_Selection(entry[-1],selection._container))
		config(font = "TkDefaultFont 8 normal roman") # user smaler font
		rcgrid(row+1,1,sticky=W+E) # layout

		if len(entry) > 1:

			# create a label with text "-"
			Label(text="-")
			rcgrid(row+1,2)

			column=0 # index for while loop
			# for each widget in the list
			while column < len(entry):

				Button(text=str(column)) # create a button, which text of it's index
				# bind command for pressing this button: selection for this widget
				button_command(Create_Selection(entry[column],selection._container))
				rcgrid(row+1,column+3,sticky=W+E) # layout

				# if this widget is the selected one, the bg color shall be yellow
				if entry[column] is selection._widget:
					config(bg="yellow")
					current_this = selection._widget

				# if the widget doesn't have a layout, the font shall be italic and otherwise normal
				if entry[column].Layout == NOLAYOUT: config(font = "TkDefaultFont 8 normal italic")
				else: config(font = "TkDefaultFont 8 normal roman")

				column += 1

			if current_this != None:
				if not current_this.isLocked:
					Label(text="-").rcgrid(row+1,column+3)
					Button(text="=>",font = "TkDefaultFont 8 normal roman",bg="orange").rcgrid(row+1,column+4)
					button_command(Create_Selection(current_this,current_this))

		else:   # if there is only one widget for this name

			# if this widget is the selected one, the bg color shall be yellow
			if entry[0] is selection._widget: config(bg="yellow")

			# if the widget doesn't have a layout, the font shall be italic and otherwise normal
			if entry[0].Layout == NOLAYOUT: config(font = "TkDefaultFont 8 normal italic")
			else: config(font = "TkDefaultFont 8 normal roman")

			if entry[0].hasConfig and entry[0].isContainer and len(entry[0].CODE) != 0: config(highlightthickness=1, highlightbackground = "blue", relief="solid")

			# if the widget is a container widget, then create label "-" and button "=>" in orange for goIn()
			if not entry[0].isLocked:
				Label(text="-").rcgrid(row+1,2) # 
				Button(text="=>",font = "TkDefaultFont 8 normal roman",bg="orange").rcgrid(row+1,3)
				button_command(Create_Selection(entry[0],entry[0]))

	def for_names(frame_Selection = Selection(),button_command = do_button_command,for_entries = for_a_name):

		selection_before = Selection() # save the user selection
		setSelection(frame_Selection) # set the selection to inside Frame SelectionShow (container is selected)
		unlayout()
		deleteAllWidgets(this()) # delete all widgets in Frame SelectionShow

		Button(text="<=") # create the button for goOut()

		def do_goOut():
			goOut()
			send("SELECTION_CHANGED")

		do_command(do_goOut)
		config(font = "TkDefaultFont 8 normal roman") # use a smaller font
		rcgrid(0,0) # layout

		Button(text=".") # create the button for selecting the container
		button_command(Create_Selection(selection_before._container,selection_before._container))
		config(font = "TkDefaultFont 8 normal roman") # use a smaller font
		rcgrid(0,1,sticky=W) # layout

		if selection_before._container is selection_before._widget: config(bg="yellow") # if the container is already selected, mark it with yellow background
		if len(selection_before._container.CODE) != 0: config(highlightthickness=1, highlightbackground = "blue", relief="solid")

		row = 0
		for name, entry in selection_before._container.Dictionary.elements.items():
			for_entries(row,name,entry,selection_before)
			row += 1

		frame_Selection._container.pack()	
		setSelection(selection_before) # restore the user selection


	do_receive('SHOW_SELECTION',for_names)

### ========================================================
