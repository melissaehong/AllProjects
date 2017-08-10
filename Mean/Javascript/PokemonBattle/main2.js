var game = {
  players: [],
  addPlayer: function(name){
    game.players.push(name);
    return players;
  }
};
function playerConstructor(name){
  player = {};
  player.name = name;
    player.hand = [];
  player.addCard = function(card){
    player.hand.push(card);
  };
  return player;
}
