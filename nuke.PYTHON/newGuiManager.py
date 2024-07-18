#GUI Manager

import nuke

def newGuiManager():

    guiExpression = '$gui'
    
    #Extracting classes in node graph
    enableOptions = ['-','SelectedNode(s)']
    
    #Extracting Nodes containing $gui
    guiNodes = []
    for n in nuke.selectedNodes():
        try:
            if n.knob('disable').animation(0).expression() == str(guiExpression):
                guiNodes.append(n.name())
        except:
            pass
    
    guiNodes.insert(0, '-')
    guiNodes.insert(1, 'AllNodes')
    
    
    #Panel Creation
    myPanel = nuke.Panel('$GUI MANAGER')
    
    myPanel.addEnumerationPulldown('Enable on', (' ').join(enableOptions))
    
    myPanel.addEnumerationPulldown('Disable on', (' ').join(guiNodes))
    
    myPanel.addBooleanCheckBox('Include All Nodes in Class', False)
    

    if myPanel.show():
    
        
        
        #actions
        #enable
        if not myPanel.value('Enable on') == 'SelectedNode(s)':
            for n in nuke.allNodes(myPanel.value('Enable on')):
                n.knob('disable').setExpression(str(guiExpression))
           
        else:
            for n in nuke.selectedNodes():
                n.knob('disable').setExpression(str(guiExpression))
          
          
            if myPanel.value('Include All Nodes in Class') == True:
                includedClasses = []
                for n in nuke.selectedNodes():
                    includedClasses.append(n.Class())
            
                   
                for n in range(len(includedClasses)):
                    for n2 in nuke.allNodes(includedClasses[n]):
                        n2.knob('disable').setExpression(str(guiExpression))
        
            
        #disable
        if myPanel.value('Disable on') == 'AllNodes':
            for n in nuke.allNodes():
                try: 
                    n.knob('disable').clearAnimated()
                except:
                    pass
        
                try:
                    n.knob('disable').setValue(False)
                except:
                    pass
        
        else:
            
            if not myPanel.value('Disable on') == '-':
                
                nuke.toNode(myPanel.value('Disable on')).knob('disable').clearAnimated()
                nuke.toNode(myPanel.value('Disable on')).knob('disable').setValue(False)
                
                
                if myPanel.value('Include All Nodes in Class') == True:
                    for n in nuke.allNodes(str(nuke.toNode(myPanel.value('Disable on')).Class())):
                       n.knob('disable').clearAnimated()
                       n.knob('disable').setValue(False)
        
newGuiManager()
                