def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome,aboard")


greet("Huy","Ha")

# 1- perfrom a task
# 2- Return a value

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Huy")
print(message)