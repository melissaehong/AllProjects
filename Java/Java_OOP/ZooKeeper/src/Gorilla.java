
public class Gorilla extends Mammal {
	public Gorilla() {
	}
	
	public void throwSomething() {
		energyLevel -= 5;
		System.out.println("Gorilla threw a banana!");
	}
	
	public void eatBananas() {
		energyLevel += 5;
		System.out.println("Gorilla ate some bananas");
	}
	
	public void climb() {
		energyLevel -= 5;
		System.out.println("Gorilla climbed a tree");
	}
	
}
