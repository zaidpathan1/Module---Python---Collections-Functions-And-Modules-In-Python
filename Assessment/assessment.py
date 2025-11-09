orders = []  


def book_repair_order():
    print("\n=== New Repair Order Booking ===")
    customer_name = input("Enter customer name: ").strip()
    device_type = input("Enter device type (e.g., Phone, Laptop): ").strip()
    issue = input("Enter issue description: ").strip()
    due_date = input("Enter expected due date (DD/MM/YYYY): ").strip()

    order = {
        "customer_name": customer_name,
        "device_type": device_type,
        "issue": issue,
        "due_date": due_date,
        "status": "Pending",
        "bill_generated": False,
        "total_amount": 0
    }

    orders.append(order)
    print("\nOrder added successfully!")
    print(f"Order ID: {len(orders)} (Use this ID for billing later)")


def generate_bill():
    print("\n=== Generate Bill ===")
    if not orders:
        print("No orders found. Please book an order first.")
        return

    try:
        order_id = int(input("Enter Order ID: "))
        if order_id < 1 or order_id > len(orders):
            print("Invalid Order ID.")
            return
    except ValueError:
        print("Please enter a valid numeric Order ID.")
        return

    order = orders[order_id - 1]

    if order["bill_generated"]:
        print("Bill has already been generated for this order.")
        return

    print(f"\nCustomer: {order['customer_name']}")
    print(f"Device: {order['device_type']}")
    print(f"Issue: {order['issue']}")
    print(f"Due Date: {order['due_date']}")

    try:
        parts_cost = float(input("\nEnter total parts replacement cost : "))
        repair_fee = float(input("Enter repair service fee : "))
        discount = float(input("Enter discount amount if any): ") or 0)
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    subtotal = parts_cost + repair_fee
    tax = subtotal * 0.18  # 18% GST
    total = subtotal + tax - discount

    order["status"] = "Completed"
    order["bill_generated"] = True
    order["total_amount"] = total

    print("\n===== FIXTRACK INVOICE =====")
    print(f"Customer Name : {order['customer_name']}")
    print(f"Device Type   : {order['device_type']}")
    print(f"Issue         : {order['issue']}")
    print(f"Due Date      : {order['due_date']}")
    print("--------------------------------")
    print(f"Parts Cost    : {parts_cost:.2f}")
    print(f"Repair Fee    : {repair_fee:.2f}")
    print(f"Tax (18%)     : {tax:.2f}")
    print(f"Discount      : {discount:.2f}")
    print("--------------------------------")
    print(f"Total Payable: {total:.2f}")
    print("================================")
    print("Bill generated successfully!\n")


def view_orders():
    print("\n=== All Repair Orders ===")
    if not orders:
        print("No orders found.")
        return

    for idx, order in enumerate(orders, start=1):
        print(f"\nOrder ID: {idx}")
        print(f"Customer: {order['customer_name']}")
        print(f"Device: {order['device_type']}")
        print(f"Issue: {order['issue']}")
        print(f"Due Date: {order['due_date']}")
        print(f"Status: {order['status']}")
        if order["bill_generated"]:
            print(f"Total Amount: {order['total_amount']:.2f}")
        print("-" * 30)


def main_menu():
    while True:
        print("\n===== FixTrack - Repair Management System =====")
        print("1. Book New Repair Order")
        print("2. View All Orders")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            book_repair_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            generate_bill()
        elif choice == '4':
            print("\nExiting FixTrack. Have a productive day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



if __name__ == "__main__":
    main_menu()