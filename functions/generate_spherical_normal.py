import bpy
from ..ngs.spherical_normal import spherical_normal_base_node_group

def generate_spherical_normal(obj, group_type, node_num):
    has_same_node_group = False
    for node_group in bpy.data.node_groups:
        if node_group.type == 'GEOMETRY' and node_group.name == f"{obj.name}_SN":
            has_same_node_group = True
            break
    
    if has_same_node_group:
        geo_nodes_mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
        geo_nodes_mod.node_group = bpy.data.node_groups.get(f"{obj.name}_SN")
    else:
        geometry_nodes = spherical_normal_base_node_group(obj, group_type, node_num)
        geo_nodes_mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
        geo_nodes_mod.node_group = geometry_nodes