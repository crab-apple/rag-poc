from sample_data import generate_users

if __name__ == "__main__":
    users = generate_users(1000)
    print(f"Generated {len(users)} users. First 10:\n")
    for user in users[:10]:
        print(f"  {user.name}")
        for position in user.employment_history:
            print(f"    {position.title} at {position.company}")
