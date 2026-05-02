import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Tracker tracker = new Tracker();
        Scanner sc = new Scanner(System.in);

        System.out.println("=========================");
        System.out.println("|    Expense Tracker    |");
        System.out.println("=========================");

        while (true) {
            System.out.println("""
            1. Add a new expense
            2. Delete an expense
            3. Display all expenses and cost
            4. Display by category
            5. Display by date range
            6. Exit
            """);

            System.out.print("Your choice here: ");
            String choice = sc.nextLine();

            // make sure choice input is valid (1, 2, 3, 4, 5, or 6)
            // will explore contains() method with ArrayList next time
            List<String> options = Arrays.asList("1", "2", "3", "4", "5", "6");

            while (!options.contains(choice)) {
                System.out.println("You must enter 1, 2, 3, 4, 5, or 6 only.");
                choice = sc.nextLine();
            }

            // at this point, choice input should be valid
            if (choice.equals("1")) {
                System.out.println("================");
                System.out.println("|   Add Item   |");
                System.out.println("================");

                System.out.print("Enter item description: ");
                String expenseName = sc.nextLine();

                System.out.print("Enter amount: $");
                float expenseAmount = sc.nextFloat();
                sc.nextLine(); // consume the leftover newline

                System.out.print("Enter item category: ");
                String expenseCategory = sc.nextLine();

                System.out.print("Enter purchase date (MM/DD/YYYY): ");
                String expenseDate = sc.nextLine();

                Expense newExpense = new Expense(expenseName, expenseAmount, expenseCategory, expenseDate);
                tracker.addExpense(newExpense);
            }
            else if (choice.equals("2")) {
                System.out.println("===================");
                System.out.println("|   Delete Item   |");
                System.out.println("===================");
                
                System.out.print("Enter expenseID to remove: ");
                String expenseID = sc.nextLine();

                tracker.removeExpense(expenseID);
            }
            else if (choice.equals("3")) {
                System.out.println("======================");
                System.out.println("|   Total Expenses   |");
                System.out.println("======================");

                tracker.displayExpenses();
                tracker.displayTotalCost();
            }
            else if (choice.equals("4")) {
                System.out.println("===================");
                System.out.println("|   By Category   |");
                System.out.println("===================");
                System.out.print("Enter category name: ");
                String category = sc.nextLine();

                tracker.displayExpensesByCategory(category);
            }
            else if (choice.equals("5")) {
                System.out.println("===============");
                System.out.println("|   By Date   |");
                System.out.println("===============");

                System.out.print("Enter start date (MM/DD/YYYY): ");
                String startDate = sc.nextLine();

                System.out.print("Enter end date (MM/DD/YYYY): ");
                String endDate = sc.nextLine();

                tracker.displayExpensesByDateRange(startDate, endDate);
            }
            else {
                System.out.println("Exiting ...");
                break;
            }
            System.out.println("-----------------------------------------\n");
        }

        // close the scanner
        sc.close();
    }
}