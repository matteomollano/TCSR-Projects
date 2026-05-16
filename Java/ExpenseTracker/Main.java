import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        Tracker tracker = new Tracker();

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

            String choice = UserInput.input("Your choice here: ");

            // make sure choice input is valid (1, 2, 3, 4, 5, or 6)
            // will explore contains() method with ArrayList next time
            List<String> options = Arrays.asList("1", "2", "3", "4", "5", "6");

            while (!options.contains(choice)) {
                System.out.println("You must enter 1, 2, 3, 4, 5, or 6 only.");
                choice = UserInput.input("");
            }

            // at this point, choice input should be valid
            if (choice.equals("1")) {
                System.out.println("================");
                System.out.println("|   Add Item   |");
                System.out.println("================");

                String expenseName = UserInput.input("Enter item description: ");

                float expenseAmount = UserInput.amountInput("Enter amount: $");
            
                String expenseCategory = UserInput.input("Enter item category: ");

                String expenseDate = UserInput.dateInput("Enter purchase date (MM/DD/YYYY): ");

                Expense newExpense = new Expense(expenseName, expenseAmount, expenseCategory, expenseDate);
                tracker.addExpense(newExpense);
            }
            else if (choice.equals("2")) {
                System.out.println("===================");
                System.out.println("|   Delete Item   |");
                System.out.println("===================");
                
                String expenseID = UserInput.input("Enter expenseID to remove: ");
                ArrayList<String> expenseIDs = tracker.getExpenseIDs();
                if (!expenseIDs.contains(expenseID)) {
                    System.out.println(expenseID + " is not a valid expense ID.");
                }
                else {
                    tracker.removeExpense(expenseID);
                    System.out.println("Removed expense #" + expenseID + " successfully!");
                }
            }
            else if (choice.equals("3")) {
                System.out.println("======================");
                System.out.println("|   Total Expenses   |");
                System.out.println("======================");

                int numExpenses = tracker.getNumExpenses();
                if (numExpenses >= 1) {
                    tracker.displayExpenses();
                    tracker.displayTotalCost();
                }
                else {
                    System.out.println("You don't have any expenses yet");
                    System.out.println("Add some expenses!");
                }

            }
            else if (choice.equals("4")) {
                System.out.println("===================");
                System.out.println("|   By Category   |");
                System.out.println("===================");
                String category = UserInput.input("Enter category name: ");

                ArrayList<String> categories = tracker.getExpenseCategories();
                if (!categories.contains(category)) {
                    System.out.println(category + " category does not exist.");
                }
                else {
                    tracker.displayExpensesByCategory(category);
                }
            }
            else if (choice.equals("5")) {
                System.out.println("===============");
                System.out.println("|   By Date   |");
                System.out.println("===============");

                String startDate = UserInput.dateInput("Enter start date (MM/DD/YYYY): ");
                String endDate = UserInput.dateInput("Enter end date (MM/DD/YYYY): ");
            
                tracker.displayExpensesByDateRange(startDate, endDate);
            }
            else {
                System.out.println("Exiting ...");
                break;
            }
            System.out.println("-----------------------------------------\n");
        }

        // close the scanner
        UserInput.close();
    }
}
