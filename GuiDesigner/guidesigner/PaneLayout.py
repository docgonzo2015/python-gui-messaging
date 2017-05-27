Button('ADD',anchor='n', bd='3', pady='2', padx='1m', text='ADD', bg='green').grid(column=1, padx=5, sticky='nesw', row=0)
Label('PaneTitle',bd='3', font='TkDefaultFont 9 bold', anchor='n', relief='ridge', fg='blue', text='pane', bg='yellow').grid(sticky='ew', row=0)
LabelFrame('Sashes',link='guidesigner/PaneLayoutSashes.py').grid(columnspan=3, row=2)
Frame('weightframe',grid_rows='(1, 25, 0, 0)', grid_cols='(2, 75, 0, 0)')
goIn()

Label('label',text='weight').grid(row=0)
Spinbox('weight',width=3, to=100.0).grid(column=1, sticky='ew', row=0)

### CODE ===================================================

container().master.parameters = {'weight' : 1}

parameters = container().master.parameters

def setconfig(key,value,parameters=parameters):

    if key == 'weight':
        try:
            value = int(value)
        except ValueError:
            value = 1
            
    if key in parameters:
        parameters[key] = value
        

def do_color_action(me,msg,parameters=parameters):
    me['bg'] = 'white'
    if msg:
        me.delete(0,END)
        me.insert(0,get_entry_as_string(parameters[me.mydata]))

def entry_event(me,parameters=parameters,setconfig=setconfig):
    setconfig(me.mydata,me.get())
    me['bg']='gray'
    informLater(300,me,'color',True)

widget('weight').delete(0,'end')
widget('weight').insert(0,parameters['weight'])
widget('weight').mydata = 'weight'
widget('weight').do_action('color',do_color_action,wishWidget=True,wishMessage=True)
widget('weight').do_command(entry_event,wishWidget=True) # via up and down buttons the option value can be changed
widget('weight').do_event("<Return>",entry_event,None,True)

### ========================================================

goOut()
grid(columnspan=2, row=1)

### CODE ===================================================


def show_weightframe(enable,frame = widget('weightframe')):
    if enable and isinstance(this().master,StatTtk.PanedWindow):
        frame.grid()
    else:
        frame.unlayout()

def do_add(parameters=container().parameters):

    if isinstance(container(),StatTtk.PanedWindow):
        pane(**parameters)
    else:
        pane()
        
    send('UPDATE_MOUSE_SELECT_ON')
    send("BASE_LAYOUT_CHANGED",NOLAYOUT) # NOLAYOUT because always trigger a sash_list_refreh via event BASE_LAYOUT_REFRESH


widget("ADD").do_command(do_add)

do_receive('ENABLE_SASH_LIST',show_weightframe,wishMessage=True)
### ========================================================
