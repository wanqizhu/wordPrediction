import re
#import pprint
import random


# data structure: tries
class tries():
	END = '_end'
	def __init__(self, words):
		self.trie = dict()
		self.size = 0
		for i in words:
			self.insert(str(i))


	def insert(self, word):
		current_dict = self.trie
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})

		current_dict[self.END] = current_dict.get(self.END, 0) + 1 # increment if exists
		self.size += 1

`


	def list(self, root=False):
		if not root:
			root = self.trie

		self.temp = [] # storing the elements
		self.list_recur(root, '')
		return self.temp


	def list_recur(self, root, string):
		'''
		recurse over each letter from root; string is the current substring leading to this node in the trie;

		we add a word to self.temp when we reach the stopping point (self.END)

		'''
		for i in root:
			if i == self.END:
				self.temp.append(string)
				continue
			string2 = string + i
			self.list_recur(root[i], string2)




	def search(self, word):
		current_dict = self.trie
		for letter in word:
			if letter in current_dict:
				current_dict = current_dict[letter]
			else:
				return -1

		if self.END not in current_dict:
			return -1

		return self.END






# a = tries([174214, 124, 1498, 1983741 ,12489, 8421, 124, 849, 6438, 841290, 748310, 12478, 1498])

# print(a.trie)

# print(a.list())





## this is just copied from Shakespeare



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


# h = text_generator("Hamlet.txt")
# s = text_generator("The Taming of the Shrew.txt")

# #random.seed(1)

# # generate 20 lines from Hamlet
# for i in range(20):
# 	h.line_from_two_gram()
# 	print ''

# # h.line_from_two_gram(start='death') # make a sentence start with death
# # h.line_from_two_gram(start='death', smooth=False) # make a sentence start with death, ALWAYS using the most common 2-gram

# # 20 lines from Shrew
# print '\n\n'
# for i in range(20):
# 	s.line_from_two_gram()
# 	print ''