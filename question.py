import nltk
import random
import csv
import os

def load_data():
	""" Load the data
	Read through each line in the file, ignoring 
	the frequency the queries. Then remove the 
	first row, as it's only the heading.
	"""
	queries = []
	with open("./queries-10k-txt", "r") as file:
		for line in file:
			queries.append(line.split()[:-1])
	queries = queries[1:]
	return queries

def check_question_keys(queries):
	""" Classify each query a either a question or a statement
	Based on a list of common English and Spanish common 
	question words, check if each query contains a word in this list.
	If so, write a flag with 1 and the associated question code from
	the list. Otherwise, the flag is 0 with code 'n/a'.
	"""
	q_words = ["who", "what", "where", "when", "how", 
				"why", "which", "can", "que", "como"]
	results = []
	for query in queries:
	    is_q = False
	    for word in query:
	        if word.lower() in q_words:
	            results.append([" ".join(query), 1, word.lower()])
	            is_q = True
	            break
	    if not is_q:
	        results.append([" ".join(query), 0, 'n/a'])
	return results

def write_to_file(results, name):
	# Create the data directory and write the data in tsv format
	os.makedirs(os.path.dirname(name), exist_ok=True)
	with open(name, 'wt') as out_file:
		tsv_writer = csv.writer(out_file, delimiter='\t')
		for query in results:
			tsv_writer.writerow(query)

def extract_questions(results):
	# From all the queries, extract only the questions by 
	# looking at the flag created previously
	questions = []
	for query in results:
		if query[1] == 1:
			questions.append(query[0])
	return questions

def extract_features(query):
    features = {}
    for word in nltk.word_tokenize(query):
        features['contains({})'.format(word.lower())] = True
    return features

def define_sub_codes(queries):
	# Add subcodes to the questions
	"""
	Compares the questions from the queries to a publicly dataset
	of labeled questions, and classify the query questions by using
	a Naive Bayes classifier.
	"""

	# Extract features from the qc labeled questions dataset
	labeled_questions = nltk.corpus.qc.tuples()
	featuresets = []
	for question in labeled_questions:
	    featuresets.append((extract_features(question[1]), question[0]))

	# Create train and test sets, and trains the ML model on the latter
	test_size = int(len(featuresets) * 0.3)
	train_set, test_set = featuresets[test_size:], featuresets[:test_size]
	classifier = nltk.NaiveBayesClassifier.train(train_set)

	# Extract features from the query questions and apply the ML model on them
	queries_featureset = [extract_features(query) for query in queries]
	labels = classifier.classify_many(queries_featureset)

	# Write the questions with the subdomain to disk
	results = []
	for query,label in zip(queries,labels):
		results.append([query, 1, label])
	return results

# Load and parse the data from the file to a list
queries = load_data()

# Check if a query is either a question or a statement
results = check_question_keys(queries)
# Write the data to disk in tsv format
write_to_file(results, './data/q1.tsv')

# From all the queries, extract only the questions
questions = extract_questions(results)
# Classify each question to a specific subdomain
results = define_sub_codes(questions)
# Write the data to disk in tsv format
write_to_file(results, './data/q2.tsv')








