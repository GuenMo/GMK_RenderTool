# -*- coding:utf-8 -*-

# Maya module
import maya.OpenMayaUI as OMUI
import pymel.core as pm

# PySide module
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

# Python module
import collections
from datetime import datetime
from distutils.command.sdist import sdist

def getMayaWindow():
    ptr = OMUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QMainWindow)

def getRootPath():
    utilsPath = __file__.replace("\\", "/")
    rootPath = utilsPath.rpartition("/")[0].rpartition("/")[0]
    print rootPath
    return rootPath

def getIconPath():
    return getRootPath() + "/icons" 

def findAllModuel(relativeDirectory):
    # relativeDirectory 경로에 모든 모듈(.py)를 검색해 리턴한다.
    allPyFiles = findAllFile( relativeDirectory, ".py" )
    returnModules = []
    
    for f in allPyFiles:
        if f != "__init__":
            returnModules.append(f)

    return returnModules

def findAllFile(relativeDirectory, fileExtension):
    # 주어진 확장자를 가지는 모든 파일을 찾아서 리턴 한다.
    import os
    
    fileDirectory = getRootPath()  + relativeDirectory + "/"
    allFiles = os.listdir(fileDirectory)
    returnFiles = []
    
    for f in allFiles:
        splitString = str(f).rpartition(fileExtension)
        if not splitString[1] == "" and splitString[2] == "":
            returnFiles.append(splitString[0])
        
    return returnFiles

def list_duplicates(seq):
    tally = collections.defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() if len(locs)>1)

def versionCheck():
    currentVersion = pm.versions.current()
    
    if '2014' in str(currentVersion): 
        return True
    elif '2016' in str(currentVersion): 
        return True
    else:
        return False    
    
def dateCheck():
    limitsDate = datetime(2015,12,31)
    currentDate = datetime.now()
    
    if currentDate <  limitsDate:
        return True
    else:
        return False
        
def checkSystem():
    verStat = versionCheck()
    dateStat = dateCheck()
    
    if verStat and dateStat:
        return True
    else:
        return False
    
def getSelectObject():
    sels = pm.ls(sl=True)
    selList = []
    for sel in sels:
        selList.append(sel.name())
    
    selStr = ','.join(selList)
    return selStr
    
def changeShaderType(originalShaderName, replaceShaderType):
    originalShader = pm.PyNode(originalShaderName)    
    diffuseColor = originalShader.diffuseColor.inputs()

    replaceWith = pm.shadingNode(replaceShaderType, asShader=True)
    if diffuseColor:
        diffuseColor[0].outColor.connect(replaceWith.color)
    else:
        replaceWith.color.set(originalShader.diffuseColor.get())
    
    #for mesh in meshes:
    sfSD = originalShader.outColor.outputs(plugs=True)[0]
    replaceWith.outColor.connect(sfSD, f=True)
    pm.delete(originalShader)
    pm.rename(replaceWith,originalShaderName) 
            
def changeShaderType1(originalShaderName, replaceShaderType):
    originalShader = pm.PyNode(originalShaderName)    
    
    color = originalShader.color.get()
    bump = originalShader.inputs(type = 'bump2d')
    specCol = originalShader.KsColor.inputs(type='file')
    
    
    replaceWith = pm.shadingNode(replaceShaderType, asShader=True)
    pm.mel.replaceNode(originalShader, replaceWith)
    pm.delete(originalShader)
    pm.rename(replaceWith,originalShaderName) 
    
    if replaceShaderType == 'VRayMtl':
        shader = pm.PyNode(originalShaderName)
        tex = shader.inputs (type = 'file')
        mif = shader.outputs(type='materialInfo')
        # hard txtet
        if tex and mif:
            tex[0].message.connect(mif[0].texture[0], f=True)
        elif not shader.inputs():
            shader.color.set(color)
        # bump
        if bump:
            bumpNode = bump[0]
            bumpVal = bumpNode.bumpDepth.get()
            bumpMap = bumpNode.inputs (type = 'file')[0]
            bumpMap.outColor.connect( shader.bumpMap, f=True)
            shader.bumpMult.set(bumpVal)
            pm.delete(bumpNode)
        if specCol:
            specNode = specCol[0]
            specNode.outColor.connect(shader.reflectionColor)
            #connectAttr -force Hana_ShoesL_Sp02_File.outColor Hana_ShoesR_shd.refractionColor;
            
def getAiShader():
    aiShaders = pm.ls(type='aiStandard')
    alSurface = pm.ls(type='alSurface')
    aiShaders.extend(alSurface)
    aiList = []
    for sd in aiShaders:
        aiList.append(sd.name())
    return aiList

def aiToBlinn(aiShaders):
    replaceShaderType = 'lambert'
    for ai in aiShaders:
        changeShaderType(ai, replaceShaderType)
        
def aiToVray(aiShaders):
    replaceShaderType = 'VRayMtl'
    for ai in aiShaders:
        changeShaderType1(ai, replaceShaderType)   
'''   
def addGamaAttr():
    vrNodes =pm.ls(type="VRayMtl")
    colorFiles = []
    
    for vr in vrNodes:
        colorFile = vr.color.inputs(type = 'file')
        specColorFile = vr.reflectionColor.inputs(type = 'file')
        colorFiles.extend(colorFile)
        colorFiles.extend(specColorFile)

    for f in colorFiles:
        pm.select(f, r=True)
        pm.vray("addAttributesFromGroup", f, "vray_file_gamma", 1)
        pm.select(f, d=True)

def addOpenSubdiv():
    transforms = pm.ls(tr=True)
    for tr in transforms:
        if tr.endswith('_sdm'):
            shape = tr.getShapes()[0]
            pm.select(cl=True)
            pm.select(shape, r=True)
            pm.vray("addAttributesFromGroup", shape, "vray_opensubdiv", 1)
            pm.select(shape, d=True)
    
'''
    