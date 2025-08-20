// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000,
    once: false,
    mirror: true,
    offset: 100
});

// Dynamic Booking Counter
let bookingCount = 80;
const counterElement = document.getElementById('bookingCount');

// Simulate real-time bookings
function incrementCounter() {
    const randomIncrement = Math.random() < 0.3; // 30% chance to increment
    if (randomIncrement) {
        bookingCount++;
        animateCounter(counterElement, bookingCount - 1, bookingCount, 500);
        
        // Save to localStorage
        localStorage.setItem('bookingCount', bookingCount);
    }
}

// Animate counter changes
function animateCounter(element, start, end, duration) {
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 16);
}

// Load saved count or use default
const savedCount = localStorage.getItem('bookingCount');
if (savedCount) {
    bookingCount = parseInt(savedCount);
    if (counterElement) {
        counterElement.textContent = bookingCount;
    }
}

// Increment counter periodically
setInterval(incrementCounter, 15000); // Check every 15 seconds

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Animated number counting for stats
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumbers = entry.target.querySelectorAll('.stat-number[data-target]');
            statNumbers.forEach(stat => {
                const target = parseInt(stat.getAttribute('data-target'));
                const duration = 2000;
                const increment = target / (duration / 16);
                let current = 0;
                
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    stat.textContent = Math.floor(current);
                }, 16);
            });
            statsObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe hero stats
const heroStats = document.querySelector('.hero-stats');
if (heroStats) {
    statsObserver.observe(heroStats);
}

// Parallax effect on scroll
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.hero');
    
    parallaxElements.forEach(element => {
        const speed = 0.5;
        element.style.transform = `translateY(${scrolled * speed}px)`;
    });
    
    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    if (scrolled > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Form submission handling
const preBookForm = document.getElementById('preBookForm');
const successMessage = document.getElementById('successMessage');

if (preBookForm) {
    preBookForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(preBookForm);
        const data = Object.fromEntries(formData);
        
        // Add timestamp
        data.timestamp = new Date().toISOString();
        
        try {
            const response = await fetch('/api/pre-book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                // Show success message
                preBookForm.style.display = 'none';
                successMessage.style.display = 'block';
                
                // Increment counter
                bookingCount++;
                animateCounter(counterElement, bookingCount - 1, bookingCount, 500);
                localStorage.setItem('bookingCount', bookingCount);
                
                // Scroll to success message
                successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                
                // Reset form after 5 seconds
                setTimeout(() => {
                    preBookForm.reset();
                    preBookForm.style.display = 'flex';
                    successMessage.style.display = 'none';
                }, 5000);
            } else {
                alert('Something went wrong. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error submitting form. Please try again.');
        }
    });
}

// Mouse move animation for floating elements
document.addEventListener('mousemove', (e) => {
    const shapes = document.querySelectorAll('.shape');
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    
    shapes.forEach((shape, index) => {
        const speed = (index + 1) * 20;
        shape.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
    });
});

// Timeline animation for How It Works section
const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const timeline = entry.target.querySelector('.timeline-line');
            if (timeline) {
                timeline.style.animation = 'growLine 2s ease-out forwards';
            }
        }
    });
}, observerOptions);

const howItWorks = document.querySelector('.how-it-works');
if (howItWorks) {
    timelineObserver.observe(howItWorks);
}

// Typing effect for hero title
function typeWriter(element, text, speed = 50) {
    let i = 0;
    element.textContent = '';
    
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Apply typing effect when page loads
window.addEventListener('load', () => {
    const heroTitle = document.querySelector('.hero-title .gradient-text');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        setTimeout(() => {
            typeWriter(heroTitle, originalText, 50);
        }, 500);
    }
});

// Scroll reveal animations
const revealElements = document.querySelectorAll('.feature-card, .pricing-card, .step');
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add('revealed');
            }, index * 100);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px'
});

revealElements.forEach(element => {
    revealObserver.observe(element);
});

// Remove excessive button animations - keep it professional

// Particle background effect (optional)
function createParticle() {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.left = Math.random() * window.innerWidth + 'px';
    particle.style.animationDuration = Math.random() * 3 + 2 + 's';
    particle.style.opacity = Math.random();
    particle.style.animationDelay = Math.random() * 2 + 's';
    document.body.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
    }, 5000);
}

// Create particles periodically (reduced frequency for less distraction)
setInterval(createParticle, 1000);

// Mobile menu toggle
const mobileMenuBtn = document.createElement('button');
mobileMenuBtn.className = 'mobile-menu-btn';
mobileMenuBtn.innerHTML = '☰';
document.querySelector('.navbar .container').appendChild(mobileMenuBtn);

mobileMenuBtn.addEventListener('click', () => {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('mobile-active');
});

// Progress bar on scroll
const progressBar = document.createElement('div');
progressBar.className = 'scroll-progress';
document.body.appendChild(progressBar);

window.addEventListener('scroll', () => {
    const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (window.scrollY / windowHeight) * 100;
    progressBar.style.width = scrolled + '%';
});