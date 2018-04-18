package com.allprojects.masterobject;

public class Samurai extends Human{
	private int health = 200;
	private static int counter;
	
	public Samurai(){
		this.health = 200;
		counter++;
	}
	
	public void deathBlow(Human h){
		health = health/2;
		h.health = 0;
	}

	public void meditate() {
		health = health + health/2;
	}
	
	public static void howMany() {
		System.out.println("Number of Samurai: " + counter);
	}
}
