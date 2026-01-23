import java.util.Random;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Hangman {

    public static void main(String[] args) {
        // generate the random word from a list of random words
        String[] words = {"generous", "curiosity", "continental", "captivate", "ubiquitous"};

        Random random = new Random();
        int randomIndex = random.nextInt(words.length);

        String randomWord = words[randomIndex];
        // System.out.println(randomWord);

        // create the underscores list
        ArrayList<String> underscores = new ArrayList<String>();
        for (int i = 0; i < randomWord.length(); i++) {
            underscores.add("_");
        }
        String result = String.join(" ", underscores);
        System.out.println(result);

        // while loop for game
        int guesses = 7;

        // create scanner for getting input
        Scanner sc = new Scanner(System.in);

        // create Set to keep track of letters guessed
        Set<Character> lettersGuessed = new HashSet<>();

        while (guesses > 0) {
            System.out.println("Number of guesses: " + guesses);
            System.out.print("Enter a letter: ");
            char letter = sc.next().charAt(0);

            while (lettersGuessed.contains(letter)) {
                System.out.println(String.format("You already guessed %c. Guess a different letter.", letter));
                System.out.print("Enter a letter: ");
                letter = sc.next().charAt(0);
            }

            // add the new letter to the lettersGuessed Set
            lettersGuessed.add(letter);

            // System.out.println("Random word length: " + randomWord.length());
            boolean guessed = false;
            for (int i = 0; i < randomWord.length(); i++) {
                // System.out.println("Comparing " + letter + " to " + randomWord.charAt(i));
                if (letter == randomWord.charAt(i)) {
                    underscores.set(i, Character.toString(letter));
                    guessed = true;
                }
            }
            result = String.join(" ", underscores);
            System.out.println(result);

            if (guessed == false) {
                    guesses--;
            }

            // contains is "in" Python equivalent
            if (!underscores.contains("_")) {
                System.out.println("You win!");
                break;
            }
            else if (guesses == 0) {
                System.out.println("Sorry you lose. The word was " + randomWord);
            }

        }
        
        sc.close();
    }
    
}