import bpy

bl_info = {
    "name": "Duplicate tools for Armature",
    "description": "Duplicate Armature and Mesh with unique bone names and correspoding vertex groups",
    "author": "Shuhei Aoki",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Tool Shelf > Tools > Duplicate with Armature",
    "support": "COMMUNITY",
    "category": "Object"
    }
    
class DuplicateArmature(bpy.types.Operator):
    bl_description = "Duplicate armature with unique bone names"
    bl_idname = "object.duplicate_armature"
    bl_label = "Duplicate Armature"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        activeExistsAndIsArmature = context.active_object is not None and context.active_object.type == 'ARMATURE'
        return context.mode == 'OBJECT' and context.area.type == 'VIEW_3D' and activeExistsAndIsArmature
    
    def execute(self, context):
        scene = context.scene
        selected = context.selected_objects
        objectOp = bpy.ops.object
        
        objectOp.editmode_toggle()
        bpy.ops.armature.select_all(action = 'SELECT')
        bpy.ops.armature.duplicate()
        bpy.ops.armature.separate()
        objectOp.editmode_toggle()
        objectOp.select_all(action = 'DESELECT')
        scene.objects.active = None
        return {'FINISHED'}
    
class DuplicateMesh(bpy.types.Operator):
    bl_description = "Duplicate mesh with modified vertex groups"
    bl_idname = "object.duplicate_mesh"
    bl_label = "Duplicate Mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        activeExistsAndIsArmature = context.active_object is not None and context.active_object.type == 'ARMATURE'
        return context.mode == 'OBJECT' and context.area.type == 'VIEW_3D' and activeExistsAndIsArmature
    
    def execute(self, context):
        scene = context.scene
        active = context.active_object
        orgArmature = None
        
        for obj in context.selected_objects:
            if obj.name != context.active_object.name and obj.type == 'ARMATURE':
                orgArmature = obj
                break
            
        if orgArmature is None:
            self.report({'ERROR'}, 'Original armature needs to be selected')
            return {'FINISHED'}
        
        for obj in context.selected_objects:
            if obj.type == 'MESH' and DuplicateMesh.findArmatureMod(obj) is not None:
                newObj = obj.copy()
                newObj.data = obj.data.copy()
                scene.objects.link(newObj)
                newObj.parent = active
                DuplicateMesh.findArmatureMod(newObj).object = active
                DuplicateMesh.SyncVertexGroups(orgArmature, active, newObj)

        return {'FINISHED'}
    
    def findArmatureMod(obj):
        if obj.modifiers.find('Armature') == -1:
            for mod in obj.modifiers:
                if mod.type == 'ARMATURE':
                    return mod
        else:
            return obj.modifiers['Armature']
        return None
    
    def SyncVertexGroups(orgArmature, newArmature, mesh):
        orgBones = orgArmature.pose.bones
        newBones = newArmature.pose.bones
        
        for newBone in newBones:
            for orgBone in orgBones:
                print(str(orgBone.bone.head) + " vs " + str(newBone.bone.head))
                headIsEqual = orgBone.bone.head_local == newBone.bone.head_local
                tailIsEqual = orgBone.bone.tail_local == newBone.bone.tail_local
                keyExists = mesh.vertex_groups.find(orgBone.name) != -1
                if headIsEqual and tailIsEqual and keyExists:
                    mesh.vertex_groups[orgBone.name].name = newBone.name
                    break
        return

class DuplicateArmatureMenu(bpy.types.Panel):
    bl_label = "Duplicate Tools for Armature"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'
    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        col.operator(operator = "object.duplicate_armature")
        col.operator(operator = "object.duplicate_mesh")
    
    
    
def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
