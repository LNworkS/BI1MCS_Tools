import bpy
from ..functions.get_materials import get_materials

def spherical_normal_node_group(obj):
    """Initialize spherical_normal node group"""
    spherical_normal = bpy.data.node_groups.new(type='GeometryNodeTree', name=obj.name + '_SN')

    spherical_normal.color_tag = 'NONE'
    spherical_normal.description = ""
    spherical_normal.default_group_node_width = 140
    spherical_normal.is_modifier = True

    # spherical_normal interface

    # Socket Geometry
    geometry_socket = spherical_normal.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = spherical_normal.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Material
    material_var = get_materials(obj, True)[0]
    material_socket = spherical_normal.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'
    material_socket.default_value = material_var

    # Socket Voxel Amount
    voxel_amount_socket = spherical_normal.interface.new_socket(name="Voxel Amount", in_out='INPUT', socket_type='NodeSocketFloat')
    voxel_amount_socket.default_value = 20.0
    voxel_amount_socket.min_value = 0.0
    voxel_amount_socket.max_value = 3.4028234663852886e+38
    voxel_amount_socket.subtype = 'NONE'
    voxel_amount_socket.attribute_domain = 'POINT'
    voxel_amount_socket.default_input = 'VALUE'
    voxel_amount_socket.structure_type = 'AUTO'

    # Socket Voxel Scale
    voxel_scale_socket = spherical_normal.interface.new_socket(name="Voxel Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    voxel_scale_socket.default_value = 0.0
    voxel_scale_socket.min_value = -10000.0
    voxel_scale_socket.max_value = 10000.0
    voxel_scale_socket.subtype = 'NONE'
    voxel_scale_socket.attribute_domain = 'POINT'
    voxel_scale_socket.default_input = 'VALUE'
    voxel_scale_socket.structure_type = 'AUTO'

    # Initialize spherical_normal nodes

    # Node Group Input
    group_input = spherical_normal.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = spherical_normal.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Mesh to Volume
    mesh_to_volume = spherical_normal.nodes.new("GeometryNodeMeshToVolume")
    mesh_to_volume.name = "Mesh to Volume"
    mesh_to_volume.resolution_mode = 'VOXEL_AMOUNT'
    # Density
    mesh_to_volume.inputs[1].default_value = 64.0
    # Interior Band Width
    mesh_to_volume.inputs[4].default_value = 0.20000000298023224

    # Node Volume to Mesh
    volume_to_mesh = spherical_normal.nodes.new("GeometryNodeVolumeToMesh")
    volume_to_mesh.name = "Volume to Mesh"
    volume_to_mesh.resolution_mode = 'GRID'
    # Threshold
    volume_to_mesh.inputs[3].default_value = 0.10000000149011612
    # Adaptivity
    volume_to_mesh.inputs[4].default_value = 0.0

    # Node Set Shade Smooth
    set_shade_smooth = spherical_normal.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # Node Capture Attribute
    capture_attribute = spherical_normal.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Normal")
    capture_attribute.capture_items["Normal"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'POINT'

    # Node Normal
    normal = spherical_normal.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    # Node Sample Nearest Surface
    sample_nearest_surface = spherical_normal.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    # Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    # Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    # Node Set Position
    set_position = spherical_normal.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Normal.001
    normal_001 = spherical_normal.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    normal_001.legacy_corner_normals = False

    # Node Vector Math.001
    vector_math_001 = spherical_normal.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SCALE'

    # Node Self Object
    self_object = spherical_normal.nodes.new("GeometryNodeSelfObject")
    self_object.name = "Self Object"

    # Node Object Info
    object_info = spherical_normal.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'ORIGINAL'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Math
    math = spherical_normal.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'DIVIDE'
    math.use_clamp = False

    # Node Set Mesh Normal
    set_mesh_normal = spherical_normal.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.domain = 'POINT'
    set_mesh_normal.mode = 'FREE'

    # Node Material Selection
    material_selection = spherical_normal.nodes.new("GeometryNodeMaterialSelection")
    material_selection.name = "Material Selection"

    # Node Separate Geometry
    separate_geometry = spherical_normal.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = 'FACE'

    # Node Reroute
    reroute = spherical_normal.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.002
    reroute_002 = spherical_normal.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Join Geometry
    join_geometry = spherical_normal.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Reroute.001
    reroute_001 = spherical_normal.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketGeometry"
    # Node Vector Math.002
    vector_math_002 = spherical_normal.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'DIVIDE'
    # Vector
    vector_math_002.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Vector_001
    vector_math_002.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Set locations
    group_input.location = (-575.9725341796875, -94.01644134521484)
    group_output.location = (1607.9554443359375, -70.9855728149414)
    mesh_to_volume.location = (43.95623016357422, -116.74063873291016)
    volume_to_mesh.location = (284.0648498535156, -117.3414306640625)
    set_shade_smooth.location = (687.4033813476562, -120.7561264038086)
    capture_attribute.location = (874.5814208984375, -123.78326416015625)
    normal.location = (689.4075317382812, -252.24679565429688)
    sample_nearest_surface.location = (1054.4169921875, -123.5376205444336)
    set_position.location = (503.54010009765625, -118.18453216552734)
    normal_001.location = (129.6200714111328, -327.3133850097656)
    vector_math_001.location = (307.43865966796875, -275.29083251953125)
    self_object.location = (-232.7079620361328, -679.1368408203125)
    object_info.location = (-57.820106506347656, -544.0846557617188)
    math.location = (131.13229370117188, -413.4574279785156)
    set_mesh_normal.location = (1253.0665283203125, 22.40302085876465)
    material_selection.location = (-369.6351013183594, -144.2990264892578)
    separate_geometry.location = (-199.38050842285156, -24.342615127563477)
    reroute.location = (-371.1038513183594, -242.91061401367188)
    reroute_002.location = (-321.05108642578125, -521.8630981445312)
    join_geometry.location = (1429.03564453125, -72.3327865600586)
    reroute_001.location = (36.58662033081055, -104.10609436035156)
    vector_math_002.location = (507.13824462890625, -394.19317626953125)

    # Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    mesh_to_volume.width, mesh_to_volume.height = 200.0, 100.0
    volume_to_mesh.width, volume_to_mesh.height = 170.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 150.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    self_object.width, self_object.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    set_mesh_normal.width, set_mesh_normal.height = 140.0, 100.0
    material_selection.width, material_selection.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    reroute.width, reroute.height = 12.5, 100.0
    reroute_002.width, reroute_002.height = 12.5, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 12.5, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0

    # Initialize spherical_normal links

    # mesh_to_volume.Volume -> volume_to_mesh.Volume
    spherical_normal.links.new(mesh_to_volume.outputs[0], volume_to_mesh.inputs[0])
    # set_shade_smooth.Geometry -> capture_attribute.Geometry
    spherical_normal.links.new(set_shade_smooth.outputs[0], capture_attribute.inputs[0])
    # normal_001.Normal -> vector_math_001.Vector
    spherical_normal.links.new(normal_001.outputs[0], vector_math_001.inputs[0])
    # self_object.Self Object -> object_info.Object
    spherical_normal.links.new(self_object.outputs[0], object_info.inputs[0])
    # vector_math_001.Vector -> set_position.Offset
    spherical_normal.links.new(vector_math_001.outputs[0], set_position.inputs[3])
    # object_info.Scale -> math.Value
    spherical_normal.links.new(object_info.outputs[3], math.inputs[1])
    # math.Value -> vector_math_001.Scale
    spherical_normal.links.new(math.outputs[0], vector_math_001.inputs[3])
    # volume_to_mesh.Mesh -> set_position.Geometry
    spherical_normal.links.new(volume_to_mesh.outputs[0], set_position.inputs[0])
    # set_position.Geometry -> set_shade_smooth.Geometry
    spherical_normal.links.new(set_position.outputs[0], set_shade_smooth.inputs[0])
    # normal.Normal -> capture_attribute.Normal
    spherical_normal.links.new(normal.outputs[0], capture_attribute.inputs[1])
    # capture_attribute.Geometry -> sample_nearest_surface.Mesh
    spherical_normal.links.new(capture_attribute.outputs[0], sample_nearest_surface.inputs[0])
    # capture_attribute.Normal -> sample_nearest_surface.Value
    spherical_normal.links.new(capture_attribute.outputs[1], sample_nearest_surface.inputs[1])
    # sample_nearest_surface.Value -> set_mesh_normal.Custom Normal
    spherical_normal.links.new(sample_nearest_surface.outputs[0], set_mesh_normal.inputs[1])
    # group_input.Geometry -> separate_geometry.Geometry
    spherical_normal.links.new(group_input.outputs[0], separate_geometry.inputs[0])
    # material_selection.Selection -> separate_geometry.Selection
    spherical_normal.links.new(material_selection.outputs[0], separate_geometry.inputs[1])
    # group_input.Material -> material_selection.Material
    spherical_normal.links.new(group_input.outputs[1], material_selection.inputs[0])
    # separate_geometry.Selection -> mesh_to_volume.Mesh
    spherical_normal.links.new(separate_geometry.outputs[0], mesh_to_volume.inputs[0])
    # group_input.Voxel Amount -> reroute.Input
    spherical_normal.links.new(group_input.outputs[2], reroute.inputs[0])
    # group_input.Voxel Scale -> reroute_002.Input
    spherical_normal.links.new(group_input.outputs[3], reroute_002.inputs[0])
    # separate_geometry.Selection -> set_mesh_normal.Mesh
    spherical_normal.links.new(separate_geometry.outputs[0], set_mesh_normal.inputs[0])
    # reroute.Output -> mesh_to_volume.Voxel Amount
    spherical_normal.links.new(reroute.outputs[0], mesh_to_volume.inputs[3])
    # reroute_001.Output -> join_geometry.Geometry
    spherical_normal.links.new(reroute_001.outputs[0], join_geometry.inputs[0])
    # separate_geometry.Inverted -> reroute_001.Input
    spherical_normal.links.new(separate_geometry.outputs[1], reroute_001.inputs[0])
    # join_geometry.Geometry -> group_output.Geometry
    spherical_normal.links.new(join_geometry.outputs[0], group_output.inputs[0])
    # reroute_002.Output -> math.Value
    spherical_normal.links.new(reroute_002.outputs[0], math.inputs[0])
    # set_mesh_normal.Mesh -> join_geometry.Geometry
    spherical_normal.links.new(set_mesh_normal.outputs[0], join_geometry.inputs[0])

    return spherical_normal
