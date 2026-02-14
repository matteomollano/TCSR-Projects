import java.util.ArrayList;

/*
    List that stores multiple Expense objects
    How to create: Expense obj1 = new Expense();
    ArrayList -> [obj1, obj2, obj3, obj4]
*/
public class ExpenseTracker {
    // TODO: Declare an ArrayList to store Expense objects
    // This will be the main collection that holds all user expenses
    ArrayList<Expense> expenses;
    
    // TODO: Constructor - initialize the ArrayList for storing expenses
    public ExpenseTracker() {
        expenses = new ArrayList<Expense>();
    }
    
    // TODO: addExpense() method
    // - Takes an Expense object as a parameter
    // - Adds it to the collection
    public void addExpense(Expense expense) {
        this.expenses.add(expense);
    }
    
    // TODO: removeExpense() method
    // - Takes an identifier (expenseID) as parameter
    // - Removes the expense from the collection
    public void removeExpense(String expenseID) {
        for (Expense expense : this.expenses) {
            String id = expense.getExpenseID();
            if (expenseID.equals(id)) {
                this.expenses.remove(expense);
                break;
            }
        }
    }

    // TODO: displayExpenses() method
    // - Display all tracked expenses
    public void displayExpenses() {
        for (Expense expense : this.expenses) {
            System.out.println(expense);
        }
    }
    
    // TODO: displayTotalExpenses() method
    // - Calculates and displays the sum of all expense amounts
    public void displayTotalExpenses() {
        // getAmount() for expense object
        // we have this.expenses -> [expense1, expense2, expense3]
        float totalAmount = 0; // 4.99 + 1299.99 + 8.99
        for (Expense expense : this.expenses) {
            // totalAmount = totalAmount + expense.getAmount();
            totalAmount += expense.getAmount();
        }
        System.out.println("Your total expenses are: $" + totalAmount);
    }
    
    // TODO: displayExpensesByCategory() method
    // - Takes a category as parameter
    // - Displays filtered expenses by that category
    public void displayExpensesByCategory(String category) {
        // we have this.expenses -> [expense1, expense2, expense3]
        for (Expense expense : this.expenses) {
            String c = expense.getCategory();
            if (c.equals(category)) {
                System.out.println(expense);
            }
        }
    }
    
    // TODO: displayExpensesByDateRange() method
    // - Takes start and end dates as parameters
    // - Displays expenses within that date range
}
