# Day 4 solution
def parse_txt_file(file_path):
	with open(file_path, 'r') as file:
		lines = file.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].strip()
			lines[i] = lines[i].split()
		return lines

file_path = 'Day4/day4.txt'
parsed_lines = parse_txt_file(file_path)

# Part 1








# Part 2
