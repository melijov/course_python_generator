def convert_to_upper_case(names_list):
  uppercase_names  = (name.upper() for name in names_list)
  return uppercase_names # returns generator object


def unit_test():
  names_list = ['Adam', 'Anne', 'Barry', 'Brianne', 'Charlie', 'Cassandra', 'David', 'Dana']

  print(f'Calling "convert_to_upper_case(names_list)" returns: {convert_to_upper_case(names_list)}')
  print(f'Calling "list(convert_to_upper_case(names_list))" returns: {list(convert_to_upper_case(names_list))}')

if __name__ =='__main__': unit_test()