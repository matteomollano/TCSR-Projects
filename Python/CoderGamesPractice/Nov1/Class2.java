import java.util.Scanner;
import java.util.HashMap;

public class Class2 {

    public static void question1() {
        /*
         * 2. FizzBuzz Challenge
         * Count from 1 to 20.
         * If a number is divisible by 3, display “Fizz”.
         * If it’s divisible by 5, display “Buzz”.
         * If it’s divisible by both, display “FizzBuzz”.
         * Otherwise, just show the number itself.
         * 
         */
        for (int i = 1; i <= 20; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }

    public static void question2() {
        /*
         * 7. Letter Frequency Counter
         * Ask the user to enter a sentence.
         * Then, display how many of each letter is present in the sentence.
        */
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a sentence: ");
        String sentence = sc.nextLine();
        sc.close();

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (char letter: sentence.toCharArray()) {
            if (letter != ' ') {
                if (map.containsKey(letter)) {
                    int value = map.get(letter);
                    map.put(letter, value+1);
                }
                else {
                    map.put(letter, 1);
                }
            }
        }
        System.out.println(map);

        // "My dog jumped over the fence"
        // {
        //     "M": 1,
        //     "y": 1,
        //     "d": 2,
        //     "o": 2,
        //     "g": 1,
        //     "j": 1,
        //     "u": 1,
        //     "m": 1,
        //     "p": 1,
        //     "e": 5,
        //     "v": 1,
        //     "r": 1,
        //     "t": 1,
        //     "h": 1,
        //     "f": 1,
        //     "n": 1,
        //     "c": 1
        // }
    }

    public static void main(String[] args) {
        // Class2.question1();
        Class2.question2();
    }
}