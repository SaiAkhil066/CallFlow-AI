from flask import Flask, render_template, request, jsonify, send_file
import json
import os
from datetime import datetime
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Store bookings in memory (for demo purposes)
# In production, use a database service like Supabase or PostgreSQL
bookings_data = []
booking_count = 80  # Starting count

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/api/pre-book', methods=['POST'])
def pre_book():
    try:
        global booking_count
        data = request.json
        
        # Generate unique access code
        import random
        import string
        access_code = 'VIP-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Add to bookings
        booking_data = {
            'id': len(bookings_data) + 1,
            'name': data.get('name'),
            'email': data.get('email'),
            'company': data.get('company'),
            'team_size': data.get('team_size'),
            'phone': data.get('phone', ''),
            'plan': data.get('plan'),
            'timestamp': datetime.now().isoformat(),
            'access_code': access_code,
            'status': 'pending'
        }
        
        bookings_data.append(booking_data)
        booking_count += 1
        
        # Log to console (Vercel logs)
        print(f"New booking: {booking_data['email']}")
        
        return jsonify({
            'success': True,
            'booking_id': booking_data['id'],
            'access_code': access_code,
            'message': 'Welcome to the exclusive pre-launch!'
        }), 200
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/bookings/count', methods=['GET'])
def get_booking_count():
    return jsonify({'count': booking_count})

@app.route('/api/bookings/export', methods=['GET'])
def export_bookings():
    """Export bookings to Excel"""
    if not bookings_data:
        # Create sample data if empty
        df = pd.DataFrame([{
            'id': 1,
            'name': 'Sample User',
            'email': 'sample@example.com',
            'company': 'Sample Co',
            'team_size': '1-5',
            'phone': '',
            'plan': 'starter',
            'timestamp': datetime.now().isoformat(),
            'status': 'pending'
        }])
    else:
        df = pd.DataFrame(bookings_data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Pre-Bookings', index=False)
    
    output.seek(0)
    
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=f'prebookings_{datetime.now().strftime("%Y%m%d")}.xlsx'
    )

@app.route('/admin/bookings')
def admin_bookings():
    return render_template('admin_bookings.html', bookings=bookings_data)

@app.route('/api/bookings/stats', methods=['GET'])
def get_booking_stats():
    total = booking_count
    recent = len([b for b in bookings_data if b.get('timestamp', '') > datetime.now().isoformat()[:10]])
    
    # Calculate stats
    by_plan = {}
    by_team_size = {}
    
    for booking in bookings_data:
        plan = booking.get('plan', 'unknown')
        by_plan[plan] = by_plan.get(plan, 0) + 1
        
        team_size = booking.get('team_size', 'unknown')
        by_team_size[team_size] = by_team_size.get(team_size, 0) + 1
    
    return jsonify({
        'total': total,
        'by_plan': by_plan,
        'by_team_size': by_team_size,
        'recent_7_days': recent
    })

# For Vercel
app.debug = False