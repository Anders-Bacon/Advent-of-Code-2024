from typing import TextIO, List, Tuple
import re


def parse_data(file: TextIO) -> Tuple[List[str], List[str]]:
    LA: List[str] = []
    RA: List[str] = []
   
    content = file.read()
    location_matching = re.finditer(r"\d+", content ,re.MULTILINE)
    for index, match in enumerate(location_matching):
        if index % 2 == 0:
            LA.append(match.group())
        else:
            RA.append(match.group())

    return LA, RA

def calculate_distance(LA: List[str], RA: List[str]) -> List[int]:
    LA.sort()
    RA.sort()

    distance: List[int] = []
    complete_distance: int = 0

    for i in range(len(LA)):
        distance.append(abs(int(LA[i]) - int(RA[i])))
        complete_distance += distance[i]
    
    return complete_distance


def calculate_weighted_sum(LA: List[str], RA: List[str]) -> int:
    count_RA = {}
    for num in RA:
        if num in count_RA:
            count_RA[num] += 1
        else:
            count_RA[num] = 1
    
    weighted_sum = 0
    
    for num in LA:
        if num in count_RA:
            weighted_sum += int(num) * count_RA[num]

    return weighted_sum
    

def main():
    input_data: TextIO = open("input.txt", "r", encoding="utf-8")
    LA, RA = parse_data(input_data)
    
    complete_distance = calculate_distance(LA, RA)
    print("The Complete distance: ", complete_distance)

    weighted_sum = calculate_weighted_sum(LA, RA)

    print("Weighted Sum: ", weighted_sum)


if __name__ == "__main__":
    main()