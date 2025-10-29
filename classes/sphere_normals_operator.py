import bpy
from ..functions.genarate_spherical_normal import Generate_spherical_normal

class Generate_Spherical_Normals(bpy.types.Operator):
    bl_idname = "mesh.generate_spherical_normal"
    bl_label = "Spherical Normal"
    bl_description = "Generate spherical normal"

    def execute(self, context):
        sel = bpy.context.selected_objects
        if sel:
            for obj in sel:     
                if obj.type != "MESH":
                    self.report({"WARNING"}, f"{obj.name}不是一个MESH")
                    return {"FINISHED"}
                if obj.modifiers:
                    self.report({"WARNING"}, f"{obj.name}有修改器，请先应用")
                    return {"FINISHED"}
        else:
            self.report({"WARNING"}, "没有选择物体")
            return {"FINISHED"}
        for obj in sel:
            Generate_spherical_normal(obj)
        return {"FINISHED"}
