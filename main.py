
## this is just copied from Shakespeare

import re
#import pprint
import random

# python 2
class text_generator():
	def __init__(self, name):
		# reads in the text
		try:
			self.text = open(name, "r").read()
		except:
			throw("No input text loaded. File not found: ", name)

		# all the words
		self.words = re.split(" +|\n+", self.text) # split by spaces or new-line
		#print(self.words[:100])

		# all consecutive word pairs
		self.two_grams = zip(self.words, self.words[1:])

		self.two_gram_cnt = {x:[] for x in self.words}
		
		# 2-grams stored in a dictionary with the first word as key
		for a,b in self.two_grams:
			self.two_gram_cnt[a].append(b)
			
		
		#pprint.pprint(self.two_gram_cnt)




	
	def line_from_two_gram(self, start='?', smooth=True, max_len=20):
		'''This generates a line by starting with /start/
		then it picks the next word based on 2-gram frequencies, i.e. which words tend to follow /start/ in the original text
		For example, if the word 'a' is followed by 'friend' 50% of the time, 'day' 20% of the time, 
			and 'ghost' 30% of the time in the original text,
		then we'll pick 'friend' half of the time, 'day' 20% of the time, etc., as the next word

		This continues until we hit a punctuation or reaches max_len
		if smooth == False, we'll always picks the most frequent 2-gram, so 'a' will alawys be followed by 'friend' in this case'''
		
		if start not in self.words:
			start = random.choice(self.words)

		for i in range(max_len):
			print start,

			if len(start) and start[-1] in ['.', '!', '?', ';']:
				break

			if smooth: #randomly pick the next word, weighted by probability
				start = random.choice(self.two_gram_cnt[start]) #randomly pick the next word
			else:
				start = max(set(self.two_gram_cnt[start]), key=self.two_gram_cnt[start].count) #pick the most frequent


h = text_generator("Hamlet.txt")
s = text_generator("The Taming of the Shrew.txt")

#random.seed(1)

# generate 20 lines from Hamlet
for i in range(20):
	h.line_from_two_gram()
	print ''

# h.line_from_two_gram(start='death') # make a sentence start with death
# h.line_from_two_gram(start='death', smooth=False) # make a sentence start with death, ALWAYS using the most common 2-gram

# 20 lines from Shrew
print '\n\n'
for i in range(20):
	s.line_from_two_gram()
	print ''