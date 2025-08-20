from flask import Flask, render_template, request, jsonify, send_file
import sqlite3
import pandas as pd
from datetime import datetime
import os
import json
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Database setup
def init_db():
    conn = sqlite3.connect('prebookings.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prebookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            company TEXT NOT NULL,
            team_size TEXT NOT NULL,
            phone TEXT,
            plan TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'pending',
            access_code TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/api/pre-book', methods=['POST'])
def pre_book():
    try:
        data = request.json
        
        # Generate unique access code for exclusive features
        import random
        import string
        access_code = 'VIP-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Save to database
        conn = sqlite3.connect('prebookings.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO prebookings (name, email, company, team_size, phone, plan, timestamp, access_code)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get('name'),
            data.get('email'),
            data.get('company'),
            data.get('team_size'),
            data.get('phone', ''),
            data.get('plan'),
            data.get('timestamp', datetime.now().isoformat()),
            access_code
        ))
        conn.commit()
        booking_id = cursor.lastrowid
        conn.close()
        
        # Also save to Excel for easy access
        data['access_code'] = access_code
        save_to_excel(data)
        
        # Send welcome email (would be implemented with actual email service)
        # send_welcome_email(data.get('email'), data.get('name'), access_code)
        
        return jsonify({
            'success': True,
            'booking_id': booking_id,
            'access_code': access_code,
            'message': 'Welcome to the exclusive pre-launch! Check your email for your VIP access code.'
        }), 200
        
    except Exception as e:
        print(f"Error in pre-booking: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def save_to_excel(data):
    """Save booking data to Excel file"""
    excel_file = 'prebookings.xlsx'
    
    # Create or load existing Excel file
    if os.path.exists(excel_file):
        df_existing = pd.read_excel(excel_file)
        df_new = pd.DataFrame([data])
        df = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df = pd.DataFrame([data])
    
    # Save to Excel
    df.to_excel(excel_file, index=False)

@app.route('/api/bookings/count', methods=['GET'])
def get_booking_count():
    """Get current booking count"""
    conn = sqlite3.connect('prebookings.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM prebookings')
    count = cursor.fetchone()[0]
    conn.close()
    
    # Add base count of 80
    total_count = 80 + count
    
    return jsonify({'count': total_count})

@app.route('/api/bookings/export', methods=['GET'])
def export_bookings():
    """Export all bookings to Excel"""
    conn = sqlite3.connect('prebookings.db')
    df = pd.read_sql_query('SELECT * FROM prebookings ORDER BY timestamp DESC', conn)
    conn.close()
    
    # Create Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Pre-Bookings', index=False)
        
        # Auto-adjust column widths
        worksheet = writer.sheets['Pre-Bookings']
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            worksheet.column_dimensions[chr(65 + col_idx)].width = min(column_width + 2, 50)
    
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=f'prebookings_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    )

@app.route('/admin/bookings')
def admin_bookings():
    """Admin page to view bookings"""
    conn = sqlite3.connect('prebookings.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM prebookings ORDER BY timestamp DESC')
    bookings = cursor.fetchall()
    conn.close()
    
    return render_template('admin_bookings.html', bookings=bookings)

@app.route('/api/bookings/stats', methods=['GET'])
def get_booking_stats():
    """Get booking statistics"""
    conn = sqlite3.connect('prebookings.db')
    cursor = conn.cursor()
    
    # Total bookings
    cursor.execute('SELECT COUNT(*) FROM prebookings')
    total = cursor.fetchone()[0] + 80  # Add base count
    
    # Bookings by plan
    cursor.execute('''
        SELECT plan, COUNT(*) as count 
        FROM prebookings 
        GROUP BY plan
    ''')
    by_plan = dict(cursor.fetchall())
    
    # Bookings by team size
    cursor.execute('''
        SELECT team_size, COUNT(*) as count 
        FROM prebookings 
        GROUP BY team_size
    ''')
    by_team_size = dict(cursor.fetchall())
    
    # Recent bookings (last 7 days)
    cursor.execute('''
        SELECT COUNT(*) 
        FROM prebookings 
        WHERE datetime(timestamp) > datetime('now', '-7 days')
    ''')
    recent = cursor.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'total': total,
        'by_plan': by_plan,
        'by_team_size': by_team_size,
        'recent_7_days': recent
    })

# For Vercel deployment
app.debug = False

if __name__ == '__main__':
    app.run(debug=True, port=5001)