import bpy

# Save dropdown attribute
class MaterialDropdownItem(bpy.types.PropertyGroup):
    material: bpy.props.StringProperty(name="Material")

class VertexGroupDropdownItem(bpy.types.PropertyGroup):
    vertex_group: bpy.props.StringProperty(name="Vertex Group")

class Generate_spherical_normal_panel(bpy.types.Panel):
    bl_label = "Spherical Normal"
    bl_idname = "PT_Spherical_normal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BI1MCS Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Create tab
        row = layout.row()
        row.prop(scene, "active_tab", expand=True)
        
        btn_cmd = ''

        # Material tab
        if scene.active_tab == "MATERIAL":
            self.draw_material_tab(context, layout)
            btn_cmd = "mesh.generate_spherical_normal"
        
        # Vertex group tab
        elif scene.active_tab == "VERTEX_GROUP":
            self.draw_vertex_group_tab(context, layout)

        layout.operator("mesh.generate_spherical_normal", text = 'Generate', icon='MOD_NORMALEDIT')

    def draw_material_tab(self, context, layout):
        scene = context.scene
        obj = context.active_object
        
        # Check if there are any selected objects
        if not obj or obj.type != 'MESH':
            layout.label(text="Mesh object not selected")
            return
        
        # Button row: Refresh and Add
        row = layout.row(align=True)
        row.operator("material.refresh_dropdowns", text="", icon='FILE_REFRESH', emboss=True)
        row.operator("material.add_dropdown", text="", icon='ADD', emboss=True)
        
        # Draw all materials dropdown list
        for i, item in enumerate(scene.material_dropdowns):
            box = layout.box()
            row = box.row()
            row.prop_search(item, "material", obj.data, "materials", text="Material")
            # Delete button
            row.operator("material.remove_dropdown", text="", icon='REMOVE', emboss=True).index = i
    
    def draw_vertex_group_tab(self, context, layout):
        scene = context.scene
        obj = context.active_object
        
        # Check if there are any selected objects
        if not obj or obj.type != 'MESH':
            layout.label(text="Mesh object not selected")
            return
        
        # Button row: Refresh and Add
        row = layout.row(align=True)
        row.operator("vertex_group.refresh_dropdowns", text="", icon='FILE_REFRESH', emboss=True)
        row.operator("vertex_group.add_dropdown", text="", icon='ADD', emboss=True)
        
        # Draw all materials dropdown list
        for i, item in enumerate(scene.vertex_group_dropdowns):
            box = layout.box()
            row = box.row()
            row.prop_search(item, "vertex_group", obj, "vertex_groups", text="Vertex Group")
            # Delete button
            row.operator("vertex_group.remove_dropdown", text="", icon='REMOVE', emboss=True).index = i

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
