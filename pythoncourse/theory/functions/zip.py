mentors = {'Kylie Ying': "python", "Lex Fridman": "exposure", "Ali Abdal": "Productivity"}
skill_level = ["professional", "master", "grandmaster"]


# zip(*iterables) when I say iterables I mean all iterables separated by a comma may be more than 2

pair = list(zip(mentors,skill_level))

for i in pair:

    print(pair)