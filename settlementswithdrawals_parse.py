import json

# Open the file
with open("settlementswithdrawals.txt", "r", encoding="utf-8", errors="ignore") as file:
    data = []
    limit = 10  # limit the output
    count = 0  # Counter for the number of events displayed
    # Read the content of the file line by line
    for line in file:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
        # Process each line as JSON
        try:
            event = json.loads(line)
            if event["eventType"] == "SETTLEMENT":
                # Handle settlement event
                print("Settlement:", event)
                # Extract relevant information and perform further processing
            elif event["eventType"] == "WITHDRAWAL":
                # Handle withdrawal event
                print("Withdrawal:", event)
                # Extract relevant information and perform further processing
            else:
                # Handle other event types if needed
                print("Unknown event type:", event)
            count += 1
            if count >= limit:
                break  # Exit the loop if the limit is reached
        except json.JSONDecodeError as e:
            print(f"Error parsing line: {line}")
            print(f"Error message: {e}")
