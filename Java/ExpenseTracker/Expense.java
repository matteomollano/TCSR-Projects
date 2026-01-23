import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.UUID;

public class Expense {

    // class variables (properties, attributes)
    private String expenseID;
    private String description;
    private float amount;
    private String category;
    private LocalDate date;
    
    // constructor -> initializes a new object
    public Expense(String description, float amount, String category, String date) {
        setExpenseID();
        setDescription(description);
        setAmount(amount);
        setCategory(category);
        setDate(date);
    }

    // Add getter methods for each property
    // - getDescription()
    // - getAmount()
    // - getCategory()
    // - getDate()
    public String getExpenseID() {
        return this.expenseID;
    }

    public String getDescription() {
        return this.description;
    }

    public float getAmount() {
        return this.amount;
    }

    public String getCategory() {
        return this.category;
    }

    public LocalDate getDate() {
        return this.date;
    }

    // Add setter methods to allow editing expenses
    // - setDescription()
    // - setAmount()
    // - setCategory()
    // - setDate()
    private void setExpenseID() {
        this.expenseID = UUID.randomUUID().toString();
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setAmount(float amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Expense amount cannot be negative");
        }
        this.amount = amount;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public void setDate(String date) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        try {
            LocalDate newDate = LocalDate.parse(date, formatter);
            this.date = newDate;
        } catch (DateTimeParseException e) {
            System.out.println("Invalid date format. Please use MM/dd/yyyy.");
        }
    }

    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String formattedDate = this.date.format(formatter);
        return String.format("""
        Expense ID: %s
        Description: %s
        Amount: $%.2f
        Category: %s
        Date: %s
        """, this.expenseID, this.description, this.amount, this.category, formattedDate);
    }
}
