
public class Mammal {
	protected int energyLevel = 100;
	public Mammal(){
	}
	
	public void setLevel(int energyLevel) {
		this.energyLevel = energyLevel;
	}
	
	public int getEnergy() {
		return energyLevel;
	}
	
	public int displayEnergy() {
		System.out.println("Energy level: " + getEnergy());
		return energyLevel;
	}
}
