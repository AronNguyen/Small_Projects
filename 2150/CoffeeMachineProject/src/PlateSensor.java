
public class PlateSensor{

	private String sensor;

	public PlateSensor() {
		
		//PotEmpty == Empty pot on plate, warmerEmpty nothing on plate, PotNotEmpty == on plate but not empty
		sensor = "PotEmpty";
	}

	public void setPlateSensor(String status) {

		sensor = status;
	}

	public String getPlateStatus() {

		return sensor;
	}

}
