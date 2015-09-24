def main(parent):

	Button('NewRow',text="""new row""",width='7').grid(column='4',row='0')
	Button('Grid0',text="""grid()""",bg='green').grid(sticky='w',columnspan='3',row='3')
	Checkbutton('IncRow').grid(column='3',row='1')
	Spinbox('Column',width='4',from_=0,to='100.0').grid(column='2',row='0')
	Label('Label',text="""inc""").grid(column='3',row='3')
	Label('Label',text="""col""").grid(column='1',row='0')
	Label('Label',text="""row""").grid(column='1',row='1')
	Button('NewCol',text="""new col""",width='7').grid(column='4',row='1')
	Checkbutton('IncCol').grid(column='3',row='0')
	Button('Grid',text="""grid""",width='7',bg='green').grid(column='4',sticky='e',row='3')
	Label('GridTitle',text="""grid""",fg='blue').grid(sticky='w',row='0')
	Spinbox('Row',width='4',from_=0,to='100.0').grid(column='2',row='1')

### CODE ===================================================

	# -- Variables for Checkboxes: mydata of Spinboxes Column und Row -------------

	var = IntVar()
	widget("IncCol").config(variable = var)
	widget("Column").mydata=var

	var = IntVar()
	widget("IncRow").config(variable = var)
	widget("Row").mydata = var

	# -- Button Command and Return key events for Button Grid and Spinboxes Row and Colum -----

	def do_grid(row = widget("Row"), column = widget("Column")):
		send('BASE_LAYOUT_PLACE_MOUSEOFF')
		layout_before = this().Layout
		rcgrid(row.get(),column.get())
		send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions
		if column.mydata.get(): column.invoke("buttonup")
		if row.mydata.get(): row.invoke("buttonup")

	widget("Row").do_event("<Return>",do_grid)
	widget("Column").do_event("<Return>",do_grid)
	widget("Grid").do_command(do_grid)

	def do_grid0():
		send('BASE_LAYOUT_PLACE_MOUSEOFF')
		layout_before = this().Layout
		grid()
		send('BASE_LAYOUT_CHANGED',layout_before) # depending on the layout change we need less or more actions

	widget("Grid0").do_command(do_grid0)

	# -- Button Commands for Buttons NewRow and  NewCol: set Row and Column values to next row or column ----

	def function(row,column):
		row.invoke("buttonup")
		column.delete(0,END)
		column.insert(0,"0")

	widget("NewRow").do_command(function,(widget("Row"),widget("Column")))
	widget("NewCol").do_command(function,(widget("Column"),widget("Row")))

	# -------- Receivers for message 'BASE_LAYOUT_REFRESH' ----------------------

	# hide LabelFrame GridFrame, if there is a PACKLAYOUT in the container of the current widget
	do_receive('BASE_LAYOUT_REFRESH', lambda cont = container(): send('HIDELAYOUT_PackOrGrid',(PACKLAYOUT,cont)))

	# set the bg color of the GridTitle label to yellow, if the current widget has a GRIDLAYOUT, otherwise to original color

	def do_bg_title(title = widget("GridTitle"),titlebg = widget("GridTitle")["bg"]):
		if this().Layout == GRIDLAYOUT: title['bg'] = "yellow"
		else: title['bg'] = titlebg

	do_receive('BASE_LAYOUT_REFRESH',do_bg_title)

	# set the row and column values according to the layout of the current widget

	def set_column_row(column = widget("Column"),row = widget("Row")):
		if this().Layout==GRIDLAYOUT:
			column.delete(0,END)
			column.insert(0,this().getlayout("column"))
			row.delete(0,END)
			row.insert(0,this().getlayout("row"))

	do_receive('BASE_LAYOUT_VALUE_REFRESH',set_column_row)
	
### ========================================================