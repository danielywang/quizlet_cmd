Welcome to the Quizlet Write module. This is a complete and full-featured flashcards study tool.

To start practicing, 
1. Copy an existing Quizlet set off the website
	a. Go to the set on quizlet.com
	b. Under the title, click on the "...". Go to "export"
	c. Enter the below custom settings for each column *with quotes*
		'Between term and definition' ⟶  ":"
		'Between rows' ⟶  ",\n"
	d. Click 'Copy text'
	e. Paste into the variable (dict) named 'stack', add 1 quote at the beginning of the dictionary, delete extra quote at the end.
	NOTE: you can also paste the dict into a new file in the folder 'stacks'. *You need to take out the \n in the between rows option since the module only reads 1 line*

2. Create your own set with ease with "quizlet_dict.py"
	a. Execute func. dict_generator(). Read doc string for details. The dict will be saved into the "stacks" folder


After you have the dictionary mapping the terms to the definitions, go to: 
quizlet_colored.py OR quizlet_uncolored.py. The former is recommended but requires library 'termcolor'.
	Install termcolor using 'pip install termcolor' or 'conda install termcolor' in terminal


In the quizlet() func., you can either use the 'stack' dictionary used in method 1 above, or input the file name of the dict you created using method 2 above. 


