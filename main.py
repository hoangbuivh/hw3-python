#Author Hoang Bui hhb5051@psu.edu
def digit_sum(n):
  if len(str(n))==1: 
    return n
  else: 
    return n%10+ digit_sum(n//10)

def run(): 
  entrance = int(input("Enter an int: "))
  print(f"sum of digits of {entrance} is {digit_sum(entrance)}.")

if __name__ == "__main__": 
  run()