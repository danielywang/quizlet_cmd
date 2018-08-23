#Quizlet_CMD module
import random, time, sys
from termcolor import colored
from pathlib import Path
from ast import literal_eval
from os import system

#See instructions from README for creating/importing flashcards

def quizlet(stack, say = True, reverse = False):
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
        whether terms/definitions are reversed. optional (default = False)"""

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
          
    q = [i for i in range(1,len(term)+1)]       #list of indexes
    right = 0       #score
    wrong = []      # list of mistakes: (index, usr input)
    start = "\033[1m"       #bold text
    end = "\033[0;0m"
    if sys.platform != "darwin":        #disable bold text for non-unix platforms
        from colorama import init
        init()
        print("\nWelcome to " + colored("Quizet_CMD","white","on_blue",["bold"]) + ". Press enter to begin, input '" + colored("#exit","magenta",attrs=["underline"]) + "' anytime to stop session and show score")
        input()
    else:
        input("\nWelcome to " + colored("Quizet_CMD","white","on_blue",["bold"]) + ". Press enter to begin, input '" + colored("#exit","magenta",attrs=["underline"]) + "' anytime to stop session and show score")        #init
    
    lang_voice = {"spanish":"paulina","english":"samantha","french":"amelie","chinese":"Ting-Ting","russian":"yuri"}     #dict for language mappings (Mac OS)
    
    if say:
        lang = False
        while lang == False:        #checks if languages are supported/spelling is correct
            try:
                lang_t = lang_voice[input("What language are the terms? For example, '"+random.choice(term) + "'\n").lower()]
                lang_d = lang_voice[input("What language are the definitions? For example, '"+random.choice(defin) + "'\n").lower()]
                lang = True
                print("\n")
            except KeyError:
                print("Check your spelling/The program does not yet support this language\n")
            
    for i in range(len(term)):      #cycles through every word in stack
        index = random.choice(q)      #randomly selects index
        print(start + f"{term[index-1]}" + end)
        if say:
            system("say -v {} {}".format(lang_t,term[index-1].replace('(',' ').replace(')',' ').replace('/',' ').replace('\'','')))
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
        elif "(" in ans and resp == ans[:ans.find("(")] or resp == ans[:ans.find("(")]+" " or resp == ans.replace("("," (") or resp == ans.replace("("," ").replace(")","") or resp == ans.replace("(","").replace(")",""):    #if there are parentheses
            correct(half=True)
            right += 1
        elif ans[ans.find("(")-1] == " " and (resp == ans[:ans.find("(")-1] or resp == ans.replace(" (","(")):
            correct(half=True)
        else:
            print("The correct answer is " + start + colored(f"{ans}","red") + end)   #if wrong, provides correct ans
            if resp in defin:
                print(f"'{resp}' is the answer for '" + colored(term[defin.index(resp)],"blue") + "'\n")
            else:
                print("\n")
            wrong.append((index,resp))
        if say:
            system("say -v {} {}".format(lang_d,ans.replace('(',' ').replace(')',' ').replace('/',' ').replace('\'','')))
        q.remove(index)       #removes index to prevent repetition
        time.sleep(0.1) if say else time.sleep(0.3)

    print(f"\nYou got {right} out of {i+1} right!\nThat's a " + colored(str(round((right/(i+1))*100)),"cyan") + " percent!\n")
    choice = input("Would you like to see the words you got wrong? [y]/n ")
    if choice == "y" or choice == "":
        stack_wrong = dict(zip([defin[i[0]-1] for i in wrong],[term[i[0]-1] for i in wrong]))       #creates dict with mistakes
        for i in wrong:
            print("\nYou entered '" + colored(i[1], "red") + "' for '" + colored(term[i[0]-1],"blue") + "'. The correct answer is '" + start + colored(defin[i[0]-1],"green",attrs=["underline"]) + end + "'")
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
            quizlet(stack_wrong,say=say,reverse=reverse)

    exit(2)

# *optional if using existing file*  Write your own dictionary here only for short stacks or testing purposes
stack = {"你好":"hello"}

#Again, 'say' is only available for Mac OS. 
#Feel free to change the params of the function!
if sys.platform == 'darwin':
    print(quizlet("example"))
else:
    print(quizlet("example", say=False))
