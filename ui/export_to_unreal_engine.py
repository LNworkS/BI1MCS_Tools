import bpy

class Export_to_Unreal_Engine_Panel(bpy.types.Panel):
    bl_label = "Export to Unreal Engine"
    bl_idname = "VIEW3D_PT_custom_plugin"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BI1MCS Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Checkbox
        checkrow = layout.row()
        checkrow.prop(scene, "selected_checkbox", text="Selected")
        checkrow.prop(scene, "LOD_checkbox", text="Independent LOD")
        
        # Checkbox
        layout.prop(scene, "rotate_checkbox", text="+90 degrees on Z")

        # Checkbox
        layout.prop(scene, "fixed_path_checkbox", text="Fixed Path (filepath \\ BlenderExport)")
        
        # Text input and folder select
        row = layout.row()
        row.prop(scene, "export_path", text='')
        #context.scene.export_path = os.path.dirname(bpy.data.filepath) + '\\'
        
        # Disable/enable based on checkbox state
        if scene.fixed_path_checkbox:
            row.enabled = False
        
        # Export button
        layout.operator("object.export_to_unreal_engine", text="Export", icon="EXPORT")

def Export_to_Unreal_Engine_menu_func(self, context):
    self.layout.operator("object.export_to_unreal_engine", text='Export to Unreal Engine')