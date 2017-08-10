var cards = [];
var hand = [];
var card = [];


function Card(rank, suit){
  this.rank = rank;
  this.suit = suit;
}

function Deck(){
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
    console.log(cards);
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
    var temp = cards.pop();
    card.push(temp);
    console.log(card);
    return card;
  };
}

function Player(name){
  this.name = name;

  this.showHand = function(){
    console.log(hand);
  };

  this.take = function(){
    hand.push(card);
  };

  this.discard = function(){
    hand.pop();
  };
}

var myDeck = new Deck();
var Melissa = new Player('Melissa');
myDeck.makeDeck();
myDeck.shuffle();
myDeck.deal();
Melissa.take();
Melissa.showHand();
myDeck.deal();
Melissa.showHand();
