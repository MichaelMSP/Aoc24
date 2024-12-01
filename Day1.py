#!/usr/bin/python3

'''
Parse File
'''
def read_file(file_path):
  # Initialize lists
  first_numbers = []
  second_numbers = []

  try: 
    # Read the file and populate the lists
    with open(file_path, "r") as file:
      for line in file:
        try:
          # Split the line into two numbers
          num1, num2 = map(int, line.split())
          first_numbers.append(num1)
          second_numbers.append(num2)
        except ValueError:
          print(f"Skipping invalid line: {line.strip()}")
  except FileNotFoundError:
     print(f"File not found at {file_path}")

  return first_numbers, second_numbers

'''
Part 1
'''
def distance_list(first, second):
  distances = []
  for a, b in zip(first, second):
    distances.append(abs(a - b))

  return distances

'''
Part 2
'''
def similarity_list(first, second):
  sims = []
  for a in first:
    sims.append(a * second.count(a))
  return sims

'''
Main function
'''
def main():
  print("Day 1")
  file_path = "inputs/day1.txt"
  l1, l2 = read_file(file_path)
  l1.sort()
  l2.sort()
  dist = distance_list(l1, l2)

  print ("Total dist: ", sum(dist))

  sims = similarity_list(l1, l2)
  print ("Similarity: ", sum(sims))

if __name__ == "__main__":
   main()