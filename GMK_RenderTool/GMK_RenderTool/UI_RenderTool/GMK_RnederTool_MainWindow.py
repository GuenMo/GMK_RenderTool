# -*- coding:utf-8 -*-

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

import Core_RenderTool.GMK_RenderTool_Utils as utils
reload(utils)

import GMK_RenderGlobalTab as RenderGlobalTab
reload(RenderGlobalTab)
import GMK_RenderLayerTab as RenderLayreTab
reload(RenderLayreTab)
import GMK_ShaderTab as ShaderTab
reload(ShaderTab)

import Gale_Logo as Logo
reload(Logo)

__version__ = "1.2.0"

class GMK_RenderToolWindow(QMainWindow):
    def __init__(self, parent=utils.getMayaWindow()):
        super(GMK_RenderToolWindow, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.main_Layout = QVBoxLayout()
        self.centralWidget.setLayout(self.main_Layout)
        
        self.tabs = QTabWidget()
        
        self.renderGlobalTab = RenderGlobalTab.GMK_RenderGlobalTab()
        self.renderLayerTab  = RenderLayreTab.GMK_RenderLayerTab()
        self.shaderLayerTab = ShaderTab.GMK_ShaderTab()
        
        self.tabs.addTab(self.renderGlobalTab, "Preset")
        self.tabs.addTab(self.renderLayerTab,  "Layer")
        self.tabs.addTab(self.shaderLayerTab,  "Shader")
        
        self.main_Layout.addWidget(self.tabs)
        
        #self.Logo = Logo.Gale_Logo()
        #self.main_Layout.addWidget(self.Logo)
        
        self.setFixedWidth(320)
        self.setWindowTitle("Render Presets Tool Window")
    
    
class CheckSystemDialog(QMessageBox):
    def __init__(self, parent=utils.getMayaWindow()):
        super(CheckSystemDialog, self).__init__(parent)
        self.setWindowTitle("System error") 
        self.setText(u"'ximya@naver.com' 또는 \nR&D팀 으로 문의 해주세요.")
         
def main():
    global win

    try:
        win.close()
        win.deleteLater()
    except:
        pass
    win = GMK_RenderToolWindow()
    win.show()
    
        
        
        
        
        