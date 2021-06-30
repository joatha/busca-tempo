import requests

#cidade = input('Digite o nome da cidade')
#estado = input('Digite a siga do estado')

print('------------BEM-VINDO AO APP BUSCA-TEMPO 1.0------------\n')
r = 'S'
while r == 'S':
    nome_cidade = input('\nDigite o nome da cidade: ')
    nome_estado = input('\nAgora digite a sigla do estado Ex.CE: ')
    print()
   
    busca = requests.get(f'https://api.hgbrasil.com/weather?key=1253b0bd&city_name={nome_cidade},{nome_estado}')

#busca = requests.get('https://api.hgbrasil.com/weather?key=1253b0bd&city_name=massape,ce')

    resultado = busca.json()

    resultado2 = resultado.get('results')
    cidade = resultado2.get('city')
    data = resultado2.get('date')
    temperatura = resultado2.get('temp')

    print('--------------RESULTADO------------------')
    print('Hoje:', data)
    print('-----------------------------------------')
    print('Na cidade de:', cidade)
    print('-----------------------------------------')
    print('Fazem:',temperatura,'Graus\n')

    print('------FINAL DA CONSULTA------------------\n')

    r = str(input('Quer continuar? [S/N]')).upper()
    






