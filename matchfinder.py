# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def findMatch (itemsList, userInput):
    isValid = False
    counter = 0
    possibilities = []
    
    while (isValid == False and counter < len(itemsList)):
    
        item = itemsList[counter] 
        
        if userInput == item :
            isValid = True
            return counter
        
        shorterWordsLength = min(len(userInput), len(item))
        letterMatch = 0
        
        for i in range(shorterWordsLength) :
            if userInput[i] == item[i] or (i < len(item)-1 and userInput == item[i+1]) or (i != 0 and userInput[i] == item[i-1]) :
                letterMatch += 1
                
        if letterMatch >= 3 :
            possibilities.append(counter)
            
        counter+=1
    
    return possibilities
    



coffeeTypes = ["Espresso", "Cappuccino", "Americano", "Macchiato", "Mocha", "Filter", "Turkish"]

userInput = (str(input("Enter input: "))).title()

result = findMatch(coffeeTypes, userInput)
    
if isinstance(result, int) :
    print("Picked: " + coffeeTypes[result])
elif len(result) > 0 :
    print("Did you mean one of below: ")
    for p in result:
        print(coffeeTypes[p])
else :
    print("No such choice.")

    
    

