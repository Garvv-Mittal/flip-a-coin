import random
from art import coin_flip
from art import logo
from art import head
from art import tail
print(logo)
print("Flipping the coin ....\n")
print(coin_flip)
random_side = random.randint(0,1)
if random_side ==1 :
  print(f"You've got Heads.\n\n{head}")
else:
  print(f"You've got Tails.\n\n{tail}")