# TCSR Projects

This repository contains all of the Python, C++, and Java projects that I have worked on as a Coding Instructor at theCoderSchool Roslyn.

This repo will continue to grow as more projects are added over time.

## Repo structure

```text
├── C++/
│   ├── Car/
│   ├── Casino/
│   └── GPA/
├── Java/
│   ├── BankAccount/
│   ├── Dog/
│   └── ExpenseTracker/
├── Python/
│   ├── AddressBook/
│   ├── Blackjack/
│   └── Snake/
├── .pre-commit-config.yaml
├── README.md
├── .gitignore
└── .github/
```

## Using pre-commit in this repo

This repository includes a pre-commit configuration to automatically lint files before they are committed. The current setup helps keep the repo clean by fixing common formatting issues such as:

- removing trailing whitespace
- ensuring files end with a newline
- normalizing line endings to LF
- sorting requirements.txt files for Python projects

### Install pre-commit

If you do not already have pre-commit installed, use the following installation method for your operating system:

**macOS**

```bash
brew install pre-commit
```

**Windows/Linux**

```
pip install pre-commit
```

### Set up the hooks

From the repo root, run:

```bash
pre-commit install
```

This installs the Git hooks so the checks run automatically whenever you make a commit.

### Run checks manually

You can also run the checks manually before making a commit using:

```bash
pre-commit run
```
