#Offline Quizlet "write" module
import random, time
from termcolor import colored
from pathlib import Path
from ast import literal_eval

"""INSTRUCTIONS FOR EXPORTING SET FROM QUIZLET
In "export" under the triple-dot, enter the below 'custom' settings (with the quotes)
Between term and definition:    ":"
Between rows:                   ",\n"
Paste in stack, add init quote
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
    input("\nWelcome to " + colored("Quizet Write","white","on_blue",["bold"]) + ". Press enter to begin, type '" + colored("exit","magenta",attrs=["underline"]) + "' anytime to stop session and show score")        #init

    for i in range(len(term)):      #cycles through every word in stack
        index = random.choice(q)      #randomly selects index
        resp = input(start + f"{term[index-1]}\n" + end).lower()
        ans = defin[index-1].lower()
        if resp == ans:       #checks for equiv
            print(colored("Correct\n","green"))
            right += 1
        elif resp == "exit":        #exits
            i -= 1
            break
        elif "/" in ans and (resp == ans.split("/")[0] or resp == ans.split("/")[1]):   #if there are 2 ans
            print(colored("Correct","green") + f" '{ans}'\n")
            right += 1
        elif "(" in ans and resp == ans[:ans.find("(")] or resp == ans[:ans.find("(")]+" ":    #if there are parentheses
            print(colored("Correct","green") + f" '{ans}'\n")
            right += 1
        elif resp == ans[:ans.find("(")-1] if ans[ans.find("(")-1].endswith(" ") else False:
            print(colored("Correct","green") + f" '{ans}'\n")
            right += 1
        else:
            print("The correct answer is " + start + colored(f"{defin[index-1]}","red") + end +"\n")   #if wrong, provides correct ans
            wrong.append((index,resp))
        q.remove(index)       #removes index to prevent repetition
        time.sleep(0.3)

    print(f"\nYou got {right} out of {i+1} right!\nThat's a " + colored(str(round((right/(i+1))*100)),"cyan") + " percent!\n")
    choice = input("Would you like to see the words you got wrong? y/n?")
    if choice == "y" or choice == "":
        for i in wrong:
            print("\nYou entered '" + colored(i[1], "red") + "' for '" + colored(term[i[0]-1],"blue") + "'. The correct answer is '" + start + colored(defin[i[0]-1],"green",attrs=["underline"]) + end + "'")
    exit(2)

#Paste flashcards here from quizlet.com (see README), *optional if using existing file*
stack = {}

print(quizlet("example"))
