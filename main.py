import random
def generate_random_number():
    return random.randint(1, 100)
    
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess(1-100):"))
            if 1 <= guess <= 100:
                return guess
            else:
                print("pleaseenter a numberbetween1 and 100.")
        except ValueError:
            print("invalid input!Pleaseenter a number.")
            
def play_game():
    print("Welcome to the number guessing game!")
    random_number = generate_random_number()
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        if guess<random_number:
            print("too low!Try again.")
        elif guess>random_number:
            print("too high try again.")
        else:
            print(f"congratulations! you guessed the number in {attempts}attempts.")
            break
        
play_game()
    

                
