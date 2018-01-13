var GAMEOVER = false;

function Card(type, number) {
	if (type === 1) {
		this.type = 's';
	}
	else if (type === 2) {
		this.type = 'h';
	}
	else if (type === 3) {
		this.type = 'c';
	}
	else if (type === 4) {
		this.type = 'd';
	}

	this.number = number;
	this.next = null;
}

function Deck() {
	function loadDeck() {
		var deck = [];
		for (var i = 1; i < 5; i++) {
			for (var j = 1; j < 14; j++) {
				deck.push(new Card(i, j));
			}
		}
		return deck;
	}

	this.createLinkedList = function(deck) {
		while (deck.length > 0) {
			var number = Math.floor(Math.random()*deck.length);
			if (!this.head) {
				this.head = deck[number];
			}
			else {
				var current = this.head;
				while (current.next) {
					current = current.next;
				}
				current.next = deck[number];
			}
			deck.splice(number, 1);
		}
	}

	this.reset = function() {
		var newDeck = loadDeck();
		this.head = null;
		this.createLinkedList(newDeck);
		return this;
	}

	this.shuffle = function() {
		var remainingDeck = [];
		var current = this.head
		while (current) {
			remainingDeck.push(current);
			current = current.next;
		}
		for (var i = 0; i < remainingDeck.length; i++) {
			remainingDeck[i].next = null;
		}
		this.head = null;
		this.createLinkedList(remainingDeck);
		return this;
	}

	this.deal = function() {
		if (this.head.next) {
			var current = this.head;
			this.head = this.head.next;
			return current;
		}
		return 'NO MORE CARDS.';
	}

	this.head = null;
	this.ordered = loadDeck();
	this.createLinkedList(this.ordered);
}

function Player(name, deck) {
	this.name = name;
	this.hand = [];
	this.score = 0;

	this.takeCard = function() {
		var card = deck.deal();
		if (typeof(card) === 'object') {
			this.hand.push(card);
		}
		else {
			console.log('no more cards.');
		}
	}
	this.discardHand = function() {
		this.hand = [];
	}
	this.updateScore = function() {
		this.score = 0;
		var hasAce = [];
		for (var i = 0; i < this.hand.length; i++) {
			if (this.hand[i].number === 1) {
				this.score += 11;
				hasAce.push(true);
			}
			else if (this.hand[i].number === 11 || this.hand[i].number === 12 || this.hand[i].number === 13) {
				this.score += 10;
			}
			else {
				this.score += this.hand[i].number;
			}

		}
		for (var i = 0; i < hasAce.length; i++) {
			if (this.score > 21 && hasAce.length !== 0) {
				this.score -= 10;
				hasAce.pop();
			}
		}
		return this.score;
	}
	this.winCondition = function(opponent) {
		if (this.score === 21) {
			GAMEOVER = true;
			fadeOutText(this.name + ' has BLACKJACK!');
			return this;
		}
		else if (this.score > 21) {
			GAMEOVER = true;
			fadeOutText(this.name + ' has busted...');
			return this;
		}
		if (typeof(opponent) === 'object') {
			if (this.score > opponent.score && this.score < 21) {
				fadeOutText(this.name + ' wins!');
			}
			else if (this.score < opponent.score && opponent.score < 21) {
				fadeOutText(opponent.name + ' wins!');
			}
			else {
				fadeOutText('Push!');
			}
			GAMEOVER = true;
			return this;
		}
	}
}

var myDeck = new Deck;
var Melissa = new Player;
myDeck.createLinkedList();
