def convert_to_integer(numbers):
  integers = (int(n) for n in numbers)
  return integers # returns generator



def unit_test():
  #list of mixed format numbers
  numbers = [7, 22, 4.5, 99.7, '3', '5']

  print(f'Calling "convert_to_integer(numbers)" returns: {convert_to_integer(numbers)}')
  print(f'Calling "list(convert_to_integer(numbers))" returns: {list(convert_to_integer(numbers))}')

if __name__ =='__main__': unit_test()