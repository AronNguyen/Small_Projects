
public class waterSensor {

	private boolean hasWater;
	private int waterLvl;

	public waterSensor() {

		hasWater = false;
		waterLvl = 0;
	}
	
	public waterSensor(Boolean hasWater, int waterLvl) {
		
		this.hasWater = hasWater;
		this.waterLvl = waterLvl;
	}

	public void setWater(int cupsOfWater) {

		waterLvl = cupsOfWater;
		
		if (cupsOfWater > 12) {
			System.out.println("Please pour no more than 12 cups of water");
			System.out.println("Water Level: " + waterLvl);

		} else {
			
			hasWater = true;
		}

	}
	
	public int getWater() {
		
		return waterLvl;
	}

	public void isEmpty() {

		if (waterLvl == 0) {
			
			System.out.println("Empty");
		} else {
			
			System.out.println("Boiler has " + waterLvl + " cups of water");
		}
	}

	public boolean readyToGo() {

		if (hasWater && waterLvl <= 12 && waterLvl > 0) {

			return true;
		}

		return false;
	}

}
