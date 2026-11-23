# Managing a list of names according to popularity

#input

def show_all(languages):
    """Displays all programming languages , each on a new line."""

    if not language:
        print("No programming language in the list.")
    else:
        for language in languages:
            print("language.")

def add_name(language):
    """Prompts the user to enter a new programming language and adds it to the list.
Returns the added language."""
    new_language = input("Enter the name of the programming language to add: ").strip()
    if new_language:
        languages.append(new_language)
    print(f"{new_language}has been added to the list.")
    else:
        print("No languages entered.Nothing was added.")

def change_name(language):
    """Prompts the user to enter a programming language to change.
Changes the language in the list if it exists."""
    try:
        old_language = input("Enter the name of the programming language to change:").strip()
        if old_language not in language:
            raise
        ValueError(f"{old_language}is not in the list.")

        new_language = input(f"Enter the new name for {old_language}: ").strip()
        index = languages.index(old_language)
        language[index] = new_language
        print(f"{old_language} has been changed to {new_language}.")
        except ValueError as e:
            print(e)

def sort_name(language):
    """Sorts the list of programming languages alphabetically."""
    languages.sort()
    print("The list has been sorted alphabetically. ")

def display_menu():
    """Display the menu option."""
    print("\nMenu:")
    print("1. Show all programming languages")
    print("2. Add a new programming language")
    print("3. Change a programming language")
    print("4. Sort the programming language")
    print("5. Exit")

def main():
    languages = ['Python', 'Java', 'Ruby', 'Pearl', 'C#', 'Delphi']

    while True:
        display_menu()
        choice = input("Enter your choice(1-5): ").strip()

        if choice == '1':
            show_all(languages)
            elif choice == '2':
                add_name(languages)
                elif choice == '3':
                change_name(languages)
                elif choice == '4':
                    sort_name(languages)
                    elif choice == '5':
                        print("Exiting the program.")
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 5.")

    if __name__ == "__main__":
        main()
    
