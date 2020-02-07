def fibonacci_gen():
  trailing, lead = 0,1
  while True:
    yield lead
    trailing, lead = lead, trailing+lead

def unit_test():
  f = fibonacci_gen()
  for _ in range(20):
    print(next(f),end = ' ')

if __name__ == '__main__': unit_test()