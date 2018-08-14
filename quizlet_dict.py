#Use this module to generate a dictionary to use in quizlet.py

def dict_generator(max_words = 50, copy = False):
    """Enter in key, value; repeat
    PRESS EXIT ANY TIME TO END SESSION

    params:
    _______
    max_words (int):
        max number of iterations. optional (default = 50)
    path (str):
        file name of stack to be saved. optinal (default = None)
    copy (bool):
        whether to copy stack. optional (default = False)

    returns:
    _______
    stack (dict)"""
    print("PRESS EXIT ANY TIME TO SAVE & EXIT\n")
    path = input("What do you want to name your quizlet?") + '.txt'
    term = []
    defin = []
    for i in range(max_words):
        word = input()
        if word == "exit":
            break
        if i%2 == 0:
            term.append(word) 
        else:
            defin.append(word)
            print("")
    stack = dict(zip(term,defin))
    if copy:        #if usr chooses to copy to clipboard
        try:
            import pyperclip
            pyperclip.copy(str(stack))      #copy to clipboard if 'pyperclip' is installed
            print("Copied to clipboard")
        except ImportError:
            print("Stack not copied")
            pass
    if path is not None:        #save in folder "stacks" if usr chooses so
        from pathlib import Path
        root = Path(".")
        path_2_stacks = root/"stacks"/path
        with open(path_2_stacks,"a") as dic:
            dic.write(str(stack))
        print("Stack saved!")
    return stack

#copy and paste dictionary into quizlet.py, under variable 'stack'
print(dict_generator(10))
