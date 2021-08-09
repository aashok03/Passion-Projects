from RubiksCube import RubiksCube3by3
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

myCube = RubiksCube3by3()

@app.route('/', methods=['GET'])
def home():

	output = """
Welcome to the Rubik\'s Cube Simulator! 

                  ______________________
	         /       /      /      /\\
	        /       /      /      /  \\
	       /_______/______/______/    \\
	      /       /      /      / \\   /\\ 
	     /       /      /      /   \\ /  \\
	    /_______/______/______/     \\    \\
	   /       /      /      / \\   / \\   /\\ 
	  /       /      /      /   \\ /   \\ /  \\
	 /_______/______/______/     \\     \\    \\
	 \\       \\      \\      \\    / \\   / \\   / 
	  \\       \\      \\      \\  /   \\ /   \\ /
	   \\_______\\______\\______\\/     \\     /
	    \\       \\      \\      \\    / \\   /
	     \\       \\      \\      \\  /   \\ /
	      \\_______\\______\\______\\/     /
	       \\       \\      \\      \\    /
	        \\       \\      \\      \\  /
	         \\_______\\______\\______\\/


To familiarize yourself with standard Rubik's cube notation, refer to https://ruwix.com/the-rubiks-cube/notation/
		        

You can use the following commands to change the cube:

X: Rotate the entire cube in the X-axis clockwise
X': Rotate the entire cube in the X-axis counter-clockwise
Y: Rotate the entire cube in the Y-axis clockwise
Y': Rotate the entire cube in the Y-axis counter-clockwise
Z: Rotate the entire cube in the Z-axis clockwise
Z': Rotate the entire cube in the Z-axis counter-clockwise

R: Turn the right face clockwise
R': Turn the right face counter-clockwise
L: Turn the left face clockwise
L': Turn the left face counter-clockwise
F: Turn the front face clockwise
F': Turn the front face counter-clockwise
B: Turn the back face clockwise
B': Turn the back face counter-clockwise
U: Turn the top face clockwise
U': Turn the top face counter-clockwise
D: Turn the bottom face clockwise
D': Turn the bottom face counter-clockwise
M: Turn the X-axis middle face clockwise
M': Turn the X-axis middle face counter-clockwise
E: Turn the Y-axis middle face clockwise
E': Turn the Y-axis middle face counter-clockwise
S: Turn the Z-axis middle face clockwise
S': Turn the Z-axis middle face counter-clockwise

set: Set a custom cube:
   - Enter the color of each square of each face row by row. Make sure you enter capital letters.
   - Faces should be entered in the following order: front, back, top, bottom, right, left
   - Color codes are -> Green: G, Blue -> B, White -> W, Yellow -> Y, Red -> R, Orange -> O
   - For instance, the default cube would be inputted as GGGGGGGGG BBBBBBBBB WWWWWWWWW YYYYYYYYY RRRRRRRRR OOOOOOOOO
   - Make sure that you enter 6 faces, each with 9 squares. Each color can only appear 9 times.
   - NOTE: Apart from the restrictions mentioned above, the cube does not verify if the combination you entered is physically possible or not.
reset: Reset the cube
split-faces: Display each face of the cube separately
combine-faces: Combine the faces of the cube in the following format:
      U
   L  F  R  B
      D
shuffle: Shuffle the cube
solve: Solve the cube
help: List the available commands
quit: Quit the simulation"""

	return output, 200, {'Content-Type': 'text/css; charset=utf-8'}


def cubeToString(cube):
	faces = ["Front", "Back", "Top", "Bottom", "Right", "Left"]
	output = ""
	for i in range (len(cube)):
		output = output + faces[i] + ": " + str(cube[i]) + "<br>"
	return output
	

@app.route('/cube', methods=['GET'])
def displayCube():
	return cubeToString(myCube.getCube())

#Reset Cube
@app.route('/cube/reset', methods=['GET'])
def resetCube():
	myCube.resetCube()
	return cubeToString(myCube.getCube())


#Right face rotations
@app.route('/cube/Rc', methods=['GET'])
def turn_Rc():
	myCube.turn_R()
	return cubeToString(myCube.getCube())

