package com.allprojects.masterobject;

public class HumanTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Human h = new Human();
		Human h2 = new Human();
		Wizard w = new Wizard();
		Samurai s = new Samurai();
		Ninja n = new Ninja();
		h.displayHealth();
		h.attack(h2);
		h.displayHealth();
		h2.displayHealth();
		System.out.println("........");
		n.steal(w);
		w.displayHealth();
		w.fireball(n);
		n.displayHealth();
		s.deathBlow(n);
		n.displayHealth();
		s.displayHealth();
		w.heal(s);
		s.displayHealth();
		
	}

}
