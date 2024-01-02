import random
import string


words = ["HELLO", "CAR", "book", "rock", "door", "hello", "guess", "laptop","garden"]

#list of wors
# 
# import random
#import alphabet as it is like a library with alphabets which are either in upperccase or lowercase

#import word
#define a function


def hangman(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words) 
    return word.upper()

    
def guessword():
    word = hangman(words)
    wordletters = set(words)
    alphabet = set(string.ascii_uppercase)
    lives = 6
    
    usedletters = set()
    
    while len(wordletters) > 0 and lives > 0:
        

        print("You have", lives,"Lives left." "USED LETTERS ARE AS FOLLOWS ",' '.join(usedletters))
        
        wordlist = [letter if letter in usedletters else '-' for letter in word]
        print('Current words:  ', ' '.join(wordlist))
        userletter = input("Enter a letter in the alphabet:   ").upper()

        
        
        if userletter in alphabet - usedletters:
            usedletters.add(userletter)
            if userletter in wordletters:
                wordletters.remove(userletter)
            else:
                lives = lives - 1
                print("Letter is not in the word")
                
        elif userletter in usedletters:
            print("You have already typed the letter")
            
        else:
            print("Invalid choice. Try again")    
            
        

      
guessword()
        
        
      
          
#pass in the list of word as a parameter
#get a random word from the list
#skip the word with - or ' '
#return the word


#keep track of letters we have guessed or keep track of letters in word we have not guesed
#define a function
#using word that was randomly selected
#define word letters a variable that saves all the letters in the word as a set 
#define used_letters a variable that will save all the uppercase letters as a set
#ascii_uppercase
#define used_letters a variable that will keep track of all the letters that user has guessed


#define use_letter a variable that will store letter that user has typed in the letter is in uppercase
#check if the letter typed in is a valid letter in the letters that have not been used yet and add it to the variable used letters
#you add the used letter to the usedletters

#then you will remove that letter from the word letters
#but if the letter has already been used or is part of used_letters you are supposed to print letter already guessed 


#return error if character typed is NULL


#iterate through the list as long as word length is greater than 0

#Infor m the user of the letters he or she has arleady used such that the letters are in string separated by a space 
#use ' '.join(used_letters)
#Create a list where all the letters that you have guessed are displayed and letters that you have not guessed are just dashes
#Tke the list and join it using a space as though it aa word and print it out

#

#You can play the game

#Make it more fun by introducing concept of lives such that if used letteris in wordletters and the letterthat user has guessed is not in word leeters the user lives decrease by 1
#Decrement lives by 1
#You can tell them the number of lives left

#if lives equal =0 you want to tell the m that they died 
