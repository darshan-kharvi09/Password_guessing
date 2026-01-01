import random
easy_words = ["state", "robot", "cooler", "colour","dress"]
mediam_words = ["private", "laptop", "village", "rocket"]
hard_words = ["karnataka", "commodity", "services", "industry"]
print("Welcome to the word guessing game")
print("Choose a difficulty level: easy, mediam, hard")

level = input("Enter difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "mediam":
 secret = random.choice(easy_words)
elif level == "hard":
 secret = random.choice(easy_words)
else:
  print("Invalid choice. Defaulting to easy level")
  secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret word")

while True:
  guess = input("Enter your guess: ").lower()
  attempts += 1
  
  if guess == secret:
    print(f'Congratulations! You guessed it in (attempts) attempts.')
    break
  
  hint = ""
  for i in range(len(secret)):
    if i < len(guess) and guess[i] == secret[i]:
      hint += guess[i]
    else:
      hint += "_"

    print("Hint:"+ hint)