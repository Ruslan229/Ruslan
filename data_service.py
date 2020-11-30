def get_dovidnik():
    with open("./data/dovidnik.txt", encoding='utf-8') as dovidnik_file:
        from_dovidnik = dovidnik_file.readlines()

    dovidnik_list = [] 

    for line in from_dovidnik:
        line_list = line.split(';')
        dovidnik_list.append(line_list)
      
      
    return dovidnik_list

def get_tovaroobig():
    with open("./data/tovaroobig.txt", encoding='utf-8') as tovaroobig_file:
        from_tovaroobig = tovaroobig_file.readlines()

    tovaroobig_list = [] 

    for line in from_tovaroobig:
        line_list = line.split(';')
        tovaroobig_list.append(line_list)
      
    return tovaroobig_list

def show_dovidnik(dovidnik):
    dovidnik_code_from = input("Який код товарної групи?")
    dovidnik_code_to = input("До якого коду товарної групи?")

    kol_lines = 0

    for cod in dovidnik:
        if dovidnik_code_from <= cod[0] <= dovidnik_code_to:
            print("Код: {:10} Назва:{:50} Торгова скидка:{:6}".format(cod[0], cod[1], cod[2].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(dovidnik_code_from, dovidnik_code_to))

def show_tovaroobig(tovaroobig):
    tovaroobig_code_from = input("З якого коду товарної групи?")
    tovaroobig_code_to = input("По який код товарної групи?")

    kol_lines = 0

    for cod in tovaroobig:
        if tovaroobig_code_from <= cod[0] <= tovaroobig_code_to:
            print("Код:{:10} План:{:7} Очікуємо виконання:{:6} Рік:{:10}".format(cod[0], cod[1], cod[2], cod[3].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(tovaroobig_code_from, tovaroobig_code_to))

 

