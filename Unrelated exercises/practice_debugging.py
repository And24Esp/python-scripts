# Here is a ready-to-run Python script intentionally broken in three different ways. 
# It's designed to practice VS Code Debugger features like basic breakpoints, conditional breakpoints, variable inspection, and debug console (far-right tab from Terminal).

def calculate_average(numbers):
    # BUG 1: Logic Error
    # This will cause a ZeroDivisionError if the list is empty.
    # Practice: Set a breakpoint here and check the value of 'numbers'.
    total = sum(numbers)
    return total / len(numbers)

def Process_user_data():
    users = [
        {"name": "Alice", "age": 25, "role": "admin"},
        {"name": "Bob", "age": 30, "role": "user"},
        {"name": "Charlie", "age": -5, "role": "user"}, # BUG 2: Bad data
        {"name": "Dave", "age": 40, "role": "admin"}
    ]
    
    print("Processing users...")
    for user in users:
        # Practice: Right-click the line below to set a 'Conditional Breakpoint'.
        # Set the condition to: user['age'] < 0
        if user["role"] == "admin":
            print(f"Admin found: {user['name']}")
            
    return users

def main():
    print("--- Starting Debugging Practice ---")
    
    # 1. Test data processing
    processed_users = Process_user_data()
    
    # 2. Test average calculation
    ages = [u["age"] for u in processed_users if u["role"] == "user"]
    print(f"User ages: {ages}")
    
    # BUG 3: Runtime Exception
    # Let's say we filter for a role that doesn't exist, resulting in an empty list.
    guest_ages = [u["age"] for u in processed_users if u["role"] == "guest"]
    
    # This call will crash the script! 
    # Practice: Use 'Step Into' to watch the execution jump into calculate_average().
    avg_guest_age = calculate_average(guest_ages) 
    print(f"Average guest age: {avg_guest_age}")

if __name__ == "__main__":
    main()
