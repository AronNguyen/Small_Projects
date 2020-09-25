import java.util.*;
public class ProgramPart1 {

	public static void main(String[] args) {
		
		LinkedHashSet<String> test1 = new LinkedHashSet<>();
		LinkedHashSet<String> test2 = new LinkedHashSet<>();
		
		test1.add("London");
		test1.add("Paris");
		test1.add("New York");
		test1.add("Memphis");
		test1.add("San Francisco");
		test1.add("Beijing");
		test1.add("Austin");
		test1.add("Honolulu");
		test1.add("Hong Kong");
		
		test2.add("New York");
		test2.add("Memphis");
		test2.add("Sydney");
		test2.add("Tokyo");
		test2.add("Oslo");
		test2.add("Washington");
		
		Iterator<String> test3 = test1.iterator();
		Iterator<String> test4 = test2.iterator();
		
		LinkedHashSet<String> union = new LinkedHashSet<>();
		LinkedHashSet<String> inter = new LinkedHashSet<>();
		
		
		union.addAll(test1);//union hash
		union.addAll(test2);
		
		while(test3.hasNext()) { //inter hash
			
			if(test2.contains(test3.next())) {
		
				inter.add(test4.next());
				
			}
				
		}
		
		
		System.out.println(union);
		System.out.println(inter);
		union.removeAll(inter);// difference
		System.out.println(union);
	}

}
