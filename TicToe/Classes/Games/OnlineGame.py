import socketio

from Classes.Games.Game import Game


class OnlineGame(Game):
    def __init__(self):
        Game.__init__(self)

        self.sio = socketio.Client()
        self.sio.connect('http://localhost:80')

        self.gameID = None
        self.sio.on('start', self.start)
        self.sio.on('moved', self.moved)
        self.sio.on('win', self.win)
        self.sio.on('draw', self.draw)
        self.sio.on('quit', self.enemyLeave)

    def moved(self, data):
        self.board.syncRects(data['fields'])
        self.curPlayer = 'X' if data['player'] == 'X' else 'O'

    def start(self, gameID):
        self.gameID = gameID

    def draw(self, *args):
        self.isDraw = True

    def win(self, winner):
        self.winner = winner

    def enemyLeave(self, *args):
        self.msg = 'Enemy leave game'
        self.isDraw = True

    def search(self):
        self.sio.emit('search')

    def clickBoard(self, coords):
        field = self.board.getRect(coords)

        if field is not None:
            self.sio.emit('move', {
                'field': field,
                'gameID': self.gameID
            })

    def draw(self, sc):
        if not self.gameID:
            self.showMessage(sc, 'Search enemy'.upper(), fill=True)
        else:
            super().draw(sc)

    def quit(self):
        self.sio.disconnect()
