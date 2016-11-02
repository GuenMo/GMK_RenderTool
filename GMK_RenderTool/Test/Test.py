import pymel.core as pm
import time

RenderGlobals       = pm.PyNode('defaultRenderGlobals')
ArnoldDriver        = pm.PyNode('defaultArnoldDriver')
ArnoldRenderOptions = pm.PyNode('defaultArnoldRenderOptions')
ArnoldFilter        = pm.PyNode('defaultArnoldFilter')
Resolution          = pm.PyNode('defaultResolution')
FrontCam            = pm.PyNode('frontShape')
PerspCam            = pm.PyNode('perspShape')
SideCam             = pm.PyNode('sideShape')
TopCam              = pm.PyNode('topShape')
RenderCam           = pm.PyNode('Rcamshape')


# File Output
RenderGlobals.imageFilePrefix.set('<RenderLayer>/<RenderLayer>_<RenderPass>') # File name prefix
ArnoldDriver.aiTranslator.set('exr')        # Image format
ArnoldDriver.exrCompression.set(3)          # Compression
ArnoldDriver.halfPrecision.set(True)        # HarfPrecision
ArnoldDriver.preserveLayerName.set(False)   # PreserveLayerName
ArnoldDriver.tiled.set(False)               # Tiled 
ArnoldDriver.autocrop.set(False)            # Autocrop 
ArnoldDriver.append.set(False)              # Append 

# Metadata
RenderGlobals.outFormatControl.set(0)
RenderGlobals.animation.set(1)
RenderGlobals.putFrameBeforeExt.set(1)
RenderGlobals.extensionPadding.set(4)       # Frame padding
RenderGlobals.outFormatExt.set('')          # Extension
RenderGlobals.renderVersion.set('')         # Version Label

# Frame range
RenderGlobals.startFrame.set(101.0)         # Start Frame
RenderGlobals.endFrame.set(215.0)           # End Frame
RenderGlobals.byFrameStep.set(1.0)          # By Frame
RenderGlobals.modifyExtension.set(False)    # Renumber frames 
RenderGlobals.startExtension.set(1.0)       # Start number
RenderGlobals.byExtension.set(1.0)          # By Frame 

# Renderable Cameras
FrontCam.renderable.set(0)
PerspCam.renderable.set(0)
SideCam.renderable.set(0)
TopCam.renderable.set(0)
RenderCam.renderable.set(1)
RenderCam.mask.set(1)

# Image Size
Resolution.aspectLock.set(0)
Resolution.width.set(960)
Resolution.height.set(540)
Resolution.lockDeviceAspectRatio.set(0)
Resolution.deviceAspectRatio.set(1.777)
Resolution.dotsPerInch.set(72)
Resolution.imageSizeUnits.set(0)
Resolution.pixelDensityUnits.set(0)
Resolution.width.set(960)
Resolution.height.set(540)

# Render Options
RenderGlobals.preMel.set('') # Pre render MEL
RenderGlobals.postMel.set('') # Post render MEL
RenderGlobals.preRenderLayerMel.set('<RenderLayer>/<RenderLayer>_<RenderPass>') # Pre render layer MEL
RenderGlobals.postRenderLayerMel.set('<RenderLayer>/<RenderLayer>_<RenderPass>') # Post render layer MEL
RenderGlobals.preRenderMel.set('<RenderLayer>/<RenderLayer>_<RenderPass>') # Pre render frame MEL
RenderGlobals.postRenderMel.set('<RenderLayer>/<RenderLayer>_<RenderPass>') # Post render frame MEL

