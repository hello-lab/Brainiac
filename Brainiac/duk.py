import json,os

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Brainiac.settings')

# Setup Django
django.setup()
from dashboard.models import Quiz, Question

# JSON data containing topics, questions, options, and answers
json_data = [
    {
        "topic": "Mathematics",
        "questions": [
            {
                "question": "What is the value of 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "Solve for x: 3x - 7 = 11",
                "options": ["2", "4", "6", "8"],
                "answer": "6"
            },
            {
                "question": "What is the perimeter of a square with each side of length 5 units?",
                "options": ["15 units", "20 units", "25 units", "30 units"],
                "answer": "20 units"
            },
            {
                "question": "What is the area of a triangle with base 6 units and height 4 units?",
                "options": ["12 square units", "16 square units", "20 square units", "24 square units"],
                "answer": "12 square units"
            },
            {
                "question": "What is 30% of 200?",
                "options": ["40", "50", "60", "70"],
                "answer": "60"
            }
        ]
    },
    {
        "topic": "History",
        "questions": [
            {
                "question": "Who was the leader of the Soviet Union during World War II?",
                "options": ["Joseph Stalin", "Vladimir Lenin", "Mikhail Gorbachev", "Nikita Khrushchev"],
                "answer": "Joseph Stalin"
            },
            {
                "question": "Which ancient civilization built the Great Pyramid of Giza?",
                "options": ["Ancient Egyptians", "Ancient Greeks", "Ancient Romans", "Mesopotamians"],
                "answer": "Ancient Egyptians"
            },
            {
                "question": "In which year did Christopher Columbus reach the Americas?",
                "options": ["1492", "1510", "1525", "1607"],
                "answer": "1492"
            },
            {
                "question": "Who was the first President of the United States?",
                "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "Which country was not part of the Axis Powers during World War II?",
                "options": ["Italy", "Germany", "Japan", "France"],
                "answer": "France"
            }
        ]
    },
    {
        "topic": "Science",
        "questions": [
            {
                "question": "What is the chemical symbol for the element Oxygen?",
                "options": ["O", "H", "He", "O2"],
                "answer": "O"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What process do plants use to make their own food?",
                "options": ["Photosynthesis", "Respiration", "Fermentation", "Combustion"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Brain", "Liver", "Skin"],
                "answer": "Skin"
            },
            {
                "question": "What is the unit of measurement for electric current?",
                "options": ["Ampere", "Volt", "Ohm", "Watt"],
                "answer": "Ampere"
            }
        ]
    },
    {
        "topic": "Literature",
        "questions": [
            {
                "question": "Who wrote the novel 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Emily Brontë", "Charlotte Brontë", "Mary Shelley"],
                "answer": "Jane Austen"
            },
            {
                "question": "In 'The Lord of the Rings' series, who is the main antagonist?",
                "options": ["Sauron", "Gollum", "Saruman", "Frodo Baggins"],
                "answer": "Sauron"
            },
            {
                "question": "Who wrote the play 'Hamlet'?",
                "options": ["William Shakespeare", "Christopher Marlowe", "Ben Jonson", "John Milton"],
                "answer": "William Shakespeare"
            },
            {
                "question": "Which novel features the character Holden Caulfield?",
                "options": ["The Catcher in the Rye", "To Kill a Mockingbird", "1984", "Moby-Dick"],
                "answer": "The Catcher in the Rye"
            },
            {
                "question": "Who wrote 'The Great Gatsby'?",
                "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "Mark Twain"],
                "answer": "F. Scott Fitzgerald"
            }
        ]
    }
]

# Function to populate the database
def populate_database():
    for topic_data in json_data:
        # Create a Quiz for each topic
        quiz = Quiz.objects.create(title=topic_data['topic'])

        # Create questions for the quiz
        for question_data in topic_data['questions']:
            question = Question.objects.create(quiz=quiz, text=question_data['question'])

            # Create answers for each question
            for option in question_data['options']:
                is_correct = option == question_data['answer']
                Answer.objects.create(question=question, text=option, is_correct=is_correct)

# Call the function to populate the database
populate_database()