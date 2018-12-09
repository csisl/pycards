#!/usr/bin/python3 
import sys
import re

# python3 flashcards.py -filename

# color codes
CRED    = '\33[31m'
CRESET  = '\33[0m'

if len(sys.argv) < 2:
	print ("Usage: -filename")
	sys.exit()

nice_message = """
 ////////////:::::::::::-----------------............................................................
++++++////////::::::::::::-----------------.....................................................----
+++++/////////:::::::::::----------------...........................................................
++++/////////:::::::::::--------------.........................```````````..........................
++++////////:::::::::::---------------.....................`````````````````````....................
+++/////////::::::::::--------------....................```````````````````````````.................
+++////////::::::::::--------------...................```````````````````````````````...............
++////////:::::::::::--------------...............```````````````````````````````:+-```.............
+/////////::::::::::--------------................```````````````````````````````hM/`````...........
++///////:::::::::::-------------................``````````````````````````````:hN/```````..........
+////////::::::::::------------.-..............``````````````````````.-``````:hMm:`````````.........
+////////::::::::::-------------...............````````````````   `sNMMs``-odMNs````````````........
+///////::::::::::--------------...............```````-o-````     .NMMMMhmMMd/.``````````````.......
/////////:::::::::--------------.............`.```````oNh/-.`...+hMMMMMMMMd:` ```````````````.......
////////::::::::::-------------................````````-+hNMMMMMMMMMMMMMMN`    ``````````````.......
////////::::::::::--------------...............````````````::-/oMMMMMMMMd:    ``````````````........
+///////:::::::::::-------------..............```````````````  `NMMMMMMm`     ``````````````........
+////////::::::::::------------................````````````````:MMMMMMMN`    ```````````````........
+////////::::::::::-------------................```````````````hMMMMMMMM:```````````````````........
+////////::::::::::-------------................``````````````.MMMMMMMMMN.`````````````````.........
++///////:::::::::::--------------................````````````:MMMMhyMMMM+````````````````..........
++////////::::::::::--------------.................```````````/MMMM:`oMMMh``````````````............
++////////::::::::::::-------------..................`````````:MMMm```sMMM/```````````..............
+++////////:::::::::::---------------..................```````.NMMy````sMMNo````````................
+++/////////:::::::::::---------------...................`````-MMM+`````oMMM+````...................
++++////////:::::::::::----------------.......................:MMM/`````.sMMN-......................
+++++////////::::::::::::----------------.....................:MMM-.......hMMh-...................--
++++++////////:::::::::::-----------------....................:MMN.........mMMMh+-..............-/+-
++++++///////oso+/:::::::::----------/o/:----................./MMh.......:dMMMMMMMdy+-........--yMNh
++++++++///sNMMMMMMNmhyso/::::ohddyshMMMMMNdhs+/:-....-+ss+shmMMMs......oNMMMMMMMMMMMMmhs+:.---oMMMM
+++++++++/sMMMMMMMMMMMMMMMMNmmMMMMMMMMMMMMMMMMMMMMNmdmMMMMMMMMMMMmo+:-.sMMMMMMMMMMMMMMMMMMMNhdMMMMMM
++++++++++mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
+++++++++oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
sNMNNmddhhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""
	
# dictionary to hold the questions and answers
qna = {}
	
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
	print("*----------------------------------------*")
	print("|\t\t\t\t\t |\n|\t\t\t\t\t |")
	print("|\t   {} questions found\t\t |".format(question_count))
	print("|\t\t\t\t\t |\n|\t\t\t\t\t |")
	print("*----------------------------------------*")
	f.close

def askQuestions():
	for q in qna.keys():
		if q != "x":
			print ("Q: {}".format(q))
			# do not show the answer until they want to continue
			input("Press enter to continue ")
			print ("A: {}".format(qna[q]))
			answer = input("Did you get the answer correct? [y/n]:  ")
			if answer.lower() == "y":
				correctAnswer(q)
			else:
				incorrectAnswer(q)

# mark the question in the dictionary as correct so it won't be asked again
def correctAnswer(q):
	qna[q] = "x"
	return 
	
def incorrectAnswer(q):
	print(CRED + "{}".format(q) + CRESET)
	if "x" in qna.keys():
		print( CRED + "Questions still need to be asked" + CRESET)
	return

if __name__ == "__main__":
	filename = sys.argv[1]
	readFile(filename)
	askQuestions()
	
	
