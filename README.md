	*----------------------------------------*
	|					 |
	|					 |
	|	         pycards		 |
	|					 |
	|					 |
	*----------------------------------------*


# pycards

A python script to replicate the functionality of flashcards

### Usage
```
python3 pycards.py study_file.txt
```


## Q/A file
This file [study_file.txt] should contain a series of questions followed by an answer.
*pycards.py* will read this file and display each question one at a time. When the user is ready, it will then display the answer.


After seeing the answer, specify if you got it wrong or right.


If you were correct, it will not ask you that question again, and continue asking questions that either haven't been asked
or were marked incorrect.

*pycards.py* will run until you have successfully answered every question correctly.

### format
*study_file.txt*

Each question should end with a question mark and every answer should be on the following line.
