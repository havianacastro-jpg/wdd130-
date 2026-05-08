import random
play_again = "yes"
while play_again.lower() == "yes":
  number = random.randint(1, 10)
  attempt = 0
  total_attempts = 0 
  print("\n---!new game¡---")
  while attempt != number:
    attempt = int (input ("guess the number from 1-10:"))
    total_attempts += 1 
    if attempt < number:
      print("higher")
    elif attempt > number:
      print("lower")  
    else:
      print (f"congratulations you did it in {total_attempts} attempts! ") 
  play_again = input ("do you want to play again? (yes/no): ")
  print ("thanks for playing!")