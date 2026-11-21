from datetime import date


class Requisition:

    next_requisition_id = 10001

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

        return self.total

    # Calculate requisition total
    def requisitions_details(self):

        total = 0

        for item in self.requisition_items:
            total += item["cost"]

        return total

    # Automatically approve or set pending status
    def approve_requisition(self):

        if self.total < 500:

            self.status = "Approved"

            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        else:

            self.status = "Pending"
            self.approval_reference = "Not available"

# Create requisition object
requisition1 = Requisition()

# Collect user input
requisition1.add_requisition()

print("Date:", requisition1.date)
print("Requisition ID:", requisition1.requisition_id)
print("Staff ID:", requisition1.staff_id)
print("Staff Name:", requisition1.staff_name)

print("\nRequisition Items:")

for item in requisition1.requisition_items:
    print(
        item["name"],
        "- $",
        format(item["cost"], ".2f")
    )

print("Total: $", format(requisition1.total, ".2f"))
print("Status:", requisition1.status)

print(
    "Approval Reference Number:",
    requisition1.approval_reference
)