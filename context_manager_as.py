from time import time
from contextlib import contextmanager

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"

@contextmanager
def new_log_file(name):
  try:
    logname = name
    f = open(logname, 'w')
    f.write(HEADER)
    yield f
  finally:
    f.write(FOOTER)
    print("logfile created")
    f.close()
    

def unit_test():
  fn = 'logfile'
  with new_log_file(fn) as file:
    file.write('this is the body')
    
if __name__=='__main__': unit_test()