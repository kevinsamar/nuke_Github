import nuke

#READ FILE PATHS
nuke.pluginAddPath('nuke.GIZMOS')
nuke.pluginAddPath('nuke.PYTHON')

# Settings:
nuke.knobDefault('Root.format', 'HD_1080')
nuke.knobDefault('Root.first_frame', '1001')
nuke.knobDefault('Root.last_frame', '1100')