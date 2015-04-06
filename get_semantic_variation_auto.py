#! /usr/bin/python
'''
A Python script to get the word semantic variation from www.persamaankata.com. A better source
is expected to replace once we know such thing exists
'''

import random
import re
import urllib
import urllib2
import sys
from bs4 import BeautifulSoup

def get_semantic_data(word):
	url = 'http://www.persamaankata.com/search.php'
	values = {'q' : word}

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	soup = BeautifulSoup(the_page, "lxml")

	ret_dict = {}

	for thesaurus_div in soup.find_all("div", class_="thesaurus_group"):
		semantic_type = unicode(thesaurus_div.h3)
		semantic_type = semantic_type[4:semantic_type.find(" ")]
		
		mini_soup = BeautifulSoup(unicode(thesaurus_div))
		synset = []
		# for thesaurus_desc in mini_soup.select(".word_thesaurus > a"):
		# 	synset.append(thesaurus_desc.string)

		first_line = mini_soup.select(".word_thesaurus")[0]
		minier_soup = BeautifulSoup(unicode(first_line))
		for thesaurus_desc in minier_soup.find_all("a"):
			synset.append(thesaurus_desc.string)

		ret_dict[semantic_type] = synset

	if 'sinonim' in ret_dict.keys():
		ret_dict['sinonim'].append(word.lower())

	return ret_dict

def get_used_type(my_dict):
	# if only 'sinonim', return it, else random by 70:30 (sinonim:antonim)
	if len(my_dict) > 1:
		roulette = random.randint(1, 10)
		if roulette >= 8:
			return 'antonim'
	return 'sinonim'

# -------------------------------------------------------------------------------------
line_number = 0

for line in sys.stdin:
	line_number += 1

	result = ""
	now = ""

	for c in line:
		if c.isalpha():
			now += c
		else:
			if len(now) != 0:
				print "Line " + str(line_number) + ", processing word: " + now
				semantic_var = get_semantic_data(now)

				if len(semantic_var) != 0:
					semantic_type = get_used_type(semantic_var)
					chosen_set = semantic_var[semantic_type]
					chosen_word = chosen_set[random.randint(0, len(chosen_set) - 1)]

					if now[0].isupper():
						chosen_word = chosen_word[0].upper() + chosen_word[1:]

					result = result[:-len(now)]
					result += chosen_word

			now = ""
		result += c

	mode = "w"
	if line_number > 1: mode = "a"
	with open("output.txt", mode) as output_file:
		output_file.write(result)