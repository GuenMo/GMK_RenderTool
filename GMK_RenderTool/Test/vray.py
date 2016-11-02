#applies Texture Input Gamma to selected File nodes
import maya.cmds as cmds
import maya.OpenMaya as om

fileNodes =cmds.ls(type="file", sl=True)
for f in fileNodes:
    cmds.select(f, r=True)
    cmds.vray("addAttributesFromGroup", f, "vray_file_gamma", 1)
    cmds.select(f, d=True)
    om.MGlobal.displayInfo("Applied Texture Input Gamma to selected File nodes")
    
    
#applies Subdivision to selected Shape nodes
import maya.cmds as cmds
import maya.OpenMaya as om

transforms = cmds.ls(tr=True, sl=True)
shapes = cmds.listRelatives(transforms, s=True)
cmds.select(shapes)
for s in shapes:
    cmds.select(s, r=True)
    cmds.vray("addAttributesFromGroup", s, "vray_subdivision", 1)
    cmds.vray("addAttributesFromGroup", s, "vray_subquality", 1)
    cmds.getAttr(".vrayOverrideGlobalSubQual")
    cmds.setAttr(".vrayOverrideGlobalSubQual", 0)
    cmds.select(s, d=True)
    om.MGlobal.displayInfo("Applied Subdivision to selected Shape nodes")
    
transforms = pm.ls(tr=True)
for tr in transforms:
    if tr.endswith('_sdm'):
        shape = tr.getShapes()[0]
        pm.select(cl=True)
        pm.select(shape, r=True)
        pm.vray("addAttributesFromGroup", shape, "vray_opensubdiv", 1)
        pm.select(shape, d=True)