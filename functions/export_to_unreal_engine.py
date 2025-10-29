import bpy
import os

def classification(isSelected, independentLod):
    if not isSelected:
        bpy.ops.object.select_all(action='SELECT')
    selected_objects = bpy.context.selected_objects
    
    if len(selected_objects) == 0:
        return [False, '没有选择物体。', None]
    
    export_list = []
    # {'mesh':[], 'active':[], 'collision':[]}

    for obj in selected_objects:
        if obj.type == 'MESH' or obj.type == 'EMPTY':
            if obj.type == 'EMPTY':
                if independentLod:
                    continue
                for export_dict in export_list:
                    if len(export_dict['mesh']) != 0:
                        for mesh in export_dict['mesh']:
                            if obj.name in mesh.name:
                                export_dict['active'] = [obj]
                                continue
                    if len(export_dict['collision']) != 0:
                        for collision in export_dict['collision']:
                            if obj.name in collision.name:
                                export_dict['active'] = [obj]
                else:
                    export_list.append({'mesh':[], 'active':[obj], 'collision':[]})
            elif 'ucx_' in obj.name[0:3].lower():
                for export_dict in export_list:
                    if independentLod:
                        for mesh in export_dict['mesh']:
                            if '_lod0' in mesh.name.lower():
                                export_dict['collision'].append(obj)
                        else:
                            continue
                    if len(export_dict['active']) > 0:
                        if export_dict['active'].name in obj.name:
                            export_dict['collision'].append(obj)
                            continue
                    if len(export_dict['mesh']) != 0:
                        for mesh in export_dict['mesh']:
                            if obj.name.lower().split('ucx_')[1].split('_lod')[0] == mesh.name.lower().split('_lod')[0]:
                                export_dict['collision'].append(obj)
                else:
                    export_list.append({'mesh':[], 'active':[], 'collision':[obj]})
            else:
                if independentLod:
                        export_list.append({'mesh':[obj], 'active':[obj], 'collision':[]})
                        continue
                for export_dict in export_list:
                    if len(export_dict['active']) > 0:
                        if export_dict['active'].name in obj.name:
                            export_dict['mesh'].append(obj)
                            continue
                    if len(export_dict['collision']) != 0:
                        for mesh in export_dict['collision']:
                            if obj.name.lower().split('ucx_')[1].split('_lod')[0] == mesh.name.lower().split('_lod')[0]:
                                export_dict['mesh'].append(obj)
                else:
                    export_list.append({'mesh':[obj], 'active':[], 'collision':[]})

    # Add Active
    for export_dict in export_list:
        if len(export_dict['active']) == 0:
            if len(export_dict['mesh']) == 1:
                export_dict['active'] = [export_dict['mesh'][0]]
            elif len(export_dict['mesh']) > 1:
                # Create EMPTY
                bpy.ops.object.empty_add(
                    type='PLAIN_AXES',
                    location=(0, 0, 0),
                    rotation=(0, 0, 0),
                    scale=(1, 1, 1)
                )
                # rename EMPTY and set parameters
                empty_obj = bpy.context.object
                empty_obj.name = f"{export_dict['mesh'][0].name.lower().split('_lod')[0]}"
                empty_obj['fbx_type'] = 'LodGroup'
                export_dict['active'] = [empty_obj]
            else:
                export_dict['active'] = [export_dict['collision'][0]]

    # create parent in LOD object 
    for export_dict in export_list:
        is_LOD = False
        for obj in export_dict['mesh']:
            if '_lod' in obj.name.lower():
                is_LOD = True
        if is_LOD:
            for obj in export_dict['mesh']:
                obj.parent = export_dict['active'][0]
    
    bpy.ops.object.select_all(action='DESELECT')
    return export_list

def separate_collision(export_list):
    # separate an rename
    for export_dict in export_list:
        if len(export_dict['collision']) > 0:
            for obj in export_dict['collision']:
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.separate(type='LOOSE')
                bpy.ops.object.mode_set(mode='OBJECT')
                obj.select_set(False)
                export_dict['collision'].extend(bpy.context.selected_objects)
            for idx, obj in enumerate(export_dict['collision'], start=1):
                obj.name = f"UCX_{export_dict['active'][0].name.lower().split('ucx_')[1] if 'ucx_' in export_dict['active'][0].name.lower() else export_dict['active'][0].name}_{idx:03d}"
            bpy.ops.object.select_all(action='DESELECT')
    return export_list

def merge_collision(export_list):
    # merge and rename
    for export_dict in export_list:
        if len(export_dict['collision']) > 0:
            bpy.ops.object.select_all(action='DESELECT')
            for obj in export_dict['collision']:
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj
            bpy.ops.object.join()
            export_dict['collision'] = bpy.context.selected_objects
            export_dict['collision'][0].name = f"UCX_{export_dict['active'][0].name.lower().split('ucx_')[1] if 'ucx_' in export_dict['active'][0].name.lower() else export_dict['active'][0].name}"
            bpy.ops.object.select_all(action='DESELECT')
    return export_list

def export_fbx(export_dict, export_path, rotate):
    rotate_angle = 0
    if rotate:
        rotate_angle = 90
    
    # rotate object
    for obj in export_dict['mesh']:
        obj.rotation_euler.z += rotate_angle * (3.1415926535 / 180)
    for obj in export_dict['collision']:
        obj.rotation_euler.z += rotate_angle * (3.1415926535 / 180)
    
    # export object
    # object_types: !LOD：{'MESH'}，LOD：{'EMPTY', 'MESH'}
    # use_custom_props：!LOD：False，LOD：True
    bpy.ops.object.select_all(action='DESELECT')
    if len(export_dict['collision']) > 0:
        for obj in export_dict['collision']:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = export_dict['collision'][0]
    if len(export_dict['mesh']) > 0:
        for obj in export_dict['mesh']:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = export_dict['mesh'][0]
    is_LOD = False
    for obj in export_dict['mesh']:
        if '_lod' in obj.name.lower():
            is_LOD = True
    if is_LOD:
        filepath = os.path.join(export_path, f"{export_dict['active'][0].name}.fbx")
        bpy.ops.export_scene.fbx(
            filepath = filepath,
            use_selection = True,
            object_types = {'MESH'},
            use_custom_props = False,
            mesh_smooth_type = 'FACE',
            use_mesh_modifiers = True,
            add_leaf_bones=False,
            bake_anim=False
        )
    else:
        for obj in export_dict['active']:
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
        filepath = os.path.join(export_path, f"{export_dict['active'][0].name}.fbx")
        bpy.ops.export_scene.fbx(
            filepath = filepath,
            use_selection = True,
            object_types = {'EMPTY', 'MESH'},
            use_custom_props = True,
            mesh_smooth_type = 'FACE',
            use_mesh_modifiers = True,
            add_leaf_bones=False,
            bake_anim=False
        )
    bpy.ops.object.select_all(action='DESELECT')
    
    # rotate object
    for obj in export_dict['mesh']:
        obj.rotation_euler.z -= rotate_angle * (3.1415926535 / 180)
    for obj in export_dict['collision']:
        obj.rotation_euler.z -= rotate_angle * (3.1415926535 / 180)

    
