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