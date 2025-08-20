# CallFlow AI Landing Page

A modern, animated landing page for CallFlow AI with pre-booking functionality and admin dashboard.

## Features

### Landing Page
- ✨ Beautiful scroll animations using AOS (Animate On Scroll)
- 🎯 Dynamic booking counter starting from 80+
- 🎨 Modern gradient design with floating shapes
- 📱 Fully responsive design
- 🚀 Smooth parallax effects
- ⚡ Real-time particle animations
- 📊 Interactive statistics counters

### Pre-Booking System
- 📝 Easy pre-booking form
- 💾 Automatic Excel export
- 🗄️ SQLite database storage
- 📈 Real-time booking counter
- ✅ Form validation
- 🎉 Success animations

### Admin Dashboard
- 📊 View all pre-bookings
- 📈 Statistics overview
- 💾 Export to Excel functionality
- 🔄 Auto-refresh every 30 seconds
- 📱 Responsive table design

## Installation

1. Navigate to the landing_page folder:
```bash
cd landing_page
```

2. Install dependencies:
```bash
pip install flask pandas openpyxl
```

## Running the Application

### Windows
Double-click `run_landing_page.bat` or run:
```bash
run_landing_page.bat
```

### Manual Start
```bash
python landing_app.py
```

## Access Points

- **Landing Page**: http://localhost:5001
- **Admin Dashboard**: http://localhost:5001/admin/bookings
- **API Endpoints**:
  - POST `/api/pre-book` - Submit pre-booking
  - GET `/api/bookings/count` - Get booking count
  - GET `/api/bookings/export` - Export to Excel
  - GET `/api/bookings/stats` - Get statistics

## Excel Export

Pre-bookings are automatically saved in two ways:

1. **Automatic Save**: Every booking is saved to `prebookings.xlsx`
2. **Manual Export**: Click "Export to Excel" button in admin dashboard

## File Structure

```
landing_page/
├── landing_app.py          # Flask application
├── prebookings.db          # SQLite database (auto-created)
├── prebookings.xlsx        # Excel file (auto-created)
├── templates/
│   ├── landing.html        # Landing page
│   └── admin_bookings.html # Admin dashboard
├── static/
│   ├── css/
│   │   └── landing.css     # Styles with animations
│   └── js/
│       └── landing.js      # Interactive features
└── run_landing_page.bat    # Windows startup script
```

## Customization

### Change Company Name
Edit `templates/landing.html` and replace "CallFlow AI" with your company name.

### Modify Starting Counter
Edit `landing_app.py` line 89 and change the base count (currently 80).

### Update Pricing
Edit the pricing section in `templates/landing.html`.

### Change Colors
Modify CSS variables in `static/css/landing.css`:
```css
:root {
    --primary: #6366f1;
    --secondary: #14b8a6;
    --gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

## Features Breakdown

### Animations
- Scroll-triggered animations (AOS)
- Floating geometric shapes
- Parallax scrolling
- Number counting animations
- Typing effect on hero title
- Particle effects
- Timeline animations

### Pre-Booking Form
- Name, Email, Company (required)
- Team size dropdown
- Phone (optional)
- Plan selection
- Automatic validation
- Success message with animation

### Admin Features
- Total bookings count
- Last 7 days bookings
- Most popular plan
- Average team size
- Sortable table
- Excel export
- Auto-refresh

## Support

For any issues or customization requests, please check the code comments or create an issue in the repository.