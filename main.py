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
        else:print(f"congratulations! you guessed the number in {attempts}attempts.")
        break
    