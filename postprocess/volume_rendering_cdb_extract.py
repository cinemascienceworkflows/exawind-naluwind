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
    layout1.SetSize(1000, 1000)
    
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
    
    # create a new 'Merge Blocks'
    mergeBlocks1 = MergeBlocks(registrationName='MergeBlocks1', Input=nonIsoEdgeOpenJete4)
    
    # create a new 'Ghost Cells Generator'
    ghostCellsGenerator1 = GhostCellsGenerator(registrationName='GhostCellsGenerator1', Input=mergeBlocks1)
    ghostCellsGenerator1.MinimumNumberOfGhostLevels = 2
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from nonIsoEdgeOpenJete4
    nonIsoEdgeOpenJete4Display = Show(nonIsoEdgeOpenJete4, renderView1, 'UnstructuredGridRepresentation')
    
    # get color transfer function/color map for 'vtkBlockColors'
    vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
    vtkBlockColorsLUT.InterpretValuesAsCategories = 1
    vtkBlockColorsLUT.AnnotationsInitialized = 1
    vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
    vtkBlockColorsLUT.ActiveAnnotatedValues = ['0']
    vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]
    
    # get opacity transfer function/opacity map for 'vtkBlockColors'
    vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
    
    # trace defaults for the display properties.
    nonIsoEdgeOpenJete4Display.Representation = 'Surface'
    nonIsoEdgeOpenJete4Display.ColorArrayName = ['FIELD', 'vtkBlockColors']
    nonIsoEdgeOpenJete4Display.LookupTable = vtkBlockColorsLUT
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
    nonIsoEdgeOpenJete4Display.ScalarOpacityFunction = vtkBlockColorsPWF
    nonIsoEdgeOpenJete4Display.ScalarOpacityUnitDistance = 0.015062372960425148
    nonIsoEdgeOpenJete4Display.OpacityArrayName = ['POINTS', 'GlobalNodeId']
    nonIsoEdgeOpenJete4Display.ExtractedBlockIndex = 2
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    nonIsoEdgeOpenJete4Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    nonIsoEdgeOpenJete4Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # show data from mergeBlocks1
    mergeBlocks1Display = Show(mergeBlocks1, renderView1, 'UnstructuredGridRepresentation')
    
    # trace defaults for the display properties.
    mergeBlocks1Display.Representation = 'Feature Edges'
    mergeBlocks1Display.ColorArrayName = [None, '']
    mergeBlocks1Display.SelectTCoordArray = 'None'
    mergeBlocks1Display.SelectNormalArray = 'None'
    mergeBlocks1Display.SelectTangentArray = 'None'
    mergeBlocks1Display.OSPRayScaleArray = 'GlobalNodeId'
    mergeBlocks1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    mergeBlocks1Display.SelectOrientationVectors = 'None'
    mergeBlocks1Display.ScaleFactor = 0.030136987566947937
    mergeBlocks1Display.SelectScaleArray = 'GlobalNodeId'
    mergeBlocks1Display.GlyphType = 'Arrow'
    mergeBlocks1Display.GlyphTableIndexArray = 'GlobalNodeId'
    mergeBlocks1Display.GaussianRadius = 0.0015068493783473968
    mergeBlocks1Display.SetScaleArray = ['POINTS', 'GlobalNodeId']
    mergeBlocks1Display.ScaleTransferFunction = 'PiecewiseFunction'
    mergeBlocks1Display.OpacityArray = ['POINTS', 'GlobalNodeId']
    mergeBlocks1Display.OpacityTransferFunction = 'PiecewiseFunction'
    mergeBlocks1Display.DataAxesGrid = 'GridAxesRepresentation'
    mergeBlocks1Display.PolarAxes = 'PolarAxesRepresentation'
    mergeBlocks1Display.ScalarOpacityUnitDistance = 0.015062372960425148
    mergeBlocks1Display.OpacityArrayName = ['POINTS', 'GlobalNodeId']
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    mergeBlocks1Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    mergeBlocks1Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # show data from ghostCellsGenerator1
    ghostCellsGenerator1Display = Show(ghostCellsGenerator1, renderView1, 'UnstructuredGridRepresentation')
    
    # get color transfer function/color map for 'velocity_'
    velocity_LUT = GetColorTransferFunction('velocity_')
    velocity_LUT.RGBPoints = [0.0, 0.267004, 0.004874, 0.329415, 0.0021899188230252364, 0.26851, 0.009605, 0.335427, 0.004379279278171068, 0.269944, 0.014625, 0.341379, 0.006569198101196304, 0.271305, 0.019942, 0.347269, 0.008758558556342135, 0.272594, 0.025563, 0.353093, 0.010948477379367372, 0.273809, 0.031497, 0.358853, 0.013137837834513206, 0.274952, 0.037752, 0.364543, 0.015327756657538442, 0.276022, 0.044167, 0.370164, 0.017517675480563676, 0.277018, 0.050344, 0.375715, 0.019707035935709508, 0.277941, 0.056324, 0.381191, 0.021896954758734745, 0.278791, 0.062145, 0.386592, 0.02408631521388058, 0.279566, 0.067836, 0.391917, 0.02627623403690581, 0.280267, 0.073417, 0.397163, 0.028465594492051646, 0.280894, 0.078907, 0.402329, 0.030655513315076884, 0.281446, 0.08432, 0.407414, 0.03284543213810212, 0.281924, 0.089666, 0.412415, 0.035034792593247946, 0.282327, 0.094955, 0.417331, 0.03722471141627319, 0.282656, 0.100196, 0.42216, 0.039414071871419015, 0.28291, 0.105393, 0.426902, 0.04160399069444426, 0.283091, 0.110553, 0.431554, 0.043793351149590085, 0.283197, 0.11568, 0.436115, 0.04598326997261532, 0.283229, 0.120777, 0.440584, 0.048173188795640566, 0.283187, 0.125848, 0.44496, 0.05036254925078639, 0.283072, 0.130895, 0.449241, 0.05255246807381162, 0.282884, 0.13592, 0.453427, 0.05474182852895746, 0.282623, 0.140926, 0.457517, 0.0569317473519827, 0.28229, 0.145912, 0.46151, 0.05912110780712853, 0.281887, 0.150881, 0.465405, 0.06131102663015377, 0.281412, 0.155834, 0.469201, 0.0635003870852996, 0.280868, 0.160771, 0.472899, 0.06569030590832484, 0.280255, 0.165693, 0.476498, 0.06788022473135007, 0.279574, 0.170599, 0.479997, 0.07006958518649589, 0.278826, 0.17549, 0.483397, 0.07225950400952114, 0.278012, 0.180367, 0.486697, 0.07444886446466698, 0.277134, 0.185228, 0.489898, 0.0766387832876922, 0.276194, 0.190074, 0.493001, 0.07882814374283803, 0.275191, 0.194905, 0.496005, 0.08101806256586327, 0.274128, 0.199721, 0.498911, 0.08320798138888852, 0.273006, 0.20452, 0.501721, 0.08539734184403434, 0.271828, 0.209303, 0.504434, 0.08758726066705957, 0.270595, 0.214069, 0.507052, 0.08977662112220541, 0.269308, 0.218818, 0.509577, 0.09196653994523064, 0.267968, 0.223549, 0.512008, 0.09415590040037648, 0.26658, 0.228262, 0.514349, 0.09634581922340173, 0.265145, 0.232956, 0.516599, 0.09853573804642694, 0.263663, 0.237631, 0.518762, 0.10072509850157278, 0.262138, 0.242286, 0.520837, 0.10291501732459803, 0.260571, 0.246922, 0.522828, 0.10510437777974387, 0.258965, 0.251537, 0.524736, 0.10729429660276908, 0.257322, 0.25613, 0.526563, 0.10948365705791492, 0.255645, 0.260703, 0.528312, 0.11167357588094017, 0.253935, 0.265254, 0.529983, 0.1138634947039654, 0.252194, 0.269783, 0.531579, 0.11605285515911122, 0.250425, 0.27429, 0.533103, 0.11824277398213646, 0.248629, 0.278775, 0.534556, 0.12043213443728229, 0.246811, 0.283237, 0.535941, 0.12262205326030753, 0.244972, 0.287675, 0.53726, 0.12481141371545336, 0.243113, 0.292092, 0.538516, 0.1270013325384786, 0.241237, 0.296485, 0.539709, 0.12919125136150383, 0.239346, 0.300855, 0.540844, 0.13138061181664967, 0.237441, 0.305202, 0.541921, 0.13357053063967492, 0.235526, 0.309527, 0.542944, 0.13575989109482073, 0.233603, 0.313828, 0.543914, 0.13794980991784597, 0.231674, 0.318106, 0.544834, 0.14013917037299178, 0.229739, 0.322361, 0.545706, 0.14232908919601706, 0.227802, 0.326594, 0.546532, 0.14451900801904227, 0.225863, 0.330805, 0.547314, 0.1467083684741881, 0.223925, 0.334994, 0.548053, 0.14889828729721333, 0.221989, 0.339161, 0.548752, 0.15108764775235917, 0.220057, 0.343307, 0.549413, 0.1532775665753844, 0.21813, 0.347432, 0.550038, 0.15546692703053022, 0.21621, 0.351535, 0.550627, 0.1576568458535555, 0.214298, 0.355619, 0.551184, 0.1598467646765807, 0.212395, 0.359683, 0.55171, 0.16203612513172655, 0.210503, 0.363727, 0.552206, 0.1642260439547518, 0.208623, 0.367752, 0.552675, 0.1664154044098976, 0.206756, 0.371758, 0.553117, 0.16860532323292285, 0.204903, 0.375746, 0.553533, 0.1707946836880687, 0.203063, 0.379716, 0.553925, 0.17298460251109393, 0.201239, 0.38367, 0.554294, 0.17517396296623974, 0.19943, 0.387607, 0.554642, 0.177363881789265, 0.197636, 0.391528, 0.554969, 0.17955380061229023, 0.19586, 0.395433, 0.555276, 0.18174316106743607, 0.1941, 0.399323, 0.555565, 0.1839330798904613, 0.192357, 0.403199, 0.555836, 0.18612244034560713, 0.190631, 0.407061, 0.556089, 0.18831235916863237, 0.188923, 0.41091, 0.556326, 0.19050171962377818, 0.187231, 0.414746, 0.556547, 0.19269163844680345, 0.185556, 0.41857, 0.556753, 0.19488155726982867, 0.183898, 0.422383, 0.556944, 0.1970709177249745, 0.182256, 0.426184, 0.55712, 0.19926083654799973, 0.180629, 0.429975, 0.557282, 0.20145019700314556, 0.179019, 0.433756, 0.55743, 0.20364011582617078, 0.177423, 0.437527, 0.557565, 0.20582947628131662, 0.175841, 0.44129, 0.557685, 0.2080193951043419, 0.174274, 0.445044, 0.557792, 0.2102093139273671, 0.172719, 0.448791, 0.557885, 0.21239867438251295, 0.171176, 0.45253, 0.557965, 0.21458859320553816, 0.169646, 0.456262, 0.55803, 0.216777953660684, 0.168126, 0.459988, 0.558082, 0.21896787248370922, 0.166617, 0.463708, 0.558119, 0.22115723293885506, 0.165117, 0.467423, 0.558141, 0.22334715176188033, 0.163625, 0.471133, 0.558148, 0.22553707058490555, 0.162142, 0.474838, 0.55814, 0.22772643104005139, 0.160665, 0.47854, 0.558115, 0.2299163498630766, 0.159194, 0.482237, 0.558073, 0.23210571031822244, 0.157729, 0.485932, 0.558013, 0.23429562914124769, 0.15627, 0.489624, 0.557936, 0.23648498959639352, 0.154815, 0.493313, 0.55784, 0.23867490841941877, 0.153364, 0.497, 0.557724, 0.24086482724244399, 0.151918, 0.500685, 0.557587, 0.24305418769758982, 0.150476, 0.504369, 0.55743, 0.24524410652061507, 0.149039, 0.508051, 0.55725, 0.24743346697576088, 0.147607, 0.511733, 0.557049, 0.24962338579878612, 0.14618, 0.515413, 0.556823, 0.25181274625393196, 0.144759, 0.519093, 0.556572, 0.2540026650769572, 0.143343, 0.522773, 0.556295, 0.25619258389998245, 0.141935, 0.526453, 0.555991, 0.2583819443551283, 0.140536, 0.530132, 0.555659, 0.2605718631781535, 0.139147, 0.533812, 0.555298, 0.26276122363329935, 0.13777, 0.537492, 0.554906, 0.26495114245632456, 0.136408, 0.541173, 0.554483, 0.2671405029114704, 0.135066, 0.544853, 0.554029, 0.2693304217344956, 0.133743, 0.548535, 0.553541, 0.2715203405575209, 0.132444, 0.552216, 0.553018, 0.27370970101266673, 0.131172, 0.555899, 0.552459, 0.27589961983569194, 0.129933, 0.559582, 0.551864, 0.2780889802908378, 0.128729, 0.563265, 0.551229, 0.280278899113863, 0.127568, 0.566949, 0.550556, 0.2824682595690089, 0.126453, 0.570633, 0.549841, 0.2846581783920341, 0.125394, 0.574318, 0.549086, 0.2868475388471799, 0.124395, 0.578002, 0.548287, 0.2890374576702051, 0.123463, 0.581687, 0.547445, 0.2912273764932303, 0.122606, 0.585371, 0.546557, 0.2934167369483762, 0.121831, 0.589055, 0.545623, 0.29560665577140144, 0.121148, 0.592739, 0.544641, 0.2977960162265473, 0.120565, 0.596422, 0.543611, 0.29998593504957255, 0.120092, 0.600104, 0.54253, 0.30217529550471833, 0.119738, 0.603785, 0.5414, 0.30436521432774355, 0.119512, 0.607464, 0.540218, 0.3065551331507688, 0.119423, 0.611141, 0.538982, 0.30874449360591466, 0.119483, 0.614817, 0.537692, 0.3109344124289399, 0.119699, 0.61849, 0.536347, 0.3131237728840857, 0.120081, 0.622161, 0.534946, 0.315313691707111, 0.120638, 0.625828, 0.533488, 0.31750305216225677, 0.12138, 0.629492, 0.531973, 0.319692970985282, 0.122312, 0.633153, 0.530398, 0.32188288980830726, 0.123444, 0.636809, 0.528763, 0.3240722502634531, 0.12478, 0.640461, 0.527068, 0.3262621690864783, 0.126326, 0.644107, 0.525311, 0.32845152954162415, 0.128087, 0.647749, 0.523491, 0.3306414483646494, 0.130067, 0.651384, 0.521608, 0.3328308088197952, 0.132268, 0.655014, 0.519661, 0.3350207276428205, 0.134692, 0.658636, 0.517649, 0.3372106464658457, 0.137339, 0.662252, 0.515571, 0.33940000692099154, 0.14021, 0.665859, 0.513427, 0.34158992574401675, 0.143303, 0.669459, 0.511215, 0.3437792861991626, 0.146616, 0.67305, 0.508936, 0.34596920502218786, 0.150148, 0.676631, 0.506589, 0.34815856547733365, 0.153894, 0.680203, 0.504172, 0.3503484843003589, 0.157851, 0.683765, 0.501686, 0.35253840312338414, 0.162016, 0.687316, 0.499129, 0.35472776357853, 0.166383, 0.690856, 0.496502, 0.35691768240155525, 0.170948, 0.694384, 0.493803, 0.35910704285670103, 0.175707, 0.6979, 0.491033, 0.3612969616797263, 0.180653, 0.701402, 0.488189, 0.36348632213487214, 0.185783, 0.704891, 0.485273, 0.36567624095789736, 0.19109, 0.708366, 0.482284, 0.3678661597809226, 0.196571, 0.711827, 0.479221, 0.3700555202360684, 0.202219, 0.715272, 0.476084, 0.3722454390590937, 0.20803, 0.718701, 0.472873, 0.37443479951423947, 0.214, 0.722114, 0.469588, 0.37662471833726474, 0.220124, 0.725509, 0.466226, 0.3788140787924106, 0.226397, 0.728888, 0.462789, 0.3810039976154358, 0.232815, 0.732247, 0.459277, 0.383193916438461, 0.239374, 0.735588, 0.455688, 0.3853832768936069, 0.24607, 0.73891, 0.452024, 0.3875731957166321, 0.252899, 0.742211, 0.448284, 0.3897625561717779, 0.259857, 0.745492, 0.444467, 0.3919524749948031, 0.266941, 0.748751, 0.440573, 0.394141835449949, 0.274149, 0.751988, 0.436601, 0.39633175427297423, 0.281477, 0.755203, 0.432552, 0.3985211147281201, 0.288921, 0.758394, 0.428426, 0.40071103355114535, 0.296479, 0.761561, 0.424223, 0.40290095237417056, 0.304148, 0.764704, 0.419943, 0.40509031282931635, 0.311925, 0.767822, 0.415586, 0.40728023165234156, 0.319809, 0.770914, 0.411152, 0.40946959210748746, 0.327796, 0.77398, 0.40664, 0.4116595109305127, 0.335885, 0.777018, 0.402049, 0.41384887138565846, 0.344074, 0.780029, 0.397381, 0.4160387902086838, 0.35236, 0.783011, 0.392636, 0.418228709031709, 0.360741, 0.785964, 0.387814, 0.4204180694868548, 0.369214, 0.788888, 0.382914, 0.42260798830988, 0.377779, 0.791781, 0.377939, 0.4247973487650259, 0.386433, 0.794644, 0.372886, 0.4269872675880511, 0.395174, 0.797475, 0.367757, 0.4291766280431969, 0.404001, 0.800275, 0.362552, 0.4313665468662222, 0.412913, 0.803041, 0.357269, 0.43355646568924744, 0.421908, 0.805774, 0.35191, 0.4357458261443932, 0.430983, 0.808473, 0.346476, 0.43793574496741844, 0.440137, 0.811138, 0.340967, 0.44012510542256433, 0.449368, 0.813768, 0.335384, 0.44231502424558955, 0.458674, 0.816363, 0.329727, 0.4445043847007354, 0.468053, 0.818921, 0.323998, 0.44669430352376066, 0.477504, 0.821444, 0.318195, 0.4488842223467859, 0.487026, 0.823929, 0.312321, 0.45107358280193166, 0.496615, 0.826376, 0.306377, 0.45326350162495693, 0.506271, 0.828786, 0.300362, 0.45545286208010277, 0.515992, 0.831158, 0.294279, 0.457642780903128, 0.525776, 0.833491, 0.288127, 0.4598321413582738, 0.535621, 0.835785, 0.281908, 0.4620220601812991, 0.545524, 0.838039, 0.275626, 0.4642119790043243, 0.555484, 0.840254, 0.269281, 0.4664013394594701, 0.565498, 0.84243, 0.262877, 0.46859125828249537, 0.575563, 0.844566, 0.256415, 0.4707806187376412, 0.585678, 0.846661, 0.249897, 0.4729705375606664, 0.595839, 0.848717, 0.243329, 0.47515989801581227, 0.606045, 0.850733, 0.236712, 0.47734981683883754, 0.616293, 0.852709, 0.230052, 0.47953973566186275, 0.626579, 0.854645, 0.223353, 0.4817290961170086, 0.636902, 0.856542, 0.21662, 0.4839190149400338, 0.647257, 0.8584, 0.209861, 0.48610837539517965, 0.657642, 0.860219, 0.203082, 0.48829829421820486, 0.668054, 0.861999, 0.196293, 0.4904876546733507, 0.678489, 0.863742, 0.189503, 0.492677573496376, 0.688944, 0.865448, 0.182725, 0.4948674923194012, 0.699415, 0.867117, 0.175971, 0.49705685277454703, 0.709898, 0.868751, 0.169257, 0.49924677159757225, 0.720391, 0.87035, 0.162603, 0.5014361320527181, 0.730889, 0.871916, 0.156029, 0.5036260508757433, 0.741388, 0.873449, 0.149561, 0.5058154113308891, 0.751884, 0.874951, 0.143228, 0.5080053301539144, 0.762373, 0.876424, 0.137064, 0.5101946906090602, 0.772852, 0.877868, 0.131109, 0.5123846094320854, 0.783315, 0.879285, 0.125405, 0.5145745282551106, 0.79376, 0.880678, 0.120005, 0.5167638887102566, 0.804182, 0.882046, 0.114965, 0.5189538075332818, 0.814576, 0.883393, 0.110347, 0.5211431679884275, 0.82494, 0.88472, 0.106217, 0.5233330868114529, 0.83527, 0.886029, 0.102646, 0.5255224472665987, 0.845561, 0.887322, 0.099702, 0.5277123660896239, 0.85581, 0.888601, 0.097452, 0.5299022849126491, 0.866013, 0.889868, 0.095953, 0.532091645367795, 0.876168, 0.891125, 0.09525, 0.5342815641908202, 0.886271, 0.892374, 0.095374, 0.536470924645966, 0.89632, 0.893616, 0.096335, 0.5386608434689912, 0.906311, 0.894855, 0.098125, 0.5408502039241371, 0.916242, 0.896091, 0.100717, 0.5430401227471623, 0.926106, 0.89733, 0.104071, 0.5452300415701876, 0.935904, 0.89857, 0.108131, 0.5474194020253335, 0.945636, 0.899815, 0.112838, 0.5496093208483587, 0.9553, 0.901065, 0.118128, 0.5517986813035045, 0.964894, 0.902323, 0.123941, 0.5539886001265297, 0.974417, 0.90359, 0.130215, 0.5561779605816756, 0.983868, 0.904867, 0.136897, 0.5583678794047008, 0.993248, 0.906157, 0.143936]
    velocity_LUT.NanColor = [1.0, 0.0, 0.0]
    velocity_LUT.ScalarRangeInitialized = 1.0
    
    # get opacity transfer function/opacity map for 'velocity_'
    velocity_PWF = GetOpacityTransferFunction('velocity_')
    velocity_PWF.Points = [0.0, 0.0, 0.5, 0.0, 0.5583678794047008, 1.0, 0.5, 0.0]
    velocity_PWF.ScalarRangeInitialized = 1
    
    # trace defaults for the display properties.
    ghostCellsGenerator1Display.Representation = 'Volume'
    ghostCellsGenerator1Display.ColorArrayName = ['POINTS', 'velocity_']
    ghostCellsGenerator1Display.LookupTable = velocity_LUT
    ghostCellsGenerator1Display.SelectTCoordArray = 'None'
    ghostCellsGenerator1Display.SelectNormalArray = 'None'
    ghostCellsGenerator1Display.SelectTangentArray = 'None'
    ghostCellsGenerator1Display.OSPRayScaleArray = 'GlobalNodeId'
    ghostCellsGenerator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    ghostCellsGenerator1Display.SelectOrientationVectors = 'None'
    ghostCellsGenerator1Display.ScaleFactor = 0.030136987566947937
    ghostCellsGenerator1Display.SelectScaleArray = 'GlobalNodeId'
    ghostCellsGenerator1Display.GlyphType = 'Arrow'
    ghostCellsGenerator1Display.GlyphTableIndexArray = 'GlobalNodeId'
    ghostCellsGenerator1Display.GaussianRadius = 0.0015068493783473968
    ghostCellsGenerator1Display.SetScaleArray = ['POINTS', 'GlobalNodeId']
    ghostCellsGenerator1Display.ScaleTransferFunction = 'PiecewiseFunction'
    ghostCellsGenerator1Display.OpacityArray = ['POINTS', 'GlobalNodeId']
    ghostCellsGenerator1Display.OpacityTransferFunction = 'PiecewiseFunction'
    ghostCellsGenerator1Display.DataAxesGrid = 'GridAxesRepresentation'
    ghostCellsGenerator1Display.PolarAxes = 'PolarAxesRepresentation'
    ghostCellsGenerator1Display.ScalarOpacityFunction = velocity_PWF
    ghostCellsGenerator1Display.ScalarOpacityUnitDistance = 0.015062372960425148
    ghostCellsGenerator1Display.OpacityArrayName = ['POINTS', 'GlobalNodeId']
    ghostCellsGenerator1Display.SelectMapper = 'Resample To Image'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    ghostCellsGenerator1Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    ghostCellsGenerator1Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 35532.0, 1.0, 0.5, 0.0]
    
    # setup the color legend parameters for each legend in this view
    
    # get color legend/bar for vtkBlockColorsLUT in view renderView1
    vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
    vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
    vtkBlockColorsLUTColorBar.ComponentTitle = ''
    
    # set color bar visibility
    vtkBlockColorsLUTColorBar.Visibility = 0
    
    # get color legend/bar for velocity_LUT in view renderView1
    velocity_LUTColorBar = GetScalarBar(velocity_LUT, renderView1)
    velocity_LUTColorBar.Title = 'velocity_'
    velocity_LUTColorBar.ComponentTitle = 'Magnitude'
    
    # set color bar visibility
    velocity_LUTColorBar.Visibility = 1
    
    # hide data in view
    Hide(nonIsoEdgeOpenJete4, renderView1)
    
    # show color legend
    ghostCellsGenerator1Display.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(ghostCellsGenerator1)
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------
    
    # create extractor
    pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
    # trace defaults for the extractor.
    # init the 'PNG' selected for 'Writer'
    pNG1.Writer.FileName = 'RenderView1_%.6ts%cm.png'
    pNG1.Writer.ImageResolution = [1000, 1000]
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
