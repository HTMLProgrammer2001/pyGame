import socketio

from Classes.Games.Game import Game

sio = socketio.Client()
sio.connect('http://localhost:80')


class OnlineGame(Game):
    def __init__(self):
        Game.__init__(self)

        self.gameID = None
        sio.on('start', self.start)
        sio.on('moved', self.moved)
        sio.on('win', self.win)

    def moved(self, data):
        print(data)

        self.board.syncRects(data)

    def start(self, gameID):
        print(gameID)
        self.gameID = gameID

    def win(self, winner):
        self.winner = winner

    @staticmethod
    def search():
        print('Search')
        sio.emit('search')

    def clickBoard(self, coords):
        field = self.board.getRect(coords)

        print(field)

        if field is not None:
            sio.emit('move', {
                'field': field,
                'gameID': self.gameID
            })

    def quit(self):
        sio.disconnect()
