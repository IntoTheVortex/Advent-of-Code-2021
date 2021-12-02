def aoc1():
  file = open('input.txt','r')
  input = True
  last = 0
  count = 0

  while(input):
    line = file.readline()
    if not line:
      input = False
    else:
      new_number = int(line)
      if new_number > last:
        count+=1
      last = new_number

  count -=1
  print("Count = ", count)


def aoc2():
  file = open('input.txt','r')
  input = True
  last_total = 0
  count = 0

  last_num1 = int(file.readline())
  last_num2 = int(file.readline())

  while(input):
    line = file.readline()
    if not line:
      input = False
    else:
      new_number = int(line)

      new_total = new_number + last_num1 + last_num2
      if new_total > last_total:
        count+=1
      
      last_total = new_total
      last_num1 = last_num2
      last_num2 = new_number

  #remove the first increase where last_total is zero
  count -=1
  print("Count = ", count)




if __name__ == '__main__':
  #aoc1()
  aoc2()