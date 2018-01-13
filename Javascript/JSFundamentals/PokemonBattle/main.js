var game = {
  players : [],
  deck : [],
  addPlayer : function(){}
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
//example:
game.addPlayer(playerConstructor('Joe'));
game.addPlayer(playerConstructor('Sarah'));
console.log(game);
// reminder of how to get things using jquery and AJAX!
$(document).ready(function(){
  $.get("http://pokeapi.co/api/v1/pokemon/1/", function(res) {
    console.log(res);
    var html_str = "";
    html_str += "<h4>Types</h4>";
    html_str += "<ul>";
    for(var i = 0; i < res.types.length; i++) {
       html_str += "<li>" + res.types[i].name + "</li>";
    }
    html_str += "</ul>";
    $("#bulbasaur").html(html_str);
  }, "json");
});
