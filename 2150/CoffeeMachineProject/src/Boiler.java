
public class Boiler {

	private boolean boiledWater;
	BoilerHeater heater = new BoilerHeater();
	waterSensor sensor = new waterSensor();
	
	public Boiler() {
		
		boiledWater = false;
	}

	public void addWater(int cupsOfWater) {

		sensor.setWater(cupsOfWater);
	}
	
	public int getWater() {
		
		return sensor.getWater();
	}
	
	public void setHeater(boolean status) {
		
		heater.setHeaterStatus(status);
	}

	public boolean isBoiling() {

		if (sensor.readyToGo()) {

			heater.setHeaterStatus(sensor.readyToGo());
			boiledWater = true;
			return boiledWater;

		} else {

			heater.setHeaterStatus(sensor.readyToGo());
			boiledWater = false;
			return boiledWater;
		}
	}

}
