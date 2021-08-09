from RubiksCube import RubiksCube3by3
import random
from colored import fg, bg, attr


class PlayRubiksCube:
	
	def __init__(self):
		self.myCube = RubiksCube3by3()

		self.displayMode = "combine-faces"

		self.commands = ["X", "X'", 
					     "Y", "Y'", 
					     "Z", "Z'", 

					     "R", "R'", "L", "L'", 
					     "F", "F'", "B", "B'",
					     "U", "U'", "D", "D'",
					     "M", "M'", "E", "E'", "S", "S'",

					     "set", "reset", "split-faces", "combine-faces", 
					     "shuffle", "solve", "help", "quit"]

		self.descriptions = ["Rotate the entire cube in the X-axis clockwise",
						     "Rotate the entire cube in the X-axis counter-clockwise",
						     "Rotate the entire cube in the Y-axis clockwise",
						     "Rotate the entire cube in the Y-axis counter-clockwise",
						     "Rotate the entire cube in the Z-axis clockwise",
						     "Rotate the entire cube in the Z-axis counter-clockwise\n",

						     "Turn the right face clockwise",
						     "Turn the right face counter-clockwise",
						     "Turn the left face clockwise",
						     "Turn the left face counter-clockwise",
						     "Turn the front face clockwise",
						     "Turn the front face counter-clockwise",
						     "Turn the back face clockwise",
						     "Turn the back face counter-clockwise",
						     "Turn the top face clockwise",
						     "Turn the top face counter-clockwise",
						     "Turn the bottom face clockwise",
						     "Turn the bottom face counter-clockwise",
						     "Turn the X-axis middle face clockwise",
						     "Turn the X-axis middle face counter-clockwise",
						     "Turn the Y-axis middle face clockwise",
						     "Turn the Y-axis middle face counter-clockwise",
						     "Turn the Z-axis middle face clockwise",
						     "Turn the Z-axis middle face counter-clockwise\n",

                             "Set a custom cube:\n" +
                             "   - Enter the color of each square of each face row by row. Make sure you enter capital letters.\n" +
		                     "   - Faces should be entered in the following order: front, back, top, bottom, right, left\n" +
		                     "   - Color codes are -> Green: G, Blue -> B, White -> W, Yellow -> Y, Red -> R, Orange -> O\n" +
		                     "   - For instance, the default cube would be inputted as GGGGGGGGG BBBBBBBBB WWWWWWWWW YYYYYYYYY RRRRRRRRR OOOOOOOOO\n" +
		                     "   - Make sure that you enter 6 faces, each with 9 squares. Each color can only appear 9 times.\n" +
		                     "   - NOTE: Apart from the restrictions mentioned above, the cube does not verify if the combination you entered is physically possible or not." ,
						     "Reset the cube",
						     "Display each face of the cube separately",
						     "Combine the faces of the cube in the following format:\n" + 
						     "      U\n" +
						     "   L  F  R  B\n"+ 
						     "      D",
						     "Shuffle the cube",
						     "Solve the cube",
						     "List the available commands",
						     "Quit the simulation\n"]


	def printRubiksCubeFaces(self):
		cube_colors = ['W', 'G', 'B', 'R', 'Y', 'O']
		color_codes = ['white', 'green' ,'blue' , 'light_red', 'light_yellow', 'orange_red_1']
		faces = self.myCube.getCube()
		print('Front \t\tBack \t\tTop \t\tBottom \t\tRight \t\tLeft')
		for i in range (3):
			for k in range(len(faces)):
				for j in range (3):
					square_color = color_codes[cube_colors.index(faces[k][i][j])]
					color = bg(square_color) + fg(square_color)
					reset = attr('reset')
					print (color + '  ' + reset, end = '  ')
				print('\t', end = '')
			print("\n")
		print()


	def printExpandedRubiksCube(self):
		cube_colors = ['W', 'G', 'B', 'R', 'Y', 'O']
		color_codes = ['white', 'green' ,'blue' , 'light_red', 'light_yellow', 'orange_red_1']
		faces = self.myCube.getCube()

		middle_faces = [faces[5], faces[0], faces[4], faces[1]]

		reset = attr('reset')

		for i in range (3):
			print("\t     ", end = '')
			for j in range (3):
				square_color = color_codes[cube_colors.index(faces[2][i][j])]
				color = bg(square_color) + fg(square_color)
				print (color + '  ' + reset, end = '  ')
			print("\n")

		for i in range (3):
			for k in range(len(middle_faces)):
				for j in range (3):
					square_color = color_codes[cube_colors.index(middle_faces[k][i][j])]
					color = bg(square_color) + fg(square_color)
					reset = attr('reset')
					print (color + '  ' + reset, end = '  ')
				print(' ', end = '')
			print("\n")

		for i in range (3):
			print("\t     ", end = '')
			for j in range (3):
				square_color = color_codes[cube_colors.index(faces[3][i][j])]
				color = bg(square_color) + fg(square_color)
				print (color + '  ' + reset, end = '  ')
			print("\n")
		print()


	def getDisplayMethod(self):
		if (self.displayMode == "combine-faces"):
			self.printExpandedRubiksCube()
		else:
			self.printRubiksCubeFaces()

	def setDisplayFaces(self):
		self.displayMode = "split-faces"

	def setDisplayCombine(self):
		self.displayMode = "combine-faces"

	
	def shuffleCube(self):
		shuffled_moves = self.myCube.shuffle(15, 50)
		print ("The cube was shuffled " + str(len(shuffled_moves)) + " times: " + ' '.join(shuffled_moves))


	def setCustomCube(self):
		colors = ['W', 'G', 'B', 'R', 'Y', 'O']
		track_colors = [0, 0, 0, 0, 0, 0]

		faces = input("Enter the faces of the cube: ").split()
		if (len(faces) != 6):
			print ("Invalid input: must enter 6 faces")
			return

		cube = []
		for i in range (len(faces)):
			split_squares = [char for char in faces[i]]
			
			if (len(split_squares) != 9):
				print("Invalid input: each face must have 9 squares")
				return

			for i in split_squares:
				if (not i in colors):
					print("Invalid input: colors must be from the set " + str(colors))
					return
				else:
					track_colors[colors.index(i)] += 1 

			row1 = split_squares[0:3]
			row2 = split_squares[3:6]
			row3 = split_squares[6:9]
			face = [row1, row2, row3]
			cube.append(face)

		for i in track_colors:
			if i != 9:
				print("Invalid input: each color can only appear 9 times")
				return

		self.myCube.setCubeFaces(cube[0], cube[1], cube[2], 
			                cube[3], cube[4], cube[5])


	def printInstructions(self):
		print("\nTo familiarize yourself with standard Rubik's cube notation, refer to https://ruwix.com/the-rubiks-cube/notation/")
		print('You can use the following commands to change the cube:\n')
		for i in range (len(self.commands)):
			print (self.commands[i] + ": " + self.descriptions[i])


	def initiateSimulator(self):

		moves = [self.myCube.turn_X, self.myCube.turn_Xprime, 
				 self.myCube.turn_Y, self.myCube.turn_Yprime, 
				 self.myCube.turn_Z, self.myCube.turn_Zprime,

				 self.myCube.turn_R, self.myCube.turn_Rprime,
				 self.myCube.turn_L, self.myCube.turn_Lprime,
				 self.myCube.turn_F, self.myCube.turn_Fprime,
				 self.myCube.turn_B, self.myCube.turn_Bprime,
				 self.myCube.turn_U, self.myCube.turn_Uprime,
				 self.myCube.turn_D, self.myCube.turn_Dprime,
				 self.myCube.turn_M, self.myCube.turn_Mprime,
				 self.myCube.turn_E, self.myCube.turn_Eprime,
				 self.myCube.turn_S, self.myCube.turn_Sprime,
		 
				 self.setCustomCube, self.myCube.resetCube, 
				 self.setDisplayFaces, self.setDisplayCombine,
				 self.shuffleCube, self.myCube.solve, self.printInstructions, exit]

		green_color = bg('green') + fg('black')
		white_color = bg('white') + fg('black')
		red_color   = bg('red') + fg('white')
		reset = attr('reset')

		print('\nWelcome to the Rubik\'s Cube Simulator!\n')
		print("         ______________________")
		print("        /       /      /      /\\")
		print("       /       /      /      /  \\")
		print("      /_______/______/______/    \\")
		print("     /       /      /      / \\   /\\")
		print("    /       /      /      /   \\ /  \\")
		print("   /_______/______/______/     \\    \\")
		print("  /       /      /      / \\   / \\   /\\")
		print(" /       /      /      /   \\ /   \\ /  \\")
		print("/_______/______/______/     \\     \\    \\")
		print("\\       \\      \\      \\    / \\   / \\   / ")
		print(" \\       \\      \\      \\  /   \\ /   \\ /")
		print("  \\_______\\______\\______\\/     \\     /")
		print("   \\       \\      \\      \\    / \\   /")
		print("    \\       \\      \\      \\  /   \\ /")
		print("     \\_______\\______\\______\\/     /")
		print("      \\       \\      \\      \\    /")
		print("       \\       \\      \\      \\  /")
		print("        \\_______\\______\\______\\/\n")

		self.printInstructions()
		self.getDisplayMethod()

		while (True):
			command = input('Enter your move: ')
			if (command in self.commands):
				i = self.commands.index(command)
				moves[i]()
				self.getDisplayMethod()
			else:
				print('Invalid move\n')
