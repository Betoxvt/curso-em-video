# Errors and Exceptions handling
# print('division')
# try:  # operation
#     a = int(input('Quotient: '))
#     b = int(input('Dividend: '))
#     r = a / b
# except Exception as error:  # fail
#     print(f'Something went wrong with {error.__class__}')
# else:  # went well
#     print(f'{r:.1f}')
# finally:  # fail or not, always shows
#     print('Thanks')

# It's possible to have multiple exception blocks for different types of errors, each with its own handling

print('division')
try:
    a = int(input('Quotient: '))
    b = int(input('Dividend: '))
    r = a / b
except (ValueError, TypeError):
    print('Problem with type of data you entered')
except ZeroDivisionError:
    print('Not possible to divide by zero')
except KeyboardInterrupt:
    print('User interrupted program')
except Exception as error:
    print(f'Error found {error}')
else:
    print(f'{r:.1f}')
finally:
    print('Thanks')