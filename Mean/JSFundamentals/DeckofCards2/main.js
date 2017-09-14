/*Create a Deck object constructor. A deck should have the following functionality:

The Deck should contain the 52 standard cards
The Deck should be able to shuffle
The Deck should be able to reset
The Deck should be able to deal a random card
Deal should return the card that was dealt and remove it from the deck
Now create a Player object constructor. A Player should have the following functionality:

The Player should have a name
The Player should have a hand
The Player should be able to take a card (use the deck.deal method)
The Player should be able to discard a card
Optional:

Create a blackjack game with your deck of cards!
A deck of card image set can be found here

Or Unicode them Unicode for card images!*/
function Card(rank, suit){
  this.rank = rank;
  this.suit = suit;
}

function Deck(){
  var deck = makeDeck();

  this.viewDeck = function(){
    console.log(deck);
  };

  function makeDeck(){
    var ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K'],
    suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs'];
    deckReturn = [];

    suits.forEach(function(suit){
      ranks.forEach(function(rank){
        deckReturn.push(new Card(rank,suit));
      });
    });
    return deckReturn;
  }

  this.shuffle = function(array){
    var shuffledcards = array.length, temp, index;
    while (shuffledcards){
      index = Math.floor(Math.random()*shuffledcards--);
      temp = array[shuffledcards];
      array[shuffledcards] = array[index];
      array[index] = temp;
    }
    return array;
  };

}
var newDeck = new Deck();

newDeck.viewDeck();
/*  this.shuffle = function(){
    var m = array.length, t, i;
    while (m){
      i = Math.floor(Math.random()*m--);
      t = array[m];
      array[m] = array[i];
      array[i] = t;
    }
    return array;
  };
  this.reset = function(){
    this.pop(Deck);
  };
  this.deal = function(){
    remove cardfromdeck;
    return card;
  };
}

function Player(){
  this.name = name;
  this.hand = hand;
  this.take = function(){
    deck.deal;
  };
  this.discard = function(){
    discard;
  };
}*/
