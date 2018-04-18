
public class Dragon extends Mammal{
	public Dragon() {
		this.energyLevel = 300;
	}
	
	public void fly() {
		System.out.println("Swoooosh!");
		energyLevel -= 50;
	}
	
	public void eatHumans() {
		energyLevel += 25;
	}
	
	public void attackTown() {
		System.out.println("Fire! Burn!");
		energyLevel -= 100;
	}
}
