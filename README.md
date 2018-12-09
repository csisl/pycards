	*----------------------------------------*
	|					 |
	|					 |
	|	      flashcards		 |
	|					 |
	|					 |
	*----------------------------------------*


# flashcards

A python script to replicate the functionality of flashcards

### Usage
```
python3 flashcards.py study_file.txt
```

## Q/A file
This file (study_file.txt) should contains a series of questions followed by an answer.
*flashcards* will read this file and display each question one at a time, then when ready, the answer.


Specify if you got the answer wrong or right.


If you were correct, it will not ask you that question again, and continue asking questions that either haven't been asked
or were marked incorrect. *flashcards* will run until you have successfully answered every question correctly.

### format
Each question should end with a question mark and every answer should be on the following line.
