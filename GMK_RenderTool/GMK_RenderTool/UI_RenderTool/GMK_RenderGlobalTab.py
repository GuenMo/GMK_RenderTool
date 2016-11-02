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

import Core_RenderTool.GMK_RenderGlobalMeta as GMK_RenderGlobalMeta
reload(GMK_RenderGlobalMeta)

class GMK_RenderGlobalTab(QWidget):
    def __init__(self, parent=None):
        super(GMK_RenderGlobalTab, self).__init__(parent)
        self.initUI()
        self.connectSignals()
        
    def initUI(self):
        # Create Widget
        self.main_Layout = QVBoxLayout()
        self.setLayout(self.main_Layout)
        
        self.renderer_Group = QButtonGroup()
        self.renderer_GroupBox = QGroupBox('Renderer')
        self.renderer_Layout = QHBoxLayout(self.renderer_GroupBox)
        self.arnold_Radio = QRadioButton('Arnold')
        self.arnold_Radio.setObjectName('arnold')
        self.arnold_Radio.setChecked(True)
        self.mentalRay_Radio = QRadioButton('Mental Ray')
        self.mentalRay_Radio.setObjectName('mentalRay')
        self.vRay_Radio = QRadioButton('V-Ray')
        self.vRay_Radio.setObjectName('VRay')
        
        self.vRay_Radio.setEnabled(False)
        
        self.renderer_Group.addButton(self.mentalRay_Radio)
        self.renderer_Group.addButton(self.arnold_Radio)
        self.renderer_Group.addButton(self.vRay_Radio)
        
        self.button_Layout = QHBoxLayout()
        self.save_Button = QPushButton('Save')
        self.edit_Button = QPushButton('Edit')
        self.load_Button = QPushButton('Load')
        self.button_Layout.addWidget(self.save_Button)
        self.button_Layout.addWidget(self.edit_Button)
        self.button_Layout.addWidget(self.load_Button)
        
        # Set Layout
        self.renderer_Layout.addWidget(self.arnold_Radio)
        self.renderer_Layout.addWidget(self.mentalRay_Radio)
        self.renderer_Layout.addWidget(self.vRay_Radio)
        
        self.main_Layout.addWidget(self.renderer_GroupBox)
        self.main_Layout.addStretch()
        self.main_Layout.addLayout(self.button_Layout)

        # Set Widget
        self.setWindowTitle("Render Global Tab")
        
    def connectSignals(self):
        self.renderer_Group.buttonReleased.connect(self.checkRenderer)
        self.save_Button.clicked.connect(self.saveRenderSet)
        self.edit_Button.clicked.connect(self.saveRenderSet)
        self.load_Button.clicked.connect(self.loadRenderSet)
    
    def checkRenderer(self):
        button = self.renderer_Group.checkedButton()
        return button.objectName()
    
    def saveRenderSet(self):
        renderer = self.checkRenderer()
        renderGlobal = GMK_RenderGlobalMeta.GMK_RenderMeta()
        status = renderGlobal.save(renderer)
        
        # 결과 출력
        if status:
            print '%s preset save success' %renderer
        else:
            print '%s preset save failed' %renderer
        
    def loadRenderSet(self):
        renderGlobal = GMK_RenderGlobalMeta.GMK_RenderMeta()
        renderGlobal.load()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = GMK_RenderGlobalTab()
    ui.show()
    sys.exit(app.exec_())
    