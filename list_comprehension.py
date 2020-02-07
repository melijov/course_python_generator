def list_comprehension(collection):
  # list comprehension: brackets
  result = [item.upper() for item in collection]
  return(result)

def generator_expression(collection):
  # generator expression: parenthesis
  result = (item.upper() for item in collection)
  return result # returns generator

def unit_test():
  collection = ['Abra', 'Cadabra', 'Pata', 'de', 'Cabra']
  print(f'Calling "list_comprehension(collection)" returns: {list_comprehension(collection)}')
  print(f'Calling "generator_expression(collection)" returns: {generator_expression(collection)}')
  print(f'Calling "list(generator_expression(collection))" returns: {list(generator_expression(collection))}')

if __name__ =='__main__': unit_test()