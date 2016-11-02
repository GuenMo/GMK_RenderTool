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

import Core_RenderTool.GMK_RenderLayer as RenderLayer
reload(RenderLayer)
import Core_RenderTool.GMK_RenderTool_Utils as utils
reload(utils)

from functools import partial

class GMK_RenderLayerTab(QWidget):
    def __init__(self, parent=None):
        super(GMK_RenderLayerTab, self).__init__(parent)
        self.initUI()
        self.connectSignals()
        self.RenderLayer = RenderLayer.GMK_RenderLayer()

    def initUI(self):
        # Create Widget
        self.main_Layout = QVBoxLayout()
        self.setLayout(self.main_Layout)
        
        self.layer_GroupBox = QGroupBox('Layer Set')
        self.layerGroupBox_Layout = QVBoxLayout()
        self.layer_GroupBox.setLayout(self.layerGroupBox_Layout)
        self.main_Layout.addWidget(self.layer_GroupBox)
        
        self.main_Layout.addStretch()
        
        self.button_Layout = QHBoxLayout()
        self.load_Button = QPushButton('Load Layer')
        self.set_Button = QPushButton('Add to Layer')
        self.button_Layout.addWidget(self.load_Button)
        self.button_Layout.addWidget(self.set_Button)
        self.main_Layout.addLayout(self.button_Layout)
        
        # Set Widget
        self.setWindowTitle("Render Layer Tab")
    
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())
    
    def initRenderLayerUI(self):
        self.clearLayout(self.layerGroupBox_Layout)
        
        categori_layout = QHBoxLayout()
        layer_Name   = QLabel('')
        type_CH      = QLabel('C')
        type_BG      = QLabel('B')
        type_PP      = QLabel('P')
        type_Custom  = QLabel('            Custom')
        
        type_CH.setAlignment(Qt.AlignCenter)
        type_BG.setAlignment(Qt.AlignCenter)
        type_PP.setAlignment(Qt.AlignCenter)
        
        layer_Name.setFixedWidth(40)
        type_Custom.setFixedWidth(150)
        
        categori_layout.addWidget(layer_Name)
        categori_layout.addWidget(type_CH)
        categori_layout.addWidget(type_BG)
        categori_layout.addWidget(type_PP)
        categori_layout.addWidget(type_Custom)
        
        self.layerGroupBox_Layout.addLayout(categori_layout)
        
        for layer in self.RenderLayer.getRenderLayer():
            layer_Layout = QHBoxLayout()
            layer_Layout.setObjectName(layer+'_Layout')
            
            layer_Label  = QLabel(layer)
            layer_Label.setFixedWidth(40)
            layer_Label.setObjectName(layer+"_Label")
            
            layer_CH = QCheckBox()
            layer_CH.setObjectName(layer+"_CH")
            
            layer_BG = QCheckBox()
            layer_BG.setObjectName(layer+"_BG")
            
            layer_PP = QCheckBox()
            layer_PP.setObjectName(layer+"_PP")
            
            layer_Custom = QLineEdit()
            layer_Custom.setObjectName(layer+"_Custom")
            
            layer_sel= QPushButton('sel')
            
            layer_Layout.addWidget(layer_Label)
            layer_Layout.addWidget(layer_CH)
            layer_Layout.addWidget(layer_BG)
            layer_Layout.addWidget(layer_PP)
            layer_Layout.addWidget(layer_Custom)
            layer_Layout.addWidget(layer_sel)
            
            layer_sel.clicked.connect(partial(self.setSelObj, layer_Custom))
            
            self.layerGroupBox_Layout.addLayout(layer_Layout)
            
    def connectSignals(self):
        self.load_Button.clicked.connect(self.initRenderLayerUI)
        self.set_Button.clicked.connect(self.setRenderLayer)
        
    def setSelObj(self, custom):
        sel = utils.getSelectObject()
        custom.setText(sel)
    
    def setRenderLayer(self):
        assetList = self.RenderLayer.getAssetList()
        CH_List = assetList['CH']
        BG_List = assetList['BG']
        PROR_List = assetList['PROP']

        for layout in self.layerGroupBox_Layout.children():
            layer = layout.objectName().rpartition('_')[0]
            if not layer == '':
                objects = []
                for widget in [layout.itemAt(i).widget() for i in range(layout.count())]:
                    if widget.objectName().rpartition('_')[2] == 'CH' and widget.checkState():
                        objects.extend(CH_List)
                    if widget.objectName().rpartition('_')[2] == 'BG' and widget.checkState():
                        objects.extend(BG_List)
                    if widget.objectName().rpartition('_')[2] == 'PP' and widget.checkState():
                        objects.extend(PROR_List)
                    if widget.objectName().rpartition('_')[2] == 'Custom' and not widget.text() == '':
                        sels = widget.text()
                        objects.extend(sels.split(','))
                if len(objects) > 0: 
                    self.RenderLayer.setRenderLayer(layer, objects)
                      
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = GMK_RenderLayerTab()
    ui.show()
    sys.exit(app.exec_())
    