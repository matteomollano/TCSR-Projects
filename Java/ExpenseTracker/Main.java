import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Tracker tracker = new Tracker();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("""
            1. Add a new expense
            2. Delete an expense
            3. Display all expenses and total
            4. Display by category
            5. Display by date range
            """);

            String choice = sc.nextLine();

            // make sure choice input is valid (1, 2, 3, 4, or 5)
            // will explore contains() method with ArrayList next time
            while (
                !choice.equals("1") &&
                !choice.equals("2") &&
                !choice.equals("3") &&
                !choice.equals("4") &&
                !choice.equals("5")
            ) {
                System.out.println("You must enter 1, 2, 3, 4, or 5 only.");
                choice = sc.nextLine();
            }

            // at this point, choice input should be valid
            if (choice.equals("1")) {
                System.out.println("Enter description: ");
                String expenseName = sc.nextLine();

                System.out.println("Enter amount ($): ");
                float expenseAmount = sc.nextFloat();

                System.out.println("Enter category: ");
                String expenseCategory = sc.nextLine();

                System.out.println("Enter date of expense (MM/DD/YYYY): ");
                String expenseDate = sc.nextLine();

                Expense newExpense = new Expense(expenseName, expenseAmount, expenseCategory, expenseDate);
                tracker.addExpense(newExpense);
            }
        }

        // need to use sc.close() when rest of code is finished
    }
}