# Makefile for compiling and running Java classes

# Variables
JAVAC = javac
JAVA = java
MAIN = Hangman
CLASSES = Hangman.java

# Default target
all: $(CLASSES)
	$(JAVAC) $(CLASSES)

run: all
	$(JAVA) $(MAIN)

clean:
	rm -f *.class