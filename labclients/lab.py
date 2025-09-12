
def clients(data):
    def check(data):
        if type(data['sum']) != int:
            return False
        return True

    def dealsum(data):
        if data['sum'] < 100:
            return 'Дрібнота'
        elif data['sum'] > 999:
            return 'Великий кліент'
        else:
            return 'Середнячок'
    
    def clientstatus(data):
        statuses = {
            'clean': 'Працювати без питань',
            'suspicious': 'Перевірити документи',
            'fraud': 'Чорний список',
        }
        if data['status'] in statuses:
            return statuses[data['status']]
        else:
            return 'Невідомий статус'
    
    for i in data:
        if check(data[i]):
            print([data[i]['name'], dealsum(data[i]), clientstatus(data[i])])
            #print(data[i]['name'], '---', dealsum(data[i]), '---', clientstatus(data[i]))



clientslist = {
    'client1' : {'name': 'Andrew', 'sum': 10, 'status': 'clean'},
    'client2' : {'name': 'Who', 'sum': 250, 'status': 'suspicious'},
    'client3' : {'name': 'Mark', 'sum' : 2, 'status': 'fraud'}
}

clients(clientslist)