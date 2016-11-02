# -*- coding: utf-8 -*-

import pymel.core as pm
import pymel.core.system as st

class GMK_RenderLayer(object):
    
    def __init__(self):
        self.ReferenceInfo = {}
        
    def setAssetList(self):
        allReferences = st.listReferences()
        # Node 최상의 노드 Type = [CH, BG, ]
        for ref in allReferences:
            namespace = ref.namespace
            topNode = ref.nodes()[0].name()
            assetType = namespace.partition('_')[0]
            self.ReferenceInfo[namespace] = {'Node': topNode, 'Type': assetType}
            
    def getAssetList(self):
        self.setAssetList()
        CH = []
        BG = []
        PROP = []
        ReferenceInfo = {}  
        for value in self.ReferenceInfo.values():
            if value['Type'] == 'CH':
                CH.append(value['Node'])
            elif value['Type'] == 'BG':
                BG.append(value['Node'])
            elif value['Type'] == 'PROP':
                PROP.append(value['Node'])
        ReferenceInfo['CH'] = CH
        ReferenceInfo['BG'] = BG
        ReferenceInfo['PROP'] = PROP
        return ReferenceInfo
        
    def getRenderLayer(self):
        renderLayer = pm.ls(type='renderLayer')
        validLayer = []
        
        for layer in renderLayer:
            if not 'defaultRenderLayer' in layer.name() and  not ':' in layer.name():
                validLayer.append(layer.name())
        return validLayer
        
    def setRenderLayer(self, layer, objects):
        pm.editRenderLayerMembers(layer, objects )
        