#!/usr/bin/python3 
import sys
import re

# python3 flashcards.py -filename

# color codes
CRED    = '\33[31m'
CRESET  = '\33[0m'
CBLINK  = '\33[5m'
CVIOLET = '\33[35m'
CBLUE   = '\33[34m'

nice_message = """
 ////////::::::-----------..................................-
+++/////:::::::---------....................................
++/////:::::::---------.............```````````.............
++/////::::::---------...........`````````````````..........
+/////::::::---------..........`````````````````.+.`........
+////:::::::--------..........`````````````````.ss````......
/////:::::::-------.........````````````-++``-sm+``````.....
/////::::::--------.........````-+```  .dMMhmm+.````````....
/////::::::--------........`````.syyyydMMMMMs` `````````....
/////::::::--------.........```````.--hMMMMo`  `````````....
/////::::::--------.........``````````hMMMM-  `````````.....
+////:::::::-------..........````````-MMMMMy```````````.....
+/////::::::--------..........```````+MMshMM.`````````......
+/////:::::::--------..........``````/MM-`hMs```````........
++/////::::::----------...........```:Mm``.yMy````..........
+++/////::::::----------.............+Md```.hM+.............
+++/////:::::::----------............/Ms....-NMh+-.......-+:
++++///hmmdyso+/:-+so+hdhyo/:-..-///odM+.../NMMMMMmyo/-.-sMN
+++++/dMMMMMMMMMMNMMMMMMMMMMMMNmNMMMMMMmyooMMMMMMMMMMMMmNMMM
+oo+++MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
mMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""

if len(sys.argv) < 2:
	print ("usage: python3 pycards.py filename.txt")
	sys.exit()
	
# dictionary to hold the questions and answers
qna = {}
	
# keep track of when an answer is incorrect
wrong_ans = 0

def readFile(filename):
	question_count = 0
	try:
		f = open(filename, 'r')
	except IOError:
		print ("Error opening file {}".format(filename))
		sys.exit()
	while True:
		line = f.readline()
		
		question = re.search(r'^(.*\?)', line)
		if question != None:
			q = (question.group(1))
			#print ("{}".format(q))
			# answer to the question is initially blank
			qna[q] = None
			question_count += 1
		answer = re.search(r'(^(.*)((?!\?).)$)', line)
		if answer != None:
			a = (answer.group(1))
			#print ("{}".format(a))
			qna[q] = a
		if line == "":
			# EOF
			break
		line = line.rstrip('\n')
	print("\n\t*----------------------------------------*")
	print("\t|\t\t\t\t\t |\n\t|\t\t\t\t\t |")
	print("\t|\t", end="")
	print(CBLINK + "   {} questions found".format(question_count) + CRESET, end="")
	print("\t\t |")
	print("\t|\t\t\t\t\t |\n\t|\t\t\t\t\t |")
	print("\t*----------------------------------------*\n")
	f.close

def askQuestions():
	global wrong_ans
	for q in qna.keys():
		if qna[q] != "x":
			print ("Q: {}".format(q))
			# do not show the answer until they want to continue
			input("Press enter to continue ")
			print ("A: {}".format(qna[q]))
			
			# make sure the user enters valid input [y/n]
			while True:
				answer = input("Did you get the answer correct? [y/n]:  ")
				if answer.lower() not in ('n', 'y'):
					print(CRED + "Response not recognized, please specify [y/n]" + CRESET)
				else:
					break
			if answer.lower() == "y":
				correctAnswer(q)
			elif answer.lower() == "n":
				wrong_ans += 1
			else: 
				print(CRED + "Response not recognized" + CRESET)
	q_round()

	
# mark the question in the dictionary as correct so it won't be asked again
def correctAnswer(q):
	qna[q] = "x"
	return 
	
def incorrectAnswer():
	for q in qna.keys():
		if q == "x":
			del qna[q]
	return

def q_round():
	global wrong_ans
	if wrong_ans > 0:
		# delete the questions that they got correct so they won't be asked again
		incorrectAnswer()
		while True:
			print(CVIOLET + "\n{} incorrect answers, let's try again".format(wrong_ans) + CRESET)
			wrong_ans = 0
			askQuestions()
			if wrong_ans == 0:
				#done_studying()
				break
	else:
		done_studying()

def done_studying():
	print(CBLUE + CBLINK + "\n\n\t\tYou're done! Go get that A!\n\n" + CRESET)
	print("{}".format(nice_message))

if __name__ == "__main__":
	filename = sys.argv[1]
	readFile(filename)
	askQuestions()
	
	
