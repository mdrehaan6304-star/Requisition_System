from datetime import date

class RequisitionSystem:

    def __init__(self):
        self.requisitions = []
        self.next_requisition_id = 10001

        self.total_requisitions = 0
        self.approved_requisitions = 0
        self.pending_requisitions = 0
        self.not_approved_requisitions = 0

    def add_requisition(self, staff_id, staff_name, items):
        total = 0
        for item in items:
            total += item["cost"]
           
            requisition_id = self.next_requisition_id
        self.next_requisition_id += 1
        # Automatically determine requisition status
        if total < 500:
            status = "Approved"
            approval_reference = staff_id + str(requisition_id)[-3:]
            self.approved_requisitions += 1
        else:
            status = "Pending"
            approval_reference = "Not available"
            self.pending_requisitions += 1

        # Store requisition information
        requisition = {
            "date": date.today().strftime("%d/%m/%Y"),
            "staff_id": staff_id,
            "staff_name": staff_name,
            "requisition_id": requisition_id,
            "items": items,
            "total": total,
            "status": status,
            "approval_reference": approval_reference
        }

        self.requisitions.append(requisition)
        self.total_requisitions += 1

        return total
    def respond_requisition(self, requisition_id, response):
    
        for requisition in self.requisitions:
                if requisition["requisition_id"] == requisition_id:
                    if requisition["status"] != "Pending":
                        print("Already processed.")
                        return
    
                    if response == "Approved":
                        requisition["status"] = "Approved"
                        requisition["approval_reference"] = (
                            requisition["staff_id"] + str(requisition_id)[-3:]
                        )
                        self.approved_requisitions += 1
                        self.pending_requisitions -= 1
    
                    elif response == "Not approved":
                        requisition["status"] = "Not approved"
                        self.not_approved_requisitions += 1
                        self.pending_requisitions -= 1
    
                    else:
                        print("Invalid response.")
                        return
    
                    print("Requisition updated.")
                    return
    
        print("Requisition not found.")
            
# Create an object of the class
system = RequisitionSystem()

print("Requisition System Started")
# Test 1: Requisition below $500
items1 = [
    {"cost": 200},
    {"cost": 150}
]

total1 = system.add_requisition("FN19", "John Paul", items1)

print("\nTest 1")
print("Total:", total1)
print("Status:", system.requisitions[0]["status"])
print("Approval Reference:", system.requisitions[0]["approval_reference"])


# Test 2: Requisition above $500
items2 = [
    {"cost": 600},
    {"cost": 400}
]

total2 = system.add_requisition("FN20", "Tracy Brown", items2)

print("\nTest 2")
print("Total:", total2)
print("Status:", system.requisitions[1]["status"])
print("Approval Reference:", system.requisitions[1]["approval_reference"])
# Test 3: Requisition below $500
items3 = [
    {"cost": 200},
    {"cost": 250}
]

total3 = system.add_requisition("FN15", "Emma Wellington", items3)

# Test 4: Requisition above $500
items4 = [
    {"cost": 800},
    {"cost": 700}
]

total4 = system.add_requisition("FN02", "Catlin White", items4)

# Test 5: Requisition below $500
items5 = [
    {"cost": 100},
    {"cost": 150}
]

total5 = system.add_requisition("FN21", "David Smith", items5)

# Display Test 3
print("\nTest 3")
print("Total:", total3)
print("Status:", system.requisitions[2]["status"])
print("Approval Reference:", system.requisitions[2]["approval_reference"])

# Display Test 4
print("\nTest 4")
print("Total:", total4)
print("Status:", system.requisitions[3]["status"])
print("Approval Reference:", system.requisitions[3]["approval_reference"])

# Display Test 5
print("\nTest 5")
print("Total:", total5)
print("Status:", system.requisitions[4]["status"])
print("Approval Reference:", system.requisitions[4]["approval_reference"])