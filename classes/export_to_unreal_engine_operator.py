import bpy
import os
from ..functions import export_to_unreal_engine

class OBJECT_OT_custom_export(bpy.types.Operator):
    """Export to Unreal Engine with custom settings"""
    bl_idname = "object.export_to_unreal_engine"
    bl_label = "Export to Unreal Engine"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        classification_result = export_to_unreal_engine.classification(scene.selected_checkbox, scene.LOD_checkbox)
        if not classification_result[0]:
            self.report({'ERROR'}, classification_result[1])
            return {'CANCELLED'}
        export_list = classification_result[2]

        if len(export_list) > 0:
            export_list = export_to_unreal_engine.separate_collision(export_list)

            if scene.fixed_path_checkbox:
                export_path = os.path.join(os.path.dirname(bpy.data.filepath), 'BlenderExport')
                if not os.path.exists(export_path):
                    os.makedirs(export_path, exist_ok=True)
                self.report({'INFO'}, f"Exporting to: {export_path}")
                for export_dict in export_list:
                    export_to_unreal_engine.export_fbx(export_dict, export_path, scene.rotate_checkbox)
            else:
                if not scene.export_path:
                    self.report({'ERROR'}, "Please select a folder first")
                    return {'CANCELLED'}
                self.report({'INFO'}, f"Exporting to: {scene.export_path}")
                for export_dict in export_list:
                    export_to_unreal_engine.export_fbx(export_dict, scene.export_path, scene.rotate_checkbox)

            export_list = export_to_unreal_engine.merge_collision(export_list)
        else:
            self.report({'INFO'}, "Please select an object first")
        
        return {'FINISHED'}

class WM_OT_path_open(bpy.types.Operator):
    """Open file browser to select path"""
    bl_idname = "wm.path_open"
    bl_label = "Select Path"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="DIR_PATH")
    hide_props_region: bpy.props.BoolProperty(default=True)
    check_existing: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        context.scene.export_path = self.filepath
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}