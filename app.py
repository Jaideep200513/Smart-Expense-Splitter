from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
import os 

app = Flask(__name__)

# --- Use a relative path for the database ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH) 
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    members = conn.execute('SELECT * FROM members').fetchall()
    expenses = conn.execute('''
        SELECT expenses.id, members.name, expenses.category, expenses.amount, expenses.date
        FROM expenses
        JOIN members ON expenses.member_id = members.id
        ORDER BY date DESC
    ''').fetchall()
    conn.close()
    return render_template('index.html', members=members, expenses=expenses)

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['member_name']
    if name: 
        conn = get_db_connection()
        conn.execute('INSERT OR IGNORE INTO members (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
    return redirect('/')

# --- FUNCTION TO DELETE A MEMBER ---
@app.route('/delete_member', methods=['POST'])
def delete_member():
    member_id = request.form.get('member_id')
    if member_id:
        conn = get_db_connection()
        conn.execute('DELETE FROM members WHERE id = ?', (member_id,))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    member_id = request.form.get('member_id')
    category = request.form.get('category')
    amount_str = request.form.get('amount')

    if not all([member_id, category, amount_str]):
        return redirect('/')

    try:
        amount = float(amount_str)
        date = datetime.now().strftime('%Y-%m-%d') 
        conn = get_db_connection()
        conn.execute('INSERT INTO expenses (member_id, category, amount, date) VALUES (?, ?, ?, ?)',
                     (int(member_id), category, amount, date))
        conn.commit()
        conn.close()
    except (ValueError, TypeError):
        print("Error adding expense: Invalid data.")
    
    return redirect('/')

# --- ADVANCED SUMMARY FUNCTION ---
@app.route('/summary')
def summary():
    conn = get_db_connection()
    members = conn.execute('SELECT * FROM members').fetchall()
    expenses = conn.execute('SELECT member_id, amount FROM expenses').fetchall()
    conn.close()

    if not members:
        return render_template('summary.html', summary=[], settlements=[])

    # 1. Calculate total paid by each member
    paid_by = {member['id']: 0 for member in members}
    member_names = {member['id']: member['name'] for member in members}
    total_spent = 0
    
    for expense in expenses:
        if expense['member_id'] in paid_by:
            paid_by[expense['member_id']] += expense['amount']
            total_spent += expense['amount']
        else:
            print(f"Warning: Found expense for unknown member_id {expense['member_id']}")

    # 2. Calculate the split
    num_members = len(members)
    if num_members == 0 or total_spent == 0:
        summary_data = [{'name': name, 'total': paid_by.get(mid, 0)} for mid, name in member_names.items()]
        return render_template('summary.html', summary=summary_data, settlements=[])

    cost_per_person = total_spent / num_members

    # 3. Calculate balances
    balances = {mid: paid - cost_per_person for mid, paid in paid_by.items()}
    
    # 4. Separate into who owes and who is owed
    owes = {mid: -balance for mid, balance in balances.items() if balance < -0.01}
    owed = {mid: balance for mid, balance in balances.items() if balance > 0.01}
    
    # 5. Calculate settlements
    settlements = []
    owers_list = sorted(owes.items(), key=lambda x: x[1], reverse=True)
    owed_list = sorted(owed.items(), key=lambda x: x[1], reverse=True)

    ower_idx = 0
    owed_idx = 0
    
    while ower_idx < len(owers_list) and owed_idx < len(owed_list):
        ower_id, ower_amount = owers_list[ower_idx]
        owed_id, owed_amount = owed_list[owed_idx]
        payment = min(ower_amount, owed_amount)
        
        if payment > 0.01: 
            settlements.append({
                'owes': member_names[ower_id],
                'owed': member_names[owed_id],
                'amount': payment
            })

            ower_amount -= payment
            owed_amount -= payment
            
            owers_list[ower_idx] = (ower_id, ower_amount)
            owed_list[owed_idx] = (owed_id, owed_amount)

        if ower_amount < 0.01:
            ower_idx += 1
        if owed_amount < 0.01:
            owed_idx += 1

    # 6. Prepare summary data for display
    summary_data = [{'name': name, 'total': paid_by.get(mid, 0)} for mid, name in member_names.items()]
    
    # 7. Pass both lists to the template
    return render_template('summary.html', summary=summary_data, settlements=settlements)

# --- "RESET EXPENSES" FUNCTION ---
@app.route('/reset', methods=['POST']) 
def reset():
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses')
    conn.execute('DELETE FROM sqlite_sequence WHERE name = ?', ('expenses',))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)