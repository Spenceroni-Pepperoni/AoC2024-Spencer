def parse_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].split()
            
    return lines

file_path = 'Day2/day2.txt'
parsed_lines = parse_txt_file(file_path)

def to_ints(left):
    for i in range(len(left)):
        for j in range(len(left[i])):
            left[i][j] = int(left[i][j])
    return left

def check_levels(lines):
    levels = []
    for i in range(len(lines)):
        flag = False
        str = ''
        for j in range(len(lines[i])):
            if j != 0:
                if lines[i][j] - lines[i][j-1] > 0:
                    if j > 1:
                        if lines[i][j-1] - lines[i][j-2] < 0 and str == 'd':
                            flag = True
                            levels.append(True)
                            break
                    if lines[i][j] <= lines[i][j-1]:
                        flag = True
                        levels.append(True)
                        break
                    str = 'i'
                    if not (1 <= lines[i][j] - lines[i][j-1] <= 3):
                        flag = True
                        levels.append(True)
                        break
                elif lines[i][j] - lines[i][j-1] < 0:
                    if j > 1:
                        if lines[i][j-1] - lines[i][j-2] > 0 and str == 'i':
                            flag = True
                            levels.append(True)
                            break
                    if lines[i][j] >= lines[i][j-1]:
                        flag = True
                        levels.append(True)
                        break
                    str = 'd'
                    if not (-3 <= lines[i][j] - lines[i][j-1] <= -1):
                        flag = True
                        levels.append(True)
                        break
                else:
                    flag = True
                    levels.append(True)
                    break
            if j == len(lines[i]) - 1:
                levels.append(False)
    return levels

def check_levels_2(levels):
    score = 0
    for i in range(len(levels)):
        if not levels[i]:
            score += 1
    return score
            
parsed_lines = to_ints(parsed_lines)
levels = check_levels(parsed_lines)
print("FIRST PART:", check_levels_2(levels))

def check_levels_3(lines, levels):
    score = check_levels_2(levels)
    check_again = []

    for i in range(len(lines)):
        if levels[i]:
            check_again.append(lines[i])

    levels_b = []
    for i in range(len(check_again)):
        flag = False
        sent = False
        temp = []
        
        for j in range(len(check_again[i])):
            temp = check_again[i].copy()
            temp.pop(j)
            flag = False
            str = ''
            if len(levels_b) > 1 and not levels_b[(len(levels_b)-1)] and sent:
                sent = False
                break
            for k in range(len(temp)):
                if k != 0:
                    if temp[k] - temp[k-1] > 0:
                        if k > 1:
                            if temp[k-1] - temp[k-2] < 0 and str == 'd':
                                flag = True
                                levels_b.append(True)
                                break
                        if temp[k] <= temp[k-1]:
                            flag = True
                            levels_b.append(True)
                            break
                        str = 'i'
                        if not (1 <= temp[k] - temp[k-1] <= 3):
                            flag = True
                            levels_b.append(True)
                            break
                    elif temp[k] - temp[k-1] < 0:
                        if k > 1:
                            if temp[k-1] - temp[k-2] > 0 and str == 'i':
                                flag = True
                                levels_b.append(True)
                                break
                        if temp[k] >= temp[k-1]:
                            flag = True
                            levels_b.append(True)
                            break
                        str = 'd'
                        if not (-3 <= temp[k] - temp[k-1] <= -1):
                            flag = True
                            levels_b.append(True)
                            break
                    else:
                        flag = True
                        levels_b.append(True)
                        break
                if k == len(temp) - 1:
                    levels_b.append(False)
                    sent = True
                    break
    inter_score = check_levels_2(levels_b)
    return score + inter_score

print("SECOND PART:", check_levels_3(parsed_lines, levels))
#569
