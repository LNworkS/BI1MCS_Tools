import bpy
import mathutils


def netwall01_node_group():
    """Initialize geometry_nodes node group"""
    geometry_nodes = bpy.data.node_groups.new(type='GeometryNodeTree', name="Geometry Nodes")

    geometry_nodes.color_tag = 'NONE'
    geometry_nodes.description = ""
    geometry_nodes.default_group_node_width = 140
    geometry_nodes.is_modifier = True

    # geometry_nodes interface

    # Socket Geometry
    geometry_socket = geometry_nodes.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = geometry_nodes.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket net - line radius
    net___line_radius_socket = geometry_nodes.interface.new_socket(name="net - line radius", in_out='INPUT', socket_type='NodeSocketFloat')
    net___line_radius_socket.default_value = 0.05000000074505806
    net___line_radius_socket.min_value = 0.0010000000474974513
    net___line_radius_socket.max_value = 10000.0
    net___line_radius_socket.subtype = 'NONE'
    net___line_radius_socket.attribute_domain = 'POINT'
    net___line_radius_socket.default_input = 'VALUE'
    net___line_radius_socket.structure_type = 'AUTO'

    # Socket net - line section segment
    net___line_section_segment_socket = geometry_nodes.interface.new_socket(name="net - line section segment", in_out='INPUT', socket_type='NodeSocketInt')
    net___line_section_segment_socket.default_value = 4
    net___line_section_segment_socket.min_value = 3
    net___line_section_segment_socket.max_value = 512
    net___line_section_segment_socket.subtype = 'NONE'
    net___line_section_segment_socket.attribute_domain = 'POINT'
    net___line_section_segment_socket.description = "Number of points on the circle"
    net___line_section_segment_socket.default_input = 'VALUE'
    net___line_section_segment_socket.structure_type = 'AUTO'

    # Socket net - line segment
    net___line_segment_socket = geometry_nodes.interface.new_socket(name="net - line segment", in_out='INPUT', socket_type='NodeSocketInt')
    net___line_segment_socket.default_value = 8
    net___line_segment_socket.min_value = 3
    net___line_segment_socket.max_value = 256
    net___line_segment_socket.attribute_domain = 'POINT'
    net___line_segment_socket.description = "The number of evaluated points on the curve"
    net___line_segment_socket.default_input = 'VALUE'
    net___line_segment_socket.structure_type = 'AUTO'

    # Socket net - line merge factor
    net___line_merge_factor_socket = geometry_nodes.interface.new_socket(name="net - line merge factor", in_out='INPUT', socket_type='NodeSocketFloat')
    net___line_merge_factor_socket.default_value = 0.014999999664723873
    net___line_merge_factor_socket.min_value = 0.0
    net___line_merge_factor_socket.max_value = 3.4028234663852886e+38
    net___line_merge_factor_socket.subtype = 'NONE'
    net___line_merge_factor_socket.attribute_domain = 'POINT'
    net___line_merge_factor_socket.default_input = 'VALUE'
    net___line_merge_factor_socket.structure_type = 'AUTO'

    # Socket net - line bend X
    net___line_bend_x_socket = geometry_nodes.interface.new_socket(name="net - line bend X", in_out='INPUT', socket_type='NodeSocketFloat')
    net___line_bend_x_socket.default_value = 0.07000000029802322
    net___line_bend_x_socket.min_value = 0.0
    net___line_bend_x_socket.max_value = 10000.0
    net___line_bend_x_socket.subtype = 'NONE'
    net___line_bend_x_socket.attribute_domain = 'POINT'
    net___line_bend_x_socket.default_input = 'VALUE'
    net___line_bend_x_socket.structure_type = 'AUTO'

    # Socket net - line bend Y
    net___line_bend_y_socket = geometry_nodes.interface.new_socket(name="net - line bend Y", in_out='INPUT', socket_type='NodeSocketFloat')
    net___line_bend_y_socket.default_value = 0.35499998927116394
    net___line_bend_y_socket.min_value = 0.0
    net___line_bend_y_socket.max_value = 10000.0
    net___line_bend_y_socket.subtype = 'NONE'
    net___line_bend_y_socket.attribute_domain = 'POINT'
    net___line_bend_y_socket.default_input = 'VALUE'
    net___line_bend_y_socket.structure_type = 'AUTO'

    # Socket net - line bend Z
    net___line_bend_z_socket = geometry_nodes.interface.new_socket(name="net - line bend Z", in_out='INPUT', socket_type='NodeSocketFloat')
    net___line_bend_z_socket.default_value = 0.17000000178813934
    net___line_bend_z_socket.min_value = 0.0
    net___line_bend_z_socket.max_value = 10000.0
    net___line_bend_z_socket.subtype = 'NONE'
    net___line_bend_z_socket.attribute_domain = 'POINT'
    net___line_bend_z_socket.default_input = 'VALUE'
    net___line_bend_z_socket.structure_type = 'AUTO'

    # Socket net - line amount X
    net___line_amount_x_socket = geometry_nodes.interface.new_socket(name="net - line amount X", in_out='INPUT', socket_type='NodeSocketInt')
    net___line_amount_x_socket.default_value = 30
    net___line_amount_x_socket.min_value = 2
    net___line_amount_x_socket.max_value = 2147483647
    net___line_amount_x_socket.subtype = 'NONE'
    net___line_amount_x_socket.attribute_domain = 'POINT'
    net___line_amount_x_socket.default_input = 'VALUE'
    net___line_amount_x_socket.structure_type = 'AUTO'

    # Socket net - line amount Y
    net___line_amount_y_socket = geometry_nodes.interface.new_socket(name="net - line amount Y", in_out='INPUT', socket_type='NodeSocketInt')
    net___line_amount_y_socket.default_value = 20
    net___line_amount_y_socket.min_value = 2
    net___line_amount_y_socket.max_value = 2147483647
    net___line_amount_y_socket.subtype = 'NONE'
    net___line_amount_y_socket.attribute_domain = 'POINT'
    net___line_amount_y_socket.default_input = 'VALUE'
    net___line_amount_y_socket.structure_type = 'AUTO'

    # Socket border - radius
    border___radius_socket = geometry_nodes.interface.new_socket(name="border - radius", in_out='INPUT', socket_type='NodeSocketFloat')
    border___radius_socket.default_value = 0.30000001192092896
    border___radius_socket.min_value = 0.009999999776482582
    border___radius_socket.max_value = 3.4028234663852886e+38
    border___radius_socket.subtype = 'NONE'
    border___radius_socket.attribute_domain = 'POINT'
    border___radius_socket.description = "Distance of the points from the origin"
    border___radius_socket.default_input = 'VALUE'
    border___radius_socket.structure_type = 'AUTO'

    # Socket border - section segment
    border___section_segment_socket = geometry_nodes.interface.new_socket(name="border - section segment", in_out='INPUT', socket_type='NodeSocketInt')
    border___section_segment_socket.default_value = 8
    border___section_segment_socket.min_value = 3
    border___section_segment_socket.max_value = 512
    border___section_segment_socket.subtype = 'NONE'
    border___section_segment_socket.attribute_domain = 'POINT'
    border___section_segment_socket.description = "Number of points on the circle"
    border___section_segment_socket.default_input = 'VALUE'
    border___section_segment_socket.structure_type = 'AUTO'

    # Socket border - bevel segment
    border___bevel_segment_socket = geometry_nodes.interface.new_socket(name="border - bevel segment", in_out='INPUT', socket_type='NodeSocketInt')
    border___bevel_segment_socket.default_value = 5
    border___bevel_segment_socket.min_value = 2
    border___bevel_segment_socket.max_value = 256
    border___bevel_segment_socket.attribute_domain = 'POINT'
    border___bevel_segment_socket.description = "The number of evaluated points on the curve"
    border___bevel_segment_socket.default_input = 'VALUE'
    border___bevel_segment_socket.structure_type = 'AUTO'

    # Socket border - bevel factor
    border___bevel_factor_socket = geometry_nodes.interface.new_socket(name="border - bevel factor", in_out='INPUT', socket_type='NodeSocketFloat')
    border___bevel_factor_socket.default_value = 0.5
    border___bevel_factor_socket.min_value = 0.0
    border___bevel_factor_socket.max_value = 10000.0
    border___bevel_factor_socket.subtype = 'NONE'
    border___bevel_factor_socket.attribute_domain = 'POINT'
    border___bevel_factor_socket.default_input = 'VALUE'
    border___bevel_factor_socket.structure_type = 'AUTO'

    # Socket border - merge factor
    border___merge_factor_socket = geometry_nodes.interface.new_socket(name="border - merge factor", in_out='INPUT', socket_type='NodeSocketFloat')
    border___merge_factor_socket.default_value = 0.014999999664723873
    border___merge_factor_socket.min_value = 0.0
    border___merge_factor_socket.max_value = 3.4028234663852886e+38
    border___merge_factor_socket.subtype = 'NONE'
    border___merge_factor_socket.attribute_domain = 'POINT'
    border___merge_factor_socket.default_input = 'VALUE'
    border___merge_factor_socket.structure_type = 'AUTO'

    # Socket connect - width
    connect___width_socket = geometry_nodes.interface.new_socket(name="connect - width", in_out='INPUT', socket_type='NodeSocketFloat')
    connect___width_socket.default_value = 0.5
    connect___width_socket.min_value = 0.009999999776482582
    connect___width_socket.max_value = 10000.0
    connect___width_socket.subtype = 'NONE'
    connect___width_socket.attribute_domain = 'POINT'
    connect___width_socket.default_input = 'VALUE'
    connect___width_socket.structure_type = 'AUTO'

    # Socket connect - amount
    connect___amount_socket = geometry_nodes.interface.new_socket(name="connect - amount", in_out='INPUT', socket_type='NodeSocketInt')
    connect___amount_socket.default_value = 3
    connect___amount_socket.min_value = 2
    connect___amount_socket.max_value = 2147483647
    connect___amount_socket.subtype = 'NONE'
    connect___amount_socket.attribute_domain = 'POINT'
    connect___amount_socket.default_input = 'VALUE'
    connect___amount_socket.structure_type = 'AUTO'

    # Socket connect - offset
    connect___offset_socket = geometry_nodes.interface.new_socket(name="connect - offset", in_out='INPUT', socket_type='NodeSocketFloat')
    connect___offset_socket.default_value = 0.44999998807907104
    connect___offset_socket.min_value = 0.0
    connect___offset_socket.max_value = 10000.0
    connect___offset_socket.subtype = 'NONE'
    connect___offset_socket.attribute_domain = 'POINT'
    connect___offset_socket.default_input = 'VALUE'
    connect___offset_socket.structure_type = 'AUTO'

    # Socket height above ground
    height_above_ground_socket = geometry_nodes.interface.new_socket(name="height above ground", in_out='INPUT', socket_type='NodeSocketFloat')
    height_above_ground_socket.default_value = 1.0
    height_above_ground_socket.min_value = 0.0
    height_above_ground_socket.max_value = 10000.0
    height_above_ground_socket.subtype = 'NONE'
    height_above_ground_socket.attribute_domain = 'POINT'
    height_above_ground_socket.default_input = 'VALUE'
    height_above_ground_socket.structure_type = 'AUTO'

    # Socket pillar - radius
    pillar___radius_socket = geometry_nodes.interface.new_socket(name="pillar - radius", in_out='INPUT', socket_type='NodeSocketFloat')
    pillar___radius_socket.default_value = 0.6499999761581421
    pillar___radius_socket.min_value = 0.009999999776482582
    pillar___radius_socket.max_value = 3.4028234663852886e+38
    pillar___radius_socket.subtype = 'NONE'
    pillar___radius_socket.attribute_domain = 'POINT'
    pillar___radius_socket.description = "The radius of the cylinder"
    pillar___radius_socket.default_input = 'VALUE'
    pillar___radius_socket.structure_type = 'AUTO'

    # Socket pillar - section segment
    pillar___section_segment_socket = geometry_nodes.interface.new_socket(name="pillar - section segment", in_out='INPUT', socket_type='NodeSocketInt')
    pillar___section_segment_socket.default_value = 8
    pillar___section_segment_socket.min_value = 3
    pillar___section_segment_socket.max_value = 512
    pillar___section_segment_socket.subtype = 'NONE'
    pillar___section_segment_socket.attribute_domain = 'POINT'
    pillar___section_segment_socket.description = "The number of vertices on the top and bottom circles"
    pillar___section_segment_socket.default_input = 'VALUE'
    pillar___section_segment_socket.structure_type = 'AUTO'

    # Socket overall height
    overall_height_socket = geometry_nodes.interface.new_socket(name="overall height", in_out='INPUT', socket_type='NodeSocketFloat')
    overall_height_socket.default_value = 2.0
    overall_height_socket.min_value = 0.10000000149011612
    overall_height_socket.max_value = 10000.0
    overall_height_socket.subtype = 'DISTANCE'
    overall_height_socket.attribute_domain = 'POINT'
    overall_height_socket.default_input = 'VALUE'
    overall_height_socket.structure_type = 'AUTO'

    # Socket overall amount
    overall_amount_socket = geometry_nodes.interface.new_socket(name="overall amount", in_out='INPUT', socket_type='NodeSocketInt')
    overall_amount_socket.default_value = 3
    overall_amount_socket.min_value = 1
    overall_amount_socket.max_value = 100000
    overall_amount_socket.subtype = 'NONE'
    overall_amount_socket.attribute_domain = 'POINT'
    overall_amount_socket.default_input = 'VALUE'
    overall_amount_socket.structure_type = 'AUTO'

    # Initialize geometry_nodes nodes

    # Node Group Input
    group_input = geometry_nodes.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = geometry_nodes.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Bézier Segment
    b_zier_segment = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    b_zier_segment.name = "Bézier Segment"
    b_zier_segment.mode = 'POSITION'

    # Node Combine XYZ
    combine_xyz = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # Y
    combine_xyz.inputs[1].default_value = 1.0
    # Z
    combine_xyz.inputs[2].default_value = 0.0

    # Node Combine XYZ.001
    combine_xyz_001 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0
    # Z
    combine_xyz_001.inputs[2].default_value = 0.0

    # Node Math
    math = geometry_nodes.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value
    math.inputs[0].default_value = 0.0

    # Node Math.001
    math_001 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    # Value
    math_001.inputs[0].default_value = 1.0

    # Node Combine XYZ.002
    combine_xyz_002 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"

    # Node Math.002
    math_002 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'SUBTRACT'
    math_002.use_clamp = False
    # Value
    math_002.inputs[0].default_value = 1.0

    # Node Combine XYZ.003
    combine_xyz_003 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"

    # Node Math.003
    math_003 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'ADD'
    math_003.use_clamp = False
    # Value
    math_003.inputs[0].default_value = 0.0

    # Node Math.004
    math_004 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = -1.0

    # Node Bézier Segment.001
    b_zier_segment_001 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    b_zier_segment_001.name = "Bézier Segment.001"
    b_zier_segment_001.mode = 'POSITION'

    # Node Combine XYZ.004
    combine_xyz_004 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"

    # Node Join Geometry.002
    join_geometry_002 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    # Node Combine XYZ.005
    combine_xyz_005 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"

    # Node Combine XYZ.006
    combine_xyz_006 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    # Y
    combine_xyz_006.inputs[1].default_value = -1.0
    # Z
    combine_xyz_006.inputs[2].default_value = 0.0

    # Node Math.005
    math_005 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    # Value_001
    math_005.inputs[1].default_value = -1.0

    # Node Math.006
    math_006 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = -1.0

    # Node Transform Geometry.002
    transform_geometry_002 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 3.1415927410125732)
    # Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry.003
    join_geometry_003 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"

    # Node Curve Circle.001
    curve_circle_001 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle_001.name = "Curve Circle.001"
    curve_circle_001.mode = 'RADIUS'

    # Node Group Input.003
    group_input_003 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"

    # Node Curve to Mesh.001
    curve_to_mesh_001 = geometry_nodes.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    # Scale
    curve_to_mesh_001.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh_001.inputs[3].default_value = False

    # Node Merge by Distance.001
    merge_by_distance_001 = geometry_nodes.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = 'ALL'
    # Selection
    merge_by_distance_001.inputs[1].default_value = True

    # Node Math.007
    math_007 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False
    # Value
    math_007.inputs[0].default_value = 0.0

    # Node Math.008
    math_008 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'ADD'
    math_008.use_clamp = False
    # Value
    math_008.inputs[0].default_value = 1.0

    # Node Bézier Segment.002
    b_zier_segment_002 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    b_zier_segment_002.name = "Bézier Segment.002"
    b_zier_segment_002.mode = 'POSITION'

    # Node Join Geometry
    join_geometry = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Group Input.004
    group_input_004 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"

    # Node Math.009
    math_009 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'SUBTRACT'
    math_009.use_clamp = False
    # Value
    math_009.inputs[0].default_value = -1.0

    # Node Math.010
    math_010 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False
    # Value_001
    math_010.inputs[1].default_value = 2.0

    # Node Combine XYZ.007
    combine_xyz_007 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    # Z
    combine_xyz_007.inputs[2].default_value = 0.0

    # Node Combine XYZ.008
    combine_xyz_008 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.name = "Combine XYZ.008"
    # Y
    combine_xyz_008.inputs[1].default_value = -1.0
    # Z
    combine_xyz_008.inputs[2].default_value = 0.0

    # Node Math.011
    math_011 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'SUBTRACT'
    math_011.use_clamp = False
    # Value_001
    math_011.inputs[1].default_value = 1.0

    # Node Math.012
    math_012 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = 'SUBTRACT'
    math_012.use_clamp = False

    # Node Math.013
    math_013 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'DIVIDE'
    math_013.use_clamp = False
    # Value_001
    math_013.inputs[1].default_value = -2.0

    # Node Combine XYZ.009
    combine_xyz_009 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_009.name = "Combine XYZ.009"
    # Z
    combine_xyz_009.inputs[2].default_value = 0.0

    # Node Combine XYZ.010
    combine_xyz_010 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_010.name = "Combine XYZ.010"
    # Y
    combine_xyz_010.inputs[1].default_value = -1.0
    # Z
    combine_xyz_010.inputs[2].default_value = 0.0

    # Node Math.014
    math_014 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'SUBTRACT'
    math_014.use_clamp = False
    # Value
    math_014.inputs[0].default_value = -1.0

    # Node Math.015
    math_015 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'SUBTRACT'
    math_015.use_clamp = False

    # Node Transform Geometry
    transform_geometry = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[3].default_value = (-1.0, 1.0, 1.0)

    # Node Group Input.005
    group_input_005 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"

    # Node Math.016
    math_016 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False
    # Value_001
    math_016.inputs[1].default_value = 2.0

    # Node Combine XYZ.011
    combine_xyz_011 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_011.name = "Combine XYZ.011"
    # Y
    combine_xyz_011.inputs[1].default_value = 0.0
    # Z
    combine_xyz_011.inputs[2].default_value = 0.0

    # Node Join Geometry.001
    join_geometry_001 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    # Node Transform Geometry.001
    transform_geometry_001 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, -1.0, 1.0)

    # Node Combine XYZ.012
    combine_xyz_012 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_012.name = "Combine XYZ.012"
    # X
    combine_xyz_012.inputs[0].default_value = 0.0
    # Z
    combine_xyz_012.inputs[2].default_value = 0.0

    # Node Join Geometry.006
    join_geometry_006 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_006.name = "Join Geometry.006"

    # Node Math.017
    math_017 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = 'MULTIPLY'
    math_017.use_clamp = False
    # Value_001
    math_017.inputs[1].default_value = 2.0

    # Node Curve Line
    curve_line = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'POINTS'

    # Node Group Input.006
    group_input_006 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"

    # Node Math.018
    math_018 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'MULTIPLY'
    math_018.use_clamp = False
    # Value_001
    math_018.inputs[1].default_value = 2.0

    # Node Curve Line.001
    curve_line_001 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_001.name = "Curve Line.001"
    curve_line_001.mode = 'POINTS'

    # Node Combine XYZ.013
    combine_xyz_013 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_013.name = "Combine XYZ.013"
    # Z
    combine_xyz_013.inputs[2].default_value = 0.0

    # Node Join Geometry.007
    join_geometry_007 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_007.name = "Join Geometry.007"

    # Node Math.021
    math_021 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.operation = 'ADD'
    math_021.use_clamp = False

    # Node Combine XYZ.014
    combine_xyz_014 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_014.name = "Combine XYZ.014"
    # Y
    combine_xyz_014.inputs[1].default_value = -1.0
    # Z
    combine_xyz_014.inputs[2].default_value = 0.0

    # Node Math.022
    math_022 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.operation = 'ADD'
    math_022.use_clamp = False

    # Node Math.023
    math_023 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.operation = 'MULTIPLY'
    math_023.use_clamp = False
    # Value_001
    math_023.inputs[1].default_value = 2.0

    # Node Math.024
    math_024 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.operation = 'SUBTRACT'
    math_024.use_clamp = False
    # Value
    math_024.inputs[0].default_value = 1.0

    # Node Math.025
    math_025 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.operation = 'ADD'
    math_025.use_clamp = False

    # Node Transform Geometry.005
    transform_geometry_005 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_005.name = "Transform Geometry.005"
    transform_geometry_005.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry.008
    join_geometry_008 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_008.name = "Join Geometry.008"

    # Node Group Input.007
    group_input_007 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"

    # Node Math.019
    math_019 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'MULTIPLY'
    math_019.use_clamp = False
    # Value_001
    math_019.inputs[1].default_value = 2.0

    # Node Combine XYZ.015
    combine_xyz_015 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_015.name = "Combine XYZ.015"
    # Y
    combine_xyz_015.inputs[1].default_value = 0.0
    # Z
    combine_xyz_015.inputs[2].default_value = 0.0

    # Node Math.020
    math_020 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = 'ADD'
    math_020.use_clamp = False
    # Value_001
    math_020.inputs[1].default_value = 1.0

    # Node Math.026
    math_026 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.operation = 'ADD'
    math_026.use_clamp = False

    # Node Math.027
    math_027 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.operation = 'MULTIPLY'
    math_027.use_clamp = False
    # Value_001
    math_027.inputs[1].default_value = 4.0

    # Node Join Geometry.009
    join_geometry_009 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_009.name = "Join Geometry.009"

    # Node Transform Geometry.006
    transform_geometry_006 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_006.name = "Transform Geometry.006"
    transform_geometry_006.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_006.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_006.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Group Input.008
    group_input_008 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"

    # Node Math.028
    math_028 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.operation = 'MULTIPLY'
    math_028.use_clamp = False
    # Value_001
    math_028.inputs[1].default_value = 2.0

    # Node Combine XYZ.016
    combine_xyz_016 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_016.name = "Combine XYZ.016"
    # X
    combine_xyz_016.inputs[0].default_value = 0.0
    # Z
    combine_xyz_016.inputs[2].default_value = 0.0

    # Node Math.029
    math_029 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.operation = 'ADD'
    math_029.use_clamp = False
    # Value_001
    math_029.inputs[1].default_value = 1.0

    # Node Join Geometry.010
    join_geometry_010 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_010.name = "Join Geometry.010"

    # Node Curve to Mesh
    curve_to_mesh = geometry_nodes.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    # Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    # Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    # Node Curve Circle.002
    curve_circle_002 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle_002.name = "Curve Circle.002"
    curve_circle_002.mode = 'RADIUS'

    # Node Group Input.009
    group_input_009 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"

    # Node Merge by Distance.002
    merge_by_distance_002 = geometry_nodes.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.mode = 'ALL'
    # Selection
    merge_by_distance_002.inputs[1].default_value = True

    # Node Cube
    cube = geometry_nodes.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    # Vertices X
    cube.inputs[1].default_value = 2
    # Vertices Y
    cube.inputs[2].default_value = 2
    # Vertices Z
    cube.inputs[3].default_value = 2

    # Node Combine XYZ.017
    combine_xyz_017 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_017.name = "Combine XYZ.017"

    # Node Math.030
    math_030 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.operation = 'MULTIPLY'
    math_030.use_clamp = False
    # Value_001
    math_030.inputs[1].default_value = 2.0

    # Node Group Input.010
    group_input_010 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"

    # Node Math.032
    math_032 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_032.name = "Math.032"
    math_032.operation = 'SUBTRACT'
    math_032.use_clamp = False
    # Value
    math_032.inputs[0].default_value = 1.0

    # Node Math.034
    math_034 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_034.name = "Math.034"
    math_034.operation = 'MULTIPLY'
    math_034.use_clamp = False
    # Value_001
    math_034.inputs[1].default_value = 0.5

    # Node Math.035
    math_035 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.operation = 'DIVIDE'
    math_035.use_clamp = False
    # Value_001
    math_035.inputs[1].default_value = 2.0

    # Node Grid
    grid = geometry_nodes.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"

    # Node Group Input.012
    group_input_012 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"

    # Node Math.038
    math_038 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_038.name = "Math.038"
    math_038.operation = 'MULTIPLY'
    math_038.use_clamp = False
    # Value_001
    math_038.inputs[1].default_value = 2.0

    # Node Set Position.002
    set_position_002 = geometry_nodes.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    # Selection
    set_position_002.inputs[1].default_value = True
    # Position
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Combine XYZ.020
    combine_xyz_020 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_020.name = "Combine XYZ.020"
    # Z
    combine_xyz_020.inputs[2].default_value = 0.0

    # Node Math.039
    math_039 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.operation = 'ADD'
    math_039.use_clamp = False
    # Value_001
    math_039.inputs[1].default_value = 1.0

    # Node Math.040
    math_040 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.operation = 'MULTIPLY'
    math_040.use_clamp = False
    # Value_001
    math_040.inputs[1].default_value = 2.0

    # Node Math.041
    math_041 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_041.name = "Math.041"
    math_041.operation = 'ADD'
    math_041.use_clamp = False
    # Value_001
    math_041.inputs[1].default_value = 1.0

    # Node Mesh to Points
    mesh_to_points = geometry_nodes.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points.name = "Mesh to Points"
    mesh_to_points.mode = 'FACES'
    # Selection
    mesh_to_points.inputs[1].default_value = True
    # Position
    mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Radius
    mesh_to_points.inputs[3].default_value = 0.05000000074505806

    # Node Instance on Points
    instance_on_points = geometry_nodes.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Math.042
    math_042 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_042.name = "Math.042"
    math_042.operation = 'ADD'
    math_042.use_clamp = False
    # Value_001
    math_042.inputs[1].default_value = 2.0

    # Node Math.043
    math_043 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_043.name = "Math.043"
    math_043.operation = 'ADD'
    math_043.use_clamp = False
    # Value_001
    math_043.inputs[1].default_value = 2.0

    # Node Curve Line.002
    curve_line_002 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_002.name = "Curve Line.002"
    curve_line_002.mode = 'POINTS'

    # Node Vector Math
    vector_math = geometry_nodes.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ADD'

    # Node Vector Math.001
    vector_math_001 = geometry_nodes.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SUBTRACT'

    # Node Combine XYZ.019
    combine_xyz_019 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_019.name = "Combine XYZ.019"
    # Z
    combine_xyz_019.inputs[2].default_value = 0.0

    # Node Combine XYZ.021
    combine_xyz_021 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_021.name = "Combine XYZ.021"
    # Z
    combine_xyz_021.inputs[2].default_value = 0.0

    # Node Math.036
    math_036 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.operation = 'MULTIPLY'
    math_036.use_clamp = False
    # Value_001
    math_036.inputs[1].default_value = -0.5

    # Node Curve to Points
    curve_to_points = geometry_nodes.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points.name = "Curve to Points"
    curve_to_points.mode = 'COUNT'

    # Node Instance on Points.001
    instance_on_points_001 = geometry_nodes.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    # Rotation
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.003
    transform_geometry_003 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_003.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
    # Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Group Input.013
    group_input_013 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"

    # Node Combine XYZ.018
    combine_xyz_018 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_018.name = "Combine XYZ.018"
    # Y
    combine_xyz_018.inputs[1].default_value = 0.0

    # Node Combine XYZ.024
    combine_xyz_024 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_024.name = "Combine XYZ.024"

    # Node Math.033
    math_033 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_033.name = "Math.033"
    math_033.operation = 'DIVIDE'
    math_033.use_clamp = False

    # Node Math.047
    math_047 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_047.name = "Math.047"
    math_047.operation = 'ADD'
    math_047.use_clamp = False
    # Value_001
    math_047.inputs[1].default_value = 1.0

    # Node Group Input.014
    group_input_014 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"

    # Node Realize Instances
    realize_instances = geometry_nodes.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Combine XYZ.025
    combine_xyz_025 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_025.name = "Combine XYZ.025"
    # Z
    combine_xyz_025.inputs[2].default_value = 0.0

    # Node Math.048
    math_048 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_048.name = "Math.048"
    math_048.operation = 'MULTIPLY'
    math_048.use_clamp = False
    # Value_001
    math_048.inputs[1].default_value = 2.0

    # Node Math.049
    math_049 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_049.name = "Math.049"
    math_049.operation = 'MULTIPLY'
    math_049.use_clamp = False
    # Value_001
    math_049.inputs[1].default_value = 2.0

    # Node Realize Instances.001
    realize_instances_001 = geometry_nodes.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Transform Geometry.004
    transform_geometry_004 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = 'COMPONENTS'
    # Translation
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Cylinder
    cylinder = geometry_nodes.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.fill_type = 'NGON'
    # Side Segments
    cylinder.inputs[1].default_value = 1
    # Fill Segments
    cylinder.inputs[2].default_value = 1

    # Node Join Geometry.004
    join_geometry_004 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_004.name = "Join Geometry.004"

    # Node Math.051
    math_051 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_051.name = "Math.051"
    math_051.operation = 'ADD'
    math_051.use_clamp = False
    # Value_001
    math_051.inputs[1].default_value = 1.0

    # Node Math.031
    math_031 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.operation = 'MULTIPLY'
    math_031.use_clamp = False
    # Value_001
    math_031.inputs[1].default_value = 2.0

    # Node Math.052
    math_052 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_052.name = "Math.052"
    math_052.operation = 'ADD'
    math_052.use_clamp = False

    # Node Set Position
    set_position = geometry_nodes.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Combine XYZ.026
    combine_xyz_026 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_026.name = "Combine XYZ.026"
    # X
    combine_xyz_026.inputs[0].default_value = 0.0
    # Y
    combine_xyz_026.inputs[1].default_value = 0.0

    # Node Math.053
    math_053 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_053.name = "Math.053"
    math_053.operation = 'MULTIPLY'
    math_053.use_clamp = False
    # Value_001
    math_053.inputs[1].default_value = 0.5

    # Node Math.054
    math_054 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_054.name = "Math.054"
    math_054.operation = 'ADD'
    math_054.use_clamp = False
    # Value_001
    math_054.inputs[1].default_value = 1.0

    # Node Math.055
    math_055 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_055.name = "Math.055"
    math_055.operation = 'MULTIPLY'
    math_055.use_clamp = False
    # Value_001
    math_055.inputs[1].default_value = 2.0

    # Node Math.056
    math_056 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_056.name = "Math.056"
    math_056.operation = 'ADD'
    math_056.use_clamp = False

    # Node Math.057
    math_057 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_057.name = "Math.057"
    math_057.operation = 'SUBTRACT'
    math_057.use_clamp = False

    # Node Math.058
    math_058 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_058.name = "Math.058"
    math_058.operation = 'MULTIPLY'
    math_058.use_clamp = False
    # Value_001
    math_058.inputs[1].default_value = 0.5

    # Node Math.059
    math_059 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_059.name = "Math.059"
    math_059.operation = 'ADD'
    math_059.use_clamp = False
    # Value_001
    math_059.inputs[1].default_value = 2.0

    # Node Group Input.015
    group_input_015 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_015.name = "Group Input.015"

    # Node Group Input.016
    group_input_016 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_016.name = "Group Input.016"

    # Node Frame
    frame = geometry_nodes.nodes.new("NodeFrame")
    frame.label = "net"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.001
    frame_001 = geometry_nodes.nodes.new("NodeFrame")
    frame_001.label = "border"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Cylinder.001
    cylinder_001 = geometry_nodes.nodes.new("GeometryNodeMeshCylinder")
    cylinder_001.name = "Cylinder.001"
    cylinder_001.fill_type = 'NGON'
    # Side Segments
    cylinder_001.inputs[1].default_value = 1
    # Fill Segments
    cylinder_001.inputs[2].default_value = 1

    # Node Math.060
    math_060 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_060.name = "Math.060"
    math_060.operation = 'ADD'
    math_060.use_clamp = False

    # Node Transform Geometry.007
    transform_geometry_007 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_007.name = "Transform Geometry.007"
    transform_geometry_007.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_007.inputs[2].default_value = (-1.5707963705062866, 0.0, 0.0)
    # Scale
    transform_geometry_007.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Math.061
    math_061 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_061.name = "Math.061"
    math_061.operation = 'MULTIPLY'
    math_061.use_clamp = False
    # Value_001
    math_061.inputs[1].default_value = -0.5

    # Node Math.062
    math_062 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_062.name = "Math.062"
    math_062.operation = 'SUBTRACT'
    math_062.use_clamp = False

    # Node Combine XYZ.027
    combine_xyz_027 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_027.name = "Combine XYZ.027"
    # Y
    combine_xyz_027.inputs[1].default_value = 0.0
    # Z
    combine_xyz_027.inputs[2].default_value = 0.0

    # Node Math.063
    math_063 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_063.name = "Math.063"
    math_063.operation = 'ADD'
    math_063.use_clamp = False

    # Node Math.064
    math_064 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_064.name = "Math.064"
    math_064.operation = 'MULTIPLY'
    math_064.use_clamp = False
    # Value_001
    math_064.inputs[1].default_value = 0.5

    # Node Transform Geometry.008
    transform_geometry_008 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_008.name = "Transform Geometry.008"
    transform_geometry_008.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_008.inputs[2].default_value = (0.0, 3.1415927410125732, 0.0)
    # Scale
    transform_geometry_008.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry.012
    join_geometry_012 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_012.name = "Join Geometry.012"

    # Node Combine XYZ.028
    combine_xyz_028 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_028.name = "Combine XYZ.028"
    # Y
    combine_xyz_028.inputs[1].default_value = 0.0
    # Z
    combine_xyz_028.inputs[2].default_value = 0.0

    # Node Math.065
    math_065 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_065.name = "Math.065"
    math_065.operation = 'MULTIPLY'
    math_065.use_clamp = False
    # Value_001
    math_065.inputs[1].default_value = 2.0

    # Node Set Shade Smooth
    set_shade_smooth = geometry_nodes.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # Node Set Shade Smooth.001
    set_shade_smooth_001 = geometry_nodes.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_001.name = "Set Shade Smooth.001"
    set_shade_smooth_001.domain = 'FACE'
    # Shade Smooth
    set_shade_smooth_001.inputs[2].default_value = True

    # Node Delete Geometry
    delete_geometry = geometry_nodes.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'

    # Node Join Geometry.011
    join_geometry_011 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_011.name = "Join Geometry.011"

    # Node Cylinder.002
    cylinder_002 = geometry_nodes.nodes.new("GeometryNodeMeshCylinder")
    cylinder_002.name = "Cylinder.002"
    cylinder_002.fill_type = 'NGON'
    # Side Segments
    cylinder_002.inputs[1].default_value = 1
    # Fill Segments
    cylinder_002.inputs[2].default_value = 1

    # Node Math.037
    math_037 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.operation = 'DIVIDE'
    math_037.use_clamp = False
    # Value_001
    math_037.inputs[1].default_value = 4.0

    # Node Math.044
    math_044 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_044.name = "Math.044"
    math_044.operation = 'DIVIDE'
    math_044.use_clamp = False
    # Value_001
    math_044.inputs[1].default_value = 2.0

    # Node Math.045
    math_045 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_045.name = "Math.045"
    math_045.operation = 'ADD'
    math_045.use_clamp = False

    # Node Set Position.001
    set_position_001 = geometry_nodes.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Selection
    set_position_001.inputs[1].default_value = True
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Combine XYZ.029
    combine_xyz_029 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_029.name = "Combine XYZ.029"
    # X
    combine_xyz_029.inputs[0].default_value = 0.0
    # Y
    combine_xyz_029.inputs[1].default_value = 0.0

    # Node Math.046
    math_046 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_046.name = "Math.046"
    math_046.operation = 'DIVIDE'
    math_046.use_clamp = False
    # Value_001
    math_046.inputs[1].default_value = 2.0

    # Node Math.066
    math_066 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_066.name = "Math.066"
    math_066.operation = 'ADD'
    math_066.use_clamp = False

    # Node Set Shade Smooth.002
    set_shade_smooth_002 = geometry_nodes.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_002.name = "Set Shade Smooth.002"
    set_shade_smooth_002.domain = 'FACE'
    # Shade Smooth
    set_shade_smooth_002.inputs[2].default_value = True

    # Node Delete Geometry.001
    delete_geometry_001 = geometry_nodes.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'FACE'
    delete_geometry_001.mode = 'ALL'

    # Node Set Position.003
    set_position_003 = geometry_nodes.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    # Selection
    set_position_003.inputs[1].default_value = True
    # Position
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Combine XYZ.030
    combine_xyz_030 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_030.name = "Combine XYZ.030"
    # X
    combine_xyz_030.inputs[0].default_value = 0.0
    # Y
    combine_xyz_030.inputs[1].default_value = 0.0

    # Node Join Geometry.013
    join_geometry_013 = geometry_nodes.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_013.name = "Join Geometry.013"

    # Node Math.067
    math_067 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_067.name = "Math.067"
    math_067.operation = 'MULTIPLY'
    math_067.use_clamp = False
    # Value_001
    math_067.inputs[1].default_value = 2.0

    # Node Math.068
    math_068 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_068.name = "Math.068"
    math_068.operation = 'ADD'
    math_068.use_clamp = False
    # Value_001
    math_068.inputs[1].default_value = 2.0

    # Node Math.069
    math_069 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_069.name = "Math.069"
    math_069.operation = 'SUBTRACT'
    math_069.use_clamp = False

    # Node Set Shade Smooth.003
    set_shade_smooth_003 = geometry_nodes.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_003.name = "Set Shade Smooth.003"
    set_shade_smooth_003.domain = 'FACE'
    # Shade Smooth
    set_shade_smooth_003.inputs[2].default_value = True

    # Node Math.070
    math_070 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_070.name = "Math.070"
    math_070.operation = 'ADD'
    math_070.use_clamp = False

    # Node UV Sphere
    uv_sphere = geometry_nodes.nodes.new("GeometryNodeMeshUVSphere")
    uv_sphere.name = "UV Sphere"

    # Node Math.071
    math_071 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_071.name = "Math.071"
    math_071.operation = 'DIVIDE'
    math_071.use_clamp = False
    # Value_001
    math_071.inputs[1].default_value = 2.0

    # Node Group Input.017
    group_input_017 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_017.name = "Group Input.017"

    # Node Group Input.018
    group_input_018 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_018.name = "Group Input.018"

    # Node Delete Geometry.002
    delete_geometry_002 = geometry_nodes.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.domain = 'FACE'
    delete_geometry_002.mode = 'ALL'

    # Node Normal
    normal = geometry_nodes.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    # Node Separate XYZ
    separate_xyz = geometry_nodes.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    # Node Compare
    compare = geometry_nodes.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_THAN'
    # B
    compare.inputs[1].default_value = 0.0

    # Node Set Position.004
    set_position_004 = geometry_nodes.nodes.new("GeometryNodeSetPosition")
    set_position_004.name = "Set Position.004"
    # Selection
    set_position_004.inputs[1].default_value = True
    # Position
    set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Math.072
    math_072 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_072.name = "Math.072"
    math_072.operation = 'ADD'
    math_072.use_clamp = False

    # Node Combine XYZ.022
    combine_xyz_022 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_022.name = "Combine XYZ.022"
    # X
    combine_xyz_022.inputs[0].default_value = 0.0
    # Y
    combine_xyz_022.inputs[1].default_value = 0.0

    # Node Math.073
    math_073 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_073.name = "Math.073"
    math_073.operation = 'MULTIPLY'
    math_073.use_clamp = False
    # Value_001
    math_073.inputs[1].default_value = 2.0

    # Node Math.074
    math_074 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_074.name = "Math.074"
    math_074.operation = 'ADD'
    math_074.use_clamp = False
    # Value_001
    math_074.inputs[1].default_value = 2.0

    # Node Transform Geometry.009
    transform_geometry_009 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_009.name = "Transform Geometry.009"
    transform_geometry_009.mode = 'COMPONENTS'
    # Translation
    transform_geometry_009.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_009.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_009.inputs[3].default_value = (1.0, 1.0, 0.30000007152557373)

    # Node Set Shade Smooth.004
    set_shade_smooth_004 = geometry_nodes.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_004.name = "Set Shade Smooth.004"
    set_shade_smooth_004.domain = 'FACE'
    # Selection
    set_shade_smooth_004.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_004.inputs[2].default_value = True

    # Node Math.075
    math_075 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_075.name = "Math.075"
    math_075.operation = 'MULTIPLY'
    math_075.use_clamp = False
    # Value_001
    math_075.inputs[1].default_value = 2.0

    # Node Group Input.020
    group_input_020 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_020.name = "Group Input.020"

    # Node Math.077
    math_077 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_077.name = "Math.077"
    math_077.operation = 'SUBTRACT'
    math_077.use_clamp = False

    # Node Math.078
    math_078 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_078.name = "Math.078"
    math_078.operation = 'MULTIPLY'
    math_078.use_clamp = False
    # Value_001
    math_078.inputs[1].default_value = 0.5

    # Node Math.079
    math_079 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_079.name = "Math.079"
    math_079.operation = 'ADD'
    math_079.use_clamp = False
    # Value_001
    math_079.inputs[1].default_value = 2.0

    # Node Math.080
    math_080 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_080.name = "Math.080"
    math_080.operation = 'ADD'
    math_080.use_clamp = False

    # Node Math.081
    math_081 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_081.name = "Math.081"
    math_081.operation = 'MULTIPLY'
    math_081.use_clamp = False
    # Value_001
    math_081.inputs[1].default_value = 2.0

    # Node Curve Line.003
    curve_line_003 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_003.name = "Curve Line.003"
    curve_line_003.mode = 'POINTS'
    # Start
    curve_line_003.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Transform Geometry.010
    transform_geometry_010 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_010.name = "Transform Geometry.010"
    transform_geometry_010.mode = 'COMPONENTS'
    # Translation
    transform_geometry_010.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_010.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
    # Scale
    transform_geometry_010.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Combine XYZ.031
    combine_xyz_031 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_031.name = "Combine XYZ.031"
    # X
    combine_xyz_031.inputs[0].default_value = 0.0
    # Y
    combine_xyz_031.inputs[1].default_value = 0.0

    # Node Curve to Points.001
    curve_to_points_001 = geometry_nodes.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points_001.name = "Curve to Points.001"
    curve_to_points_001.mode = 'COUNT'

    # Node Math.076
    math_076 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_076.name = "Math.076"
    math_076.operation = 'MULTIPLY'
    math_076.use_clamp = False

    # Node Instance on Points.002
    instance_on_points_002 = geometry_nodes.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    # Selection
    instance_on_points_002.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0
    # Rotation
    instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Math.082
    math_082 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_082.name = "Math.082"
    math_082.operation = 'ADD'
    math_082.use_clamp = False
    # Value_001
    math_082.inputs[1].default_value = 1.0

    # Node Math.083
    math_083 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_083.name = "Math.083"
    math_083.operation = 'MULTIPLY'
    math_083.use_clamp = False
    # Value_001
    math_083.inputs[1].default_value = 2.0

    # Node Group Input.021
    group_input_021 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_021.name = "Group Input.021"

    # Node Math.084
    math_084 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_084.name = "Math.084"
    math_084.operation = 'SUBTRACT'
    math_084.use_clamp = False

    # Node Math.085
    math_085 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_085.name = "Math.085"
    math_085.operation = 'MULTIPLY'
    math_085.use_clamp = False
    # Value_001
    math_085.inputs[1].default_value = 0.5

    # Node Math.086
    math_086 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_086.name = "Math.086"
    math_086.operation = 'ADD'
    math_086.use_clamp = False
    # Value_001
    math_086.inputs[1].default_value = 2.0

    # Node Math.087
    math_087 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_087.name = "Math.087"
    math_087.operation = 'ADD'
    math_087.use_clamp = False

    # Node Math.088
    math_088 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_088.name = "Math.088"
    math_088.operation = 'MULTIPLY'
    math_088.use_clamp = False
    # Value_001
    math_088.inputs[1].default_value = 2.0

    # Node Curve Line.004
    curve_line_004 = geometry_nodes.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_004.name = "Curve Line.004"
    curve_line_004.mode = 'POINTS'
    # Start
    curve_line_004.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Transform Geometry.011
    transform_geometry_011 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_011.name = "Transform Geometry.011"
    transform_geometry_011.mode = 'COMPONENTS'
    # Translation
    transform_geometry_011.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_011.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
    # Scale
    transform_geometry_011.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Combine XYZ.032
    combine_xyz_032 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_032.name = "Combine XYZ.032"
    # X
    combine_xyz_032.inputs[0].default_value = 0.0
    # Y
    combine_xyz_032.inputs[1].default_value = 0.0

    # Node Curve to Points.002
    curve_to_points_002 = geometry_nodes.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points_002.name = "Curve to Points.002"
    curve_to_points_002.mode = 'COUNT'

    # Node Math.089
    math_089 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_089.name = "Math.089"
    math_089.operation = 'MULTIPLY'
    math_089.use_clamp = False

    # Node Math.091
    math_091 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_091.name = "Math.091"
    math_091.operation = 'SUBTRACT'
    math_091.use_clamp = False
    # Value_001
    math_091.inputs[1].default_value = 1.0

    # Node Instance on Points.003
    instance_on_points_003 = geometry_nodes.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_003.name = "Instance on Points.003"
    # Selection
    instance_on_points_003.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_003.inputs[3].default_value = False
    # Instance Index
    instance_on_points_003.inputs[4].default_value = 0
    # Rotation
    instance_on_points_003.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_003.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Curve to Points.003
    curve_to_points_003 = geometry_nodes.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points_003.name = "Curve to Points.003"
    curve_to_points_003.mode = 'COUNT'

    # Node Instance on Points.004
    instance_on_points_004 = geometry_nodes.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_004.name = "Instance on Points.004"
    # Selection
    instance_on_points_004.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_004.inputs[3].default_value = False
    # Instance Index
    instance_on_points_004.inputs[4].default_value = 0
    # Rotation
    instance_on_points_004.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points_004.inputs[6].default_value = (1.0, 1.0, 1.0)

    # Node Transform Geometry.012
    transform_geometry_012 = geometry_nodes.nodes.new("GeometryNodeTransform")
    transform_geometry_012.name = "Transform Geometry.012"
    transform_geometry_012.mode = 'COMPONENTS'
    # Rotation
    transform_geometry_012.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
    # Scale
    transform_geometry_012.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Group Input.019
    group_input_019 = geometry_nodes.nodes.new("NodeGroupInput")
    group_input_019.name = "Group Input.019"

    # Node Combine XYZ.023
    combine_xyz_023 = geometry_nodes.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_023.name = "Combine XYZ.023"
    # Y
    combine_xyz_023.inputs[1].default_value = 0.0

    # Node Math.090
    math_090 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_090.name = "Math.090"
    math_090.operation = 'ADD'
    math_090.use_clamp = False
    # Value_001
    math_090.inputs[1].default_value = 1.0

    # Node Math.092
    math_092 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_092.name = "Math.092"
    math_092.operation = 'SUBTRACT'
    math_092.use_clamp = False

    # Node Math.093
    math_093 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_093.name = "Math.093"
    math_093.operation = 'MULTIPLY'
    math_093.use_clamp = False
    # Value_001
    math_093.inputs[1].default_value = 0.5

    # Node Math.094
    math_094 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_094.name = "Math.094"
    math_094.operation = 'ADD'
    math_094.use_clamp = False
    # Value_001
    math_094.inputs[1].default_value = 2.0

    # Node Realize Instances.002
    realize_instances_002 = geometry_nodes.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_002.name = "Realize Instances.002"
    # Selection
    realize_instances_002.inputs[1].default_value = True
    # Realize All
    realize_instances_002.inputs[2].default_value = True
    # Depth
    realize_instances_002.inputs[3].default_value = 0

    # Node Realize Instances.003
    realize_instances_003 = geometry_nodes.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_003.name = "Realize Instances.003"
    # Selection
    realize_instances_003.inputs[1].default_value = True
    # Realize All
    realize_instances_003.inputs[2].default_value = True
    # Depth
    realize_instances_003.inputs[3].default_value = 0

    # Node Realize Instances.004
    realize_instances_004 = geometry_nodes.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_004.name = "Realize Instances.004"
    # Selection
    realize_instances_004.inputs[1].default_value = True
    # Realize All
    realize_instances_004.inputs[2].default_value = True
    # Depth
    realize_instances_004.inputs[3].default_value = 0

    # Node Math.095
    math_095 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_095.name = "Math.095"
    math_095.operation = 'ADD'
    math_095.use_clamp = False

    # Node Math.097
    math_097 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_097.name = "Math.097"
    math_097.operation = 'ADD'
    math_097.use_clamp = False

    # Node Math.098
    math_098 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_098.name = "Math.098"
    math_098.operation = 'MULTIPLY'
    math_098.use_clamp = False
    # Value_001
    math_098.inputs[1].default_value = 0.30000001192092896

    # Node Math.099
    math_099 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_099.name = "Math.099"
    math_099.operation = 'ADD'
    math_099.use_clamp = False

    # Node Math.100
    math_100 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_100.name = "Math.100"
    math_100.operation = 'MULTIPLY'
    math_100.use_clamp = False
    # Value_001
    math_100.inputs[1].default_value = 2.0

    # Node Math.050
    math_050 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_050.name = "Math.050"
    math_050.operation = 'MULTIPLY'
    math_050.use_clamp = False
    # Value_001
    math_050.inputs[1].default_value = 2.0

    # Node Math.096
    math_096 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_096.name = "Math.096"
    math_096.operation = 'DIVIDE'
    math_096.use_clamp = False
    # Value_001
    math_096.inputs[1].default_value = 4.0

    # Node Math.101
    math_101 = geometry_nodes.nodes.new("ShaderNodeMath")
    math_101.name = "Math.101"
    math_101.operation = 'ADD'
    math_101.use_clamp = False

    # Node Frame.002
    frame_002 = geometry_nodes.nodes.new("NodeFrame")
    frame_002.label = "connect"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = geometry_nodes.nodes.new("NodeFrame")
    frame_003.label = "connect_ring"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = geometry_nodes.nodes.new("NodeFrame")
    frame_004.label = "netwall_coordinates"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = geometry_nodes.nodes.new("NodeFrame")
    frame_005.label = "netwall_extend"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Frame.006
    frame_006 = geometry_nodes.nodes.new("NodeFrame")
    frame_006.label = "pillar"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # Node Frame.007
    frame_007 = geometry_nodes.nodes.new("NodeFrame")
    frame_007.label = "pillar_extend"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    # Node Frame.008
    frame_008 = geometry_nodes.nodes.new("NodeFrame")
    frame_008.label = "scale"
    frame_008.name = "Frame.008"
    frame_008.label_size = 20
    frame_008.shrink = True

    # Set parents
    group_input.parent = frame
    b_zier_segment.parent = frame
    combine_xyz.parent = frame
    combine_xyz_001.parent = frame
    math.parent = frame
    math_001.parent = frame
    combine_xyz_002.parent = frame
    math_002.parent = frame
    combine_xyz_003.parent = frame
    math_003.parent = frame
    math_004.parent = frame
    b_zier_segment_001.parent = frame
    combine_xyz_004.parent = frame
    join_geometry_002.parent = frame
    combine_xyz_005.parent = frame
    combine_xyz_006.parent = frame
    math_005.parent = frame
    math_006.parent = frame
    transform_geometry_002.parent = frame
    join_geometry_003.parent = frame
    curve_circle_001.parent = frame
    group_input_003.parent = frame
    curve_to_mesh_001.parent = frame
    merge_by_distance_001.parent = frame
    math_007.parent = frame
    math_008.parent = frame
    b_zier_segment_002.parent = frame_001
    group_input_004.parent = frame_001
    math_009.parent = frame_001
    math_010.parent = frame_001
    combine_xyz_007.parent = frame_001
    combine_xyz_008.parent = frame_001
    math_011.parent = frame_001
    math_012.parent = frame_001
    math_013.parent = frame_001
    combine_xyz_009.parent = frame_001
    combine_xyz_010.parent = frame_001
    math_014.parent = frame_001
    math_015.parent = frame_001
    transform_geometry.parent = frame_001
    group_input_005.parent = frame_001
    math_016.parent = frame_001
    combine_xyz_011.parent = frame_001
    join_geometry_001.parent = frame_001
    transform_geometry_001.parent = frame_001
    combine_xyz_012.parent = frame_001
    join_geometry_006.parent = frame_001
    math_017.parent = frame_001
    curve_line.parent = frame_001
    group_input_006.parent = frame_001
    math_018.parent = frame_001
    curve_line_001.parent = frame_001
    combine_xyz_013.parent = frame_001
    join_geometry_007.parent = frame_001
    math_021.parent = frame_001
    combine_xyz_014.parent = frame_001
    math_022.parent = frame_001
    math_023.parent = frame_001
    math_024.parent = frame_001
    math_025.parent = frame_001
    transform_geometry_005.parent = frame_001
    join_geometry_008.parent = frame_001
    group_input_007.parent = frame_001
    math_019.parent = frame_001
    combine_xyz_015.parent = frame_001
    math_020.parent = frame_001
    math_026.parent = frame_001
    math_027.parent = frame_001
    join_geometry_009.parent = frame_001
    transform_geometry_006.parent = frame_001
    group_input_008.parent = frame_001
    math_028.parent = frame_001
    combine_xyz_016.parent = frame_001
    math_029.parent = frame_001
    join_geometry_010.parent = frame_001
    curve_to_mesh.parent = frame_001
    curve_circle_002.parent = frame_001
    group_input_009.parent = frame_001
    merge_by_distance_002.parent = frame_001
    cube.parent = frame_002
    combine_xyz_017.parent = frame_002
    math_030.parent = frame_002
    group_input_010.parent = frame_002
    math_032.parent = frame_002
    math_034.parent = frame_002
    math_035.parent = frame_002
    grid.parent = frame
    group_input_012.parent = frame
    math_038.parent = frame
    set_position_002.parent = frame
    combine_xyz_020.parent = frame
    math_039.parent = frame
    math_040.parent = frame
    math_041.parent = frame
    mesh_to_points.parent = frame
    instance_on_points.parent = frame
    math_042.parent = frame
    math_043.parent = frame
    curve_line_002.parent = frame_002
    vector_math.parent = frame_002
    vector_math_001.parent = frame_002
    combine_xyz_019.parent = frame_002
    combine_xyz_021.parent = frame_002
    math_036.parent = frame_002
    curve_to_points.parent = frame_002
    instance_on_points_001.parent = frame_002
    transform_geometry_003.parent = frame_004
    group_input_013.parent = frame_004
    combine_xyz_018.parent = frame_004
    combine_xyz_024.parent = frame_008
    math_033.parent = frame_008
    math_047.parent = frame_008
    group_input_014.parent = frame
    realize_instances.parent = frame
    combine_xyz_025.parent = frame
    math_048.parent = frame
    math_049.parent = frame
    realize_instances_001.parent = frame_002
    transform_geometry_004.parent = frame_008
    cylinder.parent = frame_006
    math_051.parent = frame_004
    math_031.parent = frame_006
    math_052.parent = frame_006
    set_position.parent = frame_006
    combine_xyz_026.parent = frame_006
    math_053.parent = frame_006
    math_054.parent = frame_006
    math_055.parent = frame_006
    math_056.parent = frame_006
    math_057.parent = frame_004
    math_058.parent = frame_004
    math_059.parent = frame_004
    group_input_015.parent = frame_008
    group_input_016.parent = frame_006
    cylinder_001.parent = frame_003
    math_060.parent = frame_003
    transform_geometry_007.parent = frame_003
    math_061.parent = frame_002
    math_062.parent = frame_003
    combine_xyz_027.parent = frame_003
    math_063.parent = frame_003
    math_064.parent = frame_003
    transform_geometry_008.parent = frame_002
    join_geometry_012.parent = frame_002
    combine_xyz_028.parent = frame_002
    math_065.parent = frame_002
    set_shade_smooth.parent = frame_003
    set_shade_smooth_001.parent = frame_006
    delete_geometry.parent = frame_006
    cylinder_002.parent = frame_006
    math_037.parent = frame_006
    math_044.parent = frame_006
    math_045.parent = frame_006
    set_position_001.parent = frame_006
    combine_xyz_029.parent = frame_006
    math_046.parent = frame_006
    math_066.parent = frame_006
    set_shade_smooth_002.parent = frame_006
    delete_geometry_001.parent = frame_006
    set_position_003.parent = frame_006
    combine_xyz_030.parent = frame_006
    join_geometry_013.parent = frame_006
    math_067.parent = frame_006
    math_068.parent = frame_006
    math_069.parent = frame_006
    set_shade_smooth_003.parent = frame_006
    math_070.parent = frame_006
    uv_sphere.parent = frame_006
    math_071.parent = frame_006
    group_input_017.parent = frame_006
    group_input_018.parent = frame_006
    delete_geometry_002.parent = frame_006
    normal.parent = frame_006
    separate_xyz.parent = frame_006
    compare.parent = frame_006
    set_position_004.parent = frame_006
    math_072.parent = frame_006
    combine_xyz_022.parent = frame_006
    math_073.parent = frame_006
    math_074.parent = frame_006
    transform_geometry_009.parent = frame_006
    set_shade_smooth_004.parent = frame_006
    math_075.parent = frame_007
    group_input_020.parent = frame_007
    math_077.parent = frame_007
    math_078.parent = frame_007
    math_079.parent = frame_007
    math_080.parent = frame_007
    math_081.parent = frame_007
    curve_line_003.parent = frame_007
    transform_geometry_010.parent = frame_007
    combine_xyz_031.parent = frame_007
    curve_to_points_001.parent = frame_007
    math_076.parent = frame_007
    instance_on_points_002.parent = frame_007
    math_082.parent = frame_007
    math_083.parent = frame_005
    group_input_021.parent = frame_005
    math_084.parent = frame_005
    math_085.parent = frame_005
    math_086.parent = frame_005
    math_087.parent = frame_005
    math_088.parent = frame_005
    curve_line_004.parent = frame_005
    transform_geometry_011.parent = frame_005
    combine_xyz_032.parent = frame_005
    curve_to_points_002.parent = frame_005
    math_089.parent = frame_005
    math_091.parent = frame_005
    instance_on_points_003.parent = frame_005
    curve_to_points_003.parent = frame_003
    instance_on_points_004.parent = frame_003
    transform_geometry_012.parent = frame_003
    group_input_019.parent = frame_003
    combine_xyz_023.parent = frame_003
    math_090.parent = frame_003
    math_092.parent = frame_003
    math_093.parent = frame_003
    math_094.parent = frame_003
    realize_instances_002.parent = frame_003
    realize_instances_003.parent = frame_005
    realize_instances_004.parent = frame_007
    math_095.parent = frame_008
    math_097.parent = frame_008
    math_098.parent = frame_008
    math_099.parent = frame_008
    math_100.parent = frame_008
    math_050.parent = frame_008
    math_096.parent = frame_008
    math_101.parent = frame_008

    # Set locations
    group_input.location = (30.32080078125, -385.72705078125)
    group_output.location = (15380.5, -4003.660888671875)
    b_zier_segment.location = (1335.40966796875, -248.52590942382812)
    combine_xyz.location = (1094.515380859375, -62.42620849609375)
    combine_xyz_001.location = (1090.0899658203125, -465.3658447265625)
    math.location = (639.303466796875, -36.15936279296875)
    math_001.location = (640.059326171875, -573.4105834960938)
    combine_xyz_002.location = (1091.4267578125, -193.73480224609375)
    math_002.location = (640.059326171875, -249.78857421875)
    combine_xyz_003.location = (1088.950439453125, -326.1301574707031)
    math_003.location = (641.360107421875, -408.6976318359375)
    math_004.location = (640.8519287109375, -732.4214477539062)
    b_zier_segment_001.location = (1346.08984375, -606.8341674804688)
    combine_xyz_004.location = (1093.244140625, -740.3359375)
    join_geometry_002.location = (1609.6563720703125, -447.68621826171875)
    combine_xyz_005.location = (1091.654296875, -602.848388671875)
    combine_xyz_006.location = (1091.1090087890625, -871.6064453125)
    math_005.location = (857.9500732421875, -271.81414794921875)
    math_006.location = (854.7611694335938, -499.4177551269531)
    transform_geometry_002.location = (5052.53564453125, -464.71014404296875)
    join_geometry_003.location = (5268.00830078125, -398.5554504394531)
    curve_circle_001.location = (1829.22314453125, -522.2468872070312)
    group_input_003.location = (1626.5693359375, -571.707275390625)
    curve_to_mesh_001.location = (2033.87548828125, -426.3681945800781)
    merge_by_distance_001.location = (3997.099609375, -355.7178955078125)
    math_007.location = (376.5120849609375, -73.68048095703125)
    math_008.location = (406.0992431640625, -276.1204528808594)
    b_zier_segment_002.location = (1271.707275390625, -177.65216064453125)
    join_geometry.location = (5416.31005859375, -1916.4254150390625)
    group_input_004.location = (74.5924072265625, -354.78314208984375)
    math_009.location = (584.9385375976562, -56.5025634765625)
    math_010.location = (339.29730224609375, -241.91650390625)
    combine_xyz_007.location = (855.052978515625, -35.7562255859375)
    combine_xyz_008.location = (949.18408203125, -536.4085083007812)
    math_011.location = (336.537353515625, -565.8869018554688)
    math_012.location = (636.6260375976562, -558.9452514648438)
    math_013.location = (335.71331787109375, -405.29583740234375)
    combine_xyz_009.location = (852.6717529296875, -206.1021728515625)
    combine_xyz_010.location = (969.2276000976562, -364.30462646484375)
    math_014.location = (586.3461303710938, -307.86737060546875)
    math_015.location = (787.8826904296875, -357.15191650390625)
    transform_geometry.location = (1871.4315185546875, -294.40777587890625)
    group_input_005.location = (1265.929931640625, -500.15753173828125)
    math_016.location = (1473.8404541015625, -507.23260498046875)
    combine_xyz_011.location = (1670.9998779296875, -412.21051025390625)
    join_geometry_001.location = (2118.5859375, -190.69964599609375)
    transform_geometry_001.location = (2413.924560546875, -255.83245849609375)
    combine_xyz_012.location = (2159.60107421875, -583.3231811523438)
    join_geometry_006.location = (3501.020263671875, -755.4203491210938)
    math_017.location = (1859.229248046875, -624.1262817382812)
    curve_line.location = (1300.824462890625, -1098.983642578125)
    group_input_006.location = (29.760986328125, -1432.619384765625)
    math_018.location = (379.15325927734375, -1348.5009765625)
    curve_line_001.location = (1293.1812744140625, -1760.137939453125)
    combine_xyz_013.location = (1035.0936279296875, -1171.16748046875)
    join_geometry_007.location = (2942.58447265625, -1124.0400390625)
    math_021.location = (795.2081298828125, -1245.631591796875)
    combine_xyz_014.location = (1070.5040283203125, -1794.038330078125)
    math_022.location = (593.195556640625, -1710.355224609375)
    math_023.location = (369.569580078125, -1752.898193359375)
    math_024.location = (371.2637634277344, -1559.4033203125)
    math_025.location = (839.9964599609375, -1689.583984375)
    transform_geometry_005.location = (2335.52294921875, -1155.799560546875)
    join_geometry_008.location = (2561.29052734375, -1114.04150390625)
    group_input_007.location = (1444.7808837890625, -1256.58544921875)
    math_019.location = (1802.034912109375, -1385.552490234375)
    combine_xyz_015.location = (2135.8515625, -1252.636474609375)
    math_020.location = (1629.7203369140625, -1385.814697265625)
    math_026.location = (1971.5428466796875, -1257.8388671875)
    math_027.location = (1699.023193359375, -1204.6337890625)
    join_geometry_009.location = (2606.50048828125, -1776.9482421875)
    transform_geometry_006.location = (2351.65283203125, -1844.53271484375)
    group_input_008.location = (1592.44091796875, -1879.4677734375)
    math_028.location = (1949.6949462890625, -2008.434814453125)
    combine_xyz_016.location = (2151.9814453125, -1941.369384765625)
    math_029.location = (1777.3804931640625, -2008.69677734375)
    join_geometry_010.location = (2765.21630859375, -191.58465576171875)
    curve_to_mesh.location = (3833.138916015625, -939.7413940429688)
    curve_circle_002.location = (3630.54345703125, -1047.439697265625)
    group_input_009.location = (3420.905029296875, -928.4978637695312)
    merge_by_distance_002.location = (4073.443603515625, -1048.149658203125)
    cube.location = (1409.6763916015625, -544.796875)
    combine_xyz_017.location = (813.5301513671875, -824.051025390625)
    math_030.location = (236.11505126953125, -378.330810546875)
    group_input_010.location = (29.94647216796875, -423.975830078125)
    math_032.location = (416.9124755859375, -339.64501953125)
    math_034.location = (757.412109375, -371.665771484375)
    math_035.location = (246.728515625, -576.062744140625)
    grid.location = (2900.31298828125, -559.1585083007812)
    group_input_012.location = (2219.148681640625, -667.9777221679688)
    math_038.location = (2668.43212890625, -541.2688598632812)
    set_position_002.location = (3116.56982421875, -698.0759887695312)
    combine_xyz_020.location = (2920.64208984375, -833.603759765625)
    math_039.location = (2500.54638671875, -538.36767578125)
    math_040.location = (2666.02392578125, -693.1823120117188)
    math_041.location = (2498.13818359375, -690.28125)
    mesh_to_points.location = (3313.486572265625, -694.7234497070312)
    instance_on_points.location = (3628.261962890625, -377.0543212890625)
    math_042.location = (2594.01123046875, -948.2945556640625)
    math_043.location = (2594.01123046875, -1104.4288330078125)
    curve_line_002.location = (1448.1915283203125, -121.583740234375)
    vector_math.location = (1227.8365478515625, -41.16455078125)
    vector_math_001.location = (1200.5419921875, -294.323486328125)
    combine_xyz_019.location = (993.6627197265625, -441.745361328125)
    combine_xyz_021.location = (989.1724853515625, -152.9296875)
    math_036.location = (649.48193359375, -136.049560546875)
    curve_to_points.location = (1815.4417724609375, -36.129638671875)
    instance_on_points_001.location = (2188.349609375, -309.228271484375)
    transform_geometry_003.location = (1106.56298828125, -36.0498046875)
    group_input_013.location = (30.04833984375, -176.8387451171875)
    combine_xyz_018.location = (886.75146484375, -245.736083984375)
    combine_xyz_024.location = (1746.5, -515.76171875)
    math_033.location = (1493.4091796875, -579.08203125)
    math_047.location = (254.9033203125, -217.56689453125)
    group_input_014.location = (3803.427978515625, -509.2518615722656)
    realize_instances.location = (3812.004638671875, -373.2237243652344)
    combine_xyz_025.location = (4396.2060546875, -655.6517333984375)
    math_048.location = (4113.587890625, -569.5821533203125)
    math_049.location = (4112.28564453125, -756.0659790039062)
    realize_instances_001.location = (2378.09716796875, -313.543701171875)
    transform_geometry_004.location = (2053.537109375, -35.762451171875)
    cylinder.location = (1039.4833984375, -90.4453125)
    join_geometry_004.location = (12874.111328125, -4024.16162109375)
    math_051.location = (655.05859375, -433.460693359375)
    math_031.location = (431.15869140625, -123.57177734375)
    math_052.location = (620.9951171875, -145.81787109375)
    set_position.location = (1891.3974609375, -109.703125)
    combine_xyz_026.location = (1460.5537109375, -299.15234375)
    math_053.location = (1038.13671875, -396.7607421875)
    math_054.location = (221.92578125, -185.7841796875)
    math_055.location = (617.68408203125, -469.83984375)
    math_056.location = (841.1904296875, -379.00146484375)
    math_057.location = (444.1728515625, -238.87255859375)
    math_058.location = (220.96728515625, -211.1162109375)
    math_059.location = (674.3125, -234.286376953125)
    group_input_015.location = (30.099609375, -204.50390625)
    group_input_016.location = (29.92138671875, -144.45849609375)
    frame.location = (-1526.800048828125, 628.7999877929688)
    frame_001.location = (-818.0, -772.7999877929688)
    cylinder_001.location = (649.037353515625, -348.8095703125)
    math_060.location = (392.4873046875, -200.3505859375)
    transform_geometry_007.location = (1505.859375, -342.63916015625)
    math_061.location = (873.781982421875, -569.063232421875)
    math_062.location = (805.38134765625, -36.3642578125)
    combine_xyz_027.location = (1242.97119140625, -173.6083984375)
    math_063.location = (1027.46533203125, -192.22412109375)
    math_064.location = (147.499267578125, -174.74951171875)
    transform_geometry_008.location = (2631.67138671875, -493.563720703125)
    join_geometry_012.location = (2852.52490234375, -318.77734375)
    combine_xyz_028.location = (2401.06005859375, -598.383056640625)
    math_065.location = (1619.9295654296875, -808.435791015625)
    set_shade_smooth.location = (895.67626953125, -362.8251953125)
    set_shade_smooth_001.location = (1648.91650390625, -86.7626953125)
    delete_geometry.location = (1467.13525390625, -35.64208984375)
    join_geometry_011.location = (8760.7197265625, -4837.75)
    cylinder_002.location = (1209.8427734375, -1956.43798828125)
    math_037.location = (849.29541015625, -1750.79931640625)
    math_044.location = (659.5419921875, -2060.28759765625)
    math_045.location = (943.2958984375, -2213.9326171875)
    set_position_001.location = (1931.73486328125, -1815.78662109375)
    combine_xyz_029.location = (1446.8505859375, -1748.4794921875)
    math_046.location = (1231.57421875, -1748.97412109375)
    math_066.location = (1252.2177734375, -414.691650390625)
    set_shade_smooth_002.location = (1675.32861328125, -1976.6123046875)
    delete_geometry_001.location = (1497.89111328125, -1899.8828125)
    set_position_003.location = (1872.76171875, -2210.98583984375)
    combine_xyz_030.location = (1525.7412109375, -2299.83642578125)
    join_geometry_013.location = (2190.11083984375, -2006.54345703125)
    math_067.location = (934.4833984375, -2416.76318359375)
    math_068.location = (677.21240234375, -2411.63134765625)
    math_069.location = (1211.52734375, -2285.1787109375)
    set_shade_smooth_003.location = (1518.77734375, -2151.65283203125)
    math_070.location = (1253.25244140625, -180.147216796875)
    uv_sphere.location = (1106.50244140625, -798.3388671875)
    math_071.location = (762.78955078125, -751.94775390625)
    group_input_017.location = (209.65087890625, -767.26806640625)
    group_input_018.location = (357.0478515625, -1897.56005859375)
    delete_geometry_002.location = (1345.44921875, -754.6943359375)
    normal.location = (763.80908203125, -1134.19189453125)
    separate_xyz.location = (951.14306640625, -1069.88427734375)
    compare.location = (1183.56494140625, -1039.22412109375)
    set_position_004.location = (1915.20556640625, -890.5302734375)
    math_072.location = (1324.45556640625, -1217.40625)
    combine_xyz_022.location = (1515.1162109375, -1059.5078125)
    math_073.location = (939.1953125, -1366.03662109375)
    math_074.location = (696.97705078125, -1371.73583984375)
    transform_geometry_009.location = (1702.98974609375, -704.6640625)
    set_shade_smooth_004.location = (1527.71484375, -713.61083984375)
    math_075.location = (413.2685546875, -409.328125)
    group_input_020.location = (29.943359375, -351.79541015625)
    math_077.location = (459.896484375, -602.26513671875)
    math_078.location = (236.6904296875, -574.50927734375)
    math_079.location = (644.3095703125, -594.15625)
    math_080.location = (1038.4501953125, -415.7275390625)
    math_081.location = (826.119140625, -567.0546875)
    curve_line_003.location = (1738.583984375, -439.53369140625)
    transform_geometry_010.location = (1925.8935546875, -417.16796875)
    combine_xyz_031.location = (1527.9970703125, -485.49609375)
    curve_to_points_001.location = (2157.5341796875, -600.05322265625)
    math_076.location = (1281.5986328125, -584.33935546875)
    instance_on_points_002.location = (2538.7998046875, -37.5830078125)
    math_082.location = (1703.8095703125, -731.30712890625)
    math_083.location = (413.474609375, -280.869140625)
    group_input_021.location = (30.14990234375, -223.3359375)
    math_084.location = (460.10302734375, -473.80615234375)
    math_085.location = (236.896484375, -446.05029296875)
    math_086.location = (644.51708984375, -465.697265625)
    math_087.location = (1038.6572265625, -287.268310546875)
    math_088.location = (826.32470703125, -438.595703125)
    curve_line_004.location = (1738.7900390625, -311.07373046875)
    transform_geometry_011.location = (1926.099609375, -288.708984375)
    combine_xyz_032.location = (1528.2041015625, -357.03662109375)
    curve_to_points_002.location = (2157.740234375, -471.59423828125)
    math_089.location = (1281.8056640625, -455.88037109375)
    math_091.location = (855.49658203125, -720.87548828125)
    instance_on_points_003.location = (2373.9375, -36.3656005859375)
    curve_to_points_003.location = (1636.543701171875, -122.5693359375)
    instance_on_points_004.location = (1890.27490234375, -240.9208984375)
    transform_geometry_012.location = (2356.050537109375, -465.966796875)
    group_input_019.location = (30.1156005859375, -363.28369140625)
    combine_xyz_023.location = (1642.50146484375, -737.98095703125)
    math_090.location = (1410.80859375, -925.70556640625)
    math_092.location = (1199.923583984375, -731.1171875)
    math_093.location = (950.046142578125, -647.7109375)
    math_094.location = (1430.0625, -726.53125)
    realize_instances_002.location = (2113.966552734375, -248.01708984375)
    realize_instances_003.location = (2629.166015625, -38.3369140625)
    realize_instances_004.location = (2830.6796875, -36.35791015625)
    math_095.location = (666.8525390625, -169.73583984375)
    math_097.location = (868.921875, -251.03564453125)
    math_098.location = (912.09375, -532.72509765625)
    math_099.location = (1240.287109375, -436.97705078125)
    math_100.location = (456.583984375, -143.68017578125)
    math_050.location = (608.0390625, -327.0419921875)
    math_096.location = (607.693359375, -481.5810546875)
    math_101.location = (1048.7685546875, -316.12353515625)
    frame_002.location = (663.5999755859375, -3523.199951171875)
    frame_003.location = (1998.800048828125, -5240.0)
    frame_004.location = (5817.2001953125, -1859.199951171875)
    frame_005.location = (7169.2001953125, -1876.0)
    frame_006.location = (5763.60009765625, -3673.60009765625)
    frame_007.location = (9034.7998046875, -4746.39990234375)
    frame_008.location = (13077.2001953125, -3965.60009765625)

    # Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    b_zier_segment.width, b_zier_segment.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    b_zier_segment_001.width, b_zier_segment_001.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
    combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
    combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
    curve_circle_001.width, curve_circle_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
    merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    b_zier_segment_002.width, b_zier_segment_002.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    combine_xyz_007.width, combine_xyz_007.height = 140.0, 100.0
    combine_xyz_008.width, combine_xyz_008.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
    combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
    math_014.width, math_014.height = 140.0, 100.0
    math_015.width, math_015.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    combine_xyz_011.width, combine_xyz_011.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    combine_xyz_012.width, combine_xyz_012.height = 140.0, 100.0
    join_geometry_006.width, join_geometry_006.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    curve_line_001.width, curve_line_001.height = 140.0, 100.0
    combine_xyz_013.width, combine_xyz_013.height = 140.0, 100.0
    join_geometry_007.width, join_geometry_007.height = 140.0, 100.0
    math_021.width, math_021.height = 140.0, 100.0
    combine_xyz_014.width, combine_xyz_014.height = 140.0, 100.0
    math_022.width, math_022.height = 140.0, 100.0
    math_023.width, math_023.height = 140.0, 100.0
    math_024.width, math_024.height = 140.0, 100.0
    math_025.width, math_025.height = 140.0, 100.0
    transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
    join_geometry_008.width, join_geometry_008.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    math_019.width, math_019.height = 140.0, 100.0
    combine_xyz_015.width, combine_xyz_015.height = 140.0, 100.0
    math_020.width, math_020.height = 140.0, 100.0
    math_026.width, math_026.height = 140.0, 100.0
    math_027.width, math_027.height = 140.0, 100.0
    join_geometry_009.width, join_geometry_009.height = 140.0, 100.0
    transform_geometry_006.width, transform_geometry_006.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    math_028.width, math_028.height = 140.0, 100.0
    combine_xyz_016.width, combine_xyz_016.height = 140.0, 100.0
    math_029.width, math_029.height = 140.0, 100.0
    join_geometry_010.width, join_geometry_010.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    curve_circle_002.width, curve_circle_002.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    merge_by_distance_002.width, merge_by_distance_002.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    combine_xyz_017.width, combine_xyz_017.height = 140.0, 100.0
    math_030.width, math_030.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    math_032.width, math_032.height = 140.0, 100.0
    math_034.width, math_034.height = 140.0, 100.0
    math_035.width, math_035.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    math_038.width, math_038.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    combine_xyz_020.width, combine_xyz_020.height = 140.0, 100.0
    math_039.width, math_039.height = 140.0, 100.0
    math_040.width, math_040.height = 140.0, 100.0
    math_041.width, math_041.height = 140.0, 100.0
    mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    math_042.width, math_042.height = 140.0, 100.0
    math_043.width, math_043.height = 140.0, 100.0
    curve_line_002.width, curve_line_002.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    combine_xyz_019.width, combine_xyz_019.height = 140.0, 100.0
    combine_xyz_021.width, combine_xyz_021.height = 140.0, 100.0
    math_036.width, math_036.height = 140.0, 100.0
    curve_to_points.width, curve_to_points.height = 140.0, 100.0
    instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    combine_xyz_018.width, combine_xyz_018.height = 140.0, 100.0
    combine_xyz_024.width, combine_xyz_024.height = 140.0, 100.0
    math_033.width, math_033.height = 140.0, 100.0
    math_047.width, math_047.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    combine_xyz_025.width, combine_xyz_025.height = 140.0, 100.0
    math_048.width, math_048.height = 140.0, 100.0
    math_049.width, math_049.height = 140.0, 100.0
    realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    cylinder.width, cylinder.height = 140.0, 100.0
    join_geometry_004.width, join_geometry_004.height = 140.0, 100.0
    math_051.width, math_051.height = 140.0, 100.0
    math_031.width, math_031.height = 140.0, 100.0
    math_052.width, math_052.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    combine_xyz_026.width, combine_xyz_026.height = 140.0, 100.0
    math_053.width, math_053.height = 140.0, 100.0
    math_054.width, math_054.height = 140.0, 100.0
    math_055.width, math_055.height = 140.0, 100.0
    math_056.width, math_056.height = 140.0, 100.0
    math_057.width, math_057.height = 140.0, 100.0
    math_058.width, math_058.height = 140.0, 100.0
    math_059.width, math_059.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    frame.width, frame.height = 5438.400390625, 1282.0
    frame_001.width, frame_001.height = 4243.2001953125, 2455.599853515625
    cylinder_001.width, cylinder_001.height = 140.0, 100.0
    math_060.width, math_060.height = 140.0, 100.0
    transform_geometry_007.width, transform_geometry_007.height = 140.0, 100.0
    math_061.width, math_061.height = 140.0, 100.0
    math_062.width, math_062.height = 140.0, 100.0
    combine_xyz_027.width, combine_xyz_027.height = 140.0, 100.0
    math_063.width, math_063.height = 140.0, 100.0
    math_064.width, math_064.height = 140.0, 100.0
    transform_geometry_008.width, transform_geometry_008.height = 140.0, 100.0
    join_geometry_012.width, join_geometry_012.height = 140.0, 100.0
    combine_xyz_028.width, combine_xyz_028.height = 140.0, 100.0
    math_065.width, math_065.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    set_shade_smooth_001.width, set_shade_smooth_001.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    join_geometry_011.width, join_geometry_011.height = 140.0, 100.0
    cylinder_002.width, cylinder_002.height = 140.0, 100.0
    math_037.width, math_037.height = 140.0, 100.0
    math_044.width, math_044.height = 140.0, 100.0
    math_045.width, math_045.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    combine_xyz_029.width, combine_xyz_029.height = 140.0, 100.0
    math_046.width, math_046.height = 140.0, 100.0
    math_066.width, math_066.height = 140.0, 100.0
    set_shade_smooth_002.width, set_shade_smooth_002.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0
    combine_xyz_030.width, combine_xyz_030.height = 140.0, 100.0
    join_geometry_013.width, join_geometry_013.height = 140.0, 100.0
    math_067.width, math_067.height = 140.0, 100.0
    math_068.width, math_068.height = 140.0, 100.0
    math_069.width, math_069.height = 140.0, 100.0
    set_shade_smooth_003.width, set_shade_smooth_003.height = 140.0, 100.0
    math_070.width, math_070.height = 140.0, 100.0
    uv_sphere.width, uv_sphere.height = 140.0, 100.0
    math_071.width, math_071.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    delete_geometry_002.width, delete_geometry_002.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    set_position_004.width, set_position_004.height = 140.0, 100.0
    math_072.width, math_072.height = 140.0, 100.0
    combine_xyz_022.width, combine_xyz_022.height = 140.0, 100.0
    math_073.width, math_073.height = 140.0, 100.0
    math_074.width, math_074.height = 140.0, 100.0
    transform_geometry_009.width, transform_geometry_009.height = 140.0, 100.0
    set_shade_smooth_004.width, set_shade_smooth_004.height = 140.0, 100.0
    math_075.width, math_075.height = 140.0, 100.0
    group_input_020.width, group_input_020.height = 140.0, 100.0
    math_077.width, math_077.height = 140.0, 100.0
    math_078.width, math_078.height = 140.0, 100.0
    math_079.width, math_079.height = 140.0, 100.0
    math_080.width, math_080.height = 140.0, 100.0
    math_081.width, math_081.height = 140.0, 100.0
    curve_line_003.width, curve_line_003.height = 140.0, 100.0
    transform_geometry_010.width, transform_geometry_010.height = 140.0, 100.0
    combine_xyz_031.width, combine_xyz_031.height = 140.0, 100.0
    curve_to_points_001.width, curve_to_points_001.height = 140.0, 100.0
    math_076.width, math_076.height = 140.0, 100.0
    instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
    math_082.width, math_082.height = 140.0, 100.0
    math_083.width, math_083.height = 140.0, 100.0
    group_input_021.width, group_input_021.height = 140.0, 100.0
    math_084.width, math_084.height = 140.0, 100.0
    math_085.width, math_085.height = 140.0, 100.0
    math_086.width, math_086.height = 140.0, 100.0
    math_087.width, math_087.height = 140.0, 100.0
    math_088.width, math_088.height = 140.0, 100.0
    curve_line_004.width, curve_line_004.height = 140.0, 100.0
    transform_geometry_011.width, transform_geometry_011.height = 140.0, 100.0
    combine_xyz_032.width, combine_xyz_032.height = 140.0, 100.0
    curve_to_points_002.width, curve_to_points_002.height = 140.0, 100.0
    math_089.width, math_089.height = 140.0, 100.0
    math_091.width, math_091.height = 140.0, 100.0
    instance_on_points_003.width, instance_on_points_003.height = 140.0, 100.0
    curve_to_points_003.width, curve_to_points_003.height = 140.0, 100.0
    instance_on_points_004.width, instance_on_points_004.height = 140.0, 100.0
    transform_geometry_012.width, transform_geometry_012.height = 140.0, 100.0
    group_input_019.width, group_input_019.height = 140.0, 100.0
    combine_xyz_023.width, combine_xyz_023.height = 140.0, 100.0
    math_090.width, math_090.height = 140.0, 100.0
    math_092.width, math_092.height = 140.0, 100.0
    math_093.width, math_093.height = 140.0, 100.0
    math_094.width, math_094.height = 140.0, 100.0
    realize_instances_002.width, realize_instances_002.height = 140.0, 100.0
    realize_instances_003.width, realize_instances_003.height = 140.0, 100.0
    realize_instances_004.width, realize_instances_004.height = 140.0, 100.0
    math_095.width, math_095.height = 140.0, 100.0
    math_097.width, math_097.height = 140.0, 100.0
    math_098.width, math_098.height = 140.0, 100.0
    math_099.width, math_099.height = 140.0, 100.0
    math_100.width, math_100.height = 140.0, 100.0
    math_050.width, math_050.height = 140.0, 100.0
    math_096.width, math_096.height = 140.0, 100.0
    math_101.width, math_101.height = 140.0, 100.0
    frame_002.width, frame_002.height = 3022.39990234375, 1000.400146484375
    frame_003.width, frame_003.height = 2526.400146484375, 1102.7998046875
    frame_004.width, frame_004.height = 1276.7998046875, 753.199951171875
    frame_005.width, frame_005.height = 2799.2001953125, 898.0
    frame_006.width, frame_006.height = 2360.0, 2594.0
    frame_007.width, frame_007.height = 3000.7998046875, 928.39990234375
    frame_008.width, frame_008.height = 2223.2001953125, 781.19970703125

    # Initialize geometry_nodes links

    # math.Value -> combine_xyz.X
    geometry_nodes.links.new(math.outputs[0], combine_xyz.inputs[0])
    # group_input.net - line radius -> math.Value
    geometry_nodes.links.new(group_input.outputs[1], math.inputs[1])
    # math_001.Value -> combine_xyz_001.X
    geometry_nodes.links.new(math_001.outputs[0], combine_xyz_001.inputs[0])
    # group_input.net - line radius -> math_001.Value
    geometry_nodes.links.new(group_input.outputs[1], math_001.inputs[1])
    # combine_xyz.Vector -> b_zier_segment.Start
    geometry_nodes.links.new(combine_xyz.outputs[0], b_zier_segment.inputs[1])
    # combine_xyz_001.Vector -> b_zier_segment.End
    geometry_nodes.links.new(combine_xyz_001.outputs[0], b_zier_segment.inputs[4])
    # math_002.Value -> combine_xyz_002.Y
    geometry_nodes.links.new(math_002.outputs[0], combine_xyz_002.inputs[1])
    # group_input.net - line bend Y -> math_002.Value
    geometry_nodes.links.new(group_input.outputs[6], math_002.inputs[1])
    # combine_xyz_002.Vector -> b_zier_segment.Start Handle
    geometry_nodes.links.new(combine_xyz_002.outputs[0], b_zier_segment.inputs[2])
    # group_input.net - line bend Y -> math_003.Value
    geometry_nodes.links.new(group_input.outputs[6], math_003.inputs[1])
    # math_003.Value -> combine_xyz_003.Y
    geometry_nodes.links.new(math_003.outputs[0], combine_xyz_003.inputs[1])
    # combine_xyz_003.Vector -> b_zier_segment.End Handle
    geometry_nodes.links.new(combine_xyz_003.outputs[0], b_zier_segment.inputs[3])
    # group_input.net - line bend Z -> combine_xyz_002.Z
    geometry_nodes.links.new(group_input.outputs[7], combine_xyz_002.inputs[2])
    # group_input.net - line bend Z -> math_004.Value
    geometry_nodes.links.new(group_input.outputs[7], math_004.inputs[0])
    # math_004.Value -> combine_xyz_003.Z
    geometry_nodes.links.new(math_004.outputs[0], combine_xyz_003.inputs[2])
    # combine_xyz_001.Vector -> b_zier_segment_001.Start
    geometry_nodes.links.new(combine_xyz_001.outputs[0], b_zier_segment_001.inputs[1])
    # b_zier_segment_001.Curve -> join_geometry_002.Geometry
    geometry_nodes.links.new(b_zier_segment_001.outputs[0], join_geometry_002.inputs[0])
    # math.Value -> combine_xyz_006.X
    geometry_nodes.links.new(math.outputs[0], combine_xyz_006.inputs[0])
    # combine_xyz_006.Vector -> b_zier_segment_001.End
    geometry_nodes.links.new(combine_xyz_006.outputs[0], b_zier_segment_001.inputs[4])
    # math_002.Value -> math_005.Value
    geometry_nodes.links.new(math_002.outputs[0], math_005.inputs[0])
    # combine_xyz_004.Vector -> b_zier_segment_001.End Handle
    geometry_nodes.links.new(combine_xyz_004.outputs[0], b_zier_segment_001.inputs[3])
    # combine_xyz_005.Vector -> b_zier_segment_001.Start Handle
    geometry_nodes.links.new(combine_xyz_005.outputs[0], b_zier_segment_001.inputs[2])
    # math_005.Value -> combine_xyz_004.Y
    geometry_nodes.links.new(math_005.outputs[0], combine_xyz_004.inputs[1])
    # math_003.Value -> math_006.Value
    geometry_nodes.links.new(math_003.outputs[0], math_006.inputs[0])
    # math_006.Value -> combine_xyz_005.Y
    geometry_nodes.links.new(math_006.outputs[0], combine_xyz_005.inputs[1])
    # group_input.net - line bend Z -> combine_xyz_005.Z
    geometry_nodes.links.new(group_input.outputs[7], combine_xyz_005.inputs[2])
    # math_004.Value -> combine_xyz_004.Z
    geometry_nodes.links.new(math_004.outputs[0], combine_xyz_004.inputs[2])
    # transform_geometry_002.Geometry -> join_geometry_003.Geometry
    geometry_nodes.links.new(transform_geometry_002.outputs[0], join_geometry_003.inputs[0])
    # group_input_003.net - line radius -> curve_circle_001.Radius
    geometry_nodes.links.new(group_input_003.outputs[1], curve_circle_001.inputs[4])
    # curve_circle_001.Curve -> curve_to_mesh_001.Profile Curve
    geometry_nodes.links.new(curve_circle_001.outputs[0], curve_to_mesh_001.inputs[1])
    # group_input.net - line segment -> b_zier_segment.Resolution
    geometry_nodes.links.new(group_input.outputs[3], b_zier_segment.inputs[0])
    # group_input.net - line segment -> b_zier_segment_001.Resolution
    geometry_nodes.links.new(group_input.outputs[3], b_zier_segment_001.inputs[0])
    # math_007.Value -> combine_xyz_002.X
    geometry_nodes.links.new(math_007.outputs[0], combine_xyz_002.inputs[0])
    # math_007.Value -> combine_xyz_004.X
    geometry_nodes.links.new(math_007.outputs[0], combine_xyz_004.inputs[0])
    # math_008.Value -> combine_xyz_003.X
    geometry_nodes.links.new(math_008.outputs[0], combine_xyz_003.inputs[0])
    # math_008.Value -> combine_xyz_005.X
    geometry_nodes.links.new(math_008.outputs[0], combine_xyz_005.inputs[0])
    # group_input.net - line bend X -> math_007.Value
    geometry_nodes.links.new(group_input.outputs[5], math_007.inputs[1])
    # group_input.net - line bend X -> math_008.Value
    geometry_nodes.links.new(group_input.outputs[5], math_008.inputs[1])
    # group_input_003.net - line section segment -> curve_circle_001.Resolution
    geometry_nodes.links.new(group_input_003.outputs[2], curve_circle_001.inputs[0])
    # group_input_004.net - line radius -> math_010.Value
    geometry_nodes.links.new(group_input_004.outputs[1], math_010.inputs[0])
    # math_010.Value -> math_009.Value
    geometry_nodes.links.new(math_010.outputs[0], math_009.inputs[1])
    # math_009.Value -> combine_xyz_007.X
    geometry_nodes.links.new(math_009.outputs[0], combine_xyz_007.inputs[0])
    # combine_xyz_007.Vector -> b_zier_segment_002.Start
    geometry_nodes.links.new(combine_xyz_007.outputs[0], b_zier_segment_002.inputs[1])
    # combine_xyz_008.Vector -> b_zier_segment_002.End
    geometry_nodes.links.new(combine_xyz_008.outputs[0], b_zier_segment_002.inputs[4])
    # math_011.Value -> combine_xyz_007.Y
    geometry_nodes.links.new(math_011.outputs[0], combine_xyz_007.inputs[1])
    # group_input_004.border - bevel factor -> math_011.Value
    geometry_nodes.links.new(group_input_004.outputs[13], math_011.inputs[0])
    # math_012.Value -> combine_xyz_008.X
    geometry_nodes.links.new(math_012.outputs[0], combine_xyz_008.inputs[0])
    # math_011.Value -> math_012.Value
    geometry_nodes.links.new(math_011.outputs[0], math_012.inputs[0])
    # math_010.Value -> math_012.Value
    geometry_nodes.links.new(math_010.outputs[0], math_012.inputs[1])
    # group_input_004.border - bevel factor -> math_013.Value
    geometry_nodes.links.new(group_input_004.outputs[13], math_013.inputs[0])
    # combine_xyz_009.Vector -> b_zier_segment_002.Start Handle
    geometry_nodes.links.new(combine_xyz_009.outputs[0], b_zier_segment_002.inputs[2])
    # combine_xyz_010.Vector -> b_zier_segment_002.End Handle
    geometry_nodes.links.new(combine_xyz_010.outputs[0], b_zier_segment_002.inputs[3])
    # math_013.Value -> math_014.Value
    geometry_nodes.links.new(math_013.outputs[0], math_014.inputs[1])
    # math_014.Value -> combine_xyz_009.Y
    geometry_nodes.links.new(math_014.outputs[0], combine_xyz_009.inputs[1])
    # math_014.Value -> math_015.Value
    geometry_nodes.links.new(math_014.outputs[0], math_015.inputs[0])
    # math_010.Value -> math_015.Value
    geometry_nodes.links.new(math_010.outputs[0], math_015.inputs[1])
    # math_015.Value -> combine_xyz_010.X
    geometry_nodes.links.new(math_015.outputs[0], combine_xyz_010.inputs[0])
    # math_009.Value -> combine_xyz_009.X
    geometry_nodes.links.new(math_009.outputs[0], combine_xyz_009.inputs[0])
    # b_zier_segment_002.Curve -> transform_geometry.Geometry
    geometry_nodes.links.new(b_zier_segment_002.outputs[0], transform_geometry.inputs[0])
    # group_input_005.net - line amount X -> math_016.Value
    geometry_nodes.links.new(group_input_005.outputs[8], math_016.inputs[0])
    # math_016.Value -> combine_xyz_011.X
    geometry_nodes.links.new(math_016.outputs[0], combine_xyz_011.inputs[0])
    # combine_xyz_011.Vector -> transform_geometry.Translation
    geometry_nodes.links.new(combine_xyz_011.outputs[0], transform_geometry.inputs[1])
    # transform_geometry.Geometry -> join_geometry_001.Geometry
    geometry_nodes.links.new(transform_geometry.outputs[0], join_geometry_001.inputs[0])
    # join_geometry_001.Geometry -> transform_geometry_001.Geometry
    geometry_nodes.links.new(join_geometry_001.outputs[0], transform_geometry_001.inputs[0])
    # combine_xyz_012.Vector -> transform_geometry_001.Translation
    geometry_nodes.links.new(combine_xyz_012.outputs[0], transform_geometry_001.inputs[1])
    # group_input_005.net - line amount Y -> math_017.Value
    geometry_nodes.links.new(group_input_005.outputs[9], math_017.inputs[0])
    # math_017.Value -> combine_xyz_012.Y
    geometry_nodes.links.new(math_017.outputs[0], combine_xyz_012.inputs[1])
    # combine_xyz_008.Vector -> curve_line_001.Start
    geometry_nodes.links.new(combine_xyz_008.outputs[0], curve_line_001.inputs[0])
    # combine_xyz_007.Vector -> curve_line.Start
    geometry_nodes.links.new(combine_xyz_007.outputs[0], curve_line.inputs[0])
    # math_009.Value -> combine_xyz_013.X
    geometry_nodes.links.new(math_009.outputs[0], combine_xyz_013.inputs[0])
    # combine_xyz_013.Vector -> curve_line.End
    geometry_nodes.links.new(combine_xyz_013.outputs[0], curve_line.inputs[1])
    # join_geometry_007.Geometry -> join_geometry_006.Geometry
    geometry_nodes.links.new(join_geometry_007.outputs[0], join_geometry_006.inputs[0])
    # combine_xyz_014.Vector -> curve_line_001.End
    geometry_nodes.links.new(combine_xyz_014.outputs[0], curve_line_001.inputs[1])
    # join_geometry_009.Geometry -> join_geometry_007.Geometry
    geometry_nodes.links.new(join_geometry_009.outputs[0], join_geometry_007.inputs[0])
    # math_023.Value -> math_022.Value
    geometry_nodes.links.new(math_023.outputs[0], math_022.inputs[1])
    # math_024.Value -> math_021.Value
    geometry_nodes.links.new(math_024.outputs[0], math_021.inputs[1])
    # math_021.Value -> combine_xyz_013.Y
    geometry_nodes.links.new(math_021.outputs[0], combine_xyz_013.inputs[1])
    # math_018.Value -> math_021.Value
    geometry_nodes.links.new(math_018.outputs[0], math_021.inputs[0])
    # math_024.Value -> math_022.Value
    geometry_nodes.links.new(math_024.outputs[0], math_022.inputs[0])
    # math_022.Value -> math_025.Value
    geometry_nodes.links.new(math_022.outputs[0], math_025.inputs[1])
    # math_010.Value -> math_025.Value
    geometry_nodes.links.new(math_010.outputs[0], math_025.inputs[0])
    # math_025.Value -> combine_xyz_014.X
    geometry_nodes.links.new(math_025.outputs[0], combine_xyz_014.inputs[0])
    # group_input_006.border - bevel factor -> math_024.Value
    geometry_nodes.links.new(group_input_006.outputs[13], math_024.inputs[1])
    # curve_line.Curve -> transform_geometry_005.Geometry
    geometry_nodes.links.new(curve_line.outputs[0], transform_geometry_005.inputs[0])
    # transform_geometry_005.Geometry -> join_geometry_008.Geometry
    geometry_nodes.links.new(transform_geometry_005.outputs[0], join_geometry_008.inputs[0])
    # combine_xyz_015.Vector -> transform_geometry_005.Translation
    geometry_nodes.links.new(combine_xyz_015.outputs[0], transform_geometry_005.inputs[1])
    # group_input_007.net - line amount X -> math_020.Value
    geometry_nodes.links.new(group_input_007.outputs[8], math_020.inputs[0])
    # math_020.Value -> math_019.Value
    geometry_nodes.links.new(math_020.outputs[0], math_019.inputs[0])
    # math_019.Value -> math_026.Value
    geometry_nodes.links.new(math_019.outputs[0], math_026.inputs[1])
    # math_026.Value -> combine_xyz_015.X
    geometry_nodes.links.new(math_026.outputs[0], combine_xyz_015.inputs[0])
    # group_input_007.net - line radius -> math_027.Value
    geometry_nodes.links.new(group_input_007.outputs[1], math_027.inputs[0])
    # math_027.Value -> math_026.Value
    geometry_nodes.links.new(math_027.outputs[0], math_026.inputs[0])
    # combine_xyz_016.Vector -> transform_geometry_006.Translation
    geometry_nodes.links.new(combine_xyz_016.outputs[0], transform_geometry_006.inputs[1])
    # math_029.Value -> math_028.Value
    geometry_nodes.links.new(math_029.outputs[0], math_028.inputs[0])
    # group_input_008.net - line amount Y -> math_029.Value
    geometry_nodes.links.new(group_input_008.outputs[9], math_029.inputs[0])
    # curve_line_001.Curve -> transform_geometry_006.Geometry
    geometry_nodes.links.new(curve_line_001.outputs[0], transform_geometry_006.inputs[0])
    # transform_geometry_006.Geometry -> join_geometry_009.Geometry
    geometry_nodes.links.new(transform_geometry_006.outputs[0], join_geometry_009.inputs[0])
    # math_028.Value -> combine_xyz_016.Y
    geometry_nodes.links.new(math_028.outputs[0], combine_xyz_016.inputs[1])
    # transform_geometry_001.Geometry -> join_geometry_010.Geometry
    geometry_nodes.links.new(transform_geometry_001.outputs[0], join_geometry_010.inputs[0])
    # join_geometry_006.Geometry -> curve_to_mesh.Curve
    geometry_nodes.links.new(join_geometry_006.outputs[0], curve_to_mesh.inputs[0])
    # group_input_009.border - radius -> curve_circle_002.Radius
    geometry_nodes.links.new(group_input_009.outputs[10], curve_circle_002.inputs[4])
    # curve_circle_002.Curve -> curve_to_mesh.Profile Curve
    geometry_nodes.links.new(curve_circle_002.outputs[0], curve_to_mesh.inputs[1])
    # curve_to_mesh.Mesh -> merge_by_distance_002.Geometry
    geometry_nodes.links.new(curve_to_mesh.outputs[0], merge_by_distance_002.inputs[0])
    # group_input_009.border - merge factor -> merge_by_distance_002.Distance
    geometry_nodes.links.new(group_input_009.outputs[14], merge_by_distance_002.inputs[2])
    # group_input_006.net - line amount Y -> math_018.Value
    geometry_nodes.links.new(group_input_006.outputs[9], math_018.inputs[0])
    # group_input_006.net - line amount X -> math_023.Value
    geometry_nodes.links.new(group_input_006.outputs[8], math_023.inputs[0])
    # group_input_004.border - bevel segment -> b_zier_segment_002.Resolution
    geometry_nodes.links.new(group_input_004.outputs[12], b_zier_segment_002.inputs[0])
    # group_input_009.border - section segment -> curve_circle_002.Resolution
    geometry_nodes.links.new(group_input_009.outputs[11], curve_circle_002.inputs[0])
    # combine_xyz_017.Vector -> cube.Size
    geometry_nodes.links.new(combine_xyz_017.outputs[0], cube.inputs[0])
    # group_input_010.net - line radius -> math_030.Value
    geometry_nodes.links.new(group_input_010.outputs[1], math_030.inputs[0])
    # math_030.Value -> math_032.Value
    geometry_nodes.links.new(math_030.outputs[0], math_032.inputs[1])
    # math_032.Value -> math_034.Value
    geometry_nodes.links.new(math_032.outputs[0], math_034.inputs[0])
    # math_032.Value -> combine_xyz_017.X
    geometry_nodes.links.new(math_032.outputs[0], combine_xyz_017.inputs[0])
    # group_input_010.connect - width -> combine_xyz_017.Y
    geometry_nodes.links.new(group_input_010.outputs[15], combine_xyz_017.inputs[1])
    # group_input_010.border - radius -> math_035.Value
    geometry_nodes.links.new(group_input_010.outputs[10], math_035.inputs[0])
    # math_035.Value -> combine_xyz_017.Z
    geometry_nodes.links.new(math_035.outputs[0], combine_xyz_017.inputs[2])
    # math_038.Value -> grid.Size X
    geometry_nodes.links.new(math_038.outputs[0], grid.inputs[0])
    # grid.Mesh -> set_position_002.Geometry
    geometry_nodes.links.new(grid.outputs[0], set_position_002.inputs[0])
    # group_input_012.net - line amount X -> combine_xyz_020.X
    geometry_nodes.links.new(group_input_012.outputs[8], combine_xyz_020.inputs[0])
    # combine_xyz_020.Vector -> set_position_002.Offset
    geometry_nodes.links.new(combine_xyz_020.outputs[0], set_position_002.inputs[3])
    # group_input_012.net - line amount X -> math_039.Value
    geometry_nodes.links.new(group_input_012.outputs[8], math_039.inputs[0])
    # math_039.Value -> math_038.Value
    geometry_nodes.links.new(math_039.outputs[0], math_038.inputs[0])
    # math_041.Value -> math_040.Value
    geometry_nodes.links.new(math_041.outputs[0], math_040.inputs[0])
    # group_input_012.net - line amount Y -> math_041.Value
    geometry_nodes.links.new(group_input_012.outputs[9], math_041.inputs[0])
    # math_040.Value -> grid.Size Y
    geometry_nodes.links.new(math_040.outputs[0], grid.inputs[1])
    # group_input_012.net - line amount Y -> combine_xyz_020.Y
    geometry_nodes.links.new(group_input_012.outputs[9], combine_xyz_020.inputs[1])
    # set_position_002.Geometry -> mesh_to_points.Mesh
    geometry_nodes.links.new(set_position_002.outputs[0], mesh_to_points.inputs[0])
    # mesh_to_points.Points -> instance_on_points.Points
    geometry_nodes.links.new(mesh_to_points.outputs[0], instance_on_points.inputs[0])
    # group_input_012.net - line amount X -> math_042.Value
    geometry_nodes.links.new(group_input_012.outputs[8], math_042.inputs[0])
    # math_042.Value -> grid.Vertices X
    geometry_nodes.links.new(math_042.outputs[0], grid.inputs[2])
    # group_input_012.net - line amount Y -> math_043.Value
    geometry_nodes.links.new(group_input_012.outputs[9], math_043.inputs[0])
    # math_043.Value -> grid.Vertices Y
    geometry_nodes.links.new(math_043.outputs[0], grid.inputs[3])
    # combine_xyz_007.Vector -> vector_math.Vector
    geometry_nodes.links.new(combine_xyz_007.outputs[0], vector_math.inputs[0])
    # vector_math.Vector -> curve_line_002.Start
    geometry_nodes.links.new(vector_math.outputs[0], curve_line_002.inputs[0])
    # combine_xyz_013.Vector -> vector_math_001.Vector
    geometry_nodes.links.new(combine_xyz_013.outputs[0], vector_math_001.inputs[0])
    # vector_math_001.Vector -> curve_line_002.End
    geometry_nodes.links.new(vector_math_001.outputs[0], curve_line_002.inputs[1])
    # group_input_010.connect - offset -> combine_xyz_019.Y
    geometry_nodes.links.new(group_input_010.outputs[17], combine_xyz_019.inputs[1])
    # math_034.Value -> combine_xyz_019.X
    geometry_nodes.links.new(math_034.outputs[0], combine_xyz_019.inputs[0])
    # group_input_010.connect - offset -> combine_xyz_021.Y
    geometry_nodes.links.new(group_input_010.outputs[17], combine_xyz_021.inputs[1])
    # math_032.Value -> math_036.Value
    geometry_nodes.links.new(math_032.outputs[0], math_036.inputs[0])
    # math_036.Value -> combine_xyz_021.X
    geometry_nodes.links.new(math_036.outputs[0], combine_xyz_021.inputs[0])
    # combine_xyz_021.Vector -> vector_math.Vector
    geometry_nodes.links.new(combine_xyz_021.outputs[0], vector_math.inputs[1])
    # combine_xyz_019.Vector -> vector_math_001.Vector
    geometry_nodes.links.new(combine_xyz_019.outputs[0], vector_math_001.inputs[1])
    # curve_to_points.Points -> instance_on_points_001.Points
    geometry_nodes.links.new(curve_to_points.outputs[0], instance_on_points_001.inputs[0])
    # combine_xyz_018.Vector -> transform_geometry_003.Translation
    geometry_nodes.links.new(combine_xyz_018.outputs[0], transform_geometry_003.inputs[1])
    # curve_to_mesh_001.Mesh -> instance_on_points.Instance
    geometry_nodes.links.new(curve_to_mesh_001.outputs[0], instance_on_points.inputs[2])
    # group_input_014.net - line merge factor -> merge_by_distance_001.Distance
    geometry_nodes.links.new(group_input_014.outputs[4], merge_by_distance_001.inputs[2])
    # instance_on_points.Instances -> realize_instances.Geometry
    geometry_nodes.links.new(instance_on_points.outputs[0], realize_instances.inputs[0])
    # realize_instances.Geometry -> merge_by_distance_001.Geometry
    geometry_nodes.links.new(realize_instances.outputs[0], merge_by_distance_001.inputs[0])
    # join_geometry_002.Geometry -> curve_to_mesh_001.Curve
    geometry_nodes.links.new(join_geometry_002.outputs[0], curve_to_mesh_001.inputs[0])
    # merge_by_distance_001.Geometry -> transform_geometry_002.Geometry
    geometry_nodes.links.new(merge_by_distance_001.outputs[0], transform_geometry_002.inputs[0])
    # group_input_014.net - line amount X -> math_048.Value
    geometry_nodes.links.new(group_input_014.outputs[8], math_048.inputs[0])
    # math_048.Value -> combine_xyz_025.X
    geometry_nodes.links.new(math_048.outputs[0], combine_xyz_025.inputs[0])
    # combine_xyz_025.Vector -> transform_geometry_002.Translation
    geometry_nodes.links.new(combine_xyz_025.outputs[0], transform_geometry_002.inputs[1])
    # group_input_014.net - line amount Y -> math_049.Value
    geometry_nodes.links.new(group_input_014.outputs[9], math_049.inputs[0])
    # math_049.Value -> combine_xyz_025.Y
    geometry_nodes.links.new(math_049.outputs[0], combine_xyz_025.inputs[1])
    # instance_on_points_001.Instances -> realize_instances_001.Geometry
    geometry_nodes.links.new(instance_on_points_001.outputs[0], realize_instances_001.inputs[0])
    # combine_xyz_024.Vector -> transform_geometry_004.Scale
    geometry_nodes.links.new(combine_xyz_024.outputs[0], transform_geometry_004.inputs[3])
    # join_geometry.Geometry -> transform_geometry_003.Geometry
    geometry_nodes.links.new(join_geometry.outputs[0], transform_geometry_003.inputs[0])
    # group_input_013.height above ground -> math_051.Value
    geometry_nodes.links.new(group_input_013.outputs[18], math_051.inputs[0])
    # math_051.Value -> combine_xyz_018.Z
    geometry_nodes.links.new(math_051.outputs[0], combine_xyz_018.inputs[2])
    # math_054.Value -> math_031.Value
    geometry_nodes.links.new(math_054.outputs[0], math_031.inputs[0])
    # math_031.Value -> math_052.Value
    geometry_nodes.links.new(math_031.outputs[0], math_052.inputs[0])
    # math_056.Value -> cylinder.Depth
    geometry_nodes.links.new(math_056.outputs[0], cylinder.inputs[4])
    # combine_xyz_026.Vector -> set_position.Offset
    geometry_nodes.links.new(combine_xyz_026.outputs[0], set_position.inputs[3])
    # math_052.Value -> math_056.Value
    geometry_nodes.links.new(math_052.outputs[0], math_056.inputs[0])
    # math_055.Value -> math_056.Value
    geometry_nodes.links.new(math_055.outputs[0], math_056.inputs[1])
    # math_056.Value -> math_053.Value
    geometry_nodes.links.new(math_056.outputs[0], math_053.inputs[0])
    # group_input_013.pillar - radius -> math_057.Value
    geometry_nodes.links.new(group_input_013.outputs[19], math_057.inputs[0])
    # group_input_013.border - radius -> math_058.Value
    geometry_nodes.links.new(group_input_013.outputs[10], math_058.inputs[0])
    # math_058.Value -> math_057.Value
    geometry_nodes.links.new(math_058.outputs[0], math_057.inputs[1])
    # math_057.Value -> math_059.Value
    geometry_nodes.links.new(math_057.outputs[0], math_059.inputs[0])
    # math_059.Value -> combine_xyz_018.X
    geometry_nodes.links.new(math_059.outputs[0], combine_xyz_018.inputs[0])
    # group_input_015.overall height -> math_033.Value
    geometry_nodes.links.new(group_input_015.outputs[21], math_033.inputs[0])
    # group_input_015.net - line amount Y -> math_047.Value
    geometry_nodes.links.new(group_input_015.outputs[9], math_047.inputs[0])
    # group_input_016.pillar - section segment -> cylinder.Vertices
    geometry_nodes.links.new(group_input_016.outputs[20], cylinder.inputs[0])
    # group_input_016.pillar - radius -> cylinder.Radius
    geometry_nodes.links.new(group_input_016.outputs[19], cylinder.inputs[3])
    # group_input_016.height above ground -> math_052.Value
    geometry_nodes.links.new(group_input_016.outputs[18], math_052.inputs[1])
    # group_input_016.net - line amount Y -> math_054.Value
    geometry_nodes.links.new(group_input_016.outputs[9], math_054.inputs[0])
    # group_input_016.border - radius -> math_055.Value
    geometry_nodes.links.new(group_input_016.outputs[10], math_055.inputs[0])
    # math_060.Value -> cylinder_001.Radius
    geometry_nodes.links.new(math_060.outputs[0], cylinder_001.inputs[3])
    # math_032.Value -> math_061.Value
    geometry_nodes.links.new(math_032.outputs[0], math_061.inputs[0])
    # math_061.Value -> math_062.Value
    geometry_nodes.links.new(math_061.outputs[0], math_062.inputs[0])
    # combine_xyz_027.Vector -> transform_geometry_007.Translation
    geometry_nodes.links.new(combine_xyz_027.outputs[0], transform_geometry_007.inputs[1])
    # math_062.Value -> math_063.Value
    geometry_nodes.links.new(math_062.outputs[0], math_063.inputs[0])
    # math_035.Value -> math_063.Value
    geometry_nodes.links.new(math_035.outputs[0], math_063.inputs[1])
    # math_063.Value -> combine_xyz_027.X
    geometry_nodes.links.new(math_063.outputs[0], combine_xyz_027.inputs[0])
    # math_035.Value -> math_064.Value
    geometry_nodes.links.new(math_035.outputs[0], math_064.inputs[0])
    # math_064.Value -> math_060.Value
    geometry_nodes.links.new(math_064.outputs[0], math_060.inputs[1])
    # curve_line_002.Curve -> curve_to_points.Curve
    geometry_nodes.links.new(curve_line_002.outputs[0], curve_to_points.inputs[0])
    # realize_instances_001.Geometry -> transform_geometry_008.Geometry
    geometry_nodes.links.new(realize_instances_001.outputs[0], transform_geometry_008.inputs[0])
    # transform_geometry_008.Geometry -> join_geometry_012.Geometry
    geometry_nodes.links.new(transform_geometry_008.outputs[0], join_geometry_012.inputs[0])
    # join_geometry_012.Geometry -> join_geometry.Geometry
    geometry_nodes.links.new(join_geometry_012.outputs[0], join_geometry.inputs[0])
    # combine_xyz_028.Vector -> transform_geometry_008.Translation
    geometry_nodes.links.new(combine_xyz_028.outputs[0], transform_geometry_008.inputs[1])
    # math_065.Value -> combine_xyz_028.X
    geometry_nodes.links.new(math_065.outputs[0], combine_xyz_028.inputs[0])
    # cylinder_001.Mesh -> set_shade_smooth.Geometry
    geometry_nodes.links.new(cylinder_001.outputs[0], set_shade_smooth.inputs[0])
    # cylinder_001.Side -> set_shade_smooth.Selection
    geometry_nodes.links.new(cylinder_001.outputs[2], set_shade_smooth.inputs[1])
    # set_shade_smooth.Geometry -> transform_geometry_007.Geometry
    geometry_nodes.links.new(set_shade_smooth.outputs[0], transform_geometry_007.inputs[0])
    # cylinder.Side -> set_shade_smooth_001.Selection
    geometry_nodes.links.new(cylinder.outputs[2], set_shade_smooth_001.inputs[1])
    # cylinder.Mesh -> delete_geometry.Geometry
    geometry_nodes.links.new(cylinder.outputs[0], delete_geometry.inputs[0])
    # delete_geometry.Geometry -> set_shade_smooth_001.Geometry
    geometry_nodes.links.new(delete_geometry.outputs[0], set_shade_smooth_001.inputs[0])
    # math_037.Value -> cylinder_002.Depth
    geometry_nodes.links.new(math_037.outputs[0], cylinder_002.inputs[4])
    # set_shade_smooth_001.Geometry -> set_position.Geometry
    geometry_nodes.links.new(set_shade_smooth_001.outputs[0], set_position.inputs[0])
    # math_044.Value -> math_045.Value
    geometry_nodes.links.new(math_044.outputs[0], math_045.inputs[0])
    # math_045.Value -> cylinder_002.Radius
    geometry_nodes.links.new(math_045.outputs[0], cylinder_002.inputs[3])
    # combine_xyz_029.Vector -> set_position_001.Offset
    geometry_nodes.links.new(combine_xyz_029.outputs[0], set_position_001.inputs[3])
    # math_037.Value -> math_046.Value
    geometry_nodes.links.new(math_037.outputs[0], math_046.inputs[0])
    # math_046.Value -> combine_xyz_029.Z
    geometry_nodes.links.new(math_046.outputs[0], combine_xyz_029.inputs[2])
    # math_053.Value -> math_066.Value
    geometry_nodes.links.new(math_053.outputs[0], math_066.inputs[0])
    # math_037.Value -> math_066.Value
    geometry_nodes.links.new(math_037.outputs[0], math_066.inputs[1])
    # math_066.Value -> combine_xyz_026.Z
    geometry_nodes.links.new(math_066.outputs[0], combine_xyz_026.inputs[2])
    # delete_geometry_001.Geometry -> set_shade_smooth_002.Geometry
    geometry_nodes.links.new(delete_geometry_001.outputs[0], set_shade_smooth_002.inputs[0])
    # set_shade_smooth_002.Geometry -> set_position_001.Geometry
    geometry_nodes.links.new(set_shade_smooth_002.outputs[0], set_position_001.inputs[0])
    # cylinder_002.Mesh -> delete_geometry_001.Geometry
    geometry_nodes.links.new(cylinder_002.outputs[0], delete_geometry_001.inputs[0])
    # cylinder_002.Side -> set_shade_smooth_002.Selection
    geometry_nodes.links.new(cylinder_002.outputs[2], set_shade_smooth_002.inputs[1])
    # cylinder_002.Bottom -> delete_geometry_001.Selection
    geometry_nodes.links.new(cylinder_002.outputs[3], delete_geometry_001.inputs[1])
    # set_shade_smooth_003.Geometry -> set_position_003.Geometry
    geometry_nodes.links.new(set_shade_smooth_003.outputs[0], set_position_003.inputs[0])
    # combine_xyz_030.Vector -> set_position_003.Offset
    geometry_nodes.links.new(combine_xyz_030.outputs[0], set_position_003.inputs[3])
    # set_position_003.Geometry -> join_geometry_013.Geometry
    geometry_nodes.links.new(set_position_003.outputs[0], join_geometry_013.inputs[0])
    # math_068.Value -> math_067.Value
    geometry_nodes.links.new(math_068.outputs[0], math_067.inputs[0])
    # math_069.Value -> combine_xyz_030.Z
    geometry_nodes.links.new(math_069.outputs[0], combine_xyz_030.inputs[2])
    # math_067.Value -> math_069.Value
    geometry_nodes.links.new(math_067.outputs[0], math_069.inputs[0])
    # cylinder_002.Mesh -> set_shade_smooth_003.Geometry
    geometry_nodes.links.new(cylinder_002.outputs[0], set_shade_smooth_003.inputs[0])
    # cylinder_002.Side -> set_shade_smooth_003.Selection
    geometry_nodes.links.new(cylinder_002.outputs[2], set_shade_smooth_003.inputs[1])
    # cylinder.Top -> math_070.Value
    geometry_nodes.links.new(cylinder.outputs[1], math_070.inputs[0])
    # cylinder.Bottom -> math_070.Value
    geometry_nodes.links.new(cylinder.outputs[3], math_070.inputs[1])
    # math_070.Value -> delete_geometry.Selection
    geometry_nodes.links.new(math_070.outputs[0], delete_geometry.inputs[1])
    # math_071.Value -> uv_sphere.Rings
    geometry_nodes.links.new(math_071.outputs[0], uv_sphere.inputs[1])
    # group_input_017.pillar - section segment -> uv_sphere.Segments
    geometry_nodes.links.new(group_input_017.outputs[20], uv_sphere.inputs[0])
    # group_input_017.pillar - section segment -> math_071.Value
    geometry_nodes.links.new(group_input_017.outputs[20], math_071.inputs[0])
    # group_input_017.pillar - radius -> uv_sphere.Radius
    geometry_nodes.links.new(group_input_017.outputs[19], uv_sphere.inputs[2])
    # group_input_018.connect - width -> math_037.Value
    geometry_nodes.links.new(group_input_018.outputs[15], math_037.inputs[0])
    # group_input_018.connect - width -> math_069.Value
    geometry_nodes.links.new(group_input_018.outputs[15], math_069.inputs[1])
    # group_input_018.pillar - section segment -> cylinder_002.Vertices
    geometry_nodes.links.new(group_input_018.outputs[20], cylinder_002.inputs[0])
    # group_input_018.net - line amount Y -> math_068.Value
    geometry_nodes.links.new(group_input_018.outputs[9], math_068.inputs[0])
    # group_input_018.border - radius -> math_044.Value
    geometry_nodes.links.new(group_input_018.outputs[10], math_044.inputs[0])
    # group_input_018.pillar - radius -> math_045.Value
    geometry_nodes.links.new(group_input_018.outputs[19], math_045.inputs[1])
    # uv_sphere.Mesh -> delete_geometry_002.Geometry
    geometry_nodes.links.new(uv_sphere.outputs[0], delete_geometry_002.inputs[0])
    # normal.Normal -> separate_xyz.Vector
    geometry_nodes.links.new(normal.outputs[0], separate_xyz.inputs[0])
    # separate_xyz.Z -> compare.A
    geometry_nodes.links.new(separate_xyz.outputs[2], compare.inputs[0])
    # compare.Result -> delete_geometry_002.Selection
    geometry_nodes.links.new(compare.outputs[0], delete_geometry_002.inputs[1])
    # math_037.Value -> math_072.Value
    geometry_nodes.links.new(math_037.outputs[0], math_072.inputs[1])
    # math_072.Value -> combine_xyz_022.Z
    geometry_nodes.links.new(math_072.outputs[0], combine_xyz_022.inputs[2])
    # combine_xyz_022.Vector -> set_position_004.Offset
    geometry_nodes.links.new(combine_xyz_022.outputs[0], set_position_004.inputs[3])
    # group_input_017.net - line amount Y -> math_074.Value
    geometry_nodes.links.new(group_input_017.outputs[9], math_074.inputs[0])
    # math_074.Value -> math_073.Value
    geometry_nodes.links.new(math_074.outputs[0], math_073.inputs[0])
    # math_056.Value -> math_072.Value
    geometry_nodes.links.new(math_056.outputs[0], math_072.inputs[0])
    # transform_geometry_009.Geometry -> set_position_004.Geometry
    geometry_nodes.links.new(transform_geometry_009.outputs[0], set_position_004.inputs[0])
    # delete_geometry_002.Geometry -> set_shade_smooth_004.Geometry
    geometry_nodes.links.new(delete_geometry_002.outputs[0], set_shade_smooth_004.inputs[0])
    # set_shade_smooth_004.Geometry -> transform_geometry_009.Geometry
    geometry_nodes.links.new(set_shade_smooth_004.outputs[0], transform_geometry_009.inputs[0])
    # group_input_020.pillar - radius -> math_077.Value
    geometry_nodes.links.new(group_input_020.outputs[19], math_077.inputs[0])
    # group_input_020.border - radius -> math_078.Value
    geometry_nodes.links.new(group_input_020.outputs[10], math_078.inputs[0])
    # math_078.Value -> math_077.Value
    geometry_nodes.links.new(math_078.outputs[0], math_077.inputs[1])
    # math_077.Value -> math_079.Value
    geometry_nodes.links.new(math_077.outputs[0], math_079.inputs[0])
    # math_075.Value -> math_080.Value
    geometry_nodes.links.new(math_075.outputs[0], math_080.inputs[1])
    # math_079.Value -> math_081.Value
    geometry_nodes.links.new(math_079.outputs[0], math_081.inputs[0])
    # math_081.Value -> math_080.Value
    geometry_nodes.links.new(math_081.outputs[0], math_080.inputs[0])
    # group_input_020.net - line amount X -> math_075.Value
    geometry_nodes.links.new(group_input_020.outputs[8], math_075.inputs[0])
    # curve_line_003.Curve -> transform_geometry_010.Geometry
    geometry_nodes.links.new(curve_line_003.outputs[0], transform_geometry_010.inputs[0])
    # combine_xyz_031.Vector -> curve_line_003.End
    geometry_nodes.links.new(combine_xyz_031.outputs[0], curve_line_003.inputs[1])
    # transform_geometry_010.Geometry -> curve_to_points_001.Curve
    geometry_nodes.links.new(transform_geometry_010.outputs[0], curve_to_points_001.inputs[0])
    # math_080.Value -> math_076.Value
    geometry_nodes.links.new(math_080.outputs[0], math_076.inputs[0])
    # group_input_020.overall amount -> math_076.Value
    geometry_nodes.links.new(group_input_020.outputs[22], math_076.inputs[1])
    # curve_to_points_001.Points -> instance_on_points_002.Points
    geometry_nodes.links.new(curve_to_points_001.outputs[0], instance_on_points_002.inputs[0])
    # join_geometry_011.Geometry -> instance_on_points_002.Instance
    geometry_nodes.links.new(join_geometry_011.outputs[0], instance_on_points_002.inputs[2])
    # math_076.Value -> combine_xyz_031.Z
    geometry_nodes.links.new(math_076.outputs[0], combine_xyz_031.inputs[2])
    # realize_instances_004.Geometry -> join_geometry_004.Geometry
    geometry_nodes.links.new(realize_instances_004.outputs[0], join_geometry_004.inputs[0])
    # group_input_020.overall amount -> math_082.Value
    geometry_nodes.links.new(group_input_020.outputs[22], math_082.inputs[0])
    # math_082.Value -> curve_to_points_001.Count
    geometry_nodes.links.new(math_082.outputs[0], curve_to_points_001.inputs[1])
    # group_input_021.pillar - radius -> math_084.Value
    geometry_nodes.links.new(group_input_021.outputs[19], math_084.inputs[0])
    # group_input_021.border - radius -> math_085.Value
    geometry_nodes.links.new(group_input_021.outputs[10], math_085.inputs[0])
    # math_085.Value -> math_084.Value
    geometry_nodes.links.new(math_085.outputs[0], math_084.inputs[1])
    # math_084.Value -> math_086.Value
    geometry_nodes.links.new(math_084.outputs[0], math_086.inputs[0])
    # math_083.Value -> math_087.Value
    geometry_nodes.links.new(math_083.outputs[0], math_087.inputs[1])
    # math_086.Value -> math_088.Value
    geometry_nodes.links.new(math_086.outputs[0], math_088.inputs[0])
    # math_088.Value -> math_087.Value
    geometry_nodes.links.new(math_088.outputs[0], math_087.inputs[0])
    # group_input_021.net - line amount X -> math_083.Value
    geometry_nodes.links.new(group_input_021.outputs[8], math_083.inputs[0])
    # curve_line_004.Curve -> transform_geometry_011.Geometry
    geometry_nodes.links.new(curve_line_004.outputs[0], transform_geometry_011.inputs[0])
    # combine_xyz_032.Vector -> curve_line_004.End
    geometry_nodes.links.new(combine_xyz_032.outputs[0], curve_line_004.inputs[1])
    # transform_geometry_011.Geometry -> curve_to_points_002.Curve
    geometry_nodes.links.new(transform_geometry_011.outputs[0], curve_to_points_002.inputs[0])
    # math_087.Value -> math_089.Value
    geometry_nodes.links.new(math_087.outputs[0], math_089.inputs[0])
    # math_089.Value -> combine_xyz_032.Z
    geometry_nodes.links.new(math_089.outputs[0], combine_xyz_032.inputs[2])
    # group_input_021.overall amount -> math_091.Value
    geometry_nodes.links.new(group_input_021.outputs[22], math_091.inputs[0])
    # math_091.Value -> math_089.Value
    geometry_nodes.links.new(math_091.outputs[0], math_089.inputs[1])
    # group_input_021.overall amount -> curve_to_points_002.Count
    geometry_nodes.links.new(group_input_021.outputs[22], curve_to_points_002.inputs[1])
    # curve_to_points_002.Points -> instance_on_points_003.Points
    geometry_nodes.links.new(curve_to_points_002.outputs[0], instance_on_points_003.inputs[0])
    # transform_geometry_003.Geometry -> instance_on_points_003.Instance
    geometry_nodes.links.new(transform_geometry_003.outputs[0], instance_on_points_003.inputs[2])
    # cube.Mesh -> instance_on_points_001.Instance
    geometry_nodes.links.new(cube.outputs[0], instance_on_points_001.inputs[2])
    # curve_line_002.Curve -> curve_to_points_003.Curve
    geometry_nodes.links.new(curve_line_002.outputs[0], curve_to_points_003.inputs[0])
    # curve_to_points_003.Points -> instance_on_points_004.Points
    geometry_nodes.links.new(curve_to_points_003.outputs[0], instance_on_points_004.inputs[0])
    # transform_geometry_007.Geometry -> instance_on_points_004.Instance
    geometry_nodes.links.new(transform_geometry_007.outputs[0], instance_on_points_004.inputs[2])
    # combine_xyz_023.Vector -> transform_geometry_012.Translation
    geometry_nodes.links.new(combine_xyz_023.outputs[0], transform_geometry_012.inputs[1])
    # group_input_019.height above ground -> math_090.Value
    geometry_nodes.links.new(group_input_019.outputs[18], math_090.inputs[0])
    # math_090.Value -> combine_xyz_023.Z
    geometry_nodes.links.new(math_090.outputs[0], combine_xyz_023.inputs[2])
    # group_input_019.pillar - radius -> math_092.Value
    geometry_nodes.links.new(group_input_019.outputs[19], math_092.inputs[0])
    # group_input_019.border - radius -> math_093.Value
    geometry_nodes.links.new(group_input_019.outputs[10], math_093.inputs[0])
    # math_093.Value -> math_092.Value
    geometry_nodes.links.new(math_093.outputs[0], math_092.inputs[1])
    # math_092.Value -> math_094.Value
    geometry_nodes.links.new(math_092.outputs[0], math_094.inputs[0])
    # math_094.Value -> combine_xyz_023.X
    geometry_nodes.links.new(math_094.outputs[0], combine_xyz_023.inputs[0])
    # group_input_019.pillar - radius -> math_060.Value
    geometry_nodes.links.new(group_input_019.outputs[19], math_060.inputs[0])
    # group_input_019.connect - width -> cylinder_001.Depth
    geometry_nodes.links.new(group_input_019.outputs[15], cylinder_001.inputs[4])
    # group_input_019.pillar - section segment -> cylinder_001.Vertices
    geometry_nodes.links.new(group_input_019.outputs[20], cylinder_001.inputs[0])
    # group_input_019.pillar - radius -> math_062.Value
    geometry_nodes.links.new(group_input_019.outputs[19], math_062.inputs[1])
    # group_input_010.connect - amount -> curve_to_points.Count
    geometry_nodes.links.new(group_input_010.outputs[16], curve_to_points.inputs[1])
    # group_input_010.net - line amount X -> math_065.Value
    geometry_nodes.links.new(group_input_010.outputs[8], math_065.inputs[0])
    # group_input_019.connect - amount -> curve_to_points_003.Count
    geometry_nodes.links.new(group_input_019.outputs[16], curve_to_points_003.inputs[1])
    # join_geometry_013.Geometry -> join_geometry_011.Geometry
    geometry_nodes.links.new(join_geometry_013.outputs[0], join_geometry_011.inputs[0])
    # instance_on_points_004.Instances -> realize_instances_002.Geometry
    geometry_nodes.links.new(instance_on_points_004.outputs[0], realize_instances_002.inputs[0])
    # realize_instances_002.Geometry -> transform_geometry_012.Geometry
    geometry_nodes.links.new(realize_instances_002.outputs[0], transform_geometry_012.inputs[0])
    # instance_on_points_003.Instances -> realize_instances_003.Geometry
    geometry_nodes.links.new(instance_on_points_003.outputs[0], realize_instances_003.inputs[0])
    # instance_on_points_002.Instances -> realize_instances_004.Geometry
    geometry_nodes.links.new(instance_on_points_002.outputs[0], realize_instances_004.inputs[0])
    # join_geometry_004.Geometry -> transform_geometry_004.Geometry
    geometry_nodes.links.new(join_geometry_004.outputs[0], transform_geometry_004.inputs[0])
    # transform_geometry_004.Geometry -> group_output.Geometry
    geometry_nodes.links.new(transform_geometry_004.outputs[0], group_output.inputs[0])
    # group_input_015.height above ground -> math_095.Value
    geometry_nodes.links.new(group_input_015.outputs[18], math_095.inputs[1])
    # math_095.Value -> math_097.Value
    geometry_nodes.links.new(math_095.outputs[0], math_097.inputs[0])
    # group_input_015.pillar - radius -> math_098.Value
    geometry_nodes.links.new(group_input_015.outputs[19], math_098.inputs[0])
    # math_101.Value -> math_099.Value
    geometry_nodes.links.new(math_101.outputs[0], math_099.inputs[0])
    # math_098.Value -> math_099.Value
    geometry_nodes.links.new(math_098.outputs[0], math_099.inputs[1])
    # math_047.Value -> math_100.Value
    geometry_nodes.links.new(math_047.outputs[0], math_100.inputs[0])
    # math_033.Value -> combine_xyz_024.X
    geometry_nodes.links.new(math_033.outputs[0], combine_xyz_024.inputs[0])
    # math_033.Value -> combine_xyz_024.Y
    geometry_nodes.links.new(math_033.outputs[0], combine_xyz_024.inputs[1])
    # math_033.Value -> combine_xyz_024.Z
    geometry_nodes.links.new(math_033.outputs[0], combine_xyz_024.inputs[2])
    # math_100.Value -> math_095.Value
    geometry_nodes.links.new(math_100.outputs[0], math_095.inputs[0])
    # group_input_015.border - radius -> math_050.Value
    geometry_nodes.links.new(group_input_015.outputs[10], math_050.inputs[0])
    # math_050.Value -> math_097.Value
    geometry_nodes.links.new(math_050.outputs[0], math_097.inputs[1])
    # math_099.Value -> math_033.Value
    geometry_nodes.links.new(math_099.outputs[0], math_033.inputs[1])
    # group_input_015.connect - width -> math_096.Value
    geometry_nodes.links.new(group_input_015.outputs[15], math_096.inputs[0])
    # math_097.Value -> math_101.Value
    geometry_nodes.links.new(math_097.outputs[0], math_101.inputs[0])
    # math_096.Value -> math_101.Value
    geometry_nodes.links.new(math_096.outputs[0], math_101.inputs[1])
    # b_zier_segment.Curve -> join_geometry_002.Geometry
    geometry_nodes.links.new(b_zier_segment.outputs[0], join_geometry_002.inputs[0])
    # b_zier_segment_002.Curve -> join_geometry_001.Geometry
    geometry_nodes.links.new(b_zier_segment_002.outputs[0], join_geometry_001.inputs[0])
    # curve_line.Curve -> join_geometry_008.Geometry
    geometry_nodes.links.new(curve_line.outputs[0], join_geometry_008.inputs[0])
    # join_geometry_008.Geometry -> join_geometry_007.Geometry
    geometry_nodes.links.new(join_geometry_008.outputs[0], join_geometry_007.inputs[0])
    # curve_line_001.Curve -> join_geometry_009.Geometry
    geometry_nodes.links.new(curve_line_001.outputs[0], join_geometry_009.inputs[0])
    # join_geometry_001.Geometry -> join_geometry_010.Geometry
    geometry_nodes.links.new(join_geometry_001.outputs[0], join_geometry_010.inputs[0])
    # join_geometry_010.Geometry -> join_geometry_006.Geometry
    geometry_nodes.links.new(join_geometry_010.outputs[0], join_geometry_006.inputs[0])
    # merge_by_distance_002.Geometry -> join_geometry.Geometry
    geometry_nodes.links.new(merge_by_distance_002.outputs[0], join_geometry.inputs[0])
    # merge_by_distance_001.Geometry -> join_geometry_003.Geometry
    geometry_nodes.links.new(merge_by_distance_001.outputs[0], join_geometry_003.inputs[0])
    # realize_instances_001.Geometry -> join_geometry_012.Geometry
    geometry_nodes.links.new(realize_instances_001.outputs[0], join_geometry_012.inputs[0])
    # set_position_001.Geometry -> join_geometry_013.Geometry
    geometry_nodes.links.new(set_position_001.outputs[0], join_geometry_013.inputs[0])
    # realize_instances_003.Geometry -> join_geometry_004.Geometry
    geometry_nodes.links.new(realize_instances_003.outputs[0], join_geometry_004.inputs[0])
    # transform_geometry_012.Geometry -> join_geometry_011.Geometry
    geometry_nodes.links.new(transform_geometry_012.outputs[0], join_geometry_011.inputs[0])
    # join_geometry_003.Geometry -> join_geometry.Geometry
    geometry_nodes.links.new(join_geometry_003.outputs[0], join_geometry.inputs[0])
    # set_position_004.Geometry -> join_geometry_011.Geometry
    geometry_nodes.links.new(set_position_004.outputs[0], join_geometry_011.inputs[0])
    # set_position.Geometry -> join_geometry_011.Geometry
    geometry_nodes.links.new(set_position.outputs[0], join_geometry_011.inputs[0])

    return geometry_nodes

