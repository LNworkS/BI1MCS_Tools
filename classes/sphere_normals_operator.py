import bpy
from ..functions.generate_spherical_normal import generate_spherical_normal

class Generate_Spherical_Normals(bpy.types.Operator):
    bl_idname = "mesh.generate_spherical_normal"
    bl_label = "Spherical Normal"
    bl_description = "Generate spherical normal"

    def execute(self, context):
        sel = bpy.context.selected_objects
        if not sel:
            self.report({"WARNING"}, "No object selected")
            return {"FINISHED"}
        
        scene = context.scene
        for obj in sel:     
            if obj.type != "MESH":
                self.report({"WARNING"}, f"{obj.name} is not a MESH")
                continue
            if obj.modifiers:
                self.report({"WARNING"}, f"{obj.name} has modifiers; please apply them first")
                continue
            
            if scene.active_tab == "MATERIAL":
                node_num = len(scene.material_dropdowns)
            else:
                node_num = len(scene.vertex_group_dropdowns)
            generate_spherical_normal(obj, scene.active_tab, node_num)
        
        return {"FINISHED"}
    
# Material operations
class MATERIAL_OT_refresh_dropdowns(bpy.types.Operator):
    bl_idname = "material.refresh_dropdowns"
    bl_label = "Refresh material dropdown list"
    bl_description = "Refresh material dropdown list of current object"
    
    def execute(self, context):
        scene = context.scene
        obj = context.active_object
        
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Please select a mesh object first")
            return {'CANCELLED'}
        
        # Clear the existing dropdown list
        scene.material_dropdowns.clear()
        
        # If there is a material, add a default dropdown list
        if obj.data.materials:
            item = scene.material_dropdowns.add()
            item.material = obj.data.materials[0].name
        
        return {'FINISHED'}

class MATERIAL_OT_add_dropdown(bpy.types.Operator):
    bl_idname = "material.add_dropdown"
    bl_label = "Add material dropdown list"
    bl_description = "Add a new material dropdown list"
    
    def execute(self, context):
        scene = context.scene
        obj = context.active_object
        
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Please select a mesh object first")
            return {'CANCELLED'}
        
        # Add a new dropdown list item
        item = scene.material_dropdowns.add()
        # If there is a material, the first one will be selected by default
        if obj.data.materials:
            item.material = obj.data.materials[0].name
        
        return {'FINISHED'}

class MATERIAL_OT_remove_dropdown(bpy.types.Operator):
    bl_idname = "material.remove_dropdown"
    bl_label = "Remove material dropdown list"
    bl_description = "Remove selected material dropdown list"
    
    index: bpy.props.IntProperty()
    
    def execute(self, context):
        scene = context.scene
        scene.material_dropdowns.remove(self.index)
        return {'FINISHED'}

# Vertex group operations
class VERTEX_GROUP_OT_refresh_dropdowns(bpy.types.Operator):
    bl_idname = "vertex_group.refresh_dropdowns"
    bl_label = "Refresh vertex group dropdown list"
    bl_description = "Refresh vertex group dropdown list of current object"
    
    def execute(self, context):
        scene = context.scene
        obj = context.active_object
        
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Please select a mesh object first")
            return {'CANCELLED'}
        
        # Clear the existing dropdown list
        scene.vertex_group_dropdowns.clear()
        
        # If there is a vertex group, add a default dropdown list
        if obj.vertex_groups:
            item = scene.vertex_group_dropdowns.add()
            item.vertex_group = obj.vertex_groups[0].name
        
        return {'FINISHED'}

class VERTEX_GROUP_OT_add_dropdown(bpy.types.Operator):
    bl_idname = "vertex_group.add_dropdown"
    bl_label = "Add vertex group dropdown list"
    bl_description = "Add a new vertex group dropdown list"
    
    def execute(self, context):
        scene = context.scene
        obj = context.active_object
        
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Please select a mesh object first")
            return {'CANCELLED'}
        
        # Add a new dropdown list item
        item = scene.vertex_group_dropdowns.add()
        # If there is a vertex group, the first one will be selected by default
        if obj.vertex_groups:
            item.vertex_group = obj.vertex_groups[0].name
        
        return {'FINISHED'}

class VERTEX_GROUP_OT_remove_dropdown(bpy.types.Operator):
    bl_idname = "vertex_group.remove_dropdown"
    bl_label = "Remove vertex group dropdown list"
    bl_description = "Remove selected vertex group dropdown list"
    
    index: bpy.props.IntProperty()
    
    def execute(self, context):
        scene = context.scene
        scene.vertex_group_dropdowns.remove(self.index)
        return {'FINISHED'}
    
