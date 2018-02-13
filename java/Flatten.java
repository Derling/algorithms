import java.util.Arrays;

/*
 * given a 2d array of integers create one array containing all the elements of every array in it
 * example [[1, 2, 3,4], [5, 6, 7, 8], [9, 10, 11, 12]]
 * output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 */


public class Flatten {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] array = new int[3][4];
		int n = 1;
		for(int i=0; i < array.length; i++) {
			for(int j=0; j< array[i].length; j++) {
				array[i][j] = n;
				n++;
			}
		}
		int[] flatArray = flatten(array);
		System.out.println(Arrays.toString(flatArray));
	}
	
	public static int[] flatten(int[][] a) {
		int[] array = new int[a.length * a[0].length];
		int index = 0;
		for(int[] i: a) {
			for(int j=0; j < i.length; j++) {
				array[index] = i[j];
				index++;
			}
		}
		return array;
	}

}
