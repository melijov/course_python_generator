# a generator solution
# This generator function will return a generator object. And the generator object will yield the values


def even_integers_generator(n):
  for i in range(n):
    if i %2 == 0:
      yield i
      
      
def unit_test():
  integers = even_integers_generator(10) # returns object
  print(f'Calling "even_integers_generator(10)" returns: {integers} -- which is the generator object') 
  
  result = list(even_integers_generator(10)) # yields all the results from the generator object
  print(f'Calling "list(even_integers_generator(10))" returns: {list(integers)} -- which are all the values yielded by the generator object')
  
  #using a loop to call next() implicintly
  integers = even_integers_generator(10) # returns object
  for n in integers:
    print(n)
  
  
if __name__ =='__main__': unit_test()