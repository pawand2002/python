import random

# Pick a random integer between 1 and 50 (both inclusive)
random_number = random.randint(1, 50)
print(f"The random number is: {random_number}")

max_attempts=5

for attempt in range (1,max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}: Guess number between 1 and 50: "))  # Converts string input to an integer
    if random_number > guess:
        print(f"Too low! Please try again")
    elif random_number < guess:
        print(f"Too High! Please try again")
    else:
        print(f"You guessed right in {attempt} attempt(s)!")
        break
else:
    print(f"❌ You've used all attempts. Correct number was : {random_number}")