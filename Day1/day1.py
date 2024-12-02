def parse_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        left = []
        right = []
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].split()
            left.append(lines[i][0])
            right.append(lines[i][1])
        
    return left, right

def to_ints(left, right):
    left = [int(i) for i in left]
    right = [int(i) for i in right]
    return left, right

def difference_full(left, right):
    diff = 0
    
    for i in range(len(left)):
        diff += abs(left[i] - right[i])
    return diff

def sim_score(left, right):
    tot_score = 0

    for i in range(len(left)):
        score = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                score += 1
        tot_score += score * left[i]
    return tot_score

# Example usage
file_path = 'Day1/day1.txt'
parsed_lines = parse_txt_file(file_path)

left, right = to_ints(parsed_lines[0], parsed_lines[1])

left.sort()
right.sort()


print("FIRST PART:", difference_full(left, right))
#1938424

print("SECOND PART:", sim_score(left, right))
#22014209