#########################
# Arnold Renderer
#########################
# Sampling
ArnoldRenderOptions.AASamples.set(8)
ArnoldRenderOptions.GIDiffuseSamples.set(2)
ArnoldRenderOptions.GIGlossySamples.set(2)
ArnoldRenderOptions.GIRefractionSamples.set(2)
ArnoldRenderOptions.sssBssrdfSamples.set(3)
ArnoldRenderOptions.volumeIndirectSamples.set(2)
ArnoldRenderOptions.lock_sampling_noise.set(1)
# Clamping
ArnoldRenderOptions.use_sample_clamp.set(1)
ArnoldRenderOptions.use_sample_clamp_AOVs.set(1)
ArnoldRenderOptions.AASampleClamp.set(2)
# Filter
ArnoldFilter.aiTranslator.set('gaussian')
ArnoldFilter.width.set(2)
# Ray Depth
ArnoldRenderOptions.GITotalDepth.set(10)
ArnoldRenderOptions.GIDiffuseDepth.set(1)
ArnoldRenderOptions.GIGlossyDepth.set(1)
ArnoldRenderOptions.GIReflectionDepth.set(2)
ArnoldRenderOptions.GIRefractionDepth.set(2)
ArnoldRenderOptions.autoTransparencyDepth.set(10)
ArnoldRenderOptions.autoTransparencyThreshold.set(0.99)
# Motion Blur
ArnoldRenderOptions.motion_blur_enable.set(1)
ArnoldRenderOptions.mb_object_deform_enable.set(1)
ArnoldRenderOptions.mb_camera_enable.set(1)
ArnoldRenderOptions.motion_steps.set(2)
ArnoldRenderOptions.range_type.set(3)
ArnoldRenderOptions.motion_frames.set(0.5)
ArnoldRenderOptions.range_type.set(3)
ArnoldRenderOptions.motion_start.set(0)
ArnoldRenderOptions.motion_end.set(1)
# Lights
ArnoldRenderOptions.lowLightThreshold.set(0.001)
ArnoldRenderOptions.lightLinking.set(1)
ArnoldRenderOptions.shadowLinking.set(1)
# Gamma Correction
ArnoldRenderOptions.display_gamma.set(2.2)
ArnoldRenderOptions.light_gamma.set(2.2)
ArnoldRenderOptions.shader_gamma.set(2.2)
ArnoldRenderOptions.texture_gamma.set(2.2)
# Textures
ArnoldRenderOptions.textureAutomip.set(1)
ArnoldRenderOptions.textureAcceptUnmipped.set(1)
ArnoldRenderOptions.autotile.set(1)
ArnoldRenderOptions.textureAutotile.set(64)
ArnoldRenderOptions.textureAcceptUntiled.set(1)
ArnoldRenderOptions.use_existing_tiled_textures.set(0)
ArnoldRenderOptions.textureMaxMemoryMB.set(1024)
ArnoldRenderOptions.textureMaxOpenFiles.set(100)
ArnoldRenderOptions.textureDiffuseBlur.set(0.031)
ArnoldRenderOptions.textureGlossyBlur.set(0)

#########################
# Override
#########################
ArnoldRenderOptions.aiUserOptions.set('')
ArnoldRenderOptions.ignoreTextures.set(0)
ArnoldRenderOptions.ignoreShaders.set(0)
ArnoldRenderOptions.ignoreAtmosphere.set(0)
ArnoldRenderOptions.ignoreLights.set(0)
ArnoldRenderOptions.ignoreShadows.set(0)
ArnoldRenderOptions.ignoreSubdivision.set(0)
ArnoldRenderOptions.ignoreDisplacement.set(0)
ArnoldRenderOptions.ignoreBump.set(0)
ArnoldRenderOptions.ignoreSmoothing.set(0)
ArnoldRenderOptions.ignoreMotionBlur.set(1)
ArnoldRenderOptions.ignoreDof.set(0)
ArnoldRenderOptions.ignoreSss.set(0)
ArnoldRenderOptions.forceTranslateShadingEngines.set(0)
ArnoldRenderOptions.maxSubdivisions.set(999)


RenderGlobals.currentRenderer.set('arnold') # Render Using
'''
nodes = ["defaultArnoldFilter"]
GMK_RenderSet = {}

AttrList = cmds.listAttr(nodes[0])
GMK_Attr = {}
for attr in AttrList:
    attrType = cmds.getAttr(nodes[0] + "." + attr, type=True)
    if not attrType in ignoreType:
        attrValue = cmds.getAttr(nodes[0] + "." + attr)
        GMK_Attr[attr] = (attrType, attrValue)
GMK_RenderSet[nodes[0]] = GMK_Attr
print GMK_RenderSet
'''