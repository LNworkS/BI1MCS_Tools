import bpy

def get_materials(self, context):
    materials = []
    
    for obj in bpy.context.selected_objects:
        has_valid_material = any(mat is not None for mat in obj.data.materials)
        if has_valid_material:
            # if has valid material，extend to materials list
            for index, mat in enumerate(obj.data.materials):
                materials.append((mat.name, mat.name, f"选择材质: {mat.name}", 'MATERIAL', index))
            #materials.extend(obj.data.materials)
    return materials

class Generate_spherical_normal_panel(bpy.types.Panel):
    bl_label = "Spherical Normal"
    bl_idname = "PT_Spherical_normal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BI1MCS Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "selected_material", text="选择材质")
        layout.operator("mesh.generate_spherical_normal", text = 'Generate', icon='MOD_NORMALEDIT')

