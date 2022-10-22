import random
import time

random_world = "principle", "deserve", "blast", "critical", \
               "ask", "factory", "smell", "difficulty", "control", "birthday", \
               "announcement", "ban", "show", "sweep", "joint", "deserve", "gasp", \
               "symbol", "myth", \
               "hold", "dependence", "soft", "introduction", "assume", "injury", \
               "exclusive", "eavesdrop", "ash", "chocolate", "salt", "defendant", \
               "attack", "pound", "dismissal", "guerrilla", "retire", "retire", \
               "refuse", "aware", "pan", "testify", "strength", \
               "counter", "dollar", "king", "summer", "moon", \
               "license", "discreet", "captain", "python", "code", \
               "free", "good", "cock", "fix", "dont", \
               "know", "got", "get", "look", "who", \
               "decide", "to", "up", "mom", "dad", \
               "offer", "talk", "walk", "speed", "listen", \
               "me", "my", "name", "sister", "brother", \
               "come", "came", "travel", "the", "world", \
               "life", "better", "mario", "kick", "next"

world_wins = 0

while True:
    world = random.choice(random_world)
    print("Try to write the world:" + " " + "\n" + '"' + world + '"')
    answer = input("write it in here: ")

    if answer == world:
        print("\n\n\n")
        world_wins += 1

        if world_wins % 10 == 0:
            print("good job you got", world_wins, "world right for now! keep going like this")
            time.sleep(2)
            print("\n\n\n")

    elif answer != world:
        print("\n\n\n")
        print("You are wrong, and you got", world_wins, "world right!")
        print("You spell the world", '"' + world + '"', "like this" + '"', answer + '"', "\nso your wrong!")
        exit()
    else:
        print("\n\n\n")
        print("Invalid reference! Try again!")
        continue