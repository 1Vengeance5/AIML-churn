# Task 2 - Level 1

def campus_assistant(user_input):
    responses = {
        "library": "The campus library is open from 9 AM to 8 PM on weekdays.",
        "hostel": "Hostel applications can be submitted through the student portal.",
        "exam": "Examination schedules are available on the official campus website.",
        "canteen": "The campus canteen is open from 8 AM to 10 PM."
    }

    for keyword in responses:
        if keyword in user_input.lower():
            return responses[keyword]

    return "Sorry, I couldn't find information on that. Please contact the campus help desk."


while True:
    user_input = input("Ask the Campus Assistant (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    print("Assistant:", campus_assistant(user_input))
