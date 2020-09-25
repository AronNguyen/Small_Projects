
public class BrewButton {

	private boolean startBrew;// True == start brewing
								// False == stop brewing
	IndicatorLight light = new IndicatorLight();

	public BrewButton() {

		startBrew = false;
	}

	public void Brew(boolean status) {

		startBrew = status;
		light.Lightstatus(!status);
		if (status) {
			System.out.println("Brew Starting" + "\nLight off");
			System.out.println("Brew Finished \nLight On");
			startBrew = false;
			light.Lightstatus(status);
		}
	}

	public void BrewIntr(boolean status) {

		startBrew = status;
		light.Lightstatus(!status);

		System.out.println("Brew Starting \nLight off");
		System.out.println("Brew Finished \nLight On");
		light.Lightstatus(status);

	}

	public void setLight(boolean status) {

		light.setLightStatus(status);
	}

	public boolean isLightOn() {

		return light.getLightStatus();
	}

}
