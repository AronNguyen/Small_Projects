
public abstract class Media {

	String rating;
	String genre;
	String Title;
	
	int year;
	
	public abstract String FindGenre(String x);
	public abstract int FindYear(String x);
	public abstract String FindTitle(String x);
	public abstract String FindRating(String x);
	
}
