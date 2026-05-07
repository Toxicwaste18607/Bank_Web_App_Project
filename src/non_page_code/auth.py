def check_login(user_id, password):
    users = load_user_data()

    if user_id in users:
        user_data = users[user_id]

        if user_data["password"] == password:
            return User(
                user_id=user_id,
                name=user_data["name"],
                role=user_data["role"],
                balance=user_data["balance"],
                email=user_data["email"]
            )

    return None