# Makefile for compiling and running Java classes

# Variables
JAVAC = javac
JAVA = java
MAIN = Main
CLASSES = Dog.java Main.java

# Default target
all: $(CLASSES)
	$(JAVAC) $(CLASSES)

run: all
	$(JAVA) $(MAIN)

clean:
	rm -f *.class