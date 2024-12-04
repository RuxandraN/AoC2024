from typing import Final

SAFE_LEVELS_DIFFS: Final = frozenset({1, 2, 3})

def get_input():
    with open("input.txt") as file:
        return([int(num) for num in line.split()] for line in file.read().splitlines())


def part_1():
    safe_reports = 0
    reports = get_input()
    
    for report in reports:
        if is_safe(report) == -1:
            safe_reports += 1
            
    return f"total: {safe_reports}"

def is_safe(report):
    """ Returns -1 if safe or the index of the level where report becomes unsafe """       
    order = None

    for index in range(len(report) - 1):
        diff = report[index] - report[index + 1]
        
        if abs(diff) not in SAFE_LEVELS_DIFFS:
            return index
        
        new_order = 'asc' if diff < 0 else 'dsc'
        
        if order is None:
            order = new_order
        elif order != new_order:
            return index
        
    return -1

    
def part_2():
    """Report is safe or becomes safe if one level is removed.
    
    If the unsafe level is the last one then it's safe.
    
    If the unsafe level is the second one, checks if report is safe without the first level.
    
    Otherwise checks if report is safe without current or next unsafe level.
    """

    safe_reports = 0
    reports = get_input()
    
    for report in reports:
        unsafe_index = is_safe(report)
                   

        if (
            unsafe_index in [-1, len(report) - 2]
            or unsafe_index == 1 and is_safe(report[unsafe_index:]) == -1
            or is_safe(report[:unsafe_index] + report[unsafe_index+1:]) == -1
            or is_safe(report[:unsafe_index+1] + report[unsafe_index+2:]) == -1
        ):
            safe_reports += 1
            
    return f"total: {safe_reports}"

print(part_1())
print(part_2())
