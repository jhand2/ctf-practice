// Using analysis from notes.txt, look for a value of i that satisfies the
// if_icmpne condition (instruction 14) in bitecode.txt to get the function
// checkNum to return 1
public class Solution {
    public static void main(String[] args) {
        int a = 525024598;
        int b = -889275714;

        for (int i = Integer.MIN_VALUE; i < Integer.MAX_VALUE; i++) {
            int s1 = (i << 3) ^ (a ^ i);
            if (s1 == b) {
                System.out.println("Proper input: " + i);
                break;
            }
        }

    }
}
