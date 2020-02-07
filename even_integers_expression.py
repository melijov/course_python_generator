#even integers generator expression
def even_integers_expression(n):
  result = (i for i in range(n) if i%2==0)
  return result # returns generator




def unit_test():
  print(f'Calling "even_integers_expression(10)" returns: {even_integers_expression(10)}')
  print(f'Calling "list(even_integers_expression(10))" returns: {list(even_integers_expression(10))}')

if __name__ =='__main__': unit_test()