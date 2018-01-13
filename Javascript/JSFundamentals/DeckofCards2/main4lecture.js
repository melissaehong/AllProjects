
function Card(suit, value){
  this.suit = suit;
  this.value = value;
}

function Deck(){
  this.reset = function(){
    this.cards = createDeck();
    return this;
  };

  this.showDeck = function(){
    console.log(this.deck);
  };

  this.createDeck = function(){
    var values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'],
    suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs'];
    this.deck = [];
      for (var j = 0; j < suits.length; j++){
        for (var k = 0; k < values.length; k++){
            this.deck.push(new Card(values[k], suits[j]));
          }
        }
    return this.deck;
  };

  this.showDeck= function(){
    console.log(this.deck);
  };

  this.deal = function(){
    return this.deck.pop();
  };
}

  Deck.prototype.shuffle = function(){
    var unshuffledEdge = this.deck.length, cardToShuffle, temp;
    while(unshuffledEdge > 0){
    cardToShuffle = Math.floor(Math.random()*unshuffledEdge);
    unshuffledEdge--;
    temp = this.deck[cardToShuffle];
    this.deck[cardToShuffle] = this.deck[unshuffledEdge];
    this.deck[unshuffledEdge] = temp;
    }
    return this.deck;
  };



var myDeck = new Deck();
myDeck.createDeck();
myDeck.showDeck();
myDeck.shuffle();
myDeck.showDeck();
myDeck.deal();
myDeck.showDeck();
