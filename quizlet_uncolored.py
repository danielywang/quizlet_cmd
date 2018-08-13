#Offline Quizlet "write" module
import random, time, sys
from pathlib import Path
from ast import literal_eval

"""INSTRUCTIONS FOR EXPORTING SET FROM QUIZLET
In "export" under the triple-dot, enter the below 'custom' settings (with the quotes)
Between term and definition:    ":"
Between rows:                   ",\n"
Paste in stack, add init quote, del. end quote
"""

def quizlet(stack, reverse = False):
    """Quizlet "write" program
    params:
    _______
    stack (dict or str):
        dictionary of words and their definitions
        or file name of existing dictionary 
    reverse (bool):
        whether terms/definitions are reversed. optional"""
    
    if isinstance(stack,str):       #reads dict from existing file if "stack" is str
        stack += "" if stack.endswith(".txt") else ".txt"
        with open(Path(".") / "stacks"/stack,"r") as dic:
            stack = literal_eval(dic.readline())

    term = [i for i in stack.values()]      #init terms and definitions. Feel free to swap 2 variables
    defin = [k for k in stack]
    if reverse:
        term, defin = defin, term
          
    q = [i for i in range(1,len(term)+1)]       #list of indexes
    right = 0       #score
    wrong = []      # list of mistakes: (index, usr input)
    start = "\033[1m"       #bold text
    end = "\033[0;0m"
    if str(sys.platform) == 'ios' or str(sys.platform) == "windows":
    	start,end = "",""
    input("\nWelcome to " + start + "Quizet Write" + end +". Press enter to begin, type 'exit' anytime")        #init

    for i in range(len(term)):      #cycles through every word in stack
        index = random.choice(q)      #randomly selects index
        resp = input(start + f"{term[index-1]}\n" + end).lower()
        ans = defin[index-1].lower()
        if resp == ans:       #checks for equiv
            print("Correct\n")
            right += 1
        elif resp == "exit":        #exits
            exit(2)
        elif "/" in ans and (resp == ans.split("/")[0] or resp == ans.split("/")[1]):   #if there are 2 ans
            print("Correct" + f" '{ans}'\n")
            right += 1
        elif "(" in ans and resp == ans[:ans.find("(")] or resp == ans[:ans.find("(")]+" ":    #if there are parentheses
            print("Correct" + f" '{ans}'\n")
            right += 1
        elif resp == ans[:ans.find("(")-1] if ans[ans.find("(")-1].endswith(" ") else False:
            print("Correct" + f" '{ans}'\n")
            right += 1 
        else:
            print("The correct answer is " + start + f"{defin[index-1]}\n" + end)   #if wrong, provides correct ans
            wrong.append((index,resp))
        q.remove(index)       #removes index to prevent repetition
        time.sleep(0.3)

    print (f"You got {right} out of {len(term)} right!\nThat's a %s percent!\n"%round((right/len(term))*100))
    choice = input("Would you like to see the words you got wrong? y/n?")
    if choice == "y" or choice == "":
        for i in wrong:
            print(f"\nYou entered '{i[1]}' for '{term[i[0]-1]}'. The correct answer is " + start + f"'{defin[i[0]-1]}'." + end)
    exit(2)

#Paste flashcards here from quizlet.com (see readme), *optional if using existing file*
stack = {}

print(quizlet("example"))
