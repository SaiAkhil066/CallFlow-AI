# Logo Setup Instructions

## Where to Place Your Logo

Place your `logo.png` file in the following location:
```
landing_page/
├── static/
│   ├── images/        <-- Place logo.png here
│   │   └── logo.png
│   ├── css/
│   └── js/
```

## Full Path
`D:\PHILL\AI-SDR\landing_page\static\images\logo.png`

## Logo Specifications
- **Recommended Size**: 200x60px or similar aspect ratio
- **Format**: PNG with transparent background preferred
- **File Name**: Must be named `logo.png`

## Where Logo Appears
1. **Navigation Bar** - Top left, next to "CallFlow AI" text (45px height)
2. **Footer** - Bottom of page, next to company name (40px height, white version)

## CSS Adjustments
If your logo needs size adjustments, modify these values in `static/css/modern-landing.css`:

```css
.logo-img {
    height: 45px;  /* Adjust navigation logo height */
}

.footer-logo {
    height: 40px;  /* Adjust footer logo height */
}
```

## Note
The footer logo automatically converts to white using CSS filters for dark background visibility.