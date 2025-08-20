import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from landing_app import app

# Vercel serverless function handler
def handler(request, response):
    return app(request, response)