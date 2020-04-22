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
        //find game
        let game = games.find((g) => g.id == data.gameID);

        //no game
        if(!game)
            return;

        if(game.move(socket, data.field)){
            //check win in game
            let winner = game.checkWin();

            if(winner){
                //emit about win
                console.log(`${socket.id} win`);
                game.emitBoth('win', winner);

                //delete game
                games.splice(games.findIndex(
                    (e) => e.id == game.id
                ), 1);
            }
            else if(game.checkDraw()){
                //draw
                console.log(`Draw`);
                game.emitBoth('draw');

                //delete game
                games.splice(games.findIndex(
                    (e) => e.id == game.id
                ), 1);
            }
        }
    });

    socket.on('disconnect', () => {
        // if it's wait client than remove him
        if(waitClient && waitClient.id == socket.id)
            waitClient = null;

        //if player was in game than emit to other player
        game = games.find((e) =>
            e.player1.id == socket.id || e.player2.id == socket.id);

        if(game)
            game.emitBoth('quit');

        console.log(`${socket.id} disconnect`);
    });
})