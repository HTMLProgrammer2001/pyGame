from Classes.Games.Game import Game


class OfflineGame(Game):
    def clickBoard(self, coords):
        if self.board.click(coords, self.curPlayer):

            if self.board.checkWin():
                self.winner = self.curPlayer
            else:
                self.isDraw = self.board.checkDraw()

            self.curPlayer = 'O' if self.curPlayer == 'X' else 'X'