@app.route('/cube/Rcc', methods=['GET'])
def turn_Rcc():
	myCube.turn_Rprime()
	return cubeToString(myCube.getCube())


#Left face rotations
@app.route('/cube/Lc', methods=['GET'])
def turn_Lc():
	myCube.turn_L()
	return cubeToString(myCube.getCube())

@app.route('/cube/Lcc', methods=['GET'])
def turn_Lcc():
	myCube.turn_Lprime()
	return cubeToString(myCube.getCube())


#Top face rotations
@app.route('/cube/Uc', methods=['GET'])
def turn_Uc():
	myCube.turn_U()
	return cubeToString(myCube.getCube())

@app.route('/cube/Ucc', methods=['GET'])
def turn_Ucc():
	myCube.turn_Uprime()
	return cubeToString(myCube.getCube())


#Bottom face rotations
@app.route('/cube/Dc', methods=['GET'])
def turn_Dc():
	myCube.turn_D()
	return cubeToString(myCube.getCube())

@app.route('/cube/Dcc', methods=['GET'])
def turn_Dcc():
	myCube.turn_Dprime()
	return cubeToString(myCube.getCube())


#Front face rotations
@app.route('/cube/Fc', methods=['GET'])
def turn_Fc():
	myCube.turn_F()
	return cubeToString(myCube.getCube())

@app.route('/cube/Fcc', methods=['GET'])
def turn_Fcc():
	myCube.turn_Fprime()
	return cubeToString(myCube.getCube())


#Back face rotations
@app.route('/cube/Bc', methods=['GET'])
def turn_Bc():
	myCube.turn_B()
	return cubeToString(myCube.getCube())

@app.route('/cube/Bcc', methods=['GET'])
def turn_Bcc():
	myCube.turn_Bprime()
	return cubeToString(myCube.getCube())


#M face rotations
@app.route('/cube/Mc', methods=['GET'])
def turn_Mc():
	myCube.turn_M()
	return cubeToString(myCube.getCube())

@app.route('/cube/Mcc', methods=['GET'])
def turn_Mcc():
	myCube.turn_Mprime()
	return cubeToString(myCube.getCube())


#E face rotations
@app.route('/cube/Ec', methods=['GET'])
def turn_Ec():
	myCube.turn_E()
	return cubeToString(myCube.getCube())

@app.route('/cube/Ecc', methods=['GET'])
def turn_Ecc():
	myCube.turn_Eprime()
	return cubeToString(myCube.getCube())


#S face rotations
@app.route('/cube/Sc', methods=['GET'])
def turn_Sc():
	myCube.turn_S()
	return cubeToString(myCube.getCube())

@app.route('/cube/Scc', methods=['GET'])
def turn_Scc():
	myCube.turn_Sprime()
	return cubeToString(myCube.getCube())


#Turn cube X
@app.route('/cube/Xc', methods=['GET'])
def turn_Xc():
	myCube.turn_X()
	return cubeToString(myCube.getCube())

@app.route('/cube/Xcc', methods=['GET'])
def turn_Xcc():
	myCube.turn_Xprime()
	return cubeToString(myCube.getCube())


#Turn cube Y
@app.route('/cube/Yc', methods=['GET'])
def turn_Yc():
	myCube.turn_Y()
	return cubeToString(myCube.getCube())

@app.route('/cube/Ycc', methods=['GET'])
def turn_Ycc():
	myCube.turn_Yprime()
	return cubeToString(myCube.getCube())


#Turn cube Z
@app.route('/cube/Zc', methods=['GET'])
def turn_Zc():
	myCube.turn_Z()
	return cubeToString(myCube.getCube())

@app.route('/cube/Zcc', methods=['GET'])
def turn_Zcc():
	myCube.turn_Zprime()
	return cubeToString(myCube.getCube())


#Shuffle cube
@app.route('/cube/shuffle', methods=['GET'])
def shuffle():
	moves = myCube.shuffle(15, 50)
	output = str(cubeToString(myCube.getCube())) + "\nMoves: " + str(moves)
	return output

app.run()