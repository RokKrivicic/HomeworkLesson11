import random
import json
import datetime
from operator import itemgetter  # library for sorting inside the list

player = str(input("Write your name: ").capitalize())
secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []


with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    sorted_list = sorted(score_list, key=itemgetter("attempts", "date"))
    print("Top scores: " + str(sorted_list[:3]))

    for score_dict in sorted_list[:3]:
        print("Player " + score_dict["player_name"] + " needed " + str(score_dict["attempts"]) +
              " attempts, on date: " + score_dict.get("date") + " and the secret number was "
              + str(score_dict.get("secret_number")) + ". He previously tried this numbers " +
              str(score_dict.get("wrong_guesses")) + ".")

while True:
    guess = int(input("Write down your guess: "))
    attempts += 1
    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()),
                           "player_name": player, "secret_number": secret, "wrong_guesses": wrong_guesses})
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Congratulation you won")
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        wrong_guesses.append(guess)
        print("Wrong, try a smaller number")
    else:
        wrong_guesses.append(guess)
        print("Wrong, try a bigger number")
