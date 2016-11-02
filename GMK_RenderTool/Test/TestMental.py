import pymel.core as pm

RenderGlobals = pm.PyNode('defaultRenderGlobals')
MentalrayGlobals = pm.PyNode("mentalrayGlobals")
Resolution          = pm.PyNode('defaultResolution')

# Common
## Color Management
RenderGlobals.colorProfileEnabled.set(0) 
RenderGlobals.inputColorProfile.set(3) 
RenderGlobals.outputColorProfile.set(2)
pm.mel.updateCommonColorProfile()

##File Output
RenderGlobals.imageFilePrefix.set('%l/T3_E00_SC000_%l') 
RenderGlobals.imageFormat.set(51) 
RenderGlobals.imfkey.set('exr')  
MentalrayGlobals.imageCompression.set(0)
RenderGlobals.animation.set(1)
RenderGlobals.putFrameBeforeExt.set(1) 
RenderGlobals.extensionPadding.set(3)
RenderGlobals.multiCamNamingMode.set(1)
RenderGlobals.bufferName.set('')
RenderGlobals.outFormatControl.set(0)
RenderGlobals.outFormatExt.set('')
RenderGlobals.renderVersion.set('')

## Frame Range
RenderGlobals.startFrame.set(1)
RenderGlobals.endFrame.set(101)
RenderGlobals.byFrameStep.set(1)
RenderGlobals.skipExistingFrames.set(0)
RenderGlobals.modifyExtension.set(0)
RenderGlobals.startExtension.set(1)
RenderGlobals.byExtension.set(1)

## Image Size
Resolution.aspectLock.set(0)
Resolution.width.set(960)
Resolution.height.set(540)
Resolution.imageSizeUnits.set(0)
Resolution.dotsPerInch.set(72)
Resolution.pixelDensityUnits.set(0)
Resolution.lockDeviceAspectRatio.set(1)
Resolution.deviceAspectRatio.set(1.778)






















# Quality
## Sampling
setAttr "miDefaultOptions.miRenderUsing" 0;
setAttr "miDefaultOptions.miSamplesQualityR" 0.25;
setAttr "miDefaultOptions.miSamplesMin" 1;
setAttr "miDefaultOptions.miSamplesMax" 100;
setAttr "miDefaultOptions.miSamplesErrorCutoffR" 0;
setAttr "miDefaultOptions.miContrastAsColor" 0;
setAttr "miDefaultOptions.miProgressiveRender" 1;
setAttr "miDefaultOptions.miProgSubsampleSize" 4;
setAttr "miDefaultOptions.miProgMaxTime" 0;
## Sample Options
setAttr "miDefaultOptions.filter" 1;
setAttr miDefaultOptions.filterWidth 1;
setAttr miDefaultOptions.filterHeight 1;
setAttr "miDefaultOptions.jitter" 1;
setAttr "miDefaultOptions.sampleLock" 1;
setAttr "miDefaultOptions.diagnoseSamples" 0;
## Raytracing
setAttr "miDefaultOptions.rayTracing" 1;
setAttr "miDefaultOptions.maxReflectionRays" 1;
setAttr "miDefaultOptions.maxRefractionRays" 1;
setAttr "miDefaultOptions.maxRayDepth" 2;
setAttr "miDefaultOptions.maxShadowRayDepth" 2;
setAttr "miDefaultOptions.maxReflectionBlur" 2;
setAttr "miDefaultOptions.maxRefractionBlur" 2;
## Motion Blur
setAttr "miDefaultOptions.motionBlur" 0;
setAttr "miDefaultOptions.motionSteps" 1;
setAttr "miDefaultOptions.motionBlurBy" 1;
    ##########Displace Motion Factor
    ##########KyFrameLocation
## Shadows
setAttr "miDefaultOptions.shadowMethod" 1;
setAttr "miDefaultOptions.rebuildShadowMaps" 1;
setAttr "miDefaultOptions.rebuildShadowMaps" 2;
setAttr "miDefaultOptions.rebuildShadowMaps" 0;
setAttr "miDefaultOptions.motionBlurShadowMaps" 1;
## Framebuffer
setAttr "miDefaultFramebuffer.datatype" 5;
setAttr "miDefaultFramebuffer.gamma" 1;
setAttr "miDefaultFramebuffer.colorclip" 2;
setAttr "miDefaultFramebuffer.interpolateSamples" 1;
setAttr "miDefaultFramebuffer.desaturate" 0;
setAttr "miDefaultFramebuffer.premultiply" 1;
setAttr "miDefaultFramebuffer.dither" 1;
    ###########Rasterizer use Opacity
    ###########contrast all buffers

