import java.util.ArrayList;

/*
 * There are people sitting in a circular fashion,
 * print every third member while removing them,
 * the next counter starts immediately after the member is removed.
 * Print till all the members are exhausted.
 * For example:
 * Input: consider 12456789 members sitting in a circular fashion,
 * Output: 372854619
 */

public class CircularCounter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Character> list = new ArrayList<Character>();
		for(char c: "123456789".toCharArray()) {
			list.add(c);
		}
		String countedResult = circularCounter(list, 3);
		System.out.println(countedResult);
	}
	
	public static String circularCounter(ArrayList<Character> list, int step) {
		StringBuilder builder = new StringBuilder();
		System.out.println(list.toString());
		int chr = -1;
		while(list.size() != 0) {
			System.out.println(chr + list.toString());
			chr = (chr + step) % list.size();
			builder.append(list.get(chr));
			list.remove(chr);
		}
		return builder.toString();
	}
}
