# -*- coding: utf-8 -*-

import os

try:
    import PySide
    from PySide.QtGui import *
    from PySide.QtCore import *
    from shiboken import wrapInstance
except:
    import PySide2
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance

import Core_RenderTool.GMK_RenderTool_Utils as util
reload(util)

class GMK_ShaderTab(QWidget):
    def __init__(self, parent=None):
        super(GMK_ShaderTab, self).__init__(parent)
        self.initUI()
        self.connectSignals()
        
    def initUI(self):
        # Create Widget
        self.main_Layout = QVBoxLayout()
        self.setLayout(self.main_Layout)
        
        self.groupBox = QGroupBox('Shader Switch')
        
        self.layout = QHBoxLayout()
        self.groupBox.setLayout(self.layout)
        self.aiToBlinn_Button = QPushButton('Ai=>Lambert')
        self.aiToVray_Button = QPushButton('Ai=>V-ray')
        
        self.layout.addWidget(self.aiToBlinn_Button)
        self.layout.addWidget(self.aiToVray_Button)
        
        self.main_Layout.addWidget(self.groupBox)
        # Set Widget
        self.setWindowTitle("Shader Tab")
        
    def connectSignals(self):
        self.aiToBlinn_Button.clicked.connect(self.aiToLambert)
        self.aiToVray_Button.clicked.connect(self.aiToVray)
        
    def aiToLambert(self):
        aiList = util.getAiShader()
        util.aiToBlinn(aiList)

        
    def aiToVray(self):
        aiList = util.getAiShader()
        util.aiToVray(aiList)
        '''
        util.addGamaAttr()
        util.addOpenSubdiv()
        '''
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = GMK_ShaderTab()
    ui.show()
    sys.exit(app.exec_())
    