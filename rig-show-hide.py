bl_info = {
    "name": "Lucas Addon",
    "category": "Object",
}

import bpy

# arms and hands
left_hand = ['c_ring1.l', 'c_ring2.l', 'c_ring3.l', 'c_middle1.l', 'c_middle2.l', 'c_middle3.l', 'c_index1.l', 'c_index2.l', 'c_index3.l', 'c_thumb1.l', 'c_thumb2.l', 'c_thumb3.l', 'c_hand_ik.l']
left_arm = ['c_shoulder.l', 'c_arm_twist_offset.l', 'c_arm_ik.l', 'c_ring1.l', 'c_ring2.l', 'c_ring3.l', 'c_middle1.l', 'c_middle2.l', 'c_middle3.l', 'c_index1.l', 'c_index2.l', 'c_index3.l', 'c_thumb1.l', 'c_thumb2.l', 'c_thumb3.l', 'c_arms_pole.l', 'c_hand_ik.l']

right_hand = ['c_ring1.r', 'c_ring2.r', 'c_ring3.r', 'c_middle1.r', 'c_middle2.r', 'c_middle3.r', 'c_index1.r', 'c_index2.r', 'c_index3.r', 'c_thumb1.r', 'c_thumb2.r', 'c_thumb3.r', 'c_hand_ik.r']
right_arm = ['c_shoulder.r', 'c_arm_twist_offset.r', 'c_arm_ik.r', 'c_ring1.r', 'c_ring2.r', 'c_ring3.r', 'c_middle1.r', 'c_middle2.r', 'c_middle3.r', 'c_index1.r', 'c_index2.r', 'c_index3.r', 'c_thumb1.r', 'c_thumb2.r', 'c_thumb3.r', 'c_arms_pole.r', 'c_hand_ik.r']

hands = left_hand + right_hand
arms = left_arm + right_arm

# legs and feet
left_leg = ['c_thigh_ik.l', 'c_foot_ik.l', 'c_toes_ik.l']
right_leg = ['c_thigh_ik.r', 'c_foot_ik.r', 'c_toes_ik.r']

legs = left_leg + right_leg

# spine
spine = ['c_root_master.x', 'c_root.x', 'c_spine_01.x', 'c_spine_02.x', 'c_spine_03.x', 'c_neck.x']

# head
head = ['c_head.x']
head_and_neck = head + ['c_neck.x']

# others
others = ['c_pos', 'c_traj', 'backpack-attach', 'c_ring1_base.l', 'c_middle1_base.l', 'c_index1_base.l', 'c_ring1_base.r', 'c_middle1_base.r', 'c_index1_base.r', 'c_thumb1_base.r', 'c_foot_01.r', 'c_foot_roll_cursor.r', 'c_leg_pole.r', 'c_foot_01.l', 'c_foot_roll_cursor.l', 'c_leg_pole.l', 'laptop-attach']

class LucasPanel(bpy.types.Panel):
    bl_label = "🤖 Lucas Rig Panel"
    bl_idname = "OBJECT_PT_lucas"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = " 📟 lucas.labs"

    def make_section(self, label):
        layout = self.layout
        pie = layout.row()
        col = pie.box()
        col.label(text=label)
        layout.row()
        layout.row()

    def make_row(self, label, bones):
        layout = self.layout
        row = layout.row()
        row.label(text=label)

        hands_column = row.column(align=True)
        show_op = hands_column.operator(OBJECT_OT_unhide_bones.bl_idname, text="👁️")
        show_op.which_bones = bones

        arms_column = row.column(align=True)
        hide_op = arms_column.operator(OBJECT_OT_hide_bones.bl_idname, text="❌")
        hide_op.which_bones = bones

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.get_selected", text="Get Selected")

        self.make_section("Hands")
        self.make_row("Left", "left_hand")
        self.make_row("Right", "right_hand")
        self.make_row("Both", "hands")

        self.make_section("Arms")
        self.make_row("Left", "left_arm")
        self.make_row("Right", "right_arm")
        self.make_row("Both", "arms")

        self.make_section("Legs")
        self.make_row("Left", "left_leg")
        self.make_row("Right", "right_leg")
        self.make_row("Both", "legs")

        self.make_section("Spine")
        self.make_row("Spine", "spine")

        self.make_section("Head")
        self.make_row("Head", "head")
        self.make_row("+ Neck", "head_and_neck")

        self.make_section("Others")
        self.make_row("Others", "others")

        self.make_section("All")
        self.make_row("All", "all")


class OBJECT_OT_get_selected(bpy.types.Operator):
    bl_idname = "object.get_selected"
    bl_label = "Get Selected"

    def execute(self, context):
        selected_bones = []
        for bone in context.selected_pose_bones:
            selected_bones.append(bone.name)
        print("Selected Bones:", selected_bones)
        return {'FINISHED'}

