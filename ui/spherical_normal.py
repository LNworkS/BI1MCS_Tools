import bpy

class Generate_spherical_normal_panel(bpy.types.Panel):
    bl_label = "Spherical Normal"
    bl_idname = "PT_Spherical_normal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BI1MCS Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.generate_spherical_normal", text = 'Generate', icon='MOD_NORMALEDIT')
