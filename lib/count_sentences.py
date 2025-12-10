#!/usr/bin/env python3

import re

class MyString:
	def __init__(self, value=''):
		self._value = ''
		self.value = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		if isinstance(new_value, str):
			self._value = new_value
		else:
			print("The value must be a string.")

	def is_sentence(self):
		return self._value.strip().endswith('.')

	def is_question(self):
		return self._value.strip().endswith('?')

	def is_exclamation(self):
		return self._value.strip().endswith('!')

	def count_sentences(self):
		if not self._value:
			return 0
		# Split on one or more sentence-ending punctuation marks
		parts = re.split(r'[.?!]+', self._value)
		# Filter out empty or whitespace-only parts
		sentences = [p for p in (part.strip() for part in parts) if p]
		return len(sentences)