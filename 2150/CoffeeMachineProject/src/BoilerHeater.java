
public class BoilerHeater{

	private boolean heaterStatus;//T == on/ F== off

	public BoilerHeater() {

		heaterStatus = false;
	}

	public void setHeaterStatus(boolean status) {
		
		heaterStatus = status;
	}

	public boolean getHeaterStatus() {

		return heaterStatus;
	}

}
