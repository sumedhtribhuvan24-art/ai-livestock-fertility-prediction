import json
import os
import hashlib
from datetime import datetime

USERS_FILE = "users.json"

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def authenticate_user(username, password):
    """Authenticate user login"""
    users = load_users()
    if username in users:
        hashed_password = hash_password(password)
        return users[username]['password'] == hashed_password
    return False

def register_user(username, password):
    """Register new user"""
    users = load_users()
    
    # Check if username already exists
    if username in users:
        return False
    
    # Add new user
    users[username] = {
        'password': hash_password(password),
        'created_at': str(datetime.now()),
        'role': 'user'  # Default role
    }
    
    save_users(users)
    return True

def is_admin(username):
    """Check if user is admin"""
    users = load_users()
    if username in users:
        return users[username].get('role', 'user') == 'admin' or username == 'admin'
    return False

# Initialize with demo users if file doesn't exist
def initialize_demo_users():
    """Create demo users for testing"""
    if not os.path.exists(USERS_FILE):
        demo_users = {
            'farmer1': {
                'password': hash_password('demo123'),
                'created_at': str(datetime.now()),
                'role': 'user'
            },
            'admin': {
                'password': hash_password('admin123'),
                'created_at': str(datetime.now()),
                'role': 'admin'
            }
        }
        save_users(demo_users)

# Initialize demo users on import
initialize_demo_users()