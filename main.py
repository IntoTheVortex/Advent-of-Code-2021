def main():
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
      print("Line:",line, "new_number =", new_number, "last =", last)
      if new_number > last:
        count+=1
      last = new_number

  count -=1
  print("Count = ", count)












if __name__ == '__main__':
  main()