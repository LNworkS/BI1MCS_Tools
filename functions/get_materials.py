import bpy

def get_materials(obj, onlyfirst):
    """return a list, The onlyfirst parameter is of Boolean type."""
    material_var = []
    has_valid_material = any(mat is not None for mat in obj.data.materials)
    if has_valid_material:
        # if has valid material，if onlyfirst is True, get the first valid material, else, get all
        if onlyfirst:
            material_var = [obj.data.materials[0]]
        else:
            material_var = obj.data.materials
        return material_var
    else:
        # If there is no material, create a default material
        default_mat = bpy.data.materials.new(name = obj.name + '_Material')
        # Configure the default material (use the node system to set basic properties)
        default_mat.use_nodes = True
        nodes = default_mat.node_tree.nodes
        links = default_mat.node_tree.links
         # Clear default nodes (Blender comes with some nodes when a new material is created; reconfigure here)
        for node in nodes:
            nodes.remove(node)
        # Create an output node
        output_node = nodes.new(type='ShaderNodeOutputMaterial')
        output_node.location = (300, 0)  # Node positions (for easy viewing in the UI)
        # Create a base material node (Principled BSDF)
        bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
        bsdf_node.location = (0, 0)
        bsdf_node.inputs['Base Color'].default_value = (0.7, 0.7, 0.7, 1)  # gray（RGBA）
        bsdf_node.inputs['Roughness'].default_value = 0.5  # Medium roughness
        # Connect nodes (output the base material to the material output)
        links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])
        # Assign the default material to the object
        obj.data.materials.append(default_mat)
        # Assign to a variable
        material_var = [default_mat]
    return material_var