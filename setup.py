import os

def create_aoc_files(start_day, end_day):
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    for day in range(start_day, end_day + 1):
        day_folder = os.path.join(base_path, f'Day{day}')
        os.makedirs(day_folder, exist_ok=True)
        
        python_file_path = os.path.join(day_folder, f'day{day}.py')
        txt_file_path = os.path.join(day_folder, f'day{day}.txt')
        
        with open(python_file_path, 'w') as py_file:
            py_file.write(f'# Day {day} solution\n')
            py_file.write('def parse_txt_file(file_path):\n'
            '\twith open(file_path, \'r\') as file:\n'
            '\t\tlines = file.readlines()\n'
            '\t\tfor i in range(len(lines)):\n'
            '\t\t\tlines[i] = lines[i].strip()\n'
            '\t\t\tlines[i] = lines[i].split()\n'
            '\t\treturn lines\n'
            f'\nfile_path = \'Day{day}/day{day}.txt\'\n'
            'parsed_lines = parse_txt_file(file_path)\n\n# Part 1\n'
            '\n\n\n\n\n\n\n\n# Part 2\n')
        
        with open(txt_file_path, 'w') as txt_file:
            pass

if __name__ == "__main__":
    start_day = int(input("Enter the start day: "))
    end_day = int(input("Enter the end day: "))
    create_aoc_files(start_day, end_day)