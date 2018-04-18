package com.allprojects.masterobject;

public class Ninja extends Human{
	protected int stealth = 10;
	public void steal(Human h) {
		h.health -= stealth;
		this.health += h.health;
	}
	public void runAway() {
		this.health -= 10;
	}

}
