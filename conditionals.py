userReply = input("Do you  need to ship a package?(Enter yes or no)")
if userReply =="yes":
    print("we can help you ship that pacakage!")
    
else:
    print("please come back when you need  to ship a pacakage.thank you.")
    
    userReply= input("would you like to buy stamps, buy an envelop, or make a copy?(enter stamps, envelop, or copy)")
    if userReply=="stamps":
        print("we have many stamp designs to choose from.")
    elif userReply =="envelop":
         print("we have many envelop sizes to choose from.")
    elif userReply =="copy":
        copies = input("how many copies would you like?(enter a number)")
        print("here are{} copies.".format (copies))
    else:
        print("thank you , please come again")
        
        
    