## Legacy Options




# Options
## Diagnostics
setAttr "miDefaultOptions.diagnoseSamples" 1;
setAttr "miDefaultOptions.diagnoseBsp" 1;
setAttr "miDefaultOptions.diagnoseGrid" 0;
setAttr "miDefaultOptions.diagnoseGridSize" 2;
setAttr "miDefaultOptions.diagnosePhoton" 1;
setAttr "miDefaultOptions.diagnosePhotonDensity" 1;
setAttr "miDefaultOptions.diagnoseFinalg" 1;
## Preview
setAttr "mentalrayGlobals.previewAnimation" 0;
setAttr "mentalrayGlobals.previewMotionBlur" 1;
setAttr "mentalrayGlobals.previewRenderTiles" 1;
setAttr "mentalrayGlobals.previewConvertTiles" 1;
setAttr "mentalrayGlobals.previewTonemapTiles" 1;
setAttr "mentalrayGlobals.tonemapRangeHigh" 2;

## mental ray Overrides
### Displacement
setAttr "miDefaultOptions.maxDisplace" 1;
### Shadow Map
setAttr "miDefaultOptions.biasShadowMaps" 1;
### Global Illumination/Caustics
    # global illum generating
    # global illum receiving
    # sautics generationg
    # caustioc reveiving
### Tessellation
    # surface approx
    # dispalce approx

## Translation
setAttr "mentalrayGlobals.exportExactHierarchy" 1;
setAttr "mentalrayGlobals.exportFullDagpath" 1;
setAttr "mentalrayGlobals.exportTexturesFirst" 1;
setAttr "mentalrayGlobals.exportParticles" 0;
setAttr "mentalrayGlobals.exportParticleInstances" 0;
setAttr "mentalrayGlobals.exportFluids" 0;
setAttr "mentalrayGlobals.exportHair" 0;
setAttr "mentalrayGlobals.exportPostEffects" 1;
setAttr "mentalrayGlobals.exportVertexColors" 0;
### Performance
setAttr "mentalrayGlobals.exportAssignedOnly" 1;
setAttr "mentalrayGlobals.exportVisibleOnly" 1;
setAttr "mentalrayGlobals.optimizeAnimateDetection" 0;
setAttr "mentalrayGlobals.exportSharedVertices" 0;
setAttr "mentalrayGlobals.optimizeRaytraceShadows" 0;
setAttr "mentalrayGlobals.exportAssembly" 0;
setAttr "mentalrayGlobals.exportMotionSegments" 0;
setAttr "mentalrayGlobals.exportTriangles" 0;
setAttr "mentalrayGlobals.exportShapeDeformation" 0;
setAttr "miDefaultOptions.forceMotionVectors" 1;
setAttr "miDefaultOptions.miTraceCameraClip" 1;
setAttr "miDefaultOptions.miTraceCameraMotionVectors" 1;
setAttr "mentalrayGlobals.exportPolygonDerivatives" 0;
setAttr "mentalrayGlobals.mayaDerivatives" 1;
setAttr "mentalrayGlobals.smoothPolygonDerivatives" 1;
setAttr "mentalrayGlobals.exportNurbsDerivatives" 1;
setAttr "mentalrayGlobals.exportObjectsOnDemand" 1;
setAttr "mentalrayGlobals.exportPlaceholderSize" 2;
setAttr "miDefaultOptions.allocateOnHeap" 0;
### Custommization
setAttr "mentalrayGlobals.renderShadersWithFiltering" 1;
setAttr "mentalrayGlobals.useLegacyShaders" 1;
setAttr "mentalrayGlobals.exportStateShader" 0;
setAttr "mentalrayGlobals.exportLightLinker" 1;
setAttr "mentalrayGlobals.exportMayaOptions" 0;
setAttr "mentalrayGlobals.exportCustomColors" 0;
setAttr "mentalrayGlobals.exportCustom" 0;
setAttr "mentalrayGlobals.exportCustomData" 0;
setAttr "mentalrayGlobals.exportCustomVectors" 0;

## Custom Entities
setAttr "mentalrayGlobals.passAlphaThrough" 0;
setAttr "mentalrayGlobals.passDepthThrough" 1;
setAttr "mentalrayGlobals.passLabelThrough" 1;
### Custom Globals
setAttr -type "string" mentalrayGlobals.versions "";
setAttr -type "string" mentalrayGlobals.links "";
setAttr -type "string" mentalrayGlobals.includes "";
### Custom Scene Text
    #Global Text
    #Options Text
    #Light Test
    #Cameras Text
    #Scene Text
    #Root Group Text
    #Render Text

