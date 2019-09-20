# identify_question

The goal of this project is to, based on a set of queries, identify which ones are questions, and which ones are statements. That was done by comparing the queries with common English keywords associated with questions: https://grammar.cl/Notes/Question_Words.htm. Upon looking at the data, I also noticed that many queries were Spanish, so I added a few common Spanish question words as well.

Below is a legend explaining what each keyword refers to:

WHO: used when referring to people. (= I want to know the person)
WHERE: used when referring to a place or location. (= I want to know the place)
WHEN: used to refer to a time or an occasion. (= I want to know the time)
WHY: used to obtain an explanation or a reason. (= I want to know the reason)
WHAT/QUE: used to refer to specific information. (= I want to know the thing)
WHICH: used when a choice needs to be made. (= I want to know the thing between alternatives)
HOW/COMO: used to describe the manner that something is done. (= I want to know the way)

The second part of the project was about identifying subdomains within the questions. That was done by training a ML model based on a publicly available dataset containing labeled questions: https://cogcomp.seas.upenn.edu/Data/QA/QC/. This approach was preferred over trying to definine my own subdomains due to the already existence of the large dataset and the validity of the research performed by the curators. 
To classify the questions a Naive Bayes model was trained on the curated dataset, then applied on the query questions. The definition of each subdomain can be found here: https://cogcomp.seas.upenn.edu/Data/QA/QC/definition.html

## Running the code

Prior to running the code, it's necessary to install the NLTK library (http://www.nltk.org/install.html), and also the QC dataset (http://www.nltk.org/data.html).

To run the code, simply execute `python3 question.py` on the command line. The code will create two files in the _data_ subfolder, 1 for the first task and 2 for the second task.

To run the tests, simply execute `python3 -m unittest test/question_test.py`.
