import bpy
from bpy.types import Panel
from ..utils import property_utils, panel_utils

class VIRCADIA_PT_custom_properties(Panel):
    bl_label = "Entity Properties"
    bl_idname = "VIEW3D_PT_vircadia_custom_properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Vircadia"

    @classmethod
    def poll(cls, context):
        # Check if there are any selected objects
        if not context.selected_objects:
            return False

        # Check the active object
        obj = context.active_object
        if obj is None:
            return False
        
        # Check for Vircadia-specific properties
        has_vircadia_props = False
        for prop in obj.keys():
            if not property_utils.should_filter_property(prop):
                has_vircadia_props = True
                break
        
        return has_vircadia_props or obj.get("type") == "Zone"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        # Get the custom property "name" for the panel title
        if obj.get("type") == "Zone":
            custom_name = obj.name
        else:
            custom_name = obj.get("name", "Unnamed")

        layout.label(text=f"{custom_name}")

        panel_utils.draw_custom_properties(context, layout, obj)

def register():
    bpy.utils.register_class(VIRCADIA_PT_custom_properties)

def unregister():
    bpy.utils.unregister_class(VIRCADIA_PT_custom_properties)

if __name__ == "__main__":
    register()