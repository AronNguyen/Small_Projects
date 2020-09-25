
public class WarmerPlate {

	private boolean plateStatus;// True == on/ False == off

	PlateSensor pSensor = new PlateSensor();
	PlateHeater pHeater = new PlateHeater();

	public WarmerPlate() {

		plateStatus = false;

	}

	public boolean getWarmerStatus() {

		return plateStatus;

	}

	public void setWarmerStatus(String sensor) {

		if (sensor == "PotNotEmpty") {
			pHeater.setPlateHeater(true);
			System.out.println("Plate Heater On");
			plateStatus = pHeater.getPlateHeaterStatus();
		} else if (sensor == "PotEmpty") {
			pHeater.setPlateHeater(false);
			plateStatus = pHeater.getPlateHeaterStatus();
			System.out.println("Empty Pot on Warmer Plate off");
		} else {

			plateStatus = pHeater.getPlateHeaterStatus();
			System.out.println("Pot off Warmer Plate");
			pHeater.setPlateHeater(false);
			System.out.println("Plater heater off");
		}

	}

}
