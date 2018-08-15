#Quizlet_CMD module
import random, time, sys
from termcolor import colored
from pathlib import Path
from ast import literal_eval
from os import system

"""INSTRUCTIONS FOR EXPORTING SET FROM QUIZLET
In "export" under the triple-dot, enter the below 'custom' settings (with the quotes)
Between term and definition:    ":"
Between rows:                   ",\n"
Paste in stack, add init quote, del. end quote
"""

def quizlet(stack, say = False, reverse = False):
    """Quizlet_CMD program
    This is a complete and full-featured flashcards study tool. Study Quizlet flashcards in the command line without an API

    params:
    _______
    stack (dict or str):
        dictionary of words and their definitions
        or file name of existing dictionary 
    say (bool):
        #ONLY AVAILABLE ON MAC OS!!!
        whether to read the terms and definitions. optional (default = True)
    reverse (bool):
        whether terms/definitions are reversed. optional"""

    def correct(half=False):
        if half:
            print(colored("Correct","green") + f" '{ans}'\n")
        else:
            print(colored("Correct\n","green"))

    if isinstance(stack,str):       #reads dict from existing file if "stack" is str
        stack += "" if stack.endswith(".txt") else ".txt"
        with open(Path(".") / "stacks"/stack,"r") as dic:
            stack = literal_eval(dic.readline())

    term = [i for i in stack.values()]      #init terms and definitions. Feel free to swap 2 variables
    defin = [k for k in stack]
    if reverse:
        term, defin = defin, term
          
    lang_voice = {"spanish":"paulina","english":"samantha","french":"amelie","chinese":"Ting-Ting","russian":"yuri"}     #dict for language mappings (Mac OS)

    q = [i for i in range(1,len(term)+1)]       #list of indexes
    right = 0       #score
    wrong = []      # list of mistakes: (index, usr input)
    start = "\033[1m"       #bold text
    end = "\033[0;0m"
    if sys.platform != "darwin":        #disable bold text for non-unix platforms
        from colorama import init
        init()
    else:
        input("\nWelcome to " + colored("Quizet_CMD","white","on_blue",["bold"]) + ". Press enter to begin, input '" + colored("#exit","magenta",attrs=["underline"]) + "' anytime to stop session and show score")        #init
    if say:
        lang_t = input("What language are the terms? For example, '"+random.choice(term) + "'\n").lower()
        lang_d = input("What language are the definitions? For example, '"+random.choice(defin) + "'\n").lower()

    for i in range(len(term)):      #cycles through every word in stack
        index = random.choice(q)      #randomly selects index
        print(start + f"{term[index-1]}" + end)
        if say:
            system(f"say -v {lang_voice[lang_t]} {term[index-1].replace('(',' ').replace(')',' ').replace('/',' ')}")
        resp = input().lower()
        ans = defin[index-1].lower()
        if resp == ans:       #checks for equiv
            correct()
            right += 1
        elif resp == "#exit":        #exits
            i -= 1
            break
        elif "/" in ans and (resp == ans.split("/")[0] or resp == ans.split("/")[1]):   #if there are 2 ans
            correct(half=True)
            right += 1
        elif "(" in ans and resp == ans[:ans.find("(")] or resp == ans[:ans.find("(")]+" ":    #if there are parentheses
            correct(half=True)
            right += 1
        elif resp == (ans[:ans.find("(")-1] or ans.replace(" (","(")) if ans[ans.find("(")-1].endswith(" ") else False:
            correct(half=True)
            right += 1
        else:
            print("The correct answer is " + start + colored(f"{ans}","red") + end)   #if wrong, provides correct ans
            if resp in defin:
                print(f"'{resp}' is the answer for '" + colored(term[defin.index(resp)],"blue") + "'\n")
            else:
                print("\n")
            wrong.append((index,resp))
        if say:
            system(f"say -v {lang_voice[lang_d]} {ans.replace('(',' ').replace(')',' ').replace('/',' ')}")
        q.remove(index)       #removes index to prevent repetition
        time.sleep(0.1) if say else time.sleep(0.3)

    print(f"\nYou got {right} out of {i+1} right!\nThat's a " + colored(str(round((right/(i+1))*100)),"cyan") + " percent!\n")
    choice = input("Would you like to see the words you got wrong? y/n?")
    if choice == "y" or choice == "":
        for i in wrong:
            print("\nYou entered '" + colored(i[1], "red") + "' for '" + colored(term[i[0]-1],"blue") + "'. The correct answer is '" + start + colored(defin[i[0]-1],"green",attrs=["underline"]) + end + "'")
    exit(2)

#Paste flashcards here from quizlet.com (see README), *optional if using existing file*
stack = {"你好":"hello"}


#Again, 'say' is only available for Mac OS. 
#Feel free to change the params of the function!
if sys.platform == 'darwin':
    print(quizlet("example", say=True))
else:
    print(quizlet("example", say=False))
