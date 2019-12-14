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
class wedgeCreator(QtWidgets.QWidget):
    def __init__(self):
        super(wedgeCreator,self).__init__()
        ui_file = '/my_qt_path/uiWedgeExpression_v03.ui'
        x = hou.readFile(ui_file)
        #ba = QtCore.QByteArray(x)
        #buff = QtCore.QBuffer(ba)
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        #Setup create Geometry Button
        self.ui.btn_create.clicked.connect(self.buttonClicked)
    def buttonClicked(self):
        #get variables from user
        start_wedge=int(self.ui.lin_start_wedge.text())
        end_wedge=int(self.ui.lin_end_wedge.text())
        pre_add=float(self.ui.lin_pre_add.text())
        post_add=float(self.ui.lin_post_add.text())
        multiplier=float(self.ui.lin_multiplier.text())
        toggle_value=int(self.ui.checkBox_valueList.isChecked())
        if(toggle_value==0):
            #compose wedge expression
            wedge_exp=prepareExp(start_wedge,end_wedge,pre_add,post_add,multiplier)
            wedge_exp=wedge_exp[:-1]
            print wedge_exp
        
        if(toggle_value==1):
            #compose wedge values expression
            value_list=str(self.ui.lin_valueList.text())
            wedge_exp=prepareExpVList(start_wedge,value_list)
            wedge_exp=wedge_exp[:-1]
            print wedge_exp
win = wedgeCreator()
win.show()
