# Quizlet_CMD

Welcome to the Quizlet_CMD module. This is a complete and full-featured flashcards study tool. Study Quizlet flashcards in the command line without an API, or make and study your own!

## Getting Started

Clone or download the repo to get started

### Prerequisites

The recommended *quizlet_colored.py* requires the **termcolor** module
cd to the repo and run 
```pip install termcolor``` 

For Anaconda, run 
```conda install termcolor```

Note: A Mac is required for the _optional_ `say` feature in *quizlet_colored.py*

If the above prerequisites cannot be fulfuilled, *quizlet_uncolored.py* is also available

### Installing

There no additional modules to install. 



***
## Running the tests

### *MAKE SURE TO CD TO THE FOLDER/OPEN THE ENTIRE FOLDER IN YOUR EDITOR*
This is required to make the file-reading and writing work


To test the *quizlet_colored* module using the pre-installed *example.txt*, cd to the folder and run:

```python -c 'import quizlet_colored; print(quizlet_colored.quizlet("example"))' ```

Again, if the above didn't work, make sure you are in the `quizlet_cmd` directory
***
## Quizlet function

If the above command worked, you are now in the main quizlet function. This function allows you to practice flashcards (in this case, a Spanish *example.txt* located in *stacks*)
Input your answer to the prompt, followed by 'enter'  
Enter ```#exit``` at any time to end practice session and show score

At the end of the session you will be prompted:

`"Would you like to see the words you got wrong? y/n?"`

Inputting "y" will show a list of words you got wrong, the prompt, and the correct answer

#### Features
* Param `stack` can either open file with file name (recommended), or use the internal `stack` dictionary 
* Param `say = True` reads prompts and answers using specified languages _(Mac only)_
	* Realized using Mac OS's built-in `say` function. User input specifies language, which activates different voices. Program is optimzed for irregular characters such as `(parentheses)` and `/` slashes
* Param `reverse = True` reverses terms/definitions
* Program notifies user if their wrong answer matches another answer  
 

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
 *quizlet_colored.py* currently has an OS detection set in place, so if you are on Mac OS, the featured will be enabled and vice versa. **feel free to change the parameters of the _quizlet_ function!** The defaults are just there as a demonstration.

***
## Getting Term-Definition Dictionaries

To get the flashcards (stacks) necessary for practicing, we can get the dictionary by:
1.  Copying an existing Quizlet set off the website
	* a. Go to the set on quizlet.com
	* b. Under the title, click on the "..."  Go to "export"
	* c. Enter the below custom settings for each column *with quotes*
		'Between term and definition' ⟶  ```":"```
		'Between rows' ⟶  ```",\n"```
	* d. Click ['Copy text']
	* e. Paste into the variable (dict) named 'stack' in *quizlet_colored.py* or *quizlet_uncolored.py*, add 1 quote at the beginning of the dictionary, delete extra quote at the end.
  
2.  You can also paste the dict from above into a new ```.txt``` file in the folder *stacks*. __You need to take out the \n in the [between rows] option since the module only reads 1 line__  -> ```","```
    * Add 1 quote at the beginning of the dictionary, delete extra quote at the end.
    * This method is *strongly* recommended if you want to store multiple sets and switch between them with ease.

3. Create your own set with ease with "quizlet_dict.py"
	* a. Execute dict_generator() in ```quizlet_dict.py```. Read doc string for details. The dict will be saved into the "stacks" folder.  
***
## Versioning

Version 1.1.1

**Now supports voice prompts!**
The *say* feature will be automatically turned on if you are on Mac OS. Again, feel free to turn it off. 
***
## Author

* **Daniel Wang** - *Initial work* - [danielywang](https://github.com/danielywang)
***

### Contributors
*Dan Bi* - [wujibi123](https://github.com/wujibi123)

*William Kopans* - [Wi11-Da-Beast](https://github.com/wi11-da-beast)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

