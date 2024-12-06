from collections import defaultdict, deque

def parse_input(file_path):
	with open(file_path, 'r') as f:
		# Read the file and split into rules and updates
		rules_section, updates_section = f.read().strip().split("\n\n")
		# Parse rules as a list of tuples
		rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
		# Parse updates as lists of integers
		updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
	return rules, updates

def is_update_valid(update, rules):
	# Create a dictionary mapping page to its index in the update
	index_map = {page: i for i, page in enumerate(update)}
	# Check all relevant rules
	for X, Y in rules:
		if X in index_map and Y in index_map:
			if index_map[X] >= index_map[Y]:
				return False
	return True

def is_update_not_valid(update, rules):
	return not is_update_valid(update, rules)

def find_middle_page(update):
	# Return the middle page of the sorted update
	return update[len(update) // 2]

def topological_sort(pages, rules):
	# Build adjacency list and in-degree count
	graph = defaultdict(list)
	in_degree = defaultdict(int)
	for X, Y in rules:
		if X in pages and Y in pages:
			graph[X].append(Y)
			in_degree[Y] += 1
			if X not in in_degree:
				in_degree[X] = 0

	# Start with nodes having no incoming edges
	queue = deque([page for page in pages if in_degree[page] == 0])
	sorted_pages = []

	while queue:
		current = queue.popleft()
		sorted_pages.append(current)
		for neighbor in graph[current]:
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0:
				queue.append(neighbor)

	return sorted_pages

def part1(file_path):
	# Parse the input
	rules, updates = parse_input(file_path)
	# Initialize total sum of middle pages
	total_middle_sum = 0
	# Process each update
	for update in updates:
		if is_update_valid(update, rules):
			# If valid, find its middle page and add to the total
			total_middle_sum += find_middle_page(update)
	return total_middle_sum

def part2(file_path):
	rules, updates = parse_input(file_path)
	total_middle_sum = 0

	for update in updates:
		if not is_update_valid(update, rules):
			# Reorder the update if it's not valid
			sorted_update = topological_sort(update, rules)
			# Find the middle page and add to the total
			total_middle_sum += find_middle_page(sorted_update)

	return total_middle_sum

file_path = 'Day5/day5.txt'
result = part1(file_path)
print(result)
# 5064

result = part2(file_path)
print(result)
