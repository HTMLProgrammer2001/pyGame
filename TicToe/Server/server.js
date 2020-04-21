const io = require('socket.io')(80);

const Game = require('./Game');

let clients = [],
    waitClient = null,
    games = [];

io.on('connection', (socket) => {
    //add to clients
    clients.push(socket);
    console.log(`A ${socket.id} connected`);

    socket.on('search', () => {
        //if server has not free client than this client will wait
        if(!waitClient){
            console.log('Wait');
            waitClient = socket;
            waitClient.emit('wait');
        }
        else{
            //create game
            games.push(new Game(socket, waitClient));

            waitClient = null;
        }
    });

    socket.on('move', (data) => {
        let game = games.find((g) => g.id == data.gameID);

        if(!game)
            return;

        if(game.move(socket, data.field)){
            let winner = game.checkWin();

            if(winner){
                console.log(`${socket.id} win`);
                game.emitBoth('win', winner);

                games.splice(games.findIndex(
                    (e) => e.id == game.id
                ), 1);
            }
            else if(game.checkDraw()){
                console.log(`Draw`);
                game.emitBoth('draw');

                games.splice(games.findIndex(
                    (e) => e.id == game.id
                ), 1);
            }
        }
    });

    socket.on('disconnect', () => {
        console.log(`${socket.id} disconnect`);
    });
})