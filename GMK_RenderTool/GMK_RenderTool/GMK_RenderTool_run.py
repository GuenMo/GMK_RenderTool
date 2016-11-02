# -*- coding:utf-8 -*-

def GMK_RenderTool_run():
    try:
        filePath = __file__
        GMK_RenderTool_Path = filePath.rpartition("\\")[0]
    except:
        print "Environ Value 'GMK_RenderTool_Path' not exist."
    
    else:
        import sys
        path = GMK_RenderTool_Path
        
        if not path in sys.path:
            sys.path.append(path)
        
        import UI_RenderTool.GMK_RnederTool_MainWindow as mainWindow
        reload(mainWindow)
        
        mainWindow.main()
    
if __name__ == "GMK_RenderTool_run":    
    GMK_RenderTool_run()    
    