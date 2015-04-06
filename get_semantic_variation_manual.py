#! /usr/bin/python
'''
A Python script to get the word semantic variation from www.persamaankata.com. A better source
is expected to replace once we know such thing exists
'''

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
		ret_dict[semantic_type] = []

		mini_soup = BeautifulSoup(unicode(thesaurus_div))
		for grouped_lines in mini_soup.find_all("div", class_="word_thesaurus"):
			synset = []
			liner_soup = BeautifulSoup(unicode(grouped_lines))
			for thesaurus_desc in liner_soup.select("a"):
				synset.append(thesaurus_desc.string.rstrip())
			
			ret_dict[semantic_type].append(synset)

	return ret_dict

def get_user_choice(semantic_var, ori_word):
	print "Choose variation from below options (or type one yourself):"
	for semantic_type in semantic_var.keys():
		print semantic_type.upper() + " (" + ori_word + ")"

		for variation_line in semantic_var[semantic_type]:
			print "-",
			for i, variation in enumerate(variation_line):
				if i > 0: print "\b,",
				print variation,
			print ""

		print ""

	chosen = raw_input()
	return chosen.rstrip()

# -------------------------------------------------------------------------------------

lines = []
with open('input.txt', 'r') as input_file:
	lines = input_file.readlines()

for line_number, line in enumerate(lines):
	result = ""
	now = ""

	for c in line:
		if c.isalpha():
			now += c
		else:
			if len(now) != 0:
				print "Line " + str(line_number + 1) + ", processing word: " + now
				semantic_var = get_semantic_data(now)

				if len(semantic_var) != 0:
					chosen_word = get_user_choice(semantic_var, now)

					if now[0].isupper():
						chosen_word = chosen_word[0].upper() + chosen_word[1:]

					result = result[:-len(now)]
					result += chosen_word

			now = ""
		result += c

	mode = "w"
	if line_number > 0: mode = "a"
	with open("output.txt", mode) as output_file:
		output_file.write(result)