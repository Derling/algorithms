/*
 *  Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".
 *	withoutString("Hello there", "llo") → "He there"
 *	withoutString("Hello there", "e") → "Hllo thr"
 *	withoutString("Hello there", "x") → "Hello there"
 * 
 */
public class WithoutString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(withoutString("abxxxab", "x"));
	}
	public static String withoutString(String base, String remove) {
		  StringBuilder builder = new StringBuilder();
		  int index = 0;
		  String firstChar = "" + remove.charAt(0);
		  int baseLength = base.length();
		  int removeLength = remove.length();
		  while(index < baseLength) {
			  String currentChar = "" + base.charAt(index);
			  if(currentChar.equalsIgnoreCase(firstChar)) {
				  int subRange = index + removeLength;
				  subRange = subRange < baseLength ? subRange : baseLength;
				  if(!base.substring(index, subRange).equalsIgnoreCase(remove)) {
					  for(int i = index; i < subRange; i++) {
						builder.append(base.charAt(i));  
					  }
				  }
				  index = subRange;
				  }
			  else {
				  builder.append(currentChar);
				  index++;
			  }
		  }
		  return builder.toString();
		}


}
