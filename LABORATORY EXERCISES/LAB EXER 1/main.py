tickets = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"]
]


def add_ticket():
    incident_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    description = input("Enter Short Description: ")

    tickets.append([incident_id, bot, description])
    print("\nTicket added successfully!")


def display_tickets():
    if len(tickets) == 0:
        print("\nNo active incident tickets.")
        return

    print("\n===== ACTIVE INCIDENT TICKETS =====")

    for ticket in tickets:
        print(f"\nIncident ID: {ticket[0]}")
        print(f"Bot: {ticket[1]}")
        print(f"Description: {ticket[2]}")


def search_ticket():
    incident_id = input("Enter Incident ID to search: ")

    for ticket in tickets:
        if ticket[0] == incident_id:
            print("\n===== TICKET FOUND =====")
            print(f"Incident ID: {ticket[0]}")
            print(f"Bot: {ticket[1]}")
            print(f"Description: {ticket[2]}")
            return

    print("\nTicket not found.")


def remove_ticket():
    incident_id = input("Enter Incident ID to remove: ")

    for ticket in tickets:
        if ticket[0] == incident_id:
            tickets.remove(ticket)
            print("\nTicket removed successfully!")
            return

    print("\nTicket not found.")


def count_tickets():
    print(f"\nTotal active incident tickets: {len(tickets)}")


while True:
    print("\n======================================")
    print(" IT AUTOMATION INCIDENT TICKET MANAGER")
    print("======================================")
    print("1. Add New Incident Ticket")
    print("2. Display All Active Tickets")
    print("3. Search for Incident Ticket")
    print("4. Remove Resolved Ticket")
    print("5. Count Active Tickets")
    print("6. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("\nThank you for using the Incident Ticket Manager!")
        break

    else:
        print("\nInvalid choice. Please try again.")
