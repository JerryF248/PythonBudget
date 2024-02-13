import sqlite3

# This database class will execute all of our sqlite commands

class Database:
    def __init__(self, db):
        self.conn = sqlite3.conenct(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS expenses (item_name text, item_price float, item_category text, purchase_date date)")
        self.conn.commit()
    
    def getExpense(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def insertExpense(self, item_name, item_price, item_category, purchase_date):
        self.cur.execute("INSERT INTO expenses VALUES (?, ?, ?, ?)", item_name, item_price, item_category, purchase_date)
        self.conn.commit()

    def removeExpense(self, eid):
        self.cur.execute("DELETE FROM expenses WHERE rowid=?", (eid, ))
        self.conn.commit()

    def updateExpense(self, item_name, item_price, item_category, purchase_date, eid):
        self.cur.execute("UPDATE expenses SET item_name = ?, item_price = ?, item_category = ?, purchase_date = ? WHERE rowid = ?)", item_name, item_price, item_category, purchase_date, eid)
        self.conn.commit()