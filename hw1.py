# Solves 4 to 1

def primitive(state):
	if state == 0:
		return "L"
	elif state == 1 or state == 2:
		return "W"
	return "U"

def gen_move(state):
	if state > 1:
		return ["take_one", "take_two"]
	return ["take_one"]

def do_move(action, state):
	if action == "take_one":
		return state - 1
	return state - 2

def solve(pos):
	if pos < 3:
		return primitive(pos)
	else:
		actions = gen_move(pos)
		for action in actions:
			if solve(do_move(action, pos)) == "L":
				return "W"
		return "L"

def init_pos():
	return 4

# Prints out values for all possible states: 0 - 4
for num in range(0, init_pos() + 1):
	print(num, ": " + solve(num))

