# Welcome to the Rubik\'s Cube Simulator! 


To familiarize yourself with standard Rubik's cube notation, refer to https://ruwix.com/the-rubiks-cube/notation/
		        

You can use the following commands to change the cube:

X: Rotate the entire cube in the X-axis clockwise\
X': Rotate the entire cube in the X-axis counter-clockwise\
Y: Rotate the entire cube in the Y-axis clockwise\
Y': Rotate the entire cube in the Y-axis counter-clockwise\
Z: Rotate the entire cube in the Z-axis clockwise\
Z': Rotate the entire cube in the Z-axis counter-clockwise\

R: Turn the right face clockwise\
R': Turn the right face counter-clockwise\
L: Turn the left face clockwise\
L': Turn the left face counter-clockwise\
F: Turn the front face clockwise\
F': Turn the front face counter-clockwise\
B: Turn the back face clockwise\
B': Turn the back face counter-clockwise\
U: Turn the top face clockwise\
U': Turn the top face counter-clockwise\
D: Turn the bottom face clockwise\
D': Turn the bottom face counter-clockwise\
M: Turn the X-axis middle face clockwise\
M': Turn the X-axis middle face counter-clockwise\
E: Turn the Y-axis middle face clockwise\
E': Turn the Y-axis middle face counter-clockwise\
S: Turn the Z-axis middle face clockwise\
S': Turn the Z-axis middle face counter-clockwise\

set: Set a custom cube:
   - Enter the color of each square of each face row by row. Make sure you enter capital letters.
   - Faces should be entered in the following order: front, back, top, bottom, right, left
   - Color codes are -> Green: G, Blue -> B, White -> W, Yellow -> Y, Red -> R, Orange -> O
   - For instance, the default cube would be inputted as GGGGGGGGG BBBBBBBBB WWWWWWWWW YYYYYYYYY RRRRRRRRR OOOOOOOOO
   - Make sure that you enter 6 faces, each with 9 squares. Each color can only appear 9 times.
   - NOTE: Apart from the restrictions mentioned above, the cube does not verify if the combination you entered is physically possible or not.
reset: Reset the cube\
split-faces: Display each face of the cube separately\
combine-faces: Combine the faces of the cube in the following format:\
&nbsp; &nbsp; U\
L  F  R  B\
&nbsp; &nbsp; D\
shuffle: Shuffle the cube\
solve: Solve the cube\
help: List the available commands\
quit: Quit the simulation\
