# DuplicateToolsForArmature
A tool for duplicating armature

You can find the tool in the tool shelf in the 3d view only in **object mode** under 

`Tools>Duplicate Tools for Armature`

##Duplicate Armature
###Description
Duplicates the armature with unique bone names (No bones have the same name from the original armature). This is useful when merging back together the bones because the vertex groups will not overlap.

 When duplicating multiple times, make sure to duplicate from the most recent duplication that you made! Or else you will have bones that have overlapping names

###Instruction
1. Select an Armature (set as currently active)
2. Press the duplicate armature

##Duplicate Mesh
###Description
A
###Instruction

##Tips
* The general use case for this plugin is to use Duplicate Armature then use Duplicate Mesh
* Merging everything together:
 * MERGING MESH AND ARMATURE: join the meshes together using (ctrl-j) then join the armature together by using the same shortcut
 * MERGING ONLY ARMATURE: Parent all the mesh to one of the armature (exluding the mesh that is already parented) and set the parent using (ctrl-p) and selecting Armature deform. Next join the armature together by using (ctrl-j)
* Make sure not to rotate the bones (only translation) because you loose the rotation data when joining the armature together
