
public class HumanTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Human h = new Human();
		h.regulateTemperature();
		h.startSleeping();
		h.goToWork();
		boolean sleeping = h.isSleeping();
		
		if(sleeping) {
			System.out.println("The human is sleeping!");
		}
	}

}
