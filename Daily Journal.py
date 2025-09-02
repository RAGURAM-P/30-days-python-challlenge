from datetime import datetime

JOURNAL_FILE = "journal.txt"

def write_entry():
    print("\n--- Write New Journal Entry ---")
    entry = input("Write your thoughts: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(JOURNAL_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n{entry}\n\n")

    print("✅ Entry saved successfully!")

def view_entries():
    print("\n--- Your Journal ---")
    try:
        with open(JOURNAL_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                print(content)
            else:
                print("No entries yet.")
    except FileNotFoundError:
        print("No journal file found. Start by writing your first entry!")

def main():
    while True:
        print("\n--- Daily Journal ---")
        print("1. Write Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("👋 Goodbye! Keep journaling daily.")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
