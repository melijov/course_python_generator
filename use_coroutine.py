from coroutine_decorator import coroutine_decorator

#regular function that opens the file and target is the coroutine that processes each line
#this separation allows to add as many pieces to processing as needed
def sender(filename, target):
  for line in open(filename):
    target.send(line)
  target.close()
  
@coroutine_decorator
def match_counter(string):
  count = 0
  try:
    while True:
      line = yield
      if string in line:
        count += 1
  except GeneratorExit:
    print('There are {} instances of {}'.format(count, string))
    
@coroutine_decorator
def longer_than(n):
  count = 0
  try:
    while True:
      line = yield
      if len(line)>n:
        print(line)
        count += 1
  except GeneratorExit:
    print('There are {} instances longer than {}'.format(count, n))
    
def unit_test():
  mc = match_counter('Da')
  sender('names.txt', mc)
  
  lt = longer_than(15)
  sender('names.txt', lt)
    
if __name__=='__main__': unit_test()