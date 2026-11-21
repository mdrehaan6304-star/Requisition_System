from datetime import date


class Requisition:

    next_requisition_id = 10001
    all_requisitions = []

    def __init__(self):
        self.date = date.today().strftime("%d/%m/%Y")
        self.requisition_id = Requisition.next_requisition_id
        Requisition.next_requisition_id += 1

        self.staff_id = ""
        self.staff_name = ""
        self.requisition_items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    # Add a new requisition
    def add_requisition(self):

        print("\nEnter Staff Details")

        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")

        print("\nEnter Requisition Items")

        number_of_items = int(
            input("How many items do you want to request? ")
        )

        for i in range(number_of_items):

            print("\nItem", i + 1)

            item_name = input("Enter item name: ")
            item_cost = float(input("Enter item cost: $"))

            self.requisition_items.append({
                "name": item_name,
                "cost": item_cost
            })

        self.total = self.requisitions_details()

        self.approve_requisition()

        Requisition.all_requisitions.append(self)

        return self.total

    # Calculate requisition total
    def requisitions_details(self):

        total = 0

        for item in self.requisition_items:
            total += item["cost"]

        return total

    # Automatic approval
    def approve_requisition(self):

        if self.total < 500:

            self.status = "Approved"

            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        else:

            self.status = "Pending"
            self.approval_reference = "Not available"

    # Manager approval or rejection
    def respond_to_requisition(self):

        print("\nPending Requisitions")

        for req in Requisition.all_requisitions:

            if req.status == "Pending":

                print("Requisition ID:", req.requisition_id)
                print("Staff Name:", req.staff_name)
                print("Total: $", req.total)

        requisition_id = int(input("\nEnter Requisition ID: "))

        for req in Requisition.all_requisitions:

            if req.requisition_id == requisition_id:

                if req.status != "Pending":

                    print("This requisition is not pending.")
                    return

                decision = input(
                    "Enter manager decision (Approved/Not approved): "
                ).strip().lower()

                if decision == "approved":

                    req.status = "Approved"

                    req.approval_reference = (
                        req.staff_id + str(req.requisition_id)[-3:]
                    )

                    print("Requisition approved.")

                elif decision == "not approved":

                    req.status = "Not approved"
                    req.approval_reference = "Not available"

                    print("Requisition not approved.")

                else:

                    print("Invalid decision.")

                return

        print("Requisition ID not found.")

    # Display one requisition
    def display_requisition(self):

        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)

        print("\nRequisition Items:")

        for item in self.requisition_items:

            print(
                item["name"],
                "- $",
                format(item["cost"], ".2f")
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


number_of_requisitions = int(
    input("\nHow many requisitions do you want to submit? ")
)

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

        manager = Requisition()
        manager.respond_to_requisition()

    elif choice == "no":

        break

    else:

        print("Please enter yes or no.")


# Display all requisitions

if Requisition.all_requisitions:

    requisition = Requisition()
    requisition.display_all_requisitions()