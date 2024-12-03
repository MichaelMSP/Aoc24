#!/usr/bin/python3

class Day02:
  def __init__(self) -> None:
    '''
    Constructor
    '''
    self.all_reports = []

  def read_input(self, file_path) -> None:
    try: 
      with open(file_path, "r") as file:
        for line in file:
          try:
            report = list(map(int, line.split()))
            self.all_reports.append(report)
          except ValueError:
            print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
      print(f"File not found at {file_path}")


  def ascend_count(self, aList: list[int]) -> int:
    '''
    Returns 0 if the list is all ascending or descending. 
    Else, returns the number of values out of place, negative value
    if the list is predominantly descending.
    '''
    a_count = 0
    d_count = 0
    for a,b in zip(aList, aList[1:]):
      if a > b:
        a_count = a_count + 1
      if b > a: 
        d_count = d_count + 1
    if a_count == 0 or d_count == 0:
      return 0
    else:
      if a_count < d_count:
        return a_count
      else:
        return -d_count

  def compare_vals(self, a: int, b: int, asc: bool) -> bool:
    if abs(a - b) > 3 or abs(a - b) < 1:
      return False
    if asc and b < a:
      return False
    if not asc and a < b:
      return False
    return True


  def is_valid(self, aList: list[int]) -> bool:
    ascending: bool = aList[1] < aList[2]
    for a,b in zip(aList, aList[1:]):
      if self.compare_vals(a,b,ascending) == False:
        return False
    return True
  
  def is_valid_damped(self, aList: list[int]) -> bool:
    if self.is_valid(aList):
      return True
    # Need to account for if the second value is wrong with the ascending/descending state
    asc_count = self.ascend_count(aList)
    if abs(asc_count) > 1:
      return False
 
    # asc_count must be 1 or 0. I.e. if we're here, there is no issue with asc or dsc. Just check too big a jumps or duplicate values.
    for idx, a in enumerate(aList):
      bList = aList[:idx] + aList[idx + 1:]
      if self.is_valid(bList):
        return True
    return False

    

  def part_one(self) -> int:
    count = 0
    for report in self.all_reports:
      if self.is_valid(report):
        count = count + 1
    return count

  def part_two(self) -> int:
    count = 0
    for report in self.all_reports:
      if self.is_valid_damped(report):
        count = count + 1
    return count
  
def main() -> None:
  solver = Day02()
  file_path = "inputs/day2.txt"
  solver.read_input(file_path)

  print(f'Part 1: {solver.part_one()}')
  print(f'Part 2: {solver.part_two()}')


if __name__ == '__main__':
  main()