

import nuke


def shuffleRGB():

	try:
		shuffleRed = nuke.nodes.Shuffle(red = 'red', green = 'red', blue = 'red', alpha = 'red', label = 'R', inputs = [nuke.selectedNode()], tile_color = 4278190335)

		shuffleGreen = nuke.nodes.Shuffle(red = 'green', green = 'green', blue = 'green', alpha = 'green', label = 'G', inputs = [nuke.selectedNode()], tile_color = 16711935)

		shuffleBlue = nuke.nodes.Shuffle(red = 'blue', green = 'blue', blue = 'blue', alpha = 'blue', label = 'B', inputs = [nuke.selectedNode()], tile_color = 65535)


	except:

		shuffleRed = nuke.nodes.Shuffle(red = 'red', green = 'red', blue = 'red', alpha = 'red', label = 'R', tile_color = 4278190335)

		shuffleGreen = nuke.nodes.Shuffle(red = 'green', green = 'green', blue = 'green', alpha = 'green', label = 'G', tile_color = 16711935)

		shuffleBlue = nuke.nodes.Shuffle(red = 'blue', green = 'blue', blue = 'blue', alpha = 'blue', label = 'B', tile_color = 65535)