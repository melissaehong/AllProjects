// Deck of Cards Game
function Deck(){
  this.buildDeck();
}

Deck.prototype.buildDeck = function(){
  var values = [ 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']; // 13
  var suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']; //4
  var self = this;

  this.cards = [];

  suits.forEach(function(suit){
    values.forEach(function(value){
      self.cards.push(new Card(value, suit));
    });
  });
  return this;
};

Deck.prototype.shuffle = function(){
  var unshuffledEdge = this.cards.length,
  cardToShuffleIdx,
  temp;

  while (unshuffledEdge > 0){
    cardToShuffleIdx = Math.floor(Math.random() * unshuffledEdge);
    unshuffledEdge -= 1;

    temp = this.cards[cardToShuffleIdx];
    this.cards[cardToShuffleIdx] = this.cards[unshuffledEdge];
    this.cards[unshuffledEdge] = temp;
  }
  return this;
};

/*Deck.prototype.shuffle = function(){
  var unshuffled = this.cards.length, nextCardToShuffle, temp;

  while (unshuffled > 0){
    nextCardToShuffle = Math.floor(Math.random() * unshuffled);
    unshuffled -= 1;

    temp = this.cards[nextCardToShuffle]; // snapshot of just shuffled card
    this.cards[nextCardToShuffle] = this.cards[unshuflled]; // next card to shuffle at end;
    this.cards[unshuffled] = temp; // just shuffled card is now shuffled
  }
}*/

Deck.prototype.reset = function(){
  this.buildDeck().shuffle();
};

Deck.prototype.dealRandomCard = function(){
  return (this.cards.length > 0) ? this.cards.pop() : null;
};

/*Deck.prototype.dealRandomCard = function(){
  if (this.cards.length >0){
    return this.cards.pop();
  }
  else{
    return null;
  }
};*/


function Card (value, suit){
  this.value = value;
  this.suit = suit;
}

//var myDeck = new Deck();
//console.log(myDeck.cards);
//myDeck.shuffle();
//console.log(myDeck.cards);

function Player(name){
  this.name = name;
  this.hand = [];
}

Player.prototype.takeCard = function(deck){
  this.hand.push(deck.dealRandomCard());
  return this;
};

Player.prototype.discard = function(cardIdx){
  if (this.hand.length > cardIdx){
    this.hand.splice(cardIdx, 1);
  }
  return this;
};

var melissa = new Player('melissa');
var deck = new Deck();
deck.shuffle();
console.log(deck);
console.log(melissa);
melissa.takeCard(deck);
console.log(melissa.hand);
console.log(deck);
melissa.discard(0);
console.log(melissa.hand);
