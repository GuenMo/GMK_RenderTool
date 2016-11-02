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

class Gale_Logo(QLabel):
    def __init__(self, parent=None):
        super(Gale_Logo, self).__init__(parent)

        logoImage = QPixmap(self.getIconPath() +'STUDIO_GALE_LOGO.png')
        
        self.setAlignment(Qt.AlignRight)
        self.setPixmap(logoImage.scaled(175,50, Qt.KeepAspectRatio))
        # Set Widget
        self.setWindowTitle("Gale Logo")
    
    def getRootPath(self):
        utilsPath = __file__.replace("\\", "/")
        rootPath = utilsPath.rpartition("/")[0].rpartition("/")[0]
        return rootPath

    def getIconPath(self):
        return self.getRootPath() + "/Icons/" 
    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Gale_Logo()
    ui.show()
    sys.exit(app.exec_())