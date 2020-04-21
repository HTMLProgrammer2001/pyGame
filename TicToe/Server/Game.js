class Game{
    constructor(player1, player2){
        this.id = +new Date();

        this.player1 = player1;
        this.player2 = player2;

        //current player
        this.curPlayer = 'O';

        //emit start event to users
        this.emitBoth('start', this.id);

        this.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    move(player, field){
        //incorrect field
        if(field < 0 || field > 8)
           return;

        //check if field is busy
        if(this.board[field])
            return;

        //check correct user check
        if(player.id == this.player1.id && this.curPlayer == 'O'){
            this.board[field] = 'O';
            this.curPlayer = 'X';
        }
        else if(player.id == this.player2.id && this.curPlayer == 'X'){
            this.board[field] = 'X';
            this.curPlayer = 'O';
        }

        this.emitBoth('moved', this.board);

        return true;
    }

    checkWin(){
        //rules of win
        let checks = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];

        for(let [a,b,c] of checks)
            if(this.board[a] && this.board[a] == this.board[b] && this.board[b] == this.board[c])
                return this.board[a];
    }

    checkDraw(){
        if(!this.checkWin())
            if(this.board.every(field => !!field))
                return true;
    }

    emitBoth(event, data){
        this.player1.emit(event, data);
        this.player2.emit(event, data);
    }
}

module.exports = Game