
public class coffeeMaker {

	private boolean hasCoffee;
	private int coffeeLvl;
	private boolean receptacle;// T == Filled/ F == Empty

	Boiler boiler = new Boiler();
	sprayControl spray = new sprayControl();
	ReliefValve valve = new ReliefValve();
	BrewButton button = new BrewButton();
	WarmerPlate plate = new WarmerPlate();

	public coffeeMaker() {

		hasCoffee = false;
		coffeeLvl = 0;
		receptacle = false;
	}

	public coffeeMaker(boolean potOnWarmer, int cupsOfWater, boolean receptacle) {

		hasCoffee = false;
		coffeeLvl = 0;

		System.out.println("Pot on Warmer Plate");
		plate.setWarmerStatus("PotEmpty");
		System.out.println("Added " + cupsOfWater + " cups of water");
		boiler.addWater(cupsOfWater);
		if (receptacle) {
			System.out.println("Coffee added to receptacle");
			this.receptacle = receptacle;
		} else {
			System.out.println("Coffee Not added");
			this.receptacle = receptacle;
		}
		System.out.println("Select coffee strength(light, medium, strong): medium is default");
		System.out.println("Press Brew");

	}

	public void setReliefValve(boolean status) {

		valve.setValveStatus(status);
	}

	public void setStrength(String strength) {

		spray.setStrength(strength);
		System.out.println("Coffee strength: " + strength);
	}

	public void beginBrew(boolean pushed) {

		if (valve.getValveStatus()) {
			System.out.println("Relief valve closed");
			button.Brew(pushed);
			coffeeLvl = boiler.getWater();
			System.out.println("Coffee made: " + coffeeLvl + " cups");
			valve.setValveStatus(false);
			System.out.println("Relief valve opened");
		} else {
			System.out.println("Please close the relief valve inorder to brew");
		}

	}
	
	public void beginBrewIntr(boolean pushed, int whenTakenOff, int amountPoured) {
//		if(valve.getValveStatus()) {
//			System.out.println("Relief valve closed");
//			button.BrewIntr(pushed);
//		}
		for(int i = 1; i <= boiler.getWater(); i++) {
			
			System.out.println("Coffee Made: " + i + " cups");
			if(i == whenTakenOff) {
				setPotStatus("warmerEmpty");
				boiler.setHeater(false);
				System.out.println("Boiler Off");
				setReliefValve(false);
				System.out.println("Relief Valve Open");
				if(button.isLightOn()) {
					button.setLight(false);
				}
				System.out.println("Lady poured " + coffeePour(amountPoured) + " cups of coffee");
				i += amountPoured;
				System.out.println("Lady returns coffee pot back");
				if(coffeeLvl == 0) {
					
					setPotStatus("PotEmpty");
				}else {
					
					setPotStatus("PotNotEmpty");
				}
				boiler.setHeater(true);
				System.out.println("Boiler On");
				plate.getWarmerStatus();
				valve.setValveStatus(true);
				System.out.println("Relief valve closed");
				
				
			}
		}
	}
	
	public int coffeePour(int i) {
		
		if(i > coffeeLvl) {
			coffeeLvl = 0;
			System.out.println("Coffee remaining: " + coffeeLvl + " cups");
			return i;
		}
		
		coffeeLvl -= i;
		System.out.println("Coffee remaining: " + coffeeLvl + " cups");
		return i;
	}

	public void setPotStatus(String status) {

		plate.setWarmerStatus(status);
		if(!plate.getWarmerStatus()) {
			
			button.setLight(false);
			System.out.println("Light off");
		}else {
			
		}

	}

	public boolean light() {

		if (button.isLightOn()) {

			return true;
		}
		return false;
	}

	public void boilerStatus() {

		if (boiler.isBoiling()) {
			System.out.println("\nBoiler is on");
			System.out.println("Water is boiled");
			boiler.setHeater(false);
			System.out.println("Boiler is off");
		} else {
			System.out.println("Boiler is off");
		}
	}

}
