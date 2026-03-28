import calendar

# Store reminders (date -> list of reminders)
reminders = {}

def show_calendar():
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1-12): "))
    
    print("\n📅 Monthly Calendar\n")
    print(calendar.month(year, month))

def add_reminder():
    date = input("Enter date (YYYY-MM-DD): ")
    note = input("Enter reminder text: ")

    if date in reminders:
        reminders[date].append(note)
    else:
        reminders[date] = [note]

    print("✅ Reminder added successfully!\n")

def view_reminders():
    date = input("Enter date (YYYY-MM-DD): ")

    if date in reminders:
        print(f"\n🔔 Reminders for {date}:")
        for i, note in enumerate(reminders[date], 1):
            print(f"{i}. {note}")
        print()
    else:
        print("❌ No reminders for this date.\n")

def main():
    while True:
        print("📆 Calendar & Reminder App")
        print("1) View Calendar")
        print("2) Add Reminder")
        print("3) View Reminders")
        print("0) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_calendar()
        elif choice == "2":
            add_reminder()
        elif choice == "3":
            view_reminders()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
