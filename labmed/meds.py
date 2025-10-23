
def prepcheck(data):
    def check(data):
        categories = ['antibiotic', 'vitamin', 'vaccine']
        if type(data['name']) != str:
            return False
        if type(data['amount']) != int:
            return False
        if data['category'] not in categories:
            return False
        if type(data['temp']) != float:
            return False
        return True

    def temperature(data):
        if data > 25:
            return 'Надто жарко'
        elif data < 5:
            return 'Надто холодно'
        else:
            return 'Норма'
        

    mcase = {'antibiotic': 'Рецептурний препарат', 'vitamin': 'Вільний продаж', 'vaccine': 'Потребує спецзберігання'}
    for i in data:
        if check(data[i]):
            print(data[i]['name'], '---', temperature(data[i]['temp']), '---', mcase[data[i]['category']])
        else:
            print('Помилка данних')
    
preps = {
    'prep1' : {'name': 'paraceomol', 'amount': 10, 'category': 'antibiotic', 'temp': 1.0},
    'prep2' : {'name': 'pivo', 'amount': 250, 'category': 'vaccine', 'temp': 5.0},
    'prep3' : {'name': 'active coal', 'amount': 2, 'category': 'unknown', 'temp': 45.5}
}


prepcheck(preps)
