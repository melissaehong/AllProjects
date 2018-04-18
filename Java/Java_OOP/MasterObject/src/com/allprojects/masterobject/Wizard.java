package com.allprojects.masterobject;

public class Wizard extends Human{
	public Wizard() {
		this.health = 50;
		this.intelligence = 8;
	}
	public void heal(Human h) {
		h.health += intelligence;
	}
	
	public void fireball(Human h) {
		h.health -= (intelligence*3);
	}
}
