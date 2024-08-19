# Analysing and generating dictionaries
# Create a program with function score(), it will receive students multiple scores and return a dictionary with the following:
# - Scores quantity
# - Highest score
# - Lowest score
# - Mean score
# - Situation (optional)
# - Also add docstrings

def scores(scr, sit=False):
    """
    -> Reads multiple scores and return a dictionary with an analysis of quantity, highest, lowest, mean score and situation of student.
    :param scr: float values for the student scores (one or more)
    :param sit: optional bool value, show or not the situation
    :return: a dictionary with multiple informations
    """
    analysis = dict()
    analysis['total'] = len(scr)
    analysis['highest'] = max(scr)
    analysis['lowest'] = min(scr)
    analysis['mean'] = float(f'{sum(scr)/len(scr):.1f}')
    if sit:
        if analysis['mean'] >= 8:
            analysis['situation'] = 'GOOD'
        elif 8 > analysis['mean'] >= 6:
            analysis['situation'] = 'AVERAGE'
        else:
            analysis['situation'] = 'BAD'
    return analysis
        

# Main program
all_scores = list()
while 999 not in all_scores:
    all_scores.append(float(input('Enter score: [999 to stop] ')))
all_scores.pop()
situation = str(input('Want to show student situation? [y/n]')).strip().lower()[0]
if situation == 'y':
    print(scores(all_scores, sit=True))
else:
    print(scores(all_scores))
