import socketio

sio = socketio.Client()


sio = socketio.Client()
isEnd = False
gameID = None


@sio.event
def start(gID):
    global gameID
    gameID = gID
    print('Start game')


@sio.event
def moved(data):
    print(data)


@sio.event
def draw():
    global isEnd
    print('Draw')
    isEnd = True


@sio.event
def win(data):
    global isEnd
    print(data + ' win')
    isEnd = True


sio.connect('http://localhost:80')
sio.emit('search')

while not isEnd:
    if gameID:
        field = input('Choose field:')
        sio.emit('move', {
            'field': field,
            'gameID': gameID
        })
