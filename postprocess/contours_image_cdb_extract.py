# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
import glob
import os

def create_cinema_csv( db, datadir ):
    files = sorted(glob.glob(db + "/RenderView*"))
    cur_image = 0
    with open(db + "/data.csv", "w") as f:
        f.write("time,FILE\n")

        for infile in files:
            path, file_name = os.path.split(infile)
            print(file_name)
            f.write(str(cur_image) + "," + file_name + "\n")
            cur_image = cur_image + 1

def paraview_set_up_extracts( db, datadir ):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    
    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------

    # black background
    LoadPalette(paletteName='BlackBackground')
    
    # get the material library
    materialLibrary1 = GetMaterialLibrary()
    
    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1920, 1080]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [-1.4435499906539917e-08, -2.2351741790771484e-08, 0.08731197472661734]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [-0.913270744661002, 0.0, 0.3921541663602877]
    renderView1.CameraFocalPoint = [-1.549582841626004e-17, 0.0, 0.1506849378347397]
    renderView1.CameraViewUp = [0.2556166324404753, 0.0, 0.9667782254580369]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 0.24449439988291152
    renderView1.BackEnd = 'OSPRay raycaster'
    renderView1.OSPRayMaterialLibrary = materialLibrary1
    
    SetActiveView(None)
    
    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------
    
    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    layout1.SetSize(1920, 1080)
    
    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------
    
    # create a new 'ExodusIIReader'
    registration_name=(datadir + '/nonIsoEdgeOpenJet.e.4.*')
    filename_list=[(datadir + '/nonIsoEdgeOpenJet.e.4.0'), (datadir + '/nonIsoEdgeOpenJet.e.4.1'), (datadir + '/nonIsoEdgeOpenJet.e.4.2'), (datadir + '/nonIsoEdgeOpenJet.e.4.3'),]
    nonIsoEdgeOpenJete4 = ExodusIIReader(registrationName=registration_name, FileName=filename_list)
    nonIsoEdgeOpenJete4.PointVariables = ['enthalpy', 'pressure', 'temperature', 'velocity_']
    nonIsoEdgeOpenJete4.SideSetArrayStatus = []
    nonIsoEdgeOpenJete4.ElementBlocks = ['block_1']
    
    # create a new 'Contour'
    negativePressureContour = Contour(registrationName='NegativePressureContour', Input=nonIsoEdgeOpenJete4)
    negativePressureContour.ContourBy = ['POINTS', 'pressure']
    negativePressureContour.Isosurfaces = [-0.0001]
    negativePressureContour.PointMergeMethod = 'Uniform Binning'
    
    # create a new 'Contour'
    enthalpyContour = Contour(registrationName='EnthalpyContour', Input=nonIsoEdgeOpenJete4)
    enthalpyContour.ContourBy = ['POINTS', 'enthalpy']
    enthalpyContour.Isosurfaces = [10000.0]
    enthalpyContour.PointMergeMethod = 'Uniform Binning'
    
    # create a new 'Contour'
    positivePressureContour = Contour(registrationName='PositivePressureContour', Input=nonIsoEdgeOpenJete4)
    positivePressureContour.ContourBy = ['POINTS', 'pressure']
    positivePressureContour.Isosurfaces = [0.0001]
    positivePressureContour.PointMergeMethod = 'Uniform Binning'
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from nonIsoEdgeOpenJete4
    nonIsoEdgeOpenJete4Display = Show(nonIsoEdgeOpenJete4, renderView1, 'UnstructuredGridRepresentation')
    
    # trace defaults for the display properties.
    nonIsoEdgeOpenJete4Display.Representation = 'Surface'
    nonIsoEdgeOpenJete4Display.ColorArrayName = ['POINTS', '']
    nonIsoEdgeOpenJete4Display.Opacity = 0.32
    nonIsoEdgeOpenJete4Display.SelectTCoordArray = 'None'
    nonIsoEdgeOpenJete4Display.SelectNormalArray = 'None'
    nonIsoEdgeOpenJete4Display.SelectTangentArray = 'None'
    nonIsoEdgeOpenJete4Display.OSPRayScaleArray = 'GlobalNodeId'
    nonIsoEdgeOpenJete4Display.OSPRayScaleFunction = 'PiecewiseFunction'
    nonIsoEdgeOpenJete4Display.SelectOrientationVectors = 'None'
    nonIsoEdgeOpenJete4Display.ScaleFactor = 0.030136987566947937
    nonIsoEdgeOpenJete4Display.SelectScaleArray = 'GlobalNodeId'
    nonIsoEdgeOpenJete4Display.GlyphType = 'Arrow'
    nonIsoEdgeOpenJete4Display.GlyphTableIndexArray = 'GlobalNodeId'
    nonIsoEdgeOpenJete4Display.GaussianRadius = 0.0015068493783473968
    nonIsoEdgeOpenJete4Display.SetScaleArray = ['POINTS', 'GlobalNodeId']
    nonIsoEdgeOpenJete4Display.ScaleTransferFunction = 'PiecewiseFunction'
    nonIsoEdgeOpenJete4Display.OpacityArray = ['POINTS', 'GlobalNodeId']
    nonIsoEdgeOpenJete4Display.OpacityTransferFunction = 'PiecewiseFunction'
    nonIsoEdgeOpenJete4Display.DataAxesGrid = 'GridAxesRepresentation'
    nonIsoEdgeOpenJete4Display.PolarAxes = 'PolarAxesRepresentation'
    nonIsoEdgeOpenJete4Display.ScalarOpacityUnitDistance = 0.015062372960425148
    nonIsoEdgeOpenJete4Display.OpacityArrayName = ['POINTS', 'GlobalNodeId']
    nonIsoEdgeOpenJete4Display.ExtractedBlockIndex = 2
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    nonIsoEdgeOpenJete4Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    nonIsoEdgeOpenJete4Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # show data from enthalpyContour
    enthalpyContourDisplay = Show(enthalpyContour, renderView1, 'GeometryRepresentation')
    
    # get color transfer function/color map for 'velocity_'
    velocity_LUT = GetColorTransferFunction('velocity_')
    velocity_LUT.RGBPoints = [-0.01593730623308355, 0.231373, 0.298039, 0.752941, 0.030675974411747547, 0.865003, 0.865003, 0.865003, 0.07728925505657865, 0.705882, 0.0156863, 0.14902]
    velocity_LUT.ScalarRangeInitialized = 1.0
    velocity_LUT.VectorComponent = 2
    velocity_LUT.VectorMode = 'Component'
    
    # trace defaults for the display properties.
    enthalpyContourDisplay.Representation = 'Surface'
    enthalpyContourDisplay.ColorArrayName = ['POINTS', 'velocity_']
    enthalpyContourDisplay.LookupTable = velocity_LUT
    enthalpyContourDisplay.SelectTCoordArray = 'None'
    enthalpyContourDisplay.SelectNormalArray = 'Normals'
    enthalpyContourDisplay.SelectTangentArray = 'None'
    enthalpyContourDisplay.OSPRayScaleArray = 'enthalpy'
    enthalpyContourDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    enthalpyContourDisplay.SelectOrientationVectors = 'None'
    enthalpyContourDisplay.ScaleFactor = 0.01933152247220278
    enthalpyContourDisplay.SelectScaleArray = 'enthalpy'
    enthalpyContourDisplay.GlyphType = 'Arrow'
    enthalpyContourDisplay.GlyphTableIndexArray = 'enthalpy'
    enthalpyContourDisplay.GaussianRadius = 0.000966576123610139
    enthalpyContourDisplay.SetScaleArray = ['POINTS', 'enthalpy']
    enthalpyContourDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    enthalpyContourDisplay.OpacityArray = ['POINTS', 'enthalpy']
    enthalpyContourDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    enthalpyContourDisplay.DataAxesGrid = 'GridAxesRepresentation'
    enthalpyContourDisplay.PolarAxes = 'PolarAxesRepresentation'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    enthalpyContourDisplay.ScaleTransferFunction.Points = [48470.90823995246, 0.0, 0.5, 0.0, 48478.91015625, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    enthalpyContourDisplay.OpacityTransferFunction.Points = [48470.90823995246, 0.0, 0.5, 0.0, 48478.91015625, 1.0, 0.5, 0.0]
    
    # setup the color legend parameters for each legend in this view
    
    # get color legend/bar for velocity_LUT in view renderView1
    velocity_LUTColorBar = GetScalarBar(velocity_LUT, renderView1)
    velocity_LUTColorBar.WindowLocation = 'UpperLeftCorner'
    velocity_LUTColorBar.Position = [0.002070393374741201, 0.6534810126582279]
    velocity_LUTColorBar.Title = 'velocity_'
    velocity_LUTColorBar.ComponentTitle = 'Z'
    
    # set color bar visibility
    velocity_LUTColorBar.Visibility = 1
    
    # show color legend
    enthalpyContourDisplay.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # get opacity transfer function/opacity map for 'velocity_'
    velocity_PWF = GetOpacityTransferFunction('velocity_')
    velocity_PWF.Points = [-0.01593730623308355, 0.0, 0.5, 0.0, 0.07728925505657865, 1.0, 0.5, 0.0]
    velocity_PWF.ScalarRangeInitialized = 1
    
    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------
    
    # create extractor
    pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
    # trace defaults for the extractor.
    # init the 'PNG' selected for 'Writer'
    pNG1.Writer.FileName = 'RenderView1_%.6ts%cm.png'
    pNG1.Writer.ImageResolution = [1920, 1080]
    pNG1.Writer.TransparentBackground = 0
    pNG1.Writer.Format = 'PNG'
    pNG1.Writer.CameraMode = 'Static'
    #pNG1.Writer.CameraMode = 'Phi-Theta'
    #pNG1.Writer.PhiResolution = 3
    #pNG1.Writer.ThetaResolution = 3
    
    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(pNG1)
    # ----------------------------------------------------------------


# -----------------------------------------------------------------------------------------------
#
# main
#
# -----------------------------------------------------------------------------------------------
if __name__ == '__main__':
    infile  = "" 
    database = ""
    if len(sys.argv) == 3:
        infile   = sys.argv[2]
        database = sys.argv[1]
    else:
        print("ERROR")

    # set up paraview pipeline and extracts for cdb
    paraview_set_up_extracts( database, infile )

    # generate extracts
    SaveExtracts(ExtractsOutputDirectory=database)

    # manually make csv file for cdb
    create_cinema_csv( database, infile )
