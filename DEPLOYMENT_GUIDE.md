# 🚀 Deployment Guide for CallFlow AI Landing Page

## Option 1: Vercel (Recommended - Full Features)

### Prerequisites
- GitHub account
- Vercel account (free at vercel.com)

### Steps:

1. **Prepare your repository**
   ```bash
   cd landing_page
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub**
   - Create a new repository on GitHub
   - Push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/callflow-landing.git
   git push -u origin main
   ```

3. **Deploy on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Vercel will auto-detect Flask and use settings from `vercel.json`
   - Click "Deploy"

4. **Environment Variables (if needed)**
   - In Vercel dashboard → Settings → Environment Variables
   - Add any secrets or API keys

### Your site will be live at: `https://your-project.vercel.app`

---

## Option 2: Netlify (Static Version Only)

### Prerequisites
- GitHub/GitLab account
- Netlify account (free at netlify.com)
- Formspree account for form handling (free at formspree.io)

### Steps:

1. **Set up Formspree**
   - Go to [formspree.io](https://formspree.io)
   - Create a new form
   - Get your form ID (looks like: `xyzabc123`)
   - Update `static_version/index.html`:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

2. **Prepare static files**
   ```bash
   cd landing_page/static_version
   cp -r ../static/css .
   cp -r ../static/js .
   cp -r ../static/images .
   ```

3. **Deploy on Netlify**
   
   **Method A: Drag & Drop**
   - Go to [netlify.com](https://netlify.com)
   - Drag the `static_version` folder to the deployment area
   
   **Method B: Git Integration**
   - Push to GitHub/GitLab
   - In Netlify: New site from Git
   - Select repository
   - Build settings:
     - Publish directory: `static_version`
   - Deploy site

### Your site will be live at: `https://amazing-name-123.netlify.app`

---

## Option 3: Vercel with Supabase (Full Features + Database)

For production with persistent database:

1. **Set up Supabase (Free)**
   - Create account at [supabase.com](https://supabase.com)
   - Create new project
   - Go to SQL Editor and create table:
   ```sql
   CREATE TABLE prebookings (
     id SERIAL PRIMARY KEY,
     name TEXT NOT NULL,
     email TEXT NOT NULL,
     company TEXT NOT NULL,
     team_size TEXT NOT NULL,
     phone TEXT,
     plan TEXT NOT NULL,
     timestamp TIMESTAMP DEFAULT NOW(),
     status TEXT DEFAULT 'pending',
     access_code TEXT UNIQUE
   );
   ```

2. **Update Flask app**
   - Install: `pip install supabase`
   - Update `landing_app.py` to use Supabase instead of SQLite

3. **Add environment variables in Vercel**
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

---

## Free Tier Limits

### Vercel Free Tier
- ✅ 100GB bandwidth/month
- ✅ Serverless functions
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Unlimited websites
- ⚠️ 10 second function timeout

### Netlify Free Tier
- ✅ 100GB bandwidth/month
- ✅ 300 build minutes/month
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Form submissions (100/month)
- ⚠️ Static sites only (unless using Netlify Functions)

### Formspree Free Tier
- ✅ 50 submissions/month
- ✅ Email notifications
- ✅ Spam filtering
- ⚠️ Formspree branding

---

## Custom Domain Setup

### For both platforms:
1. Buy domain from Namecheap, GoDaddy, or Google Domains
2. In Vercel/Netlify:
   - Settings → Domains → Add Domain
   - Follow DNS configuration instructions
3. SSL certificate auto-configured

---

## Which Should You Choose?

### Choose Vercel if:
- You want the full Flask backend
- Need database functionality
- Want Excel export feature
- Need dynamic booking counter
- Want admin dashboard

### Choose Netlify if:
- You only need a static landing page
- Form submissions via email are enough
- You want the simplest deployment
- You don't need backend features

---

## Post-Deployment Checklist

- [ ] Test form submissions
- [ ] Check responsive design on mobile
- [ ] Verify logo and images load
- [ ] Test all navigation links
- [ ] Check page load speed
- [ ] Set up Google Analytics (optional)
- [ ] Configure custom domain (optional)
- [ ] Set up email notifications

---

## Troubleshooting

### Vercel Issues
- **"Module not found"**: Check `requirements.txt`
- **Function timeout**: Optimize database queries
- **CORS errors**: Add CORS headers in Flask

### Netlify Issues
- **Form not working**: Check Formspree form ID
- **Images not loading**: Check file paths (case-sensitive)
- **Page not found**: Check `netlify.toml` configuration

---

## Need Help?
- Vercel Docs: https://vercel.com/docs
- Netlify Docs: https://docs.netlify.com
- Formspree Docs: https://formspree.io/docs