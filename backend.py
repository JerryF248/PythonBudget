import sqlite3
from expense import Expense
# This database class will execute all of our sqlite commands

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS expenses (item_name text, item_cost float, item_category text, purchase_date date)")
        self.conn.commit()
    
    def getExpense(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def insertExpense(self, expense):
        self.cur.execute(f"INSERT INTO expenses VALUES {expense.item_name}, {expense.item_name}, {expense.item_cost}, {expense.item_category}, {expense.date}")
        self.conn.commit()

    def removeExpense(self, eid):
        self.cur.execute("DELETE FROM expenses WHERE rowid=?", (eid, ))
        self.conn.commit()

    def updateExpense(self, expense, eid):
        self.cur.execute("UPDATE expenses SET item_name = ?, item_cost = ?, item_category = ?, purchase_date = ? WHERE rowid = ?)", expense.item_name, expense.item_cost, expense.item_category, expense.date, eid)
        self.conn.commit()