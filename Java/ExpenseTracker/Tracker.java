import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;

public class Tracker {
    // Add an ArrayList to store Expense objects
    // This will be the main collection that holds all user expenses
    ArrayList<Expense> expenses;

    // Constructor - initialize the collection for storing expenses
    public Tracker() {
        this.expenses = new ArrayList<Expense>();
    }

    // addExpense() method
    // - Takes an Expense object as a parameter
    // - Adds it to the collection
    public void addExpense(Expense expense) {
        this.expenses.add(expense);
    }

    // removeExpense() method
    // - Takes an identifier (index, description, or date) as parameter
    // - Removes the expense from the collection
    public void removeExpense(String expenseID) {
        this.expenses.removeIf(expense -> expense.getExpenseID().equals(expenseID));
    }

    // displayExpenses() method
    // - Display all tracked expenses
    public void displayExpenses() {
        for (Expense e: this.expenses) {
            System.out.println(e);
        }
    }

    // displayTotalExpenses() method
    // - Calculates and displays the sum of all expense amounts
    public void displayTotalExpenses() {
        float total = 0;
        for (Expense e: this.expenses) {
            total += e.getAmount();
        }
        System.out.println("Your total expenses are: $" + total);
    }

    // displayExpensesByCategory() method
    // - Takes a category as parameter
    // - Displays filtered expenses by that category
    public void displayExpensesByCategory(String category) {
        System.out.println(String.format("Displaying expenses for %s category\n", category));
        for (Expense e: this.expenses) {
            if (e.getCategory().equals(category)) {
                System.out.println(e);
            }
        }
    }

    // displayExpensesByDateRange() method
    // - Takes start and end dates as parameters
    // - Displays expenses within that date range
    public void displayExpensesByDateRange(String startDate, String endDate) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");

        try {
            LocalDate start = LocalDate.parse(startDate, formatter);
            LocalDate end = LocalDate.parse(endDate, formatter);

            System.out.println(String.format("Displaying expenses between %s and %s:\n", startDate, endDate));
            for (Expense e: this.expenses) {
                LocalDate expenseDate = e.getDate();
                if (!expenseDate.isBefore(start) && !expenseDate.isAfter(end)) {
                    System.out.println(e);
                }
            }
        } catch (DateTimeParseException e) {
            System.out.println("Invalid date format. Please use MM/dd/yyyy.");
        }
    }
}
