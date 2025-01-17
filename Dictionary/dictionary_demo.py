user_details = {
    "user_id": 1001,
    "user_name": "Alice",
    "user_email": "alice@example.com",
    "user_password": "123456",
    "user_address": {
        "present_address":{
           "city": "dhaka",
            "street": 123,
            "post_Code": [12,44,55]
        },
        "permanent_address":{
            "city": "NY",
            "street": "47 New Avenue",
            "post_Code": [1221,4544,48455]
        }
    }
}

user_name = user_details["user_name"]
print(user_name)

print(len(user_details))

city = user_details["user_address"]["permanent_address"]["city"]
print(city)

post_code = user_details["user_address"]["permanent_address"]["post_Code"][0]
print(post_code)