def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    age = set_age(-5)
except ValueError as e:
    print(f"Error: {e}")

finally:
    print("Execution finished")
