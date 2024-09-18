import sqlite3
from datetime import datetime

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """Create tables for products and transactions"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                product_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                total REAL NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        self.conn.commit()

    def add_product(self, name, price, quantity):
        """Add a product to the table"""
        self.cursor.execute('''
            INSERT INTO products (name, price, quantity)
            VALUES (?, ?, ?)
        ''', (name, price, quantity))
        self.conn.commit()

    def get_all_products(self):
        """Get all products from the table"""
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def get_product_by_id(self, id):
        """Get a product by ID"""
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def edit_product(self, id, name, price, quantity):
        """Edit a product"""
        self.cursor.execute('''
            UPDATE products
            SET name = ?, price = ?, quantity = ?
            WHERE id = ?
        ''', (name, price, quantity, id))
        self.conn.commit()

    def delete_product(self, id):
        """Delete a product"""
        self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        self.conn.commit()

    def add_transaction(self, product_id, transaction_type, quantity):
        """Add a transaction"""
        product = self.get_product_by_id(product_id)
        if product:
            total = product[2] * quantity
            self.cursor.execute('''
                INSERT INTO transactions (product_id, transaction_type, quantity, total, date)
                VALUES (?, ?, ?, ?, ?)
            ''', (product_id, transaction_type, quantity, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            self.conn.commit()
            if transaction_type == 'sale':
                self.cursor.execute('''
                    UPDATE products
                    SET quantity = quantity - ?
                    WHERE id = ?
                ''', (quantity, product_id))
            elif transaction_type == 'purchase':
                self.cursor.execute('''
                    UPDATE products
                    SET quantity = quantity + ?
                    WHERE id = ?
                ''', (quantity, product_id))
            self.conn.commit()
        else:
            print("Product not found.")

    def get_all_transactions(self):
        """Get all transactions"""
        self.cursor.execute('SELECT * FROM transactions')
        return self.cursor.fetchall()

    def close_connection(self):
        """Close the database connection"""
        self.conn.close()


# Example usage
if __name__ == '__main__':
    db_name = 'products.db'
    product_db = ProductDatabase(db_name)
    product_db.create_tables()

    # Add products
    product_db.add_product('Apple iPhone', 999.99, 100)
    product_db.add_product('Samsung TV', 1299.99, 50)
    product_db.add_product('Sony Headphones', 99.99, 200)

    # Get all products
    print("All products:")
    for product in product_db.get_all_products():
        print(product)

    # Add transactions
    product_db.add_transaction(1, 'sale', 10)
    product_db.add_transaction(2, 'purchase', 20)
    product_db.add_transaction(3, 'sale', 30)

    # Get all transactions
    print("\nAll transactions:")
    for transaction in product_db.get_all_transactions():
        print(transaction)

    # Get all products again to see the changes
    print("\nAll products after transactions:")
    for product in product_db.get_all_products():
        print(product)

    product_db.close_connection()