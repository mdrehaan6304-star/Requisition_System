class RequisitionSystem:

    def __init__(self):
        self.requisitions = []
        self.next_requisition_id = 10001

        self.total_requisitions = 0
        self.approved_requisitions = 0
        self.pending_requisitions = 0
        self.not_approved_requisitions = 0


# Create an object of the class
system = RequisitionSystem()

print("Requisition System Started")
