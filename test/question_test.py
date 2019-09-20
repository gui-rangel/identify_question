import os
import unittest
import question

class TestIdentifyQuestion(unittest.TestCase):

	def setUp(self):
		queries = question.load_data()
		self.results = question.check_question_keys(queries)

	def test_identify_question_by_key(self):
		right_format = True
		for q in self.results:
			if len(q) != 3:
				right_format = False
		self.assertTrue(right_format)

	def test_define_sub_codes(self):
		questions = question.extract_questions(self.results)
		questions_sub_codes = question.define_sub_codes(questions)
		right_format = True
		for q in questions_sub_codes:
			if ":" not in q[2]:
				print(q)
				right_format = False
		self.assertTrue(right_format)

if __name__ == '__main__':
    unittest.main()