from pattern.web import *
from pattern.en import *
import string

persuassion_full_text = 'persuasion.txt'
#print persuassion_full_text''''''''''''''''''''' 

#ef get_word_list(filename):
	# = openfile


def process_text(filename):
	wentworth_mood = []
	wentworth_line = []
	wentworth_subject = []


	f = open(filename,'r')
	lines = f.readlines()
	curr_line = 0
	
	for line in lines:
		if "Wentworth" in line:
			mood = sentiment(line)[0]
			subject = sentiment(line)[1]
			#print mood
			#print curr_line
			wentworth_mood.append(mood)
			wentworth_line.append(curr_line)
			wentworth_subject.append(subject)
			curr_line += 1
		else:
			#print curr_line
			curr_line += 1

	
	f.close
	wentworth_list = wentworth_mood, wentworth_subject, wentworth_line
	return wentworth_list


wentworth_list = process_text(persuassion_full_text)




def plotting_sentiment(list):
	import matplotlib.pyplot as plt
	wentworth_mood = wentworth_list[0]
	#print len(wentworth_mood)
	wentworth_subject = wentworth_list[1]
	wentworth_line = wentworth_list[2]
	#print  len(wentworth_line)
	
	plt.plot(wentworth_line, wentworth_mood, 'ro')
	
	plt.ylabel('Sentiment towards Wentworth')
	plt.xlabel('Line in Text')
	plt.axis([0, 10000, -1, 1])
	plt.show()



plotting_sentiment(wentworth_list)




	 