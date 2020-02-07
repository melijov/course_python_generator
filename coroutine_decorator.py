def coroutine_decorator(func):
  def wrap(*args, **kwargs):
    cr = func(*args, **kwargs)
    next(cr) # the purpose of the decorator is to prime the coroutine
    return cr
  return wrap
  
@coroutine_decorator
def coroutine_example():
  while True:
    x = yield
    #do something with x
    print(x)

def unit_test():
  cre = coroutine_example()
  cre.send(10)
  cre.send("Hello, World!!!")
    
    
    
if __name__=='__main__': unit_test()