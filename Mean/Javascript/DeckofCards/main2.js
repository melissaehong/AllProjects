function Card(rank, suit){
  this.rank = rank;
  this.suit = suit;
}

function Deck(){
  var cards = [];
  this.makeDeck = function(){
    var ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'],
    suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs'];
      for (var j = 0; j < suits.length; j++){
        for (var k = 0; k < ranks.length; k++){
            cards.push(new Card(ranks[k], suits[j]));
          }
        }
    return cards;
  };

  this.showDeck = function(){
    return(cards);
  };

  this.shuffle = function(){
    var unshuffledEdge = cards.length, cardsIdx, temp;
    while (unshuffledEdge > 0){
      cardsIdx = Math.floor(Math.random()*unshuffledEdge);
      unshuffledEdge--;
      temp = cards[cardsIdx];
      cards[cardsIdx] = cards[unshuffledEdge];
      cards[unshuffledEdge] = temp;
    }
    return cards;
  };

  this.reset = function(){
    cards = this.makeDeck();
    return this;
  };

  this.deal = function(){
    return cards.pop();
  };
  this.makeDeck();
}

function Player(name){
  this.name = name;
  var hand = [];

  this.showHand = function(){
    console.log(hand);
  };

  this.take = function(deck){
    var playerCard = deck.deal();
    hand.push(playerCard);
  };

  this.discard = function(){
    hand.pop();
  };
}

function Game(){
  this.deck = new Deck();
  this.players = [];
  this.addPlayer = function(player){
    this.players.push(player);
  };
}

var game = new Game();
var myDeck = new Deck();
var Melissa = new Player('Melissa', myDeck);
var gideon = new Player('Gideon', myDeck);
myDeck.makeDeck();
myDeck.shuffle();
myDeck.deal();
Melissa.take(myDeck);
Melissa.showHand();
myDeck.deal(myDeck);
Melissa.take(myDeck);
Melissa.showHand();
Melissa.discard();
Melissa.showHand();
game.addPlayer(gideon);
