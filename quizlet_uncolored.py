#Quizlet_CMD module
import random, time, sys
from pathlib import Path
from ast import literal_eval

#See instructions from README for creating/importing flashcards

def quizlet(stack, reverse = False):
    """Quizlet_CMD program
    This is a complete and full-featured flashcards study tool. Study Quizlet flashcards in the command line without an API

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
    if sys.platform != "darwin":
    	start,end = "",""
    input("\nWelcome to " + start + "Quizet_CMD" + end +". Press enter to begin, input '"+start+ "#exit" + end +"' anytime to stop session and show score")        #init

    for i in range(len(term)):      #cycles through every word in stack
        index = random.choice(q)      #randomly selects index
        resp = input(start + f"{term[index-1]}\n" + end).lower()
        ans = defin[index-1].lower()
        if resp == ans:       #checks for equiv
            print("Correct\n")
            right += 1
        elif resp == "#exit":        #exits
            i -= 1
            break
        elif "/" in ans and (resp == ans.split("/")[0] or resp == ans.split("/")[1]):   #if there are 2 ans
            print("Correct" + f" '{ans}'\n")
            right += 1 
        elif "(" in ans and resp == ans[:ans.find("(")] or resp == ans[:ans.find("(")]+" " or resp == ans.replace("("," (") or resp == ans.replace("("," ").replace(")","") or resp == ans.replace("(","").replace(")",""):    #if there are parentheses
            print("Correct" + f" '{ans}'\n")
            right += 1 
        elif ans[ans.find("(")-1] == " " and (resp == ans[:ans.find("(")-1] or resp == ans.replace(" (","(")):
            print("Correct" + f" '{ans}'\n")
            right += 1 
        else:
            print("The correct answer is " + start + f"{defin[index-1]}" + end)   #if wrong, provides correct ans
            if resp in defin:
                print(f"'{resp}' is the answer for '" + start + term[defin.index(resp)] + end + "'\n")
            else:
                print("\n")
            wrong.append((index,resp))
        q.remove(index)       #removes index to prevent repetition
        time.sleep(0.35)

    print(f"You got {right} out of {i+1} right!\nThat's a %s percent!\n"%round((right/(i+1))*100))
    choice = input("Would you like to see the words you got wrong? [y]/n ")
    if choice == "y" or choice == "":
        stack_wrong = dict(zip([defin[i[0]-1] for i in wrong],[term[i[0]-1] for i in wrong]))       #creates new dict of mistakes
        for i in wrong:
            print(f"\nYou entered '{i[1]}' for '{term[i[0]-1]}'. The correct answer is " + start + f"'{defin[i[0]-1]}'." + end)
        save = input("\nWould you like to save the words you got wrong into a stack? y/[n] ")
        if save != "n" and save != "" and save != "no":
            root = Path(".")
            new = False
            while new == False:
                path = input(f"What would you like to name your new file?  {(stack + '_') if isinstance(stack,str) else ''}") 
                path = (stack + "_") if isinstance(stack,str) else "" + path
                path += "" if path.endswith(".txt") else ".txt"              
                path_2_stacks = root/"stacks"/path
                if path_2_stacks.exists():
                    print("File already exists\n")
                else: new = True
            with open(path_2_stacks,"a") as dic:
                dic.write(str(stack_wrong))
            print("Stack is saved at '" + str(path_2_stacks) + "'!")
        study = input("\nWould you like to study the words you got wrong? y/[n] ")
        if study != "n" and study != "" and study != "no":
            quizlet(stack_wrong,reverse=reverse)


    exit(2)

# *optional if using existing file*  Write your own dictionary here only for short stacks or testing purposes
stack = {"你好":"hello"}

print(quizlet("example"))
