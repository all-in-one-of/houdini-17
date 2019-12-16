import hou
from PySide2 import QtCore, QtUiTools, QtWidgets
def prepareExp(start_wedge,end_wedge,pre_add,post_add,multiplier):
    exp=""
    for i in range(start_wedge,end_wedge+1):
        exp+="if($WEDGE=="+str(i)+","+str(((i+pre_add)*multiplier)+post_add)+",1)*"
    return exp
def prepareExpVList(start_wedge,value_list):
    myarray=value_list.split(",")
    expVL=""
    for i in range(len(myarray)):
        expVL+="if($WEDGE=="+str(i+start_wedge)+","+str(myarray[i])+",1)*"
    return expVL    
def prepareExpVRange(start_wedge,end_wedge,parm_start,parm_end):
    size_wedge=end_wedge-start_wedge
    parm_inc=(parm_end-parm_start)/(size_wedge)
    i=parm_start
    count=start_wedge
    expRG=""
    while(i<=parm_end):
        expRG+="if($WEDGE=="+str(count)+","+str(i)+",1)*"
        i=i+parm_inc
        count+=1
    return expRG
class wedgeCreator(QtWidgets.QWidget):
    def __init__(self):
        super(wedgeCreator,self).__init__()
        ui_file = 'uipath'
        x = hou.readFile(ui_file)
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)       
        self.ui.btn_create.clicked.connect(self.buttonClicked)
    def buttonClicked(self):
        start_wedge=int(self.ui.lin_start_wedge.text())
        end_wedge=int(self.ui.lin_end_wedge.text())
        pre_add=float(self.ui.lin_pre_add.text())
        post_add=float(self.ui.lin_post_add.text())
        multiplier=float(self.ui.lin_multiplier.text())
        toggle_value=int(self.ui.checkBox_valueList.isChecked())
        toggle_value_2=int(self.ui.checkBox_valueList_2.isChecked())
        parm_start=float(self.ui.lin_start_parm.text())
        parm_end=float(self.ui.lin_end_parm.text())
        if(toggle_value_2==1):
            toggle_value=2
        if(toggle_value==0):
            wedge_exp=prepareExp(start_wedge,end_wedge,pre_add,post_add,multiplier)
            wedge_exp=wedge_exp[:-1]
            hou.ui.copyTextToClipboard(wedge_exp)
            hou.ui.displayMessage(text="The expression has been copied to your clipboard",details_label="Click to see the expression",details=wedge_exp)
            print wedge_exp
        if(toggle_value==1):
            value_list=str(self.ui.lin_valueList.text())
            wedge_exp=prepareExpVList(start_wedge,value_list)
            wedge_exp=wedge_exp[:-1]
            hou.ui.copyTextToClipboard(wedge_exp)
            hou.ui.displayMessage(text="The expression has been copied to your clipboard",details_label="Click to see the expression",details=wedge_exp)
            print wedge_exp
        if(toggle_value==2):
            value_list=str(self.ui.lin_valueList.text())
            wedge_exp=prepareExpVRange(start_wedge,end_wedge,parm_start,parm_end)
            wedge_exp=wedge_exp[:-1]
            hou.ui.copyTextToClipboard(wedge_exp)
            hou.ui.displayMessage(text="The expression has been copied to your clipboard",details_label="Click to see the expression",details=wedge_exp)
            print wedge_exp
win = wedgeCreator()
win.show()
