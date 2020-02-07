# using generators to find the longest name

def longest_name(fn):
  full_names = (name.strip() for name in open(fn)) # generator expression 
  lengths = ((name, len(name)) for name in full_names) # second generator expression
  longest = max(lengths, key=lambda x:x[1])
  return longest

def unit_test():
  fn = 'names.txt'
  ln = longest_name(fn)
  print(f'"{ln[0]}" is the longest name in file "{fn}" with {ln[1]} characters')
  
if __name__ == '__main__': unit_test()