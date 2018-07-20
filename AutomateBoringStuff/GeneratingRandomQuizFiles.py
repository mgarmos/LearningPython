#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

"""
Problem statement

Say you’re a geography teacher with 35 students in your class and you want
to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in
it, and you can’t trust the students not to cheat. You’d like to randomize the
order of questions so that each quiz is unique, making it impossible for anyone
to crib answers from anyone else. Of course, doing this by hand would
be a lengthy and boring affair.
"""

"""
1- Store the Quiz Data in a Dictionary
2- Create the Quiz File and Shuffle the Question Order
3- Create the Answer Options
4- Write Content to the Quiz and Answer Key Files

"""

# 1- Store the Quiz Data in a Dictionary
# The quiz data. Keys are states and values are their capitals.
v capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def generateQuiz(quiznum=''):
    quizFile = open(r'D:\LearningPython\AutomateBoringStuff\capitalsquiz%s' % (quiznum), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name\nDate\nPeriod\n\n')

