# Day 3 solution
import re

def parse_txt_file(file_path):
	with open(file_path, 'r') as file:
		lines = file.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].strip()
			lines[i] = lines[i].split()
			
		return lines

file_path = 'Day3/day3.txt'
# file_path = 'Day3/test.txt'
parsed_lines = parse_txt_file(file_path)
print(parsed_lines)

# Part 1
def find_in_string(string):
	pattern = r"mul\((\d+),(\d+)\)"
	found = re.findall(pattern, string)
	found_int = [(int(x), int(y)) for x, y in found]
	print(found_int)
	return found_int

def find_mul(parsed_lines):
	count = 0
	combined_string = ' '.join([' '.join(line) for line in parsed_lines])
	found = find_in_string(combined_string)
	for x, y in found:
		count += x * y
	return count

print(find_mul(parsed_lines))
# 175015740
	
# Part 2

def find_mul_with_do_dont(parsed_lines):
	combined_string = ' '.join([' '.join(line) for line in parsed_lines])
	pattern = r"don't\(\).*?do\(\)"
	modified_string = re.sub(pattern, '', combined_string)
	return find_mul([modified_string.split()])
	

print(find_mul_with_do_dont(parsed_lines))
#112272912

