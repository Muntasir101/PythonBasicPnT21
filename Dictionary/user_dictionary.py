users = {
    "user_001": {
        "personal_info": {
            "name": "Alice Johnson",
            "age": 29,
            "gender": "Female",
            "contact": {
                "email": "alice.johnson@example.com",
                "phone": "+1234567890",
                "address": {
                    "street": "123 Elm St",
                    "city": "Springfield",
                    "state": "IL",
                    "zip": "62704",
                },
            },
        },
        "preferences": {
            "language": "English",
            "notifications": {
                "email": True,
                "sms": False,
                "push": True,
            },
            "theme": "Dark",
        },
        "account": {
            "username": "alicej",
            "password": "securepassword123",  # In real systems, use hashed passwords
            "created_at": "2023-10-01",
            "last_login": "2025-01-15",
            "status": "Active",
        },
        "roles": ["Admin", "Editor"],
        "activity": {
            "last_action": "Updated profile",
            "recent_logins": [
                "2025-01-15 10:30:00",
                "2025-01-14 18:45:00",
                "2025-01-10 09:00:00",
            ],
        },
    },
    "user_002": {
        "personal_info": {
            "name": "Bob Smith",
            "age": 34,
            "gender": "Male",
            "contact": {
                "email": "bob.smith@example.com",
                "phone": "+0987654321",
                "address": {
                    "street": "456 Oak St",
                    "city": "Metropolis",
                    "state": "NY",
                    "zip": "10118",
                },
            },
        },
        "preferences": {
            "language": "Spanish",
            "notifications": {
                "email": True,
                "sms": True,
                "push": False,
            },
            "theme": "Light",
        },
        "account": {
            "username": "bobsmith",
            "password": "anothersecurepassword456",
            "created_at": "2022-07-15",
            "last_login": "2025-01-16",
            "status": "Inactive",
        },
        "roles": ["Viewer"],
        "activity": {
            "last_action": "Browsed products",
            "recent_logins": [
                "2025-01-16 14:20:00",
                "2025-01-12 11:50:00",
                "2025-01-08 08:30:00",
            ],
        },
    },
}
