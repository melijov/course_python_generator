def coroutine_example():
  while True:
    x = yield
    #do something with x
    print(x)
    
def unit_test():
  c = coroutine_example()
  #priming a coroutine using next()
  next(c)
  c.send(10)
    
if __name__=='__main__': unit_test()