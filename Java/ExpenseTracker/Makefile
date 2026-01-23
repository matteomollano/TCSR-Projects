# Variables
JAVAC = javac
JAVA = java
MAIN = Main
SRC = $(wildcard *.java)   # All .java files in the directory
OBJ = $(SRC:.java=.class)  # Convert .java files to .class files

# Default target - compile all Java files
all: $(OBJ)

# Compile class files from .java files
%.class: %.java
	$(JAVAC) $<

# Run the program (Main.java should be the entry point)
run: all
	$(JAVA) $(MAIN)

# Clean up compiled .class files
clean:
	rm -f $(OBJ)