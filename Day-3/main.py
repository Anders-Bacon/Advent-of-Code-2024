from typing import TextIO, List
import re


def main():
    
    with open("input.txt", "r", encoding="utf-8") as file:
        pairs = parse_data(file)
        result_without_control = multiply_numbers(pairs)
        print(f"Result without control: {result_without_control}")

    with open("input.txt", "r", encoding="utf-8") as file:
        result_with_control = multiply_numbers_control(file)
        print(f"Result with control: {result_with_control}")

def parse_data(file: TextIO) -> List[int]:
    content = file.read()
    matches = re.findall(r"mul\((\d+),\s*(\d+)\)", content)
    return [(int(num1), int(num2)) for num1, num2 in matches]

def multiply_numbers_control(file: TextIO) -> List[tuple[int, int]]:
    data = file.read()
    # Regex pattern to match valid mul(X,Y) instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Regex patterns to match do() and don't() instructions
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    # Find all mul instructions with their positions
    mul_matches = [(match.start(), int(match.group(1)), int(match.group(2)))
                   for match in re.finditer(mul_pattern, data)]
    
    # Find all do() and don't() instructions with their positions
    do_matches = [match.start() for match in re.finditer(do_pattern, data)]
    dont_matches = [match.start() for match in re.finditer(dont_pattern, data)]

    # Combine do() and don't() instructions to determine the state of mul enabling
    control_matches = [(pos, 'do') for pos in do_matches] + [(pos, "don't") for pos in dont_matches]
    control_matches.sort()  # Sort by position to process in sequence

    mul_enabled = True  # Initial state of mul enabling
    current_control_idx = 0
    total_sum = 0

    for pos, x, y in mul_matches:
        # Update the mul_enabled state based on the most recent control instruction before the current mul
        while current_control_idx < len(control_matches) and control_matches[current_control_idx][0] < pos:
            _, control = control_matches[current_control_idx]
            if control == 'do':
                mul_enabled = True
            elif control == "don't":
                mul_enabled = False
            current_control_idx += 1
        
        # If mul is enabled, add the result of the multiplication
        if mul_enabled:
            total_sum += x * y
    
    return total_sum

def multiply_numbers(pairs: List[tuple[int, int]]) -> int:
    result = 0
    for num1, num2 in pairs:
        result += num1 * num2
    return result


if __name__ == "__main__":
    main()