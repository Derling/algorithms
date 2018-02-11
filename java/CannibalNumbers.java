import java.util.Arrays;
import java.util.Scanner;

public class CannibalNumbers {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the sacrifices: ");
		int[] integers = createIntArray(in.nextLine().split(" "));
		
		System.out.println("Enter the query: ");
		int query = Integer.parseInt(in.nextLine());
		in.close();
		
		int cannibals = findCannibals(integers.clone(), query);
		System.out.print("With the numbers " + Arrays.toString(integers));
		System.out.print(" there are " + cannibals + " cannibals");
		
	}
	
	public static int findCannibals(int[] a, int q) {
		// sort array to place all possible cannibals at the end of the array
		// and all the numbers that will be consumed at the beginning of the array
		int cannibals = 0;
		Arrays.sort(a);
		int nextSacrifice = 0;
		int nextCannibal = a.length - 1;
		
		// if next number to be eaten is the number that will be doing the eating then there is no one else to eat
		while(nextSacrifice != nextCannibal){
			if(a[nextCannibal] >= q) {
				cannibals++;
				nextCannibal--;
			}
			else {
				a[nextCannibal] += 1;
				nextSacrifice++;
			}
		}
		
		// last number doesn't get evaluated 
		if(a[nextCannibal] >= q) {
			cannibals++;
		}
		
		return cannibals;
	}
	
	public static int[] createIntArray(String[] a) {
		int[] array = new int[a.length];
		for(int i=0; i < a.length; i++) {
			array[i] = Integer.parseInt(a[i]);
		}
		return array;
	}
}
