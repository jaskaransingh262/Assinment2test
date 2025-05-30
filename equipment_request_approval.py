from equipment_request_total import equipment_request_total

def equipment_request_approval():
    date, staff_id, staff_name, request_id, city, total = equipment_request_total()
    if total < 300:
        status = "Approved"
        approval_ref = staff_id + str(request_id)[-3:]
    else:
        status = "Pending"
        approval_ref = "N/A"

    print(f"/n")        