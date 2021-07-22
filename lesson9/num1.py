class TrafficLight:
    __color = ['red', 'yellow', 'green']


def running(i):
    if i < 7:
        sost = 'Red'
        print(f'На данный момент на светофоре горит: {sost}')
    elif 7 <= i < 9:
        sost = 'Yellow'
        print(f'На данный момент на светофоре горит: {sost}')
    else:
        sost = 'Green'
        print(f'На данный момент на светофоре горит: {sost}')



a = TrafficLight()
running(7)

