import bpy
import os
import math

def classification(isSelected, independentLod):
    if not isSelected:
        bpy.ops.object.select_all(action='SELECT')
    selected_objects = bpy.context.selected_objects
    
    if len(selected_objects) == 0:
        return [False, 'No selected object。', None]

    export_list = []

    for obj in selected_objects:
        if obj.type not in ('MESH', 'EMPTY'):
            continue

        if obj.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        
        if obj.type == 'EMPTY':
            if independentLod:
                continue
            found = False
            for export_dict in export_list:
                if any(obj.name in mesh.name for mesh in export_dict['mesh']):
                    export_dict['active'] = [obj]
                    found = True
                    break
                if any(obj.name in collision.name for collision in export_dict['collision']):
                    export_dict['active'] = [obj]
                    found = True
                    break
            if not found:
                export_list.append({'mesh':[], 'active':[obj], 'collision':[]})
        
        elif len(obj.name) >= 3 and obj.name[0:3].lower() == 'ucx':
            found = False
            for export_dict in export_list:
                if independentLod:
                    if any('_lod0' in mesh.name.lower() for mesh in export_dict['mesh']):
                        export_dict['collision'].append(obj)
                        found = True
                        break
                else:
                    if (export_dict['active'] and 
                        export_dict['active'][0].name in obj.name):
                        export_dict['collision'].append(obj)
                        found = True
                        break
                    if any(obj.name.lower().split('ucx_')[1].split('_lod')[0] == 
                           mesh.name.lower().split('_lod')[0] for mesh in export_dict['mesh']):
                        export_dict['collision'].append(obj)
                        found = True
                        break
            if not found:
                export_list.append({'mesh':[], 'active':[], 'collision':[obj]})
        
        else:
            if independentLod:
                export_list.append({'mesh':[obj], 'active':[obj], 'collision':[]})
                continue
            found = False
            for export_dict in export_list:
                if (export_dict['active'] and 
                    export_dict['active'][0].name in obj.name):
                    export_dict['mesh'].append(obj)
                    found = True
                    break
                if any(obj.name.lower().split('_lod')[0] == 
                       col.name.lower().split('ucx_')[1].split('_lod')[0] 
                       for col in export_dict['collision']):
                    export_dict['mesh'].append(obj)
                    found = True
                    break
            if not found:
                export_list.append({'mesh':[obj], 'active':[], 'collision':[]})

    # create active
    for export_dict in export_list:
        if len(export_dict['active']) == 0:
            if len(export_dict['mesh']) == 1:
                export_dict['active'] = [export_dict['mesh'][0]]
            elif len(export_dict['mesh']) > 1:
                bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0,0,0))
                empty_obj = bpy.context.object
                empty_obj.name = f"{export_dict['mesh'][0].name.lower().split('_lod')[0]}"
                empty_obj['fbx_type'] = 'LodGroup'
                export_dict['active'] = [empty_obj]
            else:
                export_dict['active'] = [export_dict['collision'][0]]

    # LOD parent
    for export_dict in export_list:
        is_LOD = any('_lod' in obj.name.lower() for obj in export_dict['mesh'])
        if is_LOD:
            for obj in export_dict['mesh']:
                obj.parent = export_dict['active'][0]
    
    bpy.ops.object.select_all(action='DESELECT')
    return [True, 'Success', export_list]

def separate_collision(export_list):
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
    rotate_angle = math.pi/2 if rotate else 0
    
    try:
        # rotate
        for obj in export_dict['mesh'] + export_dict['collision']:
            obj.rotation_euler.z += rotate_angle

        # export
        bpy.ops.object.select_all(action='DESELECT')
        for obj in export_dict['collision'] + export_dict['mesh']:
            obj.select_set(True)
        
        is_LOD = any('_lod' in obj.name.lower() for obj in export_dict['mesh'])
        filepath = os.path.join(export_path, f"{export_dict['active'][0].name}.fbx")
        
        if is_LOD:
            bpy.ops.export_scene.fbx(
                filepath=filepath,
                use_selection=True,
                object_types={'MESH'},
                use_custom_props=False,
                mesh_smooth_type='FACE',
                use_mesh_modifiers=True,
                add_leaf_bones=False,
                bake_anim=False
            )
        else:
            for obj in export_dict['active']:
                obj.select_set(True)
            bpy.ops.export_scene.fbx(
                filepath=filepath,
                use_selection=True,
                object_types={'EMPTY', 'MESH'},
                use_custom_props=True,
                mesh_smooth_type='FACE',
                use_mesh_modifiers=True,
                add_leaf_bones=False,
                bake_anim=False
            )
    
    finally:
        # rotate
        for obj in export_dict['mesh'] + export_dict['collision']:
            obj.rotation_euler.z -= rotate_angle
    
    bpy.ops.object.select_all(action='DESELECT')