# Respondendo ao usuário
"""Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas."""
nome = input('Qual o seu nome? ')
print('É um prazer te conhecer, {}{}{}!'.format('\033[3:97:40m', nome, '\033[m'))
