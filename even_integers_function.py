
# function solution
# first all results are stored in a list then the list is returned: Consumes more memory.
def even_integers_function(n):
  result = []
  for i in range(n):
    if i % 2 == 0:
      result.append(i)
  return result
  
  
  
def unit_test():
  result = even_integers_function(10) # returns list of results
  print(result) 
  
  
  
if __name__ =='__main__': unit_test()