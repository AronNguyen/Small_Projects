
public class IndicatorLight {

	private boolean light;//T == on/ F == off
	
	public IndicatorLight() {
		
		light = false;
	}
	
	public void Lightstatus(boolean status) {
		
		light = status;
	}
	
	public boolean getLightStatus() {
		
		return light;
	}
	
	public void setLightStatus(boolean status) {
		
		light = status;
	}
			
}
