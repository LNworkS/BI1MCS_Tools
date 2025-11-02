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

