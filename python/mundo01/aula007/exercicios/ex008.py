# Conversor de medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print(f'A medida de {m} m corresponde a:\n{mm} mm\n{cm} cm\n{dm} dm\n{dam} dam\n{hm} hm\n{km} km')
