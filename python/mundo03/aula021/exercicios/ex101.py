# Create a program which have a function named vote(), it shall receive as a parâmeter a persons year of birth,
# returning a literal value indicating whether a person has mandatory, optional ou denied vote at the elections.
def vote(year_of_birth):
    from datetime import date
    age = date.today().year - year_of_birth
    if age < 16:
        return f'With {age} years: voting is DENIED.'
    elif age > 70 or age < 18:
        return f'With {age} years: voting is OPTIONAL.'
    else:
        return f'With {age} years: voting is MANDATORY.'


# Main code
birth = int(input('Please inform year of birth: '))
print(vote(birth))
