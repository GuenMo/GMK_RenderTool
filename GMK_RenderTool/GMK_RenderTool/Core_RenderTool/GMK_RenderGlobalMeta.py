# -*- coding: utf-8 -*-

import pymel.core as pm
import maya.mel as mel
import pymel.core.animation as at

class GMK_RenderMeta(object):
    
    def __init__(self):
        
        # default
        self.RenderGlobals       = 'defaultRenderGlobals'
        self.Resolution          = 'defaultResolution'
        
        self.RenderGlobalsData = {}
        self.RenderGlobalAttrList = ['colorProfileEnabled','inputColorProfile','outputColorProfile',
                                     'imageFilePrefix','imageFormat','imfkey',
                                     'outFormatControl','animation','putFrameBeforeExt','extensionPadding',
                                     'multiCamNamingMode','bufferName', 
                                     'outFormatExt','renderVersion','modifyExtension','startExtension','byExtension',
                                     'preMel','postMel']#,'preRenderLayerMel','postRenderLayerMel','preRenderMel','postRenderMel'] 
        
        self.ResolutionData = {}
        self.ResolutionAttrList = ['aspectLock','width','height','lockDeviceAspectRatio',
                                   'deviceAspectRatio','dotsPerInch','imageSizeUnits',
                                   'pixelDensityUnits']
        
        # anrold
        self.ArnoldDriver        = 'defaultArnoldDriver'
        self.ArnoldRenderOptions = 'defaultArnoldRenderOptions'
        self.ArnoldFilter        = 'defaultArnoldFilter'
         

        self.ArnoldDriverData = {}
        self.ArnoldDriverAttrList = ['aiTranslator','exrCompression','halfPrecision','preserveLayerName','tiled','autocrop','append']
        
        self.ArnoldRenderOptionsData = {}
        self.ArnoldRenderOptionsAttrList = ['AASamples','GIDiffuseSamples','GIGlossySamples','GIRefractionSamples','sssBssrdfSamples',
                                            'volumeIndirectSamples','lock_sampling_noise','use_sample_clamp','use_sample_clamp_AOVs',
                                            'AASampleClamp','GITotalDepth','GIDiffuseDepth','GIGlossyDepth','GIReflectionDepth',
                                            'GIRefractionDepth','autoTransparencyDepth','autoTransparencyThreshold','motion_blur_enable',
                                            'mb_object_deform_enable','mb_camera_enable','motion_steps','range_type','motion_frames',
                                            'range_type','motion_start','motion_end','lowLightThreshold','lightLinking','shadowLinking',
                                            'display_gamma','light_gamma','shader_gamma','texture_gamma','textureAutomip','textureAcceptUnmipped',
                                            'autotile','textureAutotile','textureAcceptUntiled','use_existing_tiled_textures','textureMaxMemoryMB',
                                            'textureMaxOpenFiles','textureDiffuseBlur','textureGlossyBlur','aiUserOptions','ignoreTextures',
                                            'ignoreShaders','ignoreAtmosphere','ignoreLights','ignoreShadows','ignoreSubdivision',
                                            'ignoreDisplacement','ignoreBump','ignoreSmoothing','ignoreMotionBlur','ignoreDof','ignoreSss',
                                            'forceTranslateShadingEngines','maxSubdivisions']
        
        self.ArnoldFilterData = {}
        self.ArnoldFilterAttrList = ['aiTranslator','width']
        
        # mental ray
        self.MentalrayGlobals = 'mentalrayGlobals'
        self.MentalrayGlobalsData = {}
        self.MentalrayGlobalsAttrList = ['imageCompression']


    def getMeta(self):
        nodes = pm.ls(type="groupId")
        for node in nodes:
            metaNode = pm.PyNode(node)
            if metaNode.hasAttr('MetaType'):
                if metaNode.MetaType.get() == 'RenderPreset':
                    return metaNode.name()
                
    def getRenderer(self):
        nodes = pm.ls(type="groupId")
        for node in nodes:
            metaNode = pm.PyNode(node)
            if metaNode.hasAttr('MetaType'):
                if metaNode.MetaType.get() == 'RenderPreset':
                    return metaNode.Renderer.get()
                
    def save(self, renderer):
        try:
            if self.getMeta() != None:
                self.delete()
                
            renderMeta = pm.createNode('groupId', name = 'RenderPreset')
            renderMeta.addAttr('MetaType', dt='string')
            renderMeta.MetaType.set('RenderPreset')
            renderMeta.MetaType.lock()
            renderMeta.addAttr('Renderer', dt='string')
            renderMeta.Renderer.set(renderer)
            renderMeta.Renderer.lock()
              
            for attr in self.RenderGlobalAttrList:
                attrNode = pm.PyNode(self.RenderGlobals+ '.' + attr)
                attrValue = attrNode.get()
                self.RenderGlobalsData[attr] = attrValue
            
            renderMeta.addAttr('RenderGlobals', dt='string')
            renderMeta.RenderGlobals.set(str(self.RenderGlobalsData))
            renderMeta.RenderGlobals.lock()
            
            for attr in self.ResolutionAttrList:
                attrNode = pm.PyNode(self.Resolution+ '.' + attr)
                attrValue = attrNode.get()
                self.ResolutionData[attr] = attrValue
            
            renderMeta.addAttr('Resolution', dt='string')
            renderMeta.Resolution.set(str(self.ResolutionData))
            renderMeta.Resolution.lock()
            
            # Arnold
            if self.getRenderer() == 'arnold':
                for attr in self.ArnoldDriverAttrList:
                    attrNode = pm.PyNode(self.ArnoldDriver+ '.' + attr)
                    attrValue = attrNode.get()
                    self.ArnoldDriverData[attr] = attrValue
                
                renderMeta.addAttr('ArnoldDriver', dt='string')
                renderMeta.ArnoldDriver.set(str(self.ArnoldDriverData))
                renderMeta.ArnoldDriver.lock()
                
                for attr in self.ArnoldRenderOptionsAttrList:
                    attrNode = pm.PyNode(self.ArnoldRenderOptions+ '.' + attr)
                    attrValue = attrNode.get()
                    self.ArnoldRenderOptionsData[attr] = attrValue
                
                renderMeta.addAttr('ArnoldRenderOptions', dt='string')
                renderMeta.ArnoldRenderOptions.set(str(self.ArnoldRenderOptionsData))
                renderMeta.ArnoldRenderOptions.lock()
                
                for attr in self.ArnoldFilterAttrList:
                    attrNode = pm.PyNode(self.ArnoldFilter+ '.' + attr)
                    attrValue = attrNode.get()
                    self.ArnoldFilterData[attr] = attrValue
    
                renderMeta.addAttr('ArnoldFilter', dt='string')
                renderMeta.ArnoldFilter.set(str(self.ArnoldFilterData))
                renderMeta.ArnoldFilter.lock()
            
            elif self.getRenderer() == 'mentalRay':
                for attr in self.MentalrayGlobalsAttrList:
                    attrNode = pm.PyNode(self.MentalrayGlobals+ '.' + attr)
                    attrValue = attrNode.get()
                    self.MentalrayGlobalsData[attr] = attrValue
                
                renderMeta.addAttr('MentalrayGlobals', dt='string')
                renderMeta.MentalrayGlobals.set(str(self.MentalrayGlobalsData))
                renderMeta.MentalrayGlobals.lock()
            
            renderMeta.lock()
            pm.select(cl=True)
            return True
        except:
            return False
            
    def delete(self):
        if self.getMeta() != None:
            renderMeta = pm.PyNode(self.getMeta())
            renderMeta.unlock()
            pm.delete(renderMeta)
           
    def convertData(self, data):
        return eval(data)
    
    def load(self):
        if self.getMeta() == None:
            print u"렌더 글로벌 데이터가 없습니다. 라이팅 셋이 임포트 되어 있지 않거나 잘못된 라이팅 셋이 임포트 되어 있습니다"
            return 
        
        renderMeta      = pm.PyNode(self.getMeta())        
        RenderGlobals   = pm.PyNode('defaultRenderGlobals')

        RenderGlobalsData       = eval(renderMeta.RenderGlobals.get())
        ResolutionData          = eval(renderMeta.Resolution.get())
        
        for attr in self.RenderGlobalAttrList:
            attrNode = pm.PyNode(self.RenderGlobals+ '.' + attr)
            if RenderGlobalsData[attr] == None:
                attrNode.set('')
            else:
                attrNode.set(RenderGlobalsData[attr])
        
        for attr in self.ResolutionAttrList:
            attrNode = pm.PyNode(self.Resolution+ '.' + attr)
            if ResolutionData[attr] == None:
                attrNode.set('')
            else:
                attrNode.set(ResolutionData[attr])
                
        if self.getRenderer() == 'arnold':
            ArnoldDriverData        = eval(renderMeta.ArnoldDriver.get())
            ArnoldRenderOptionsData = eval(renderMeta.ArnoldRenderOptions.get())
            ArnoldFilterData        = eval(renderMeta.ArnoldFilter.get())
            
            for attr in self.ArnoldDriverAttrList:
                attrNode = pm.PyNode(self.ArnoldDriver+ '.' + attr)
                if ArnoldDriverData[attr] == None:
                    attrNode.set('')
                else:
                    attrNode.set(ArnoldDriverData[attr])
                    
            for attr in self.ArnoldRenderOptionsAttrList:
                attrNode = pm.PyNode(self.ArnoldRenderOptions+ '.' + attr)
                if ArnoldRenderOptionsData[attr] == None:
                    attrNode.set('')
                else:
                    attrNode.set(ArnoldRenderOptionsData[attr])
                    
            for attr in self.ArnoldFilterAttrList:
                attrNode = pm.PyNode(self.ArnoldFilter+ '.' + attr)
                if ArnoldFilterData[attr] == None:
                    attrNode.set('')
                else:
                    attrNode.set(ArnoldFilterData[attr])
        
            RenderGlobals.currentRenderer.set('arnold')
        
        elif self.getRenderer() == 'mentalRay':
            MentalrayGlobalsData = eval(renderMeta.MentalrayGlobals.get())
            for attr in self.MentalrayGlobalsAttrList:
                attrNode = pm.PyNode(self.MentalrayGlobals+ '.' + attr)
                if MentalrayGlobalsData[attr] == None:
                    attrNode.set('')
                else:
                    attrNode.set(MentalrayGlobalsData[attr])
            mel.eval('updateCommonColorProfile();')
            RenderGlobals.currentRenderer.set('mentalRay')
        
        # Frame Range
        startFrame  = at.playbackOptions(q=True, animationStartTime =True)
        endFrame    = at.playbackOptions(q=True, animationEndTime =True)
        
        RenderGlobals.startFrame.set(startFrame)
        RenderGlobals.endFrame.set(endFrame)
        
#         try:
#             mel.eval('updateCommonColorProfile();')
#         except:
#             mel.eval('updateCommonColorProfile();')
        
        self.delete()
        print u'렌더 프리셋 로드 성공'

"""
Test 
aroldMeta = GMK_RenderMeta()
aroldMeta.save()
aroldMeta.load()
"""

