# Duplicate Tools For Armature
A tool for duplicating armature  
You can find the tool in the tool shelf in the 3d view only in **object mode** under 

`Tools>Duplicate Tools for Armature`

##Duplicate Armature
###Description
Duplicates the armature with unique bone names (No bones have the same name from the original armature). This is useful when merging back together the bones because the vertex groups will not overlap.  
 When duplicating multiple times, make sure to duplicate from the most recent duplication that you made! Or else you will have bones that have overlapping names

###Instruction
1. Select an Armature (set as currently active)
2. Press the duplicate armature button

##Duplicate Mesh
###Description
Duplicates the mesh so it has the corresponding  vertex groups and bone names.

###Instruction
1. Select the mesh you want to get copied, then select the original armature.
2. Select the duplicated armature (set as currently active)
3. Press the duplicate mesh button

##Tips
* The general use case for this plugin is to use Duplicate Armature then use Duplicate Mesh
* Merging everything together:
 * MERGING MESH AND ARMATURE: join the meshes together using (ctrl-j) then join the armature together by using the same shortcut
 * MERGING ONLY ARMATURE: Parent all the mesh to one of the armature (excluding  the mesh that is already parented) and set the parent using (ctrl-p) and selecting Armature deform. Next join the armature together by using (ctrl-j)
* Make sure not to rotate the bones (only translation) because you lose the rotation data when joining the armature together. The work around is to join everything together first then use pose mode to rotate it. Applying the armature position if necessary (details instructions are below)

From http://blender.stackexchange.com/questions/49768/can-i-set-my-pose-position-like-the-new-rest-position

1. Apply the armature modifier - armature in rest pose doesn't deform anything, so we need also a mesh to match the new rest pose.
2. Pose > Apply Pose as Rest Pose. This will set current pose as the rest pose. It sets only bones poses - constraints or custom properties in complicated or badly designed rigs might make the rig act weird with bones in different rest state!
3. Add the armature modifier back.
