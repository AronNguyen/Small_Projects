
public class Movie extends Media {
	
	Movie(String x){
		
		this.genre = FindGenre(x);
		this.rating = FindRating(x);
		this.year = FindYear(x);
		
	}

	
	public String FindGenre(String x) {
		
		String temp = x.substring(x.lastIndexOf(','), x.length());
		
		return temp;
	}


	public int FindYear(String x) {
		// TODO Auto-generated method stub
		return 0;
	}


	
	public String FindTitle(String x) {
		// TODO Auto-generated method stub
		return null;
	}


	
	public String FindRating(String x) {
		// TODO Auto-generated method stub
		return null;
	}

}
