import re

class letters:
	X = 1
	M = 2
	A = 3
	S = 4

# Day 4 solution
def parse_txt_file(file_path):
	with open(file_path, 'r') as file:
		lines = file.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].strip()
			lines[i] = lines[i].split()
		return lines

file_path = 'Day4/day4.txt'
# file_path = 'Day4/test.txt'
# file_path = 'Day4/test2.txt'
parsed_lines = parse_txt_file(file_path)

def check_XMAS(a,b,c,d):
	if a+b+c+d == "XMAS":
		return True
	else:
		return False

# Part 1
def search_for_XMAS():
	index_of_XMAS = [] #Tuple of (line, index)
	letter_count = 0
	for i in range(len(parsed_lines)):
		for k in range(len(parsed_lines[i])):
			for j in range(len(parsed_lines[i][k])):
				# diagonal up/down left
				if i - 3 >= 0 and j - 3 >= 0:
					
					# check diagonal up left
					if check_XMAS(parsed_lines[i-3][k][j-3],parsed_lines[i-2][k][j-2],parsed_lines[i-1][k][j-1],parsed_lines[i][k][j]):
						index_of_XMAS.append([(i-3, j-3), (i-2, j-2), (i-1, j-1), (i, j)])
						letter_count += 1
					# check diagonal down left
					if check_XMAS(parsed_lines[i][k][j],parsed_lines[i-1][k][j-1],parsed_lines[i-2][k][j-2],parsed_lines[i-3][k][j-3]):
						index_of_XMAS.append([(i, j), (i-1, j-1), (i-2, j-2), (i-3, j-3)])
						letter_count += 1

				if i - 3 >= 0 and j + 3 < len(parsed_lines[i]):
					# check diagonal up right
					if check_XMAS(parsed_lines[i-3][k][j+3],parsed_lines[i-2][k][j+2],parsed_lines[i-1][k][j+1],parsed_lines[i][k][j]):
						index_of_XMAS.append([(i-3, j+3), (i-2, j+2), (i-1, j+1), (i, j)])
						letter_count += 1
					# check diagonal down right
					if check_XMAS(parsed_lines[i][k][j],parsed_lines[i-1][k][j+1],parsed_lines[i-2][k][j+2],parsed_lines[i-3][k][j+3]):
						index_of_XMAS.append([(i, j), (i-1, j+1), (i-2, j+2), (i-3, j+3)])
						letter_count += 1

				if i + 3 < len(parsed_lines) and j - 3 >=0:
					# check diagonal down left
					if check_XMAS(parsed_lines[i+3][k][j-3],parsed_lines[i+2][k][j-2],parsed_lines[i+1][k][j-1],parsed_lines[i][k][j]):
						index_of_XMAS.append([(i+3, j-3), (i+2, j-2), (i+1, j-1), (i, j)])
						letter_count += 1
					# check diagonal up right
					if check_XMAS(parsed_lines[i][k][j],parsed_lines[i+1][k][j-1],parsed_lines[i+2][k][j-2],parsed_lines[i+3][k][j-3]):
						index_of_XMAS.append([(i, j), (i+1, j-1), (i+2, j-2), (i+3, j-3)])
						letter_count += 1
				
				if j + 3 < len(parsed_lines[i]):
					# check right
					if check_XMAS(parsed_lines[i][k][j], parsed_lines[i][k][j+1], parsed_lines[i][k][j+2], parsed_lines[i][k][j+3]):
						index_of_XMAS.append([(i, j), (i, j+1), (i, j+2), (i, j+3)])
						letter_count += 1
					# check left
					if check_XMAS(parsed_lines[i][k][j+3], parsed_lines[i][k][j+2], parsed_lines[i][k][j+1], parsed_lines[i][k][j]):
						index_of_XMAS.append([(i, j+3), (i, j+2), (i, j+1), (i, j)])
						letter_count += 1

				if i + 3 < len(parsed_lines):
					if check_XMAS(parsed_lines[i][k][j], parsed_lines[i+1][k][j], parsed_lines[i+2][k][j], parsed_lines[i+3][k][j]):
						index_of_XMAS.append([(i, j), (i+1, j), (i+2, j), (i+3, j)])
						letter_count += 1
					if check_XMAS(parsed_lines[i+3][k][j], parsed_lines[i+2][k][j], parsed_lines[i+1][k][j], parsed_lines[i][k][j]):
						index_of_XMAS.append([(i+3, j), (i+2, j), (i+1, j), (i, j)])
						letter_count += 1

				if i - 3 >= 0:
					if check_XMAS(parsed_lines[i-3][k][j], parsed_lines[i-2][k][j], parsed_lines[i-1][k][j], parsed_lines[i][k][j]):
						index_of_XMAS.append([(i-3, j), (i-2, j), (i-1, j), (i, j)])
						letter_count += 1
					if check_XMAS(parsed_lines[i][k][j], parsed_lines[i-1][k][j], parsed_lines[i-2][k][j], parsed_lines[i-3][k][j]):
						index_of_XMAS.append([(i, j), (i-1, j), (i-2, j), (i-3, j)])
						letter_count += 1

				if j - 3 >= 0:
					if check_XMAS(parsed_lines[i][k][j-3], parsed_lines[i][k][j-2], parsed_lines[i][k][j-1], parsed_lines[i][k][j]):
						index_of_XMAS.append([(i, j-3), (i, j-2), (i, j-1), (i, j)])
						letter_count += 1

					if check_XMAS(parsed_lines[i][k][j], parsed_lines[i][k][j-1], parsed_lines[i][k][j-2], parsed_lines[i][k][j-3]):
						index_of_XMAS.append([(i, j), (i, j-1), (i, j-2), (i, j-3)])
						letter_count += 1

	return index_of_XMAS, letter_count

def duplicate_check(XMAS, count):
	temp = count
	for i in range(len(XMAS)):
		for j in range(i+1, len(XMAS)):
			if XMAS[i] == XMAS[j]:
				temp -= 1
	return temp

xmas, count = search_for_XMAS()

print(duplicate_check(xmas, count))
#2578
	
# Part 2
def check_x_mas(a,b,c,d,e):
	# print(a, " ", b, "\n ", c, "\n", d, " ", e)

	if c == 'A':
		if a == b == 'M' and d == e == 'S':
			return True
		if a == b == 'S' and d == e == 'M':
			return True
		# if a == e == 'M' and b == d == 'S':
		# 	return True
		# if a == e == 'S' and b == d == 'M':
		# 	return True
		if a == d == 'M' and b == e == 'S':
			return True
		if a == d == 'S' and b == e == 'M':
			return True
		
	return False

def find_crossed():
	letter_count = 0
	for i in range(len(parsed_lines)):
		for k in range(len(parsed_lines[i])):
			for j in range(len(parsed_lines[i][k])):
				if (i > 0 and j > 0):
					if (j < len(parsed_lines[i][k]) - 1 and i < len(parsed_lines) - 1):
						if check_x_mas(parsed_lines[i-1][k][j-1], parsed_lines[i-1][k][j+1], parsed_lines[i][k][j], parsed_lines[i+1][k][j-1], parsed_lines[i+1][k][j+1]):
							letter_count += 1
	return letter_count

print(find_crossed())
#1972