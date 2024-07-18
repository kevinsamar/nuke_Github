import nuke
import os
import random

#READING GIZMOS
Gizmos = nuke.toolbar('Nodes').addMenu('Gizmos')
Gizmos.addCommand('DasGrain', 'nuke.createNode("DasGrain")', icon='')
Gizmos.addCommand('Exponential_Glow', 'nuke.createNode("Exponential_Glow")', icon='')
Gizmos.addCommand('normalish', 'nuke.createNode("normalish")', icon='')
Gizmos.addCommand('iBlur', 'nuke.createNode("iBlur")', icon='')

#PYTHON COMMANDS
Python = nuke.toolbar('Nodes').addMenu('PythonScripts')
Python.addCommand('Shuffle RGB', 'execute_shuffleRGB()', 'Ctrl+Shift+L')
Python.addCommand('GuiManager', 'execute_newGuiManager()', '')
Python.addCommand('Create Backdrop', 'create_backdrop()', 'Shift+B')

#FRAMEHOLD
def set_framehold_to_current_frame():
    node = nuke.thisNode()
    if node.Class() == 'FrameHold':
        current_frame = nuke.frame()
        node['first_frame'].setValue(current_frame)

nuke.addOnCreate(set_framehold_to_current_frame, nodeClass='FrameHold')

#SHUFFLE RGB
def execute_shuffleRGB():
    import shuffleRGB
    shuffleRGB.shuffleRGB()

#GUI MANAGER
def execute_newGuiManager():
    import newGuiManager
    newGuiManager.newGuiManager()

#BACKDROP
def create_backdrop():
    # Function to create a backdrop over the selected nodes
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        nuke.message("No nodes selected")
        return
    
    # Determine the bounding box of the selected nodes
    x_min = min(node.xpos() for node in selected_nodes)
    y_min = min(node.ypos() for node in selected_nodes)
    x_max = max(node.xpos() + node.screenWidth() for node in selected_nodes)
    y_max = max(node.ypos() + node.screenHeight() for node in selected_nodes)
    
    # Create a backdrop node
    backdrop = nuke.createNode('BackdropNode')
    backdrop['xpos'].setValue(x_min - 10)  # Add some padding
    backdrop['ypos'].setValue(y_min - 80)
    backdrop['bdwidth'].setValue(x_max - x_min + 20)
    backdrop['bdheight'].setValue(y_max - y_min + 90)
    
    # Optionally, set additional properties for the backdrop node
    backdrop['note_font_size'].setValue(42)
    