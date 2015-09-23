def main(parent):

	Frame('CreateFrame',link="guidesigner/CreateFrame.py")
	grid(sticky='n',row='0')

	Frame('CreateAndLayout',link="guidesigner/CreateAndLayout.py")
	grid(column='1',sticky='n',row='0')

	LabelFrame("ConfigOptions",text="Config",link="guidesigner/ConfigOptions.py")
	rcgrid(0,2,sticky=N)

	Frame("DetailedLayout",link="guidesigner/DetailedLayout.py")
	rcgrid(0,3,sticky=N)

	LabelFrame("Selection",text="Selection",link="guidesigner/Selection.py")
	rcgrid(0,4,sticky=N)

### CODE ===================================================

	widget("ConfigOptions").unlayout()
	widget("DetailedLayout").unlayout()

### ========================================================

