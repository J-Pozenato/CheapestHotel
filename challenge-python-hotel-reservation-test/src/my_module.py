import csv
import sys

# cria a lista de hoteis
hotels = []

# imaginei que seria melhor ter uma database, assim caso no futuro for adicionado mais hoteis fica facil de escalar o projeto
with open("database.csv") as csvf:
    reader = csv.DictReader(csvf)
    
    # transforma todos os numeros em int e adiciona o hotel na lista
    for hotel in reader:
        hotel['Rating'] = int(hotel['Rating'])
        hotel['PriceND'] = int(hotel['PriceND'])
        hotel['PriceRD'] = int(hotel['PriceRD'])
        hotel['PriceNE'] = int(hotel['PriceNE'])
        hotel['PriceRE'] = int(hotel['PriceRE'])
        hotels.append(hotel)

# Se for rodado pelo terminal como "python my_module.py "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"" ativa a parte de rodando pelo terminal
# não pode esquecer das "" na string para que o terminal não use nenhuma das palavras como algum comando, aconteceu comigo algumas vezes, principalmente com o "mon" ;D
cmdo = False
if len(sys.argv) > 1:
    cmdo = True

if cmdo:
    text = sys.argv[1]

    print(text)



def get_cheapest_hotel(number):   #DO NOT change the function's name

    # descobre se o usuario é Regular ou faz parte do programa de fidelidade
    if number[0:7] == "Regular":
        keyD = "PriceND"
        keyE = "PriceNE"
        #return "regular"
    elif number[0:7] == "Rewards":
        keyD = "PriceRD"
        keyE = "PriceRE"
        #return "rewards"
    else:
        return "Input invalido\nForma certa: <tipo_do_cliente>: <data1>, <data2>, <data3>, ..."

    # conta o 
    days = 1 + number.count(',')
    dates = number[9: len(number)]
    daysW = []

    for i in range(days):
        # print(dates)
        daysW.append(dates[dates.find('(') + 1: dates.find(')')])
        if i != days:
            dates = dates[dates.find(',') + 1: len(dates)]
    # print(daysW)

    # loop que encontra o hotel mais barato na lista hotels
    cheapest = 0
    for hotel in hotels:
        count = 0
        # para cada dia dos solicitados aumentar o custo
        for day in daysW:
            # checa se o dia é no final de semana
            if day == "sat" or day == "sun":
                count += hotel[keyE]
            else:
                count += hotel[keyD]
        # print(hotel['Name'])
        # print(count)

        # Checa se a opção calculada é a mais barata e atualiza o cheapest_hotel se for verdade
        if count < cheapest or cheapest == 0:
            cheapest = count
            cheapest_hotel = hotel
        # em caso de empate usa o rating do hotel para escolher o com melhor rating
        elif count == cheapest:
            if hotel['Rating'] > cheapest_hotel['Rating']:
                cheapest = count
                cheapest_hotel = hotel

    # teste pra entender melhor como funciona o py.test
    # if number == "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)":
    #     return "massa"

    
    return cheapest_hotel['Name']

if cmdo:
    print(get_cheapest_hotel(text))

