import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

public class Tracker {
    // Add an ArrayList to store Expense objects
    // This will be the main collection that holds all user expenses
    ArrayList<Expense> expenses;

    // Constructor - initialize the collection for storing expenses
    public Tracker() {
        this.expenses = new ArrayList<Expense>();
    }

    // getNumExpenses() method
    // - Returns the total number of expenses
    public int getNumExpenses() {
        return this.expenses.size();
    }

    // getExpenseIDs() method
    // - Returns an ArrayList of all expense IDs
    public ArrayList<String> getExpenseIDs() {
        ArrayList<String> ids = new ArrayList<>();
        for (Expense expense : this.expenses) {
            ids.add(expense.getExpenseID());
        }
        return ids;
    }

    // getExpenseCategories() method
    // - Returns an ArrayList of all unique categories
    public ArrayList<String> getExpenseCategories() {
        ArrayList<String> categories = new ArrayList<>();
        for (Expense expense : this.expenses) {
            String category = expense.getCategory();
            if (!categories.contains(category)) {
                categories.add(category);
            }
        }
        return categories;
    }

    // addExpense() method
    // - Takes an Expense object as a parameter
    // - Adds it to the collection
    public void addExpense(Expense expense) {
        this.expenses.add(expense);
    }

    // removeExpense() method
    // - Takes an identifier (expenseID) as parameter
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

    // displayTotalCost() method
    // - Calculates and displays the total expense cost
    public void displayTotalCost() {
        float total = 0;
        for (Expense e: this.expenses) {
            total += e.getAmount();
        }
        System.out.printf("Your total cost is: $%.2f%n", total);
    }

    // displayExpensesByCategory() method
    // - Takes a category as parameter
    // - Displays filtered expenses by that category
    public void displayExpensesByCategory(String category) {
        System.out.println(String.format("Displaying expenses for %s category\n", category));
        for (Expense expense: this.expenses) {
            String c = expense.getCategory().strip().toLowerCase();
            if (c.equals(category)) {
                System.out.println(expense);
            }
        }
    }

    // displayExpensesByDateRange() method
    // - Takes start and end dates as parameters
    // - Displays expenses within that date range
    public void displayExpensesByDateRange(String startDate, String endDate) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");

        LocalDate start = LocalDate.parse(startDate, formatter);
        LocalDate end = LocalDate.parse(endDate, formatter);

        System.out.println(String.format("Displaying expenses between %s and %s:\n", startDate, endDate));
        
        int expensesWithinRange = 0;
        
        for (Expense e: this.expenses) {
            LocalDate expenseDate = e.getDate();
            if (!expenseDate.isBefore(start) && !expenseDate.isAfter(end)) {
                System.out.println(e);
                expensesWithinRange += 1;
            }
        }

        if (expensesWithinRange == 0) {
            System.out.println("There are no expenses within this range");
            System.out.println("Try a different range!");
        }
    }
}
