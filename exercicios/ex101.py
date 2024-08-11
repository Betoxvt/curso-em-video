# Create a program which have a function named vote(), it shall receive as a parâmeter a persons year of birth,
# returning a literal value indicating whether a person has mandatory, optional ou denied vote at the elections.
from datetime import date


def vote(year_of_birth):
    age_now = date.today().year - year_of_birth
    if age_now < 16:
        return 'DENIED'
    elif age_now > 70 or age_now < 18:
        return 'OPTIONAL'
    else:
        return 'MANDATORY'


person = int(input('Please inform year of birth: '))
age = date.today().year - person
print(f'At age {age} vote is {vote(person)}')
