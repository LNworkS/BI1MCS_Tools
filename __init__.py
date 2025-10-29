bl_info = {
    "name": "BI1MCS Tools",
    "author": "BI1MCS",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Problem Feedback：WeChat BI1MCS",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy
from bpy.props import EnumProperty
from .classes.export_to_unreal_engine_operator import OBJECT_OT_custom_export, WM_OT_path_open
from .classes.sphere_normals_operator import Generate_Spherical_Normals
from .ui.export_to_unreal_engine import Export_to_Unreal_Engine_Panel, Export_to_Unreal_Engine_menu_func
from .ui.spherical_normal import Generate_spherical_normal_panel, get_materials

all_classes = (
    OBJECT_OT_custom_export,
    WM_OT_path_open,
    Generate_Spherical_Normals,
    Export_to_Unreal_Engine_Panel,
    Generate_spherical_normal_panel,
)

def register():
    bpy.types.Scene.selected_checkbox = bpy.props.BoolProperty(
        name="Selected Checkbox",
        description="Export selected objects",
        default=True
    )

    bpy.types.Scene.LOD_checkbox = bpy.props.BoolProperty(
        name="LOD Checkbox",
        description="Export models separately for each level of LOD.",
        default=True
    )

    bpy.types.Scene.fixed_path_checkbox = bpy.props.BoolProperty(
        name="Fixed Path Checkbox",
        description="Enable/disable custom path",
        default=True
    )
    
    bpy.types.Scene.export_path = bpy.props.StringProperty(
        name="Export Path",
        description="Path to export files",
        subtype="DIR_PATH"
    )
    
    bpy.types.Scene.rotate_checkbox = bpy.props.BoolProperty(
        name="Rotate Checkbox",
        description="+90 degrees on Z",
        default=True
    )

    bpy.types.Scene.selected_material = EnumProperty(
        name="材质列表",
        description="可用材质列表",
        items=get_materials
    )

    for cls in all_classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.append(Export_to_Unreal_Engine_menu_func)

def unregister():
    for cls in all_classes:
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.remove(Export_to_Unreal_Engine_menu_func)

    del bpy.types.Scene.selected_material

    del bpy.types.Scene.selected_checkbox
    del bpy.types.Scene.LOD_checkbox
    del bpy.types.Scene.fixed_path_checkbox
    del bpy.types.Scene.export_path
    del bpy.types.Scene.rotate_checkbox

if __name__ == "__main__":
    register()

