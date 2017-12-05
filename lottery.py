# -*- coding: utf-8 -*-

import csv
import time
import random
import os
import playsound
import sys
#install: pip install playsound (eventuelt med sudo foran om du får permission error)

def read_from_file(filename):
	data = []
	with open(filename,"rb") as csvfile:
		spamreader = csv.reader(csvfile, delimiter =',', quotechar='|')
		for row in spamreader:
			for _ in range(int(row[1])):
				data.append(row[0].decode('utf-8','ignore').encode("utf-8"))
	return data

def draw_three_winners(data):
	winner = data.pop(random.randint(0,len(data)-1))
	second = data.pop(random.randint(0,len(data)-1))
	third = data.pop(random.randint(0,len(data)-1))
	return [winner, second, third]

def draw_single_winner(data):
	winner = data.pop(random.randint(0, len(data) - 1))
	return [winner, data]

if __name__ == "__main__":
	data = read_from_file("data2.csv")
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	print "======================================="
	print "Velkommen til indøks vin-lotteri-maskin"
	print "======================================="
	playsound.playsound(os.path.join(sys.path[0], 'intro.mp3'), True)

	print "\nAntall lodd i trekningen:", len(data)
	print "Antall unike deltakere med vinnermuligheter:", len(set(data)), "\n"

	action = raw_input("'Enter' for å trekke vinner, 'e' for å avbryte: ")
	count = 0
	while action not in ("e", "exit", "stop", "s"):

		results = draw_single_winner(data)
		data = results[1]
		winner = results[0]
		
		os.system("echo '"+ "3"+"'")
		os.system("say -v Anna '"+ "3"+"'")
		time.sleep(2)
		os.system("echo '"+ "2"+"'")
		os.system("say -v Anna '"+ "2" +"'")
		time.sleep(2)
		os.system("echo '"+ "1"+"'")
		os.system("say -v Anna '"+ "1" +"'")
		time.sleep(2)

		playsound.playsound(os.path.join(sys.path[0],"fanfare"+str(count%3+1)+".mp3"), True)

		winner_Color = '\x1b[6;30;42m' + winner + '\x1b[0m'
		print "\n\tWINNER: ", winner_Color
		print "\tAntall gjenværende lodd i trekningen:", len(data)
		print "\tAntall gjenværende deltakere:", len(set(data))
		os.system("say -v Anna '"+ winner +"'") 
		playsound.playsound(os.path.join(sys.path[0], "party"+str(count%3+1)+".mp3"), True)
		action = raw_input("\nTrykk enter for å trekke vinner, 'e' for å avbryte: ")
		count+=1

