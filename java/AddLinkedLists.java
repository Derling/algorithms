import java.util.ArrayList;
import java.util.Collections;
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

public class AddLinkedLists {
	public int value;
	private AddLinkedLists next;
		
	public AddLinkedLists(int value) {
		this.value = value;
	}

	public int getValue() {
		return this.value;
	}
		
	public AddLinkedLists getNext() {
		return this.next;
	}
		
	public void setNext(AddLinkedLists node) {
		this.next = node;
	}
	
	public boolean hasNext() {
		return this.next != null;
	}
	
	public static void main(String[] args) {
		// create first list 2 -> 4 -> 3 which represents the number 342
		AddLinkedLists firstList = new AddLinkedLists(2);
		firstList.setNext(new AddLinkedLists(4));
		firstList.getNext().setNext(new AddLinkedLists(3));
		System.out.print("first list: ");
		printList(firstList);
		
		//create second list 5 -> 6 -> 4 which represents the number 465
		AddLinkedLists secondList = new AddLinkedLists(5);
		secondList.setNext(new AddLinkedLists(6));
		secondList.getNext().setNext(new AddLinkedLists(4));
		System.out.print("second list: ");
		printList(secondList);
		
		// add the two lists together
		ArrayList<Integer> sum = addLists(firstList, secondList);
		AddLinkedLists sumList = createList(sum);
		
		System.out.print("sum list structure: ");
		printList(sumList);
		
		String actualNumber = combineList(sum);
		System.out.println("sum: " + actualNumber);
		
	}
	
	public static String combineList(ArrayList<Integer> aList) {
		StringBuilder builder = new StringBuilder();
		Collections.reverse(aList); // reverse array list as numbers are stored in ascending decimals place
		for(int i: aList) {
			builder.append(i);
		}
		return builder.toString();
	}
	
	public static AddLinkedLists createList(ArrayList<Integer> aList) {
		AddLinkedLists list = new AddLinkedLists(0);
		AddLinkedLists dummyNode = list; // dummy will be used to return the actual head
		for(int i : aList) {
			list.setNext(new AddLinkedLists(i));
			list = list.getNext();
		}
		return dummyNode.getNext();
	}
	
	public static void printList(AddLinkedLists list) {
		while(list != null) {
			System.out.print(list.value + " ");
			if(list.hasNext()) {
				System.out.print("-> ");
			}
			list = list.getNext();
		}
		System.out.println();
	}
	
	public static ArrayList<Integer> addLists(AddLinkedLists firstList, AddLinkedLists secondList) {
		ArrayList<Integer> sum = new ArrayList<Integer>();
		boolean carryOver = false;
		while(firstList != null || secondList != null) {
			int firstValue = 0; int secondValue = 0;
			
			if(firstList != null) {
				firstValue = firstList.getValue();
				firstList = firstList.getNext();
			}
			
			if(secondList != null) {
				secondValue = secondList.getValue();
				secondList = secondList.getNext();
			}
			
			// assuming node only holds single digit values
			int total = (carryOver) ? 1 + firstValue + secondValue : firstValue + secondValue; 
			
			if(total >= 10) {
				sum.add(total % 10);
				carryOver = true;
			}
			else {
				sum.add(total);
				carryOver = false;
			}
			
		}
		return sum;
	}

}

