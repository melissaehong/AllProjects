package com.allprojects.masterobject;

public class Human {
	protected int strength = 3;
	protected int stealth = 3;
	protected int intelligence = 3;
	protected int health = 100;
	
	public void displayHealth() {
		System.out.println("Health: " + health);
	}
	
	public void attack(Human h) {
		h.health -= strength;
	}
	
}
