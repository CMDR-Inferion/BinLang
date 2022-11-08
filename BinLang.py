#!/usr/local/bin/python3

import wave
import time
import pyaudio
import sys
import os


if __name__ == '__main__':
	baseLocation = os.path.dirname(__file__)
	if len(sys.argv) == 2:
		word = sys.argv[-1].lower()
	elif len(sys.argv) == 1:
		s = input("Ввод: ")
		if s == "DT":
			s = "arpa arpb arpc arpd arpe arpf arpg ca fa fb tra ala alb gta gtb gtc gtd gte gtg gth gti gtj gtk gtl no nope taa tab tac tad tae taf tag tah tb tc td te tf tg th"
		word = s.split(' ')
		word.append('tac')
		#word = ['tg','tac']
	else:
		print("Usage : ./BinLang".py (string))
		sys.exit(-1)
	root = baseLocation + "/sounds/{0}.wav"
	p = pyaudio.PyAudio()
	stream = p.open(format = p.get_format_from_width(2),
		channels = 1,
		rate = 22050,
		output = True)
	data = b""
	chunk = 1024
	for letter in word:
		if not letter.isalpha():
			continue
		try:
			with wave.open(root.format(letter), "rb") as f:
				data += f.readframes(f.getnframes())
		except Exception as e:
			print(e)
	print("Звук:")
	stream.write(data)
	wf = wave.open(baseLocation + "/out.wav", 'wb')
	wf.setnchannels(1)
	wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
	wf.setframerate(22050)
	wf.writeframes(data)
	wf.close()
	p.terminate()
