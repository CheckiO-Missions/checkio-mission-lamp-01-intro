"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[(2015, 1, 12, 10, 0 , 0),
        (2015, 1, 12, 10, 10 , 10),
        (2015, 1, 12, 11, 0 , 0),
        (2015, 1, 12, 11, 10 , 10),]],
            "answer": 1220,
        },
        {
            "input": [[(2015, 1, 12, 10, 0 , 0),
        (2015, 1, 12, 10, 10 , 10),]],
            "answer": 610,
        },
        {
            "input": [[(2015, 1, 12, 10, 0 , 0),
        (2015, 1, 12, 10, 10 , 10),
        (2015, 1, 12, 11, 0 , 0),
        (2015, 1, 12, 11, 10 , 10),
        (2015, 1, 12, 11, 10 , 10),
        (2015, 1, 12, 12, 10 , 10),]],
            "answer": 4820,
        },
        {
            "input": [[(2015, 1, 12, 10, 0 , 0),
        (2015, 1, 12, 10, 0 , 1),]],
            "answer": 1,
        },
    ],
    "Extra": [
        {
            "input": [[(2015, 1, 12, 10, 0 , 0),
        (2015, 1, 12, 10, 0 , 10),]],
            "answer": 10,
        },
    ]
}
