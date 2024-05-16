# Author: Raphael Carneiro
# Week 3 Project: Adventure Game
import os
# Introduction
print("Please select one of the three scenarios below to begin your adventure!")
print("Type your answer ACCORDING ALL CAPS WORD.")
print("--------------------------------------")
print("\nScenario 1: 🪨 The Mysterious CAVE")
print("Scenario 2: 🏚️ The Lost CITY of Pokémon")
print("Scenario 3: 🐉 The LEGENDARY Pokémon")
scenario = input("\nType what scenario have you choose: ")

# Cleaning the screen
os.system('cls')

# First Path 1/3
if scenario.lower() == "cave":
    print("🪨 The Mysterious Cave")
    print("\nYou are hiking through a dense forest when you come across a small cave hidden among the trees.")
    print("\n--------------------------------------")
    path_1 = input("\nWhat will you do? \n[ ENTER the cave | LEAVE the cave | COVER the cave entrance ]-> ")
    os.system('cls')
    # First Path 2/3
    if path_1.lower() == "enter":
        print("🪨 The Mysterious Cave")
        print("\nYou decide to enter the cave to see what you can find.")
        print("In the center of the cave, there is a glowing egg.")
        print("\n--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ TOUCH the egg | LEAVE the egg alone | ATTACK the egg ]-> ")
        os.system('cls')
        # First Path 3/3
        if path_2.lower() == "touch":
            print("🪨 The Mysterious Cave")
            print("\nAs you reach out to touch the egg, it hatches into a rare and powerful Pokémon.")
            print("The Pokémon immediately forms a strong bond with you.")
            print("--- The End ---\n")
        elif path_2.lower() == "leave":
            print("🪨 The Mysterious CAVE")
            print("\nYou decide to leave the egg alone and continue on your way.")
            print("As you walk away, you feel a sense of regret.")
            print("You know that you have missed out on a once-in-a-lifetime opportunity.")
            print("--- The End ---\n")
        elif path_2.lower() == "attack":
            print("🪨 The Mysterious CAVE")
            print("\nAt the time when you lifted a large rock and were about to destroy that egg,")
            print("is emitted a strong light and a fierce dragon came out of it and devoured it.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    elif path_1.lower() == "leave":
        print("🪨 The Mysterious Cave")
        print("\nYou decide to leave the cave and continue on your way.")
        print("As you walk away, you hear a voice whisper in your ear, 'You have chosen wisely.'")
        print("\n--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ Turn BACK | Continue CLIMBING | EXPLORE the forest ]->")
        os.system('cls')
        # First Path 3/3
        if path_2.lower() == "back":
            print("🪨 The Mysterious Cave")
            print("\nYou decide to turn back and enter into the cave again.")
            print("As you walk deeper into the cave, you come across a hidden chamber.")
            print("You decide to explore the chamber further.")
            print("As you do, you discover a hidden treasure chest.")
            print("Inside the chest, you find a powerful artifact.")
            print("--- The End ---\n")
        if path_2.lower() == "climbing":
            print("🪨 The Mysterious Cave")
            print("\nDetermined to reach the summit, you emerge onto a rocky ")
            print("plateau overlooking the entire forest below.")
            print("A Celebi, the mythical time-traveling Pokémon, appears before you,")
            print("offering a glimpse into the past or the future before vanishing.")
            print("--- The End ---\n")
        if path_2.lower() == "explore":
            print("🪨 The Mysterious Cave")
            print("\nYou stumble upon a local tribe in the forest, surrounded by fierce warriors.")
            print("As you reach for your Poké Balls, a massive Ursaring charges out, causing the tribe to panic.")
            print("Taking advantage of the chaos, you make a hasty retreat, ")
            print("grateful for the wild Pokémon's intervention.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    elif path_1.lower() == "cover":
        print("🪨 The Mysterious Cave")
        print("\nAs you cover the cave entrance with a large boulder,")
        print(" you hear a faint, eerie whisper emanating from within.")
        print("--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ Ignore it and CAMP there | Ignore it and go HOME | REOPEN the entrance ]->")
        os.system('cls')
        # First Path 3/3
        if path_2.lower() == "camp":
            print("🪨 The Mysterious Cave")
            print("\nYou cover the cave entrance with a boulder, ")
            print("ignoring a faint whisper from within.")
            print("Later, a spectral figure emerges from the cave, ")
            print("a vengeful spirit unleashed upon the world.")
            print("--- The End ---\n")
        if path_2.lower() == "home":
            print("🪨 The Mysterious Cave")
            print("\nYou cover the cave entrance, the ground rumbles, ")
            print("revealing a hidden chamber below.")
            print("You discover a forgotten shrine but are confronted by a guardian spirit.")
            print("--- The End ---\n")
        if path_2.lower() == "reopen":
            print("🪨 The Mysterious Cave")
            print("\nAs you open the cave entrance again, ")
            print("you feel a sense of accomplishment and security,")
            print("believing that you have successfully avoided any lurking dangers.")
            print("Continuing the walk, you follow a winding trail deeper into the forest,")
            print("marveling at the tranquility of nature.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    else:
        print("[ Please, reboot this program and type a possible answer! ]")
# Second Path 1/3
elif scenario.lower() == "city":
    print("🏚️ The Lost City of Pokémon")
    print("\nYou are traveling through a remote desert when you come across a group of nomads.")
    print("\n--------------------------------------")
    print("\nWhat will you do?")
    path_1 = input("[ BEFRIEND the nomads | IGNORE the nomads | HELP the nomads find their lost Pokémon ]-> ")
    os.system('cls')
    # Second Path 2/3
    if path_1.lower() == "befriend":
        print("🏚️ The Lost City of Pokémon")
        print("\nYou decide to befriend the nomads and learn about their culture.")
        print("They tell you about a lost city of Pokémon that is said to be hidden somewhere in the desert.")
        print("\n--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ LEARN more about their culture | LEAVE the nomads | ATTACK the nomads ]-> ")
        os.system('cls')
        # Second Path 3/3
        if path_2.lower() == "learn":
            print("🏚️ The Lost City of Pokémon")
            print("\nYou decide to learn more about the nomads' culture.")
            print("They teach you about their traditions, their beliefs, and their way of life.")
            print("--- The End ---\n")
        elif path_2.lower() == "leave":
            print("🏚️ The Lost City of Pokémon")
            print("\nYou decide to leave the nomads and continue on your way.")
            print("As you walk away, you feel a sense of gratitude for the time you spent with them.")
            print("You know that you have learned valuable lessons from them.")
            print("--- The End ---\n")
        elif path_2.lower() == "attack":
            print("🏚️ The Lost City of Pokémon")
            print("\nYou attacked the nomads for their provisions, but they caught you by surprise and knocked you out.")
            print("As you lay there, surrounded by them, you feel your life slipping away.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    elif path_1.lower() == "ignore":
        print("🏚️ The Lost City of Pokémon")
        print("\nYou decide to ignore the nomads and continue on your way.")
        print("As you walk away, you hear a voice whisper in your ear, 'You have missed out on a great adventure.'")
        print("\n--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ SEARCH for the lost city | GIVE UP on the search | EXPLORE the desert and its secrets ]-> ")
        os.system('cls')
        # Second Path 3/3
        if path_2 == "search":
            print("🏚️ The Lost City of Pokémon")
            print("\nAfter days of searching, you finally find it.")
            print("The city is full of ancient ruins and forgotten treasures.")
            print("--- The End ---\n")
        elif path_2 == "give up":
            print("🏚️ The Lost City of Pokémon")
            print("\nAs you walk away, you feel a sense of disappointment.")
            print("You know that you have given up on a dream that could have come true.")
            print("--- The End ---\n")
        elif path_2 == "explore":
            print("🏚️ The Lost City of Pokémon")
            print("\nAs you explore, you discover a hidden library")
            print("The library contains ancient texts that reveal")
            print("the history of the city and the power of the Pokémon that once lived there")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    elif path_1.lower() == "help":
        print("🏚️ The Lost City of Pokémon")
        print("\nYou notice that the nomads are looking for something.")
        print("They tell you that they have lost one of their Pokémon.")
        print("You decide to help them find it.")
        print("As you search the desert, you come across a group of wild Pokémon. ")
        print("They help you to find the lost Pokémon, and the nomads are grateful for your help.")
        print("\n--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ VISIT the nomad's camp | Become a PILGRIM | Go to the nomads' CEREMONY in the desert ]-> ")
        os.system('cls')
        # Second Path 3/3
        if path_2.lower() == "visit":
            print("🏚️ The Lost City of Pokémon")
            print("\nThe nomads' camp is deserted, with signs of a struggle.")
            print("It's clear that a rival group has attacked them.")
            print("You are determined to rescue them and their Pokémon.")
            print("--- The End ---\n")
        if path_2.lower() == "pilgrim":
            print("🏚️ The Lost City of Pokémon")
            print("\nThe nomads invite you on a pilgrimage through the desert,")
            print("overcoming trials and forming bonds.")
            print("You reach a sacred oasis, experiencing its mystical powers and rejuvenating waters.")
            print("--- The End ---\n")
        if path_2.lower() == "ceremony":
            print("🏚️ The Lost City of Pokémon")
            print("\nAfter finding the lost Pokémon, the nomads invite you to a desert ceremony.")
            print("You prove your worth by capturing a powerful wild Pokémon, earning the nomads' respect.")
            print("This solidifies your place as a trusted ally in their community.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    else:
        print("[ Please, reboot this program and type a possible answer! ]")
# Third Path 1/3
elif scenario.lower() == "legendary":
    print("🐉 The Legendary Pokémon")
    print("\nYou are exploring a dense forest when you come across a clearing.")
    print("--------------------------------------")
    print("\nWhat will you do?")
    path_1 = input("[ ENTER the clearing | LEAVE the clearing | CLIMBING the mountain ]-> ")
    os.system('cls')
    # Third Path 2/3
    if path_1.lower() == "enter":
        print("🐉 The Legendary Pokémon")
        print("\nAs you walk into the clearing,")
        print("you see a legendary Pokémon standing in the center.")
        print("--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ APPROACH the legendary Pokémon | RUN AWAY from the legendary Pokémon | OFFER the legendary Pokémon a gift you've been carrying ]-> ")
        os.system('cls')
        # Third Path 3/3
        if path_2.lower() == "approach":
            print("🐉 The Legendary Pokémon")
            print("\nThe Pokémon is friendly and allows you to touch it.")
            print("You feel a surge of power coursing through your body.")
            print("--- The End ---\n")
        elif path_2.lower() == "run away":
            print("🐉 The Legendary Pokémon")
            print("\nThe Pokémon is disappointed but does not pursue you.")
            print("--- The End ---\n")
        elif path_2.lower() == "offer":
            print("🐉 The Legendary Pokémon")
            print("\nYou reach into your bag and pull out a rare berry or poffin you've been saving. ")
            print("You offer it to the legendary Pokémon as a gesture of respect.")
            print("The Pokémon is surprised by your gesture and accepts the gift.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    elif path_1.lower() == "leave":
        print("🐉 The Legendary Pokémon")
        print("\nAs you walk away, you hear a voice say,")
        print("'You have chosen wisely.'")
        print("\n--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ SEARCH | HESITATE | CAMP ]-> ")
        os.system('cls')
        # Third Path 3/3
        if path_2 == "search":
            print("🐉 The Legendary Pokémon")
            print("\nYou decide to explore the clearing further.")
            print("As you do, you discover a hidden spring.")
            print("The water from the spring is said to have healing powers.")
            print("--- The End ---\n")
        elif path_2 == "hesitate":
            print("🐉 The Legendary Pokémon")
            print("\nYou hesitate to enter the clearing and instead choose to observe it from a distance.")
            print("You notice strange markings on the ground and decide to carefully")
            print("document them in your Pokédex for future reference.")
            print("--- The End ---\n")
        elif path_2 == "camp":
            print("🐉 The Legendary Pokémon")
            print("\nYou continue on your path and later at your campsite, ")
            print("you see the legendary Pokémon disappearing into the forest,")
            print("possibly keeping an eye on you.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    elif path_1.lower() == "climbing":
        print("🐉 The Legendary Pokémon")
        print("\nAs you are climbing the mountain, you notice that a storm is approaching.")
        print("You decide to seek shelter in a nearby cave. As you enter the cave,")
        print("you discover a hidden treasure chest.")
        print("Inside the chest, you find a powerful artifact.")
        print("--------------------------------------")
        path_2 = input("\nWhat will you do? \n[ TOUCH the orb | LEAVE the orb alone | Investigate the SOURCE of the orb's glow ]-> ")
        os.system('cls')
        # Third Path 3/3
        if path_2.lower() == "touch":
            print("🐉 The Legendary Pokémon")
            print("\nAs you reach out to touch the orb,")
            print("a surge of energy courses through your body.")
            print("You feel suddenly stronger and more powerful.")
            print("--- The End ---\n")
        if path_2.lower() == "leave":
            print("🐉 The Legendary Pokémon")
            print("\nAs you walk away, you hear a voice whisper in your ear,")
            print("'You have made the right choice.'")
            print("--- The End ---\n")
        if path_2.lower() == "source":
            print("🐉 The Legendary Pokémon")
            print("\nAs you follow the light, you come across a hidden portal.")
            print("The portal leads to another world, a world of magic and wonder.")
            print("--- The End ---\n")
        else:
            print("[ Please, reboot this program and type a possible answer! ]")
    else:
        print("[ Please, reboot this program and type a possible answer! ]")
# Error Path
else:
    print("[ Please, reboot this program and type a possible answer! ]")
