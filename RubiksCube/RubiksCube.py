import numpy as np
import random

#reference: https://ruwix.com/the-rubiks-cube/notation/

class RubiksCube3by3:

	def __init__(self):
		self.front  = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
		self.back   = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
		self.top    = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
		self.bottom = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
		self.right  = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
		self.left   = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

	def setCubeFaces(self, front, back, top, bottom, left, right):
		self.front = front
		self.back   = back
		self.top    = top
		self.bottom = bottom
		self.right  = right
		self.left   = left

	def getCube(self):
		return [self.front, self.back, self.top, self.bottom, self.right, self.left]

	def resetCube(self):
		self.front  = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
		self.back   = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
		self.top    = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
		self.bottom = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
		self.right  = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
		self.left   = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

	def rotateSideClockwise(self, side):
		return np.transpose([side[2], side[1], side[0]]).tolist()

	def rotateSideCounterClockwise(self, side):
		side[0].reverse()
		side[1].reverse()
		side[2].reverse()
		return np.transpose(side).tolist()

	def rotateSide180(self, side):
		side = self.rotateSideClockwise(side)
		return self.rotateSideClockwise(side)


	def turn_X(self):
		front  = self.front
		back   = self.back
		top    = self.top
		bottom = self.bottom

		self.front  = bottom
		self.top    = front
		self.back   = self.rotateSide180(top)
		self.bottom = self.rotateSide180(back)
		self.right  = self.rotateSideClockwise(self.right)
		self.left   = self.rotateSideCounterClockwise(self.left) 

	def turn_Xprime(self):
		front  = self.front
		back   = self.back
		top    = self.top
		bottom = self.bottom

		self.front  = top
		self.top    = self.rotateSide180(back)
		self.back   = self.rotateSide180(bottom)
		self.bottom = front
		self.right  = self.rotateSideCounterClockwise(self.right)
		self.left   = self.rotateSideClockwise(self.left)


	def turn_Y(self):
		front = self.front
		back  = self.back
		right = self.right
		left  = self.left

		self.front  = right
		self.right  = back
		self.back   = left
		self.left   = front
		self.top    = self.rotateSideClockwise(self.top)
		self.bottom = self.rotateSideCounterClockwise(self.bottom)

	def turn_Yprime(self):
		front = self.front
		back  = self.back
		right = self.right
		left  = self.left

		self.front  = left
		self.right  = front
		self.back   = right
		self.left   = back
		self.top    = self.rotateSideCounterClockwise(self.top)
		self.bottom = self.rotateSideClockwise(self.bottom)


	def turn_Z(self):
		top    = self.top
		bottom = self.bottom
		right  = self.right
		left   = self.left

		self.top    = self.rotateSideClockwise(left)
		self.bottom = self.rotateSideClockwise(right)
		self.right  = self.rotateSideClockwise(top) 
		self.left   = self.rotateSideClockwise(bottom)
		self.front  = self.rotateSideClockwise(self.front)
		self.back   = self.rotateSideCounterClockwise(self.back)

	def turn_Zprime(self):
		top    = self.top
		bottom = self.bottom
		right  = self.right
		left   = self.left

		self.top    = self.rotateSideCounterClockwise(right)
		self.bottom = self.rotateSideCounterClockwise(left)
		self.right  = self.rotateSideCounterClockwise(bottom)
		self.left   = self.rotateSideCounterClockwise(top)
		self.front  = self.rotateSideCounterClockwise(self.front)
		self.back   = self.rotateSideClockwise(self.back)



	def turn_R (self):
		top3    = [i[2] for i in self.top]
		back3   = [i[0] for i in self.back]
		bottom3 = [i[2] for i in self.bottom]
		front3  = [i[2] for i in self.front]
		top3.reverse()
		back3.reverse()

		self.top    = np.transpose([[i[0] for i in self.top], [i[1] for i in self.top], front3]).tolist()
		self.back   = np.transpose([top3, [i[1] for i in self.back], [i[2] for i in self.back]]).tolist()
		self.bottom = np.transpose([[i[0] for i in self.bottom], [i[1] for i in self.bottom], back3]).tolist()
		self.front  = np.transpose([[i[0] for i in self.front], [i[1] for i in self.front], bottom3]).tolist()
		self.right  = self.rotateSideClockwise(self.right)

	def turn_Rprime(self):
		top3    = [i[2] for i in self.top]
		back3   = [i[0] for i in self.back]
		bottom3 = [i[2] for i in self.bottom]
		front3  = [i[2] for i in self.front]
		bottom3.reverse()
		back3.reverse()

		self.top    = np.transpose([[i[0] for i in self.top], [i[1] for i in self.top], back3]).tolist()
		self.back   = np.transpose([bottom3, [i[1] for i in self.back], [i[2] for i in self.back]]).tolist()
		self.bottom = np.transpose([[i[0] for i in self.bottom], [i[1] for i in self.bottom], front3]).tolist()
		self.front  = np.transpose([[i[0] for i in self.front], [i[1] for i in self.front], top3]).tolist()
		self.right  = self.rotateSideCounterClockwise(self.right)


	def turn_L(self):
		top3    = [i[0] for i in self.top]
		back3   = [i[2] for i in self.back]
		bottom3 = [i[0] for i in self.bottom]
		front3  = [i[0] for i in self.front]
		bottom3.reverse()
		back3.reverse()

		self.top    = np.transpose([back3, [i[1] for i in self.top], [i[2] for i in self.top]]).tolist()
		self.back   = np.transpose([[i[0] for i in self.back], [i[1] for i in self.back], bottom3]).tolist()
		self.bottom = np.transpose([front3, [i[1] for i in self.bottom], [i[2] for i in self.bottom]]).tolist()
		self.front  = np.transpose([top3, [i[1] for i in self.front], [i[2] for i in self.front]]).tolist()
		self.left   = self.rotateSideClockwise(self.left)

	def turn_Lprime (self):
		top3    = [i[0] for i in self.top]
		back3   = [i[2] for i in self.back]
		bottom3 = [i[0] for i in self.bottom]
		front3  = [i[0] for i in self.front]
		top3.reverse()
		back3.reverse()

		self.top    = np.transpose([front3, [i[1] for i in self.top], [i[2] for i in self.top]]).tolist()
		self.back   = np.transpose([[i[0] for i in self.back], [i[1] for i in self.back], top3]).tolist()
		self.bottom = np.transpose([back3, [i[1] for i in self.bottom], [i[2] for i in self.bottom]]).tolist()
		self.front  = np.transpose([bottom3, [i[1] for i in self.front], [i[2] for i in self.front]]).tolist()
		self.left   = self.rotateSideCounterClockwise(self.left)


	def turn_F (self):
		top3    = self.top[2]
		bottom3 = self.bottom[0]
		right3  = [i[0] for i in self.right]
		left3   = [i[2] for i in self.left]
		right3.reverse()
		left3.reverse()

		self.top    = [self.top[0], self.top[1], left3]
		self.bottom = [right3, self.bottom[1], self.bottom[2]] 
		self.right  = np.transpose([top3, np.transpose([i[1] for i in self.right]), np.transpose([i[2] for i in self.right])]).tolist()
		self.left   = np.transpose([np.transpose([i[0] for i in self.left]), np.transpose([i[1] for i in self.left]), bottom3]).tolist()	
		self.front  = self.rotateSideClockwise(self.front)

	def turn_Fprime(self):
		top3    = self.top[2]
		bottom3 = self.bottom[0]
		right3  = [i[0] for i in self.right]
		left3   = [i[2] for i in self.left]
		bottom3.reverse()
		top3.reverse()

		self.top    = [self.top[0], self.top[1], right3]
		self.bottom = [left3, self.bottom[1], self.bottom[2]] 
		self.right  = np.transpose([bottom3, [i[1] for i in self.right], [i[2] for i in self.right]]).tolist()
		self.left   = np.transpose([[i[0] for i in self.left], [i[1] for i in self.left], top3]).tolist()
		self.front  = self.rotateSideCounterClockwise(self.front)


	def turn_B (self):
		top3    = self.top[0]
		bottom3 = self.bottom[2]
		right3  = [i[2] for i in self.right]
		left3   = [i[0] for i in self.left]
		bottom3.reverse()
		top3.reverse()

		self.top    = [right3, self.top[1], self.top[2]]
		self.bottom = [self.bottom[0], self.bottom[1], left3] 
		self.right  = np.transpose([[i[0] for i in self.right], [i[1] for i in self.right], bottom3]).tolist()
		self.left   = np.transpose([top3, [i[1] for i in self.left], [i[2] for i in self.left]]).tolist()
		self.back   = self.rotateSideClockwise(self.back)

	def turn_Bprime(self):
		top3    = self.top[0]
		bottom3 = self.bottom[2]
		right3  = [i[2] for i in self.right]
		left3   = [i[0] for i in self.left]
		right3.reverse()
		left3.reverse()

		self.top     = [left3, self.top[1], self.top[2]]
		self.bottom  = [self.bottom[0], self.bottom[1], right3] 
		self.right   = np.transpose([[i[0] for i in self.right], [i[1] for i in self.right], top3]).tolist()
		self.left    = np.transpose([bottom3, [i[1] for i in self.left], [i[2] for i in self.left]]).tolist()
		self.back    = self.rotateSideCounterClockwise(self.back)


	def turn_U (self):
		front3 = self.front[0]
		back3  = self.back[0]
		right3 = self.right[0]
		left3  = self.left[0]

		self.front = [right3, self.front[1], self.front[2]]
		self.back  = [left3, self.back[1], self.back[2]]
		self.right = [back3, self.right[1], self.right[2]]
		self.left  = [front3, self.left[1], self.left[2]]
		self.top   = self.rotateSideClockwise(self.top)

	def turn_Uprime(self):
		front3 = self.front[0]
		back3  = self.back[0]
		right3 = self.right[0]
		left3  = self.left[0]

		self.front = [left3, self.front[1], self.front[2]]
		self.back  = [right3, self.back[1], self.back[2]]
		self.right = [front3, self.right[1], self.right[2]]
		self.left  = [back3, self.left[1], self.left[2]]
		self.top   = self.rotateSideCounterClockwise(self.top)


	def turn_D (self):
		front3 = self.front[2]
		back3  = self.back[2]
		right3 = self.right[2]
		left3  = self.left[2]

		self.front  = [self.front[0], self.front[1], left3]
		self.back   = [self.back[0], self.back[1], right3]
		self.right  = [self.right[0], self.right[1], front3]
		self.left   = [self.left[0], self.left[1], back3]
		self.bottom = self.rotateSideClockwise(self.bottom)

	def turn_Dprime(self):
		front3 = self.front[2]
		back3  = self.back[2]
		right3 = self.right[2]
		left3  = self.left[2]

		self.front  = [self.front[0], self.front[1], right3]
		self.back   = [self.back[0], self.back[1], left3]
		self.right  = [self.right[0], self.right[1], back3]
		self.left   = [self.left[0], self.left[1], front3]
		self.bottom = self.rotateSideCounterClockwise(self.bottom)


	def turn_M (self):
		top3    = [i[1] for i in self.top]
		bottom3 = [i[1] for i in self.bottom]
		front3  = [i[1] for i in self.front]
		back3   = [i[1] for i in self.back]
		bottom3.reverse()
		back3.reverse()

		self.top    = np.transpose([[i[0] for i in self.top], back3, [i[2] for i in self.top]]).tolist()
		self.bottom = np.transpose([[i[0] for i in self.bottom], front3, [i[2] for i in self.bottom]]).tolist()
		self.front  = np.transpose([[i[0] for i in self.front], top3, [i[2] for i in self.front]]).tolist()
		self.back   = np.transpose([[i[0] for i in self.back], bottom3, [i[2] for i in self.back]]).tolist()

	def turn_Mprime(self):
		top3    = [i[1] for i in self.top]
		bottom3 = [i[1] for i in self.bottom]
		front3  = [i[1] for i in self.front]
		back3   = [i[1] for i in self.back]
		top3.reverse()
		back3.reverse()

		self.top    = np.transpose([[i[0] for i in self.top], front3, [i[2] for i in self.top]]).tolist()
		self.bottom = np.transpose([[i[0] for i in self.bottom], back3, [i[2] for i in self.bottom]]).tolist()
		self.front  = np.transpose([[i[0] for i in self.front], bottom3, [i[2] for i in self.front]]).tolist()
		self.back   = np.transpose([[i[0] for i in self.back], top3, [i[2] for i in self.back]]).tolist()


	def turn_E (self):
		front3 = self.front[1]
		back3  = self.back[1]
		right3 = self.right[1]
		left3  = self.left[1]

		self.front = [self.front[0], left3, self.front[2]]
		self.back  = [self.back[0], right3, self.back[2]]
		self.right = [self.right[0], front3, self.right[2]]
		self.left  = [self.left[0], back3, self.left[2]]

	def turn_Eprime(self):
		front3 = self.front[1]
		back3  = self.back[1]
		right3 = self.right[1]
		left3  = self.left[1]

		self.front = [self.front[0], right3, self.front[2]]
		self.back  = [self.back[0], left3, self.back[2]]
		self.right = [self.right[0], back3, self.right[2]]
		self.left  = [self.left[0], front3, self.left[2]]


	def turn_S (self):
		top3    = self.top[1]
		bottom3 = self.bottom[1]
		right3  = [i[1] for i in self.right]
		left3   = [i[1] for i in self.left]
		left3.reverse()
		right3.reverse()

		self.top    = [self.top[0], left3, self.top[2]]
		self.bottom = [self.bottom[0], right3, self.bottom[2]] 
		self.right  = np.transpose([[i[0] for i in self.right], top3, [i[2] for i in self.right]]).tolist()
		self.left   = np.transpose([[i[0] for i in self.left], bottom3, [i[2] for i in self.left]]).tolist()	

	def turn_Sprime(self):
		top3    = self.top[1]
		bottom3 = self.bottom[1]
		right3  = [i[1] for i in self.right]
		left3   = [i[1] for i in self.left]
		top3.reverse()
		bottom3.reverse()

		self.top    = [self.top[0], right3, self.top[2]]
		self.bottom = [self.bottom[0], left3, self.bottom[2]] 
		self.right  = np.transpose([[i[0] for i in self.right], bottom3, [i[2] for i in self.right]]).tolist()
		self.left   = np.transpose([[i[0] for i in self.left], top3, [i[2] for i in self.left]]).tolist()	


	def shuffle (self, min, max):
		moves = [self.turn_X, self.turn_Xprime,
				 self.turn_Y, self.turn_Yprime,
				 self.turn_Z, self.turn_Zprime,

				 self.turn_R, self.turn_Rprime,
				 self.turn_L, self.turn_Lprime,
				 self.turn_F, self.turn_Fprime,
				 self.turn_B, self.turn_Bprime,
				 self.turn_U, self.turn_Uprime,
				 self.turn_D, self.turn_Dprime,
				 self.turn_M, self.turn_Mprime,
				 self.turn_E, self.turn_Eprime,
				 self.turn_S, self.turn_Sprime]

		commands = ["X", "X'",
					"Y", "Y'",
					"Z", "Z'",

					"R", "R'", "L", "L'",
					"F", "F'", "B", "B'",
					"U", "U'", "D", "D'",
					"M", "M'", "E", "E'", "S", "S'"]

		num_moves = random.randint(min, max)
		shuffled_moves = []
		for i in range(num_moves):
			random_move = random.randint(0, len(moves) - 1)
			moves[random_move]()
			shuffled_moves.append(commands[random_move])
		return shuffled_moves

	def solve(self):
		print('Solved')

