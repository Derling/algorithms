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
	
	public static void main(String[] args) {
		// create first list 2 -> 4 -> 3 which represents the number 342
		Node firstList = new Node(2);
		firstList.setNext(new Node(4));
		firstList.getNext().setNext(new Node(3));
		System.out.print("first list: ");
		printList(firstList);
		
		//create second list 5 -> 6 -> 4 which represents the number 465
		Node secondList = new Node(5);
		secondList.setNext(new Node(6));
		secondList.getNext().setNext(new Node(4));
		System.out.print("second list: ");
		printList(secondList);
		
		// add the two lists together
		ArrayList<Integer> sum = addLists(firstList, secondList);
		Node sumList = createList(sum);
		
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
	
	public static Node createList(ArrayList<Integer> aList) {
		Node list = new Node(0);
		Node dummyNode = list; // dummy will be used to return the actual head
		for(int i : aList) {
			list.setNext(new Node(i));
			list = list.getNext();
		}
		return dummyNode.getNext();
	}
	
	public static void printList(Node list) {
		while(list != null) {
			System.out.print(list.value + " ");
			if(list.hasNext()) {
				System.out.print("-> ");
			}
			list = list.getNext();
		}
		System.out.println();
	}
	
	public static ArrayList<Integer> addLists(Node firstList, Node secondList) {
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

class Node {
	public int value;
	private Node next;
		
	public Node(int value) {
		this.value = value;
	}

	public int getValue() {
		return this.value;
	}
		
	public Node getNext() {
		return this.next;
	}
		
	public void setNext(Node node) {
		this.next = node;
	}
	
	public boolean hasNext() {
		return this.next != null;
	}
}
