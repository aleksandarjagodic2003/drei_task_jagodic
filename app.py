import csv
import sqlite3

# Function to create SQLite database and table
def create_database():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers_sales (
                    "Index" INTEGER,
                    "Customer Id" TEXT,
                    "First Name" TEXT,
                    "Last Name" TEXT,
                    "Company" TEXT,
                    "City" TEXT,
                    "Country" TEXT,
                    "Phone 1" TEXT,
                    "Phone 2" TEXT,
                    "Email" TEXT,
                    "Subscription Date" TEXT,
                    "Website" TEXT,
                    "SALES 2021" TEXT,
                    "SALES 2022" TEXT
                )''')
    conn.commit()
    conn.close()
    
def import_data_from_csv(csv_file):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file,"utf-8")
        for row in csv_reader:
            #print(row.get('u').split(';'))
            if len(row.get('u').split(';')) is 14:
                cursor.execute('''INSERT INTO customers_sales ("Index","Customer Id","First Name","Last Name","Company","City","Country","Phone 1","Phone 2","Email","Subscription Date", "Website","SALES 2021","SALES 2022")
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                            (row.get('u').split(';')[0], row.get('u').split(';')[1], row.get('u').split(';')[2], row.get('u').split(';')[3], row.get('u').split(';')[4], row.get('u').split(';')[5], row.get('u').split(';')[6],row.get('u').split(';')[7], row.get('u').split(';')[8], row.get('u').split(';')[9], row.get('u').split(';')[10], row.get('u').split(';')[11], row.get('u').split(';')[12],row.get('u').split(';')[13]))
            elif len(row.get('u').split(';')) is 5:
                 cursor.execute('''INSERT INTO customers_sales ("Index","Customer Id","First Name","Last Name","Company")
                                VALUES (?, ?, ?, ?, ?)''', 
                            (row.get('u').split(';')[0], row.get('u').split(';')[1], row.get('u').split(';')[2], row.get('u').split(';')[3], row.get('u').split(';')[4]))
                
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    import_data_from_csv('customers_sales_2021_2022.csv')
    print("Data imported successfully.")
