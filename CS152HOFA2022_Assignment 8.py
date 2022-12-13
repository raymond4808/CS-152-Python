#Assignment 8
#Practicing with Validation and Other Loops
#Raymond Cheung 11/02/2022
import random
def get_next_marquee (aWord):
    #simple takes word and places first letter to end
    length = (len(aWord))    
    switchedWord = aWord    
    firstLetter= switchedWord[0]
    switchedWord= switchedWord[1:] + firstLetter
    return switchedWord

def get_next_marquee_letter_mover(aWord, aNum):    
    #takes number placed in function and moves x amount of letters to back end of the str passed in the function    
    switchedWord = aWord    
    alteredSwitchWord= switchedWord[0:aNum]
    switchedWord= switchedWord[aNum:] + alteredSwitchWord
    return switchedWord

def threeParameterMarquee (aString, displaySize, bNum):
    #takes a parameter str with parameter passed display size, and displays the nth number of the marquee passed through it, should be valid for any nth number| EXTRA CREDIT
    aStringLength= len(aString)
    finalBNum= bNum%aStringLength
    alteredString= aString [0:finalBNum]
    preFinalWord= aString [finalBNum:]+ alteredString 
    finalWord= preFinalWord [0:displaySize]
    return finalWord

def validInput (enteredInput):
    #checks if input for display size is valid for Part B
    return enteredInput >4 and enteredInput < 26

def main ():    
    #Part A: Write a fruitful function with one parameter, a string, that returns the next full string in the marquee sequence. 
    print (get_next_marquee("Hello"))
    
    word= "Python"
    #Improved part a which displays the whole word marquee w/ looped fruitful function
    wordLength = len (word)
    print (word)
    for wordOver in range (wordLength):
        word = get_next_marquee (word)
        print (word)
    
    #Part B: Write in main function print all the possible displays of string limited by user input value, stopping when it gets back to the original
    stringMessage= "This is a string message. "
    lengthStringMessage= len(stringMessage)
    enteredInput = int(input("Enter a valid display size input between 5 and 25 for part B: "))                
    while not validInput(enteredInput):
        enteredInput = int(input("Seriously, enter a valid display size input between 5 and 25 for part B: "))
        
    print (stringMessage [0:enteredInput])
    for partB in range (lengthStringMessage):
        firstLetter= stringMessage[0]
        stringMessage = stringMessage[1:] + firstLetter
        print (stringMessage[:enteredInput])
        
    
    #Part C: Version of get_next_marquee which has two parameters, an string and an integer. The integer tells you how many characters to move from the front of the string to the end. 
    print (get_next_marquee_letter_mover("Hello", 3))  
    #Part D: Add 3-5 print statements to your main function to test your new function.
    print (get_next_marquee_letter_mover("I think this does its function okay, maybe? ", 20)) 
    print (get_next_marquee_letter_mover("Programming homework while at work on company time. ", 15))
    print (get_next_marquee_letter_mover("Im typing strings to test out my code, this is print statement 3/5. ", 21)) 
    print (get_next_marquee_letter_mover("Wondering what am I doing this early in the morning to do an assignment.... ", 27))
    
    #Last part for fun, part of Part D (since i already got my (3-5 print statements w/ function)
    lastString = "What is the average number of coffees a person drinks per day just to stay functional? "
    #Remove hashtag below to use your own string
    #lastString = input("Enter your string: ")
    lengthLastStr= len(lastString)
    randIntInRange= random.randrange (1, lengthLastStr)
    print (get_next_marquee_letter_mover(lastString, randIntInRange)) 
    
    #Extra Credit function with 3 passed values for marquee function, should return the nth string w/ NO LOOP
    print (threeParameterMarquee ("Python", 5, 3))
    print (threeParameterMarquee("Testing longer string for marquee board", 28, 11515515151))
    print (threeParameterMarquee("Python is so good at manipulating string values ", 23, 10))
    
main()