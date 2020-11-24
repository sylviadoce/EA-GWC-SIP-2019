print("You are a hedgehog. The next few minutes of your life will change you forever. Your mission, if you choose to accept it? Get the cheese.")
answer = input("You're in a forest and you see only 2 trees. Do you go to the pine tree or the oak tree?")
print(answer, "it is!")
if answer == "oak tree":
    print("Oh no, a wild turkey!")
    answer = input("What should you do? Should you run? Or should you hide?")
    print(answer, ", good thinking.")
    if answer == "run":
        print("Luckily, you're the best sprinter in hedgehog land. On the way, you stumble across your cheese! Congrats! :)")
        print("Game over.")
        #end 1
    elif answer == "hide":
        print("You try to hide, but you're too horizontally challenged. The turkey finds you. DEATH.")
        print("Game over.")
        #end 2

elif answer == "pine tree":
    print("This is a pretty tall pine tree, it seems there's something at the top.")
    answer = input("Will you climb the tree or stay low?")
    print("Ok, I'll", answer)
    if answer == "climb" or answer == "climb the tree":
        print("There's a patch of Ken Moss on the tree. You slip. DEATH.")
        print("Game over.")
            #end 3

    elif answer == "stay low":
        print("You find two holes within the bottom of the tree. There's something in both of them.")
        answer = input("Left or right hole?")
        if answer == "left" or answer == "left hole":
            print("There's a familiar smell. It's your cheese! Congrats! :)")
                #end 4

        elif answer == "right" or answer == "right hole":
            print("You stick your nose in. There's termites! DEATH.")
            print("Game over.")
                #end 5
