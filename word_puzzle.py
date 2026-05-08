play_again="yes"
while play_again.lower() == "yes":
  word = input("write the book of mormon character: ")
  attempt = 0
  total_attempts = 0 
  print("\n---!new game¡---")
  while attempt != word:
    attempt = input ("guess the book of mormon character :")
    total_attempts += 1 
    if attempt == word:
      print("correct")
    elif attempt != word: 
      print ("your guess was not correct")
  else:
    print (f"congratulations you did it in {total_attempts} attempts! ") 
  play_again = input ("do you want to play again? (yes/no): ")
  print ("thanks for playing!")