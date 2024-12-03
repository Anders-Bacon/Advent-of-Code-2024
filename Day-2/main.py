from typing import TextIO, List
import re
"""
def parse_data(file: TextIO) -> List[int]:
    array1: List[List[int]] = []
    content = file.read().strip()
    for line in content.split("\n"):
        array = [int(num) for num in line.split()]
        array1.append(array)
    return array1

def safe_array(array: List[int]) -> bool:
    is_safe: bool = True
    if len(array) < 2:
        return is_safe
    
    increasing = all(array[i] < array[i+1] for i in range(len(array) - 1))
    decreasing = all(array[i] > array[i+1] for i in range(len(array)-1))

    if not (increasing or decreasing):
        is_safe = False
    
    for i in range(len(array)-1):
        diff = abs(array[i+1] - array[i])
        if diff < 1 or diff > 3:
            is_safe = False
        
    return is_safe


def can_make_safe(array1: list[int]) -> bool:
    

    for i in range(len(array1)):
        modfied_array = array1[:i] + array1[i+1:]

        if safe_array(modfied_array):
            return True
    return False

def get_safe_array_count(array1: list[int]) -> bool:
    return can_make_safe(array1)
    
    
def main():
    
    input_data: TextIO = open("input.txt", "r", encoding="utf-8")
    data = parse_data(input_data)

    checked_arrays = map(safe_array, data)

    safe_array_count = 0
    for array in data:
        if safe_array(array):
            safe_array_count += 1
    
    print(f"Number of safe arrays_: {safe_array_count}")
"""

def main():
    input_data: TextIO = open("input.txt", "r", encoding="utf-8")
    reports = parse_data(input_data)

    checked_reports = map(get_reportArray_safety, reports)
    safe_reports = [status for status in checked_reports if status == True] 
    print(f"Number of safe reports: {len(safe_reports)}")

    lenient_checked_reports = map(can_be_safe, reports)
    lenient_safe_reports = [status for status in lenient_checked_reports if status == True]
    print(f"Number of lenient safe reports: {len(lenient_safe_reports)}")

def parse_data(data: TextIO) -> List[list[int]]:
    reports: List[list[int]] = []
    for report in data.readlines():
        level_matches = re.finditer(r"\d+", report)
        levels: list[int] = []
        for match in level_matches:
            levels.append(int(match.group()))
        reports.append(levels)

    return reports

def get_reportArray_safety(report: list[int]) -> bool:
    is_safe: bool = True
    decending: bool | None = None
    for index, level in enumerate(report):
        if index + 1 < len(report):
            distance = level - report[index + 1]
            if abs(distance) > 3 or abs(distance) < 1:
                is_safe = False
            ascending: bool = distance < 0
            if decending is not None and decending != ascending:
                is_safe = False
            decending = ascending

    return is_safe

def can_be_safe(report: list[int]) -> bool:


    for i in range(len(report)-1):
        new_report = report[:i] + report[i+1:]
        if get_reportArray_safety(new_report):
            return True
    return False


def can_be_safe(report: list[int]) -> bool:
    for i in range (len(report)):
        new_report = report[:i] + report[i+1:]
        if get_reportArray_safety(new_report):
            return True
    return False

if __name__ == "__main__":
    main()