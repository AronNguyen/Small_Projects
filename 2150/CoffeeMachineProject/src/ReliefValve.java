
public class ReliefValve{

	private boolean valveStatus;// True for close / False for open

	public ReliefValve() {

		valveStatus = false;
	}

	public void setValveStatus(boolean status) {

		valveStatus = status;
	}

	public boolean getValveStatus() {

		return valveStatus;
	}

}
