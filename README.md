# Quizlet_CMD

Welcome to the Quizlet_CMD module. This is a complete and full-featured flashcards study tool. Study Quizlet flashcards in the command line without an API, or make and study your own!

## Getting Started

Clone or download the repo to get started

## Prerequisites

The recommended *quizlet_colored.py* requires the **termcolor** module
(*If you are on Windows*, install **colorama** in addition to *termcolor*)

#### In terminal, cd to the repo folder and run 
`pip install -r requirements.txt`  

**Make sure you are in the `quizlet_cmd` directory*

Anaconda users: use `conda` instead
  
Note: Mac OS is required for the _optional_ `say` feature in *quizlet_colored.py* (turned on by default)
***
If the above doesn't work, run
`pip install termcolor`
`pip install colorama` (Windows)



**If the above prerequisites cannot be fulfuilled, *quizlet_uncolored.py* is also available**




***
## Running the tests

### *MAKE SURE TO CD TO THE FOLDER/OPEN THE ENTIRE FOLDER IN YOUR EDITOR*
This is required to make the file-reading and writing work


To test the *quizlet_colored* module using the pre-installed *example.txt*, cd to the folder and run:

```python quizlet_colored.py ```

Again, if the above didn't work, make sure you are in the `quizlet_cmd` directory
***
## Quizlet function

If the above command worked, you are now in the main quizlet function. This function allows you to practice flashcards (in this case, a Spanish *example.txt* located in *stacks*)
Input your answer to the prompt, followed by 'enter'  
Enter ```#exit``` at any time to end practice session and show score

#### Features
* Param `stack` can either open file with file name (recommended), or use the internal `stack` dictionary 
* Param `say = True` (default) reads prompts and answers using specified languages _(Mac only)_
	* Realized using Mac OS's built-in `say` function. User input specifies language, which activates different voices. Program is optimzed for irregular characters such as `(parentheses)` and `/` slashes
* Param `reverse = True` reverses terms/definitions
* Program notifies user if their wrong answer matches another answer  

* Program shows a list of words you got wrong, the prompt, and the correct answer
* Asks if user wants to save the set of words they got wrong into a new file
* Asks if user wants to practice the words they got wrong  
 

* If there are synonyms in the answer separated by `/`, eg `"car":"el coche/el carro"`, entering either (or both) would count as a correct answer
* If there are parentheses in the answer denoting optional content, eg `"red":"rojo(a)"`, not entering the content in the parentheses would also work. 
	* Irregular spacing is also accounted for. The following would all constitutue as correct:

	| Answer     | User    |
	|------------|---------|
	| 'rojo(a)'  | 'rojo'  |
	| 'rojo(a)'  | 'rojo` `' |
	| 'rojo` `(a)' | 'rojo'  |
	| 'rojo` `(a)' | 'rojo` `' |


#### Remarks
A **Mac** is required for the _optional_ `say` feature in *quizlet_colored.py*, which speaks the terms and definitions out loud.
 *quizlet_colored.py* currently has an OS detection set in place, so if you are not on Mac OS, the featured will be disabled. **feel free to change the parameters of the _quizlet_ function!** The defaults are just there as a demonstration.

***
## Getting Term-Definition Dictionaries

To get the flashcards (stacks) necessary for practicing, we can get the dictionary by:

1. Create your own set with ease with "quizlet_dict.py"
	* Execute dict_generator() in `quizlet_dict.py`. Read doc string for details. The dict will be saved as a text file into the "stacks" folder.    
	
2.  Copying an existing Quizlet set off the website
	* a. Go to the set on quizlet.com
	* b. Under the title, click on the "..."  Go to "export"
	* c. Enter the below custom settings for each column *with quotes*
		'Between term and definition' ⟶  `":"`
		'Between rows' ⟶  `","`
	* d. Click ['Copy text']
	* e. Go to *quizlet_dict.py*, and change the param `from_export` to `True`, run the file. When prompted, paste the above copied text. The program converts the text into a dictionary. A new text file with the name of your choosing will be stored in the `stacks` folder. To study the set, simply input the name of the file into the `quizlet` function in *quizlet_colored.py* (or *quizlet_uncolored.py*)

3.  For short flash cards or to test/have fun with the `quizlet` program, you can also manually type in a term-to-def. dictionary under the `stack` variable in *quizlet_colored.py* (or *quizlet_uncolored.py*). Be sure to change the param of the `quizlet` function to the variable `stack`

***
## Versioning

Version 1.2.2

**1.1 Now supports voice prompts!**
The *say* feature will be automatically turned on if you are on Mac OS. Again, feel free to turn it off.  

**1.1.3 Colors and bolding support Windows**  

Known issues:
Colors and bolding in Windows only work in CMD  

**1.2 Now asks user if they want to save the set of words they got wrong into a new file, and whether they want to practice them**
***
## Author

* **Daniel Wang** - *Initial work* - [danielywang](https://github.com/danielywang)
***

### Contributors
*Dan Bi* - [wujibi123](https://github.com/wujibi123)

*William Kopans* - [Wi11-Da-Beast](https://github.com/wi11-da-beast)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

