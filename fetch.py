import sqlite3
import json

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute('''SELECT * FROM customers_sales''')
    data = cursor.fetchall()

    conn.close()

    # Convert data to JSON format
    json_data = []
    for row in data:
        json_data.append({
            "Index": row[0],
            "Customer Id": row[1],
            "First Name": row[2],
            "Last Name": row[3],
            "Company": row[4],
            "City": row[5],
            "Country": row[6],
            "Phone 1": row[7],
            "Phone 2": row[8],
            "Email": row[9],
            "Subscription Date": row[10],
            "Website": row[11],
            "SALES 2021": row[12],
            "SALES 2022": row[13]
            # Add more columns as needed
        })

    return json_data

if __name__ == "__main__":
    fetched_data = fetch_data()
    with open('data.json', 'w') as outfile:
        json.dump(fetched_data, outfile)  # Output the fetched data in JSON format
