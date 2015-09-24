def main(parent):

	LabelFrame('CreateWidget',text="""Create Widget""",link="guidesigner/CreateWidget.py")
	pack(ipady='4',anchor='n',fill='x')

	LabelFrame('SelectType',text="""Select Widget Type""",link="guidesigner/SelectType.py")
	pack()

### CODE ===================================================

	def function(msg,container):
		if msg: container.unlayout()
		else: container.grid()

	do_receive("HIDE_CREATE",function,container(),wishMessage=True)

### ========================================================