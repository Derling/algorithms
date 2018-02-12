import java.util.HashMap;
import java.util.Scanner;

public class WordCount {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the words: ");
		String[] words = in.nextLine().split(" ");
		in.close();
		
		HashMap<String, Integer> count = wordCount(words);
		
		System.out.println(count.toString());
	}
	
	public static HashMap<String, Integer> wordCount(String[] words) {
		HashMap<String, Integer> count = new HashMap<String, Integer>();
		for(String str: words) {
			if(count.containsKey(str)) {
				count.put(str, count.get(str) + 1);
			}
			else {
				count.put(str, 1);
			}
		}
		return count;
	}

}
