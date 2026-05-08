print ("Hello adventurer, welcome to this new adventure. Please choose your weapon: knife or flashlight.")
weapon= input (" please chose your weapon: KNIFE , FLASHLIGHT:")
if weapon== "KNIFE":
    print("very nice, lets go to the forest")
chose= input ("you see a wild wolf!, do you FIGTH or RUN:")
if chose== "FIGTH":
    print ("you defeated the wolf whith your knife! you win!")
chose_2= input ("Which do you prefer? To go BACK HOME and finish the game, or to live in the forest and become a LEGEND?")
if chose_2== "BACK HOME":
    print ("END") 
    exit ()
elif chose_2== "LEGEND":
    print ("END") 
    exit ()
elif chose== "RUN":
    print ("You ran, but now you're badly hurt.")
chose_3= input ("You will die, would you rather die in your house like a NERD or in your house like a HERO?")
if chose_3== "NERD":
    print ("NERD,END") 
    exit ()
elif chose_3== "HERO":
    print ("END") 
    exit ()
elif weapon== "FLASHLIGHT":
    print ("very nice, lets go to the cave")
chose_4= input ("There's a tribe of cannibals in the cave. Do you show them the flashlight and give it to them as a MIRACLE, or do you let them EAT you so they have something to eat that day?")
if chose_4== "MIRACLE":
    print ("you're safe")
chose_5= ("If they consider you a god, do you STAY with them and let them worship you, or do you LEAVE before they kill you?")
if chose_5== "STAY":
    print ("end") 
    exit ()
elif chose_5== "LEAVE":
    print ("end") 
    exit ()
elif chose_4== "EAT":
    print ("Congratulations, today you will eat human soup")
chose_6= ("ESCAPE and put a cannibal in the soup, or DIE?")
if chose_6== "ESCAPE":
    print("you win, end") 
    exit ()
elif chose_6== "DIE":
    print ("loser , end") 
    exit ()