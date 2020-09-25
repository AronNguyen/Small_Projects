import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class lll {

	public static void main(String[] args) throws FileNotFoundException {
		
		File file = new File("NetFlixShows.txt");
		System.out.println(file.canRead());
		
		Scanner input = new Scanner(new FileReader(file));
		
		ArrayList<Media> Master = new ArrayList<>();
		
		
		
		while(input.hasNext()) {
			
			String test = input.next();
			
			Master.add(new Movie(test));
			//System.out.println(Master.size());
			
		}
		
		for(int i = 0; i < Master.size(); i++) {
			System.out.println(Master.get(i));
		}
		
		
		
		
		
	}
}
