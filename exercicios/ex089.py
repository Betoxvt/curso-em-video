# Report Card with Nested Lists
# Create a program that collects the names and two grades of multiple students
# and stores this information in a nested numbers_list.
# Calculate and display the average grade for each student and
# allow the user to view the individual grades of a specific student. (999 to end program)
students = []
print('='*30)
print('Report Cards'.center(30))
while True:
    print('='*30)
    student = [str(input('Name: ')).title().strip(),
               float(input('Grade 1: ')),
               float(input('Grade 2: '))]
    average = float('{:.1f}'.format((student[1] + student[2]) / 2))
    student.append(average)
    students.append(student[:])
    student.clear()
    print('='*30)
    answer = str(input('Next student? [Y/N]')).upper().strip()[0]
    while answer not in 'YN':
        answer = str(input('Next student? [Y/N]')).upper().strip()[0]
    if answer == 'N':
        break
print('—'*30)
print('No. | Students Name | Average')
print('—'*30)
for i, s in enumerate(students):
    print(f'{i:>3} | {s[0]:<14}|    {s[3]:>4}')
print('—'*50)
while True:
    no = int(input('Show grades from which student? ([999]to quit) '))
    if no == 999:
        break
    else:
        for i, s in enumerate(students):
            if no == i:
                print(f"{s[0]}'s grades are {s[1]} and {s[2]}")
                print('—'*50)
print('='*50)
print('END OF PROGRAM')

# Teacher's solution
# ficha = numbers_list()
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = input('Quer continuar? [S/N] ')
#     if resp in 'Nn':
#         break
# print('-='*30)
# print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-'*26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-'*35)
#     opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')
