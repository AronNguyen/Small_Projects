import java.util.ArrayList;
public class Test {

	public static void main(String[] args) {
		
		double total = 0;
		ArrayList<Double> condiments = new ArrayList<>();
		condiments.add(0.90);
		condiments.add(1.25);
		
		//CASE 1
		
		//Put pot on warmer
		//Fill boiler with water
		//Put coffee in receptacle
		System.out.println("CASE 1 \n");
		
		coffeeMaker coffee = new coffeeMaker(true, 12, true);
		
		//closes relief valve
		coffee.setReliefValve(true);
		//Turns on Boiler
		coffee.boilerStatus();
		coffee.setStrength("medium");
//		coffee.setReliefValve(false);
		coffee.beginBrew(true);
		
		
		//#######################################################################################################################################################################
		
		//CASE 2
		coffeeMaker coffee2 = new coffeeMaker(true, 12, true);
		
		System.out.println("\nCASE 2 \n");
		
		coffee.setReliefValve(true);
		coffee.beginBrew(true);
		System.out.println("Coffee Brewed");
		System.out.println("Lady lifts pot from coffee maker");
		coffee.setPotStatus("warmerPlate");
		System.out.println("Pot returned to Coffee maker");
		coffee.setPotStatus("PotNotEmpty");
		System.out.println("Lady poured " + coffee.coffeePour(1) + " cup of coffee");
		total += 1.10;
		System.out.println("Current Cost: " + total);
		condiments.add(0.90);
		total += condiments.get(2);
		System.out.println("Current Cost: " + total);
		
		//##########################################################################################
		
		//CASE 3
		
		System.out.println("\nCASE 3 \n");
		coffeeMaker coffee3 = new coffeeMaker(true, 12, true);
		
		coffee.setReliefValve(true);
		System.out.println();
		coffee.beginBrewIntr(true, 6, 2);
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