# hides bones depending on the selected list of bones (arms, legs, hands, spine)
class OBJECT_OT_hide_bones(bpy.types.Operator):
    bl_idname = "object.hide_bones"
    bl_label = "Hide Bones"

    # can be left_hand, left_arm, right_hand, right_arm, hands, arms, left_leg, right_leg, legs, spine
    which_bones: bpy.props.StringProperty()

    @classmethod 
    def description(self, context, properties): return "Hide"

    def execute(self, context):
        print("Will hide:", self.which_bones)
        bones = []

        match self.which_bones: 
            case "left_hand":
                bones = left_hand
            case "left_arm":
                bones = left_arm
            case "right_hand":
                bones = right_hand
            case "right_arm":
                bones = right_arm
            case "hands":
                bones = hands
            case "arms":
                bones = arms
            case "left_leg":
                bones = left_leg
            case "right_leg":
                bones = right_leg
            case "legs":
                bones = legs
            case "spine":
                bones = spine
            case "head":
                bones = head
            case "head_and_neck":
                bones = head_and_neck
            case "others":
                bones = others
            case other:
                print("Unknown bones:", self.which_bones)
        
        print("Will hide:", self.which_bones, "which is:", bones)

        # get selected armature and hide bones which names match the list
        # check if selected object has something to avoid list index out of range
        if len(bpy.context.selected_objects) == 0:
            print("No object selected")
            return {'FINISHED'}
        
        armature = bpy.context.selected_objects[0]
        
        # check if the selected object is an armature
        if armature.type == 'ARMATURE':
            print("Selected object is an armature, will hide bones in the list", self.which_bones)

            # if the list is empty and self.which_bones is "all", hide all bones
            if len(bones) == 0 and self.which_bones == "all":
                for bone in armature.pose.bones:
                    bone.bone.hide = True
            else:
                for bone in armature.pose.bones:
                    if bone.name in bones:
                        bone.bone.hide = True
        else:
            print("Selected object is not an armature")

        return {'FINISHED'}

# unhides bones depending on the selected list of bones (arms, legs, hands, spine)
class OBJECT_OT_unhide_bones(bpy.types.Operator):
    bl_idname = "object.unhide_bones"
    bl_label = "Hide Bones"

    # can be left_hand, left_arm, right_hand, right_arm, hands, arms, left_leg, right_leg, legs, spine
    which_bones: bpy.props.StringProperty()

    @classmethod
    def description(self, context, properties): return "Show"

    def execute(self, context):
        print("Will show:", self.which_bones)
        bones = []

        match self.which_bones: 
            case "left_hand":
                bones = left_hand
            case "left_arm":
                bones = left_arm
            case "right_hand":
                bones = right_hand
            case "right_arm":
                bones = right_arm
            case "hands":
                bones = hands
            case "arms":
                bones = arms
            case "left_leg":
                bones = left_leg
            case "right_leg":
                bones = right_leg
            case "legs":
                bones = legs
            case "spine":
                bones = spine
            case "head":
                bones = head
            case "head_and_neck":
                bones = head_and_neck
            case "others":
                bones = others
            case other:
                print("Unknown bones:", self.which_bones)
        
        print("Will show:", self.which_bones, "which is:", bones)

        # get selected armature and hide bones which names match the list
        # check if selected object has something to avoid list index out of range
        if len(bpy.context.selected_objects) == 0:
            print("No object selected")
            return {'FINISHED'}
        
        armature = bpy.context.selected_objects[0]
        # check if the selected object is an armature
        if armature.type == 'ARMATURE':
            print("Selected object is an armature, will show bones in the list", self.which_bones)

            # if the list is empty and self.which_bones is "all", show all bones
            if len(bones) == 0 and self.which_bones == "all":
                for bone in armature.pose.bones:
                    bone.bone.hide = False
            else:
                for bone in armature.pose.bones:
                    if bone.name in bones:
                        bone.bone.hide = False
        else:
            print("Selected object is not an armature")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(LucasPanel)
    bpy.utils.register_class(OBJECT_OT_get_selected)
    bpy.utils.register_class(OBJECT_OT_hide_bones)
    bpy.utils.register_class(OBJECT_OT_unhide_bones)

def unregister():
    bpy.utils.unregister_class(LucasPanel)
    bpy.utils.unregister_class(OBJECT_OT_get_selected)
    bpy.utils.unregister_class(OBJECT_OT_hide_bones)
    bpy.utils.unregister_class(OBJECT_OT_unhide_bones)

if __name__ == "__main__":
    register()
