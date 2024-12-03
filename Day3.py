#!/usr/bin/python3

import re

class Day03:
  def __init__(self) -> None:
    '''
    Constructor
    '''
    self.input = ''
    self.pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

  def read_input(self, file_path) -> None:
    '''
    Parse the input file.
    '''
    try: 
      with open(file_path, "r") as file:
        for line in file:
          try:
            self.input = self.input + line
          except ValueError:
            print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
      print(f"File not found at {file_path}")


  def mul_regex(self, line: str):
    '''
    Parses out all valid mul(x,y) commands into a list.
    '''
    return re.findall(self.pattern, line)
    
  def perf_mul(self, allMuls: list[str]) -> int:
    '''
    Perform all the multiplications.
    '''
    result = 0
    for aMatch in allMuls:
      first = int(aMatch[0])
      second = int(aMatch[1])
      result = result + (first * second)
    return result
  
  def find_cmds(self, line: str) -> int:
    newPat = r'(' + self.pattern + r')|(do\(\))|(don\'t\(\))'
    mult: bool = True
    result = 0
    for match in re.finditer(newPat, line):
      if match.lastindex == 1:
        # Matched mul()
        if mult:
          result = result + (int(match[2]) * int(match[3]))

      elif match.lastindex == 4:
        # Matched do()
        mult = True

      elif match.lastindex == 5:
        # Matched don't()
        mult = False
    return result

  def part_one(self) -> int:
    '''
    Part 1 of the challenge.
    '''
    allMuls = self.mul_regex(self.input)
    multiple = self.perf_mul(allMuls)
    return multiple

  def part_two(self) -> int:
    '''
    Part 2 of the challenge.
    '''
    return self.find_cmds(self.input)
  
def main() -> None:
  solver = Day03()
  file_path = "inputs/day3.txt"
  solver.read_input(file_path)

  print(f'Part 1: {solver.part_one()}')
  print(f'Part 2: {solver.part_two()}')


if __name__ == '__main__':
  main()