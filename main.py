# Author: Yan Lu yfl5541@psu.edu
# Collaborator: Spoorthi Dhulappanavar sxd5682@psu.edu
# Collaborator: Nicole Giron nqg5259@psu.edu
# Collaborator: Xiaolong Lin xxl5453@psu.edu
# Section: 4
# Breakout: 11

def digit_sum(n):
  if n>=10 :
    return int(n%10 + digit_sum(n//10))
  else:
    return n

if __name__ =="__main__":
  a = int(input("Enter an int: "))
  print(f"sum of digits of {a} is {digit_sum(a)}.")    