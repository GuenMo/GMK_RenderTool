def run():
    try:
        filePath = __file__
        appPath = filePath.rpartition("\\")[0]
    except:
        print "Application`s path not exist."

    else:
        import sys
        path = appPath

        if not path in sys.path:
            sys.path.append(path)

        import UI_RenderTool.GMK_RnederTool_MainWindow 
        reload(UI_RenderTool.GMK_RnederTool_MainWindow )
        UI_RenderTool.GMK_RnederTool_MainWindow 