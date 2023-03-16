descriptions = {"kitchen": "You checked every one of your dirty shelves – nothing there!",
                "bathroom": "What a mess! But no phone anywhere. Continue your search.",
                "hallway": "Choose a room!",
                "living room": "No, the phone is not here...But what about this: You found the key to the study!",
                "study": "Nope, again no phone. Damn, all these dusted books...you should read more!",
                "bedroom": "Maybe it's burried under the blanket..no, nothing. Hm, you cannot find it. Maybe you should put your glasses on."}
movement = {'kitchen': 'hallway', 'bathroom': 'hallway', 
            'hallway': ['kitchen', 'bathroom', 'living room', 'study', 'bedroom'],
            'living room': 'hallway', 'study': 'hallway', 'bedroom': 'hallway'}

room='kitchen'
key=False
glasses=False


print("""
Find your Phone!
===================

Your quest starts.
""")

player_name=input("Please enter your name: ")
player_name=player_name.upper()

print(f"""\n{player_name}, it happened again: You got coffee in the kitchen 
and wanted to check your Instagram, but where did you put your phone?\n""")

start=input("Hit ENTER to continue:\n")

print("There are 6 rooms in your flat: kitchen, bathroom, hallway, living room, study, and bedroom.\n")
next=input("Hit ENTER to continue:\n")

while room in descriptions and room!= 'bedroom':
    print(f"You are in the {room}.")
    print(descriptions[room])
    target = input("Where would you like to go? ")
    target=target.lower()
    while target not in descriptions:
        print("That room does not exist.")
        target = input("Try again: ")
    while target==room:
        print(f"You already are in the {room}")
        target=input("Where to now? ")
    while target not in movement[room]:
        print(f"You cannot access {target} from where you are! You are in the {room}.")
        target = input("Try again: ")
    room=target
    
    if room=='living room' and not key:
        key = True
    elif room=='study' and key:
        print("You unlocked your study and found your glasses! Maybe you can see clearer now.")
        glasses = True
    elif room=='bedroom' and glasses==False:
        print(f"You are in the {room}.")
        print("Hm, you cannot find it. Maybe you should put your glasses on. Look somewhere else!")
        target=input("Where do you want to go next? ")
        room=target
    elif room=='study' and key==False:
        print("The study is locked. Where did you put the key?")
        room='hallway'
    elif room =='bedroom' and glasses==True:
        print("""*Puts on glasses* ... 
        
        Oh my god, you finally found it. Your black phone was hiding on your black shelf.\n
        Your quest has been successful!
        ===============================\n""")
 


    


    