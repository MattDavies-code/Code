import random                                   #Importing Python Module 'random' for use in creating a random integer
                                                #ADD COMMENTS and make guessMultiple better
def hangmanFunc():
    print("Welcome to Hangman!")
    wordFile = open("hangmanWords.txt", "r")
    solved = False
    turns = 0
    revealWordList = []
    r = random.randint(1,40)
    if wordFile.readable() == True:
        randomWordList = list(str(wordFile.readlines()[r]))
        randomWordList.remove('\n')
        print(randomWordList)

    for x in range (0, len(randomWordList)):
        revealWordList.extend("-")
        
    
    while solved == False and turns<=9:
        userGuess = input(str("\nPlease enter a letter as your guess: "))
        turns = turns+1

        
        if userGuess in randomWordList:

            guessOccurences = randomWordList.count(userGuess)

            if guessOccurences == 1:
            
                position = randomWordList.index(userGuess)
                p = int(position)
                revealWordList[p] = randomWordList[p]
                print("\nA letter has been revealed!")
                print("The word is now:", ''.join(revealWordList))
                print("Number of turns remaining:",10-turns)

            else:

                guessMultiple = [i for i, x in enumerate(randomWordList) if x == userGuess]
                print(guessMultiple)

                for x in range (0, len(guessMultiple)):
                    revealWordList[guessMultiple[x]] = randomWordList[guessMultiple[x]]
                    print("\nA letter has been revealed!")
                    print("The word is now:", ''.join(revealWordList))
                    print("Number of turns remaining:",10-turns)
                    
            
        else:
            print("Unlucky, try again!")
            print("Number of turns remaining:",10-turns)
            

        if revealWordList == randomWordList:
            solved = True
            print("\nYou won in",turns,"turns!")
            print("The word was:",''.join(revealWordList))

    if turns <= 9:
        print("You ran out of lives")
        print("The word was:",''.join(revealWordList))
            
    
        
        

    
hangmanFunc()






    
