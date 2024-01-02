# dictionary_comprehension = {key: expresion for key,value in iterable}
# dictionary_comprehension = {key: expresion for key,value in iterable if conditional}
# dictionary_comprehension = {key:  (if/else) expresion for key,value in iterable}
# dictionary_comprehension = {key: function(value) for key,value in iterable}

lectures = {'Katiku': 35, 'Kimei': 40, 'Noela': 50, 'Ogada': 50 }


lecture_evaluation = {key: value*100 for (key,value) in lectures.items()}

print(lecture_evaluation)