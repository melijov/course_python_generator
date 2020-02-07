def reverse_capital_too_long(names_list):
  #too long: nested expressions
  reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))
  return reverse_uppercase
  
def reverse_capital(names_list):
  #breaking it up
  uppercase = (name.upper() for name in names_list)
  reverse_uppercase = (name[::-1] for name in uppercase)
  return reverse_uppercase


def unit_test():
  names_list = ['Adam', 'Anne', 'Barry', 'Brianne', 'Charlie', 'Cassandra', 'David', 'Dana']

  print(f'Calling "list(reverse_capital_too_long(names_list))" returns: {list(reverse_capital_too_long(names_list))}')
  print(f'Calling "list(reverse_capital(names_list))" returns: {list(reverse_capital(names_list))}')

if __name__ =='__main__': unit_test()