def main():
    room = {'CIS401': 'TR101',
            'CIS402': 'TR402',
            'CIS403': 'TR403',
            'CIS404': 'TR404',
            'CIS303': 'TR303',}

    teacher = {'CIS401': 'Kara',
            'CIS402': 'Jacob',
            'CIS403': 'Skye',
            'CIS404': 'Malik',
            'CIS303': 'Kachoon',}

    classTime = {'CIS401': '8:00 am',
    'CIS403': '9:00 am',
    'CIS404': '10:30 am',
    'CIS303': '3:30 pm',}

    print("---------------------------------------------")
    print("\tCourse Info")
    print("---------------------------------------------")
    name = input('Enter Your name: ')
    lcj = input('Enter course number: ')
    print("---------------------------------------------")


    lcj = lcj.upper()

    if lcj not in room:
        print(f"{lcj} is not a valid course number.")
        print(f"Return program to look up a valid course.")

    else:
        print(f"Room: {room[lcj]}\nInstructor: {teacher[lcj]}\nTime: {classTime[lcj]}")

        print("---------------------------------------------")

main()



DEF main()
    room = {'CIS401': 'TR101',
            'CIS402': 'TR402',
            'CIS403': 'TR403',
            'CIS404': 'TR404',
            'CIS303': 'TR303',}

    teacher = {'CIS401': 'Kara',
            'CIS402': 'Jacob',
            'CIS403': 'Skye',
            'CIS404': 'Malik',
            'CIS303': 'Kachoon',}

    classTime = {'CIS401': '8:00 am',
    'CIS403': '9:00 am',
    'CIS404': '10:30 am',
    'CIS303': '3:30 pm',}

    PROMPT for name 
    DISPLAY "Enter name: "
    PROMPT for course
    DISPLAY "Enter coursee number: "

    IF lcj not in room:    
        DISPLAY "{lcj} is not a valid course number."
        DISPLAY "Return program to look up a valid course."

    ELSE:
        DISPLAY "Room: {room[lcj]}\nInstructor: {teacher[lcj]}\nTime: {classTime[lcj]}"

MAIN()
