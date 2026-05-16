import java.util.Scanner;
import java.time.format.DateTimeFormatter;
import java.time.LocalDate;

public class UserInput {

    private static Scanner sc = new Scanner(System.in);

    public static String input(String prompt) {
        System.out.print(prompt);
        String userInput = sc.nextLine().strip().toLowerCase();
        return userInput;
    }

    public static float amountInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String stringAmount = sc.nextLine().strip();
                float expenseAmount = Float.parseFloat(stringAmount);
                return expenseAmount;
            }
            catch (Exception e) {
                System.out.println("You must enter a number only.");
            }
        }
    }

    public static String dateInput(String prompt) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        
        while (true) {
            try {
                System.out.print(prompt);
                String input = sc.nextLine().strip();
                
                // split by "/" and pad each part
                String[] parts = input.split("/");
                if (parts.length != 3) {
                    System.out.println("Invalid date format. Please use MM/DD/YYYY.");
                    continue;
                }
                
                // pad month and day with leading zeros, handle 2-digit years
                int year = Integer.parseInt(parts[2]);
                if (year < 100) {
                    year += 2000;
                }
                
                String paddedDate = String.format("%02d/%02d/%04d", 
                    Integer.parseInt(parts[0]), 
                    Integer.parseInt(parts[1]), 
                    year);
                
                // validate by parsing to LocalDate
                LocalDate.parse(paddedDate, formatter);
                
                return paddedDate;
            }
            catch (Exception e) {
                System.out.println("Invalid date format. Please use MM/DD/YYYY.");
            }
        }
    }

    public static void close() {
        sc.close();
    }
}
