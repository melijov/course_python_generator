#coroutine
def counter(string):
  count = 0
  try:
    while True:
      item = yield
      if isinstance(item, str):
        if item in string:
          count +=1
          print(item)
        else:
          print('Not a match')
      else:
        print('Not a string')
  except GeneratorExit:
    print(count)

def unit_test():
  c = counter('California')
  next(c) # prime the coroutine
  c.send('Cali') 
  c.send('nia')
  c.send('Hawaii')
  c.send(123)
  c.close() # this will generate a Generator Exit exception
      
if __name__ =='__main__': unit_test()