#!/usr/bin/python3 
import sys
import re

# python3 flashcards.py -filename

if len(sys.argv) < 2:
	print ("Usage: -filename")
	sys.exit()
	
# dictionary to hold the questions and answers
qna = {}
	
def readFile(filename):
	try:
		f = open(filename, 'r')
	except IOError:
		print ("Error opening file {}".format(filename))
		sys.exit()
	while True:
		line = f.readline()
		
		question = re.search(r'Q:(.*)', line)
		if question != None:
			q = (question.group(1))
			#print ("{}".format(q))
			# answer to the question is initially blank
			qna[q] = None
		answer = re.search(r'A:(.*)', line)
		if answer != None:
			a = (answer.group(1))
			#print ("{}".format(a))
			qna[q] = a
		if line == "":
			# EOF
			break
		
		line = line.rstrip('\n')
	f.close

def askQuestions():
	for q in qna:
		print ("Q: {}".format(q))
		# do not show the answer until they want to continue
		#show_ans = input("Continue? [y/n]:  ")
		show_ans = waitToShowAns()
		if show_ans == "y":
			print ("A: {}".format(qna[q]))
			answer = input("Did you get the answer correct? [y/n]:  ")
			if answer.lower() == "y":
				correctAnswer(q)
				askQuestions()
			else:
				askQuestions()
		else:
			waitToShowAns()
		return

def waitToShowAns():
	show_ans = input("Show answer? [y/n]:  ")
	if show_ans.lower() != "y":
		waitToShowAns()
	else:
		return show_ans

def correctAnswer(q):
	del qna[q]
	return 
	

if __name__ == "__main__":
	filename = sys.argv[1]
	readFile(filename)
	askQuestions()
	
	
