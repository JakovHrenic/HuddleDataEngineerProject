import json

# Open the JSON file
with open("transactions.data", "r", encoding="utf-8", errors="ignore") as file:
    data = []
    # Read the content of the file line by line
    for line in file:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
        # Process each line as JSON
        try:
            transaction = json.loads(line)
            data.append(transaction)
        except json.JSONDecodeError as e:
            print(f"Error parsing line: {line}")
            print(f"Error message: {e}")

    # Process a limited number of extracted data
    limit = 10  # limit the output
    for i, transaction in enumerate(data[:limit]):
        # Print the entire transaction object
        print(f"Transaction {i+1}: {transaction}")
