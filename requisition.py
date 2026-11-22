from datetime import date


class Requisition:

    next_requisition_id = 10001
    all_requisitions = []

    def __init__(self):

        self.date = date.today().strftime("%d/%m/%Y")
        self.requisition_id = Requisition.next_requisition_id

        self.staff_id = ""
        self.staff_name = ""
        self.requisition_items = {}
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    # Add a new requisition
    def add_requisition(self):

        print("\nEnter Staff Details")

        self.staff_id = input("Enter Staff ID: ").strip()
        self.staff_name = input("Enter Staff Name: ").strip()

        while self.staff_id == "" or self.staff_name == "":
            print("Staff ID and name cannot be empty.")
            self.staff_id = input("Enter Staff ID: ").strip()
            self.staff_name = input("Enter Staff Name: ").strip()

        print("\nEnter Requisition Items")

        while True:
            try:
                number_of_items = int(
                    input("How many items do you want to request? ")
                )

                if number_of_items > 0:
                    break
                else:
                    print("Enter at least one item.")

            except ValueError:
                print("Please enter a valid number.")

        for i in range(number_of_items):

            print("\nItem", i + 1)

            item_name = input("Enter item name: ").strip()

            while item_name == "" or item_name in self.requisition_items:
                print("Item name cannot be empty or repeated.")
                item_name = input("Enter item name: ").strip()

            while True:
                try:
                    item_cost = float(
                        input("Enter item cost: $")
                    )

                    if item_cost > 0:
                        break
                    else:
                        print("Item cost must be greater than zero.")

                except ValueError:
                    print("Please enter a valid cost.")

            self.requisition_items[item_name] = item_cost

        self.total = self.requisitions_details()

        self.approve_requisition()

        Requisition.all_requisitions.append(self)

        Requisition.next_requisition_id += 1

        print("\nRequisition added successfully.")

        return True

    # Calculate requisition total
    def requisitions_details(self):

        total = 0

        for cost in self.requisition_items.values():
            total += cost

        return total

    # Generate approval reference
    def generate_approval_reference(self):

        return (
            self.staff_id + str(self.requisition_id)[-3:]
        )

    # Automatic approval
    def approve_requisition(self):

        if self.total < 500:

            self.status = "Approved"

            self.approval_reference = (
                self.generate_approval_reference()
            )

        else:

            self.status = "Pending"
            self.approval_reference = "Not available"

    # Manager approval or rejection
    def respond_to_requisition(self):

        print("\nPending Requisitions")

        pending_exists = False

        for req in Requisition.all_requisitions:

            if req.status == "Pending":

                pending_exists = True

                print("Requisition ID:", req.requisition_id)
                print("Staff Name:", req.staff_name)
                print("Total: $", format(req.total, ".2f"))

        if not pending_exists:
            print("No pending requisitions.")
            return

        while True:
            try:
                requisition_id = int(
                    input("\nEnter Requisition ID: ")
                )
                break

            except ValueError:
                print("Please enter a valid requisition ID.")

        for req in Requisition.all_requisitions:

            if req.requisition_id == requisition_id:

                if req.status != "Pending":

                    print("This requisition is not pending.")
                    return

                while True:

                    decision = input(
                        "Enter manager decision (Approved/Not approved): "
                    ).strip().lower()

                    if decision == "approved":

                        req.status = "Approved"

                        req.approval_reference = (
                            req.generate_approval_reference()
                        )

                        print("Requisition approved.")
                        return

                    elif decision == "not approved":

                        req.status = "Not approved"
                        req.approval_reference = "Not available"

                        print("Requisition not approved.")
                        return

                    else:

                        print("Invalid decision. Please try again.")

        print("Requisition ID not found.")

    # Display one requisition
    def display_requisition(self):

        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("\nRequisition Items:")

        for item_name, item_cost in self.requisition_items.items():

            print(
                item_name,
                "- $",
                format(item_cost, ".2f")
            )

        print("Total: $", format(self.total, ".2f"))
        print("Status:", self.status)

        print(
            "Approval Reference Number:",
            self.approval_reference
        )

    # Display all requisitions
    def display_all_requisitions(self):

        for req in Requisition.all_requisitions:

            req.display_requisition()

    # Display requisition statistics
    def requisition_statistics(self):

        total_requisitions = len(Requisition.all_requisitions)

        approved = 0
        pending = 0
        not_approved = 0

        for req in Requisition.all_requisitions:

            if req.status == "Approved":
                approved += 1

            elif req.status == "Pending":
                pending += 1

            elif req.status == "Not approved":
                not_approved += 1

        print("Total Requisitions:", total_requisitions)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not approved:", not_approved)


# Main program
if __name__ == "__main__":

    while True:
        try:
            number_of_requisitions = int(
                input("\nHow many requisitions do you want to submit? ")
            )

            if number_of_requisitions > 0:
                break
            else:
                print("Enter at least one requisition.")

        except ValueError:
            print("Please enter a valid number.")

    for i in range(number_of_requisitions):

        requisition = Requisition()
        requisition.add_requisition()

    # Manager response
    while True:

        pending_exists = any(
            req.status == "Pending"
            for req in Requisition.all_requisitions
        )

        if not pending_exists:
            break

        choice = input(
            "\nDoes the manager want to respond to a pending requisition? (yes/no): "
        ).strip().lower()

        if choice == "yes":

            requisition.respond_to_requisition()

        elif choice == "no":

            break

        else:

            print("Please enter yes or no.")

    # Display all requisitions and statistics
    if Requisition.all_requisitions:

        requisition.display_all_requisitions()

        requisition.requisition_statistics()