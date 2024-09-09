import time
import os

# Function to read the students.txt file and organize the data
def read_students_file(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    # Split the line into components and validate the number of fields
                    fields = line.split(',')
                    if len(fields) == 7:
                        st_last_name, st_first_name, grade, classroom, bus, t_last_name, t_first_name = fields
                        student = {
                            'StLastName': st_last_name,
                            'StFirstName': st_first_name,
                            'Grade': int(grade),
                            'Classroom': int(classroom),
                            'Bus': int(bus),
                            'TLastName': t_last_name,
                            'TFirstName': t_first_name
                        }
                        students.append(student)
                    else:
                        print(f"Invalid line format: {line}")
    except FileNotFoundError:
        print(f"File {filename} not found. Exiting the program.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)
    return students

# Search for students by last name
def search_student_by_lastname(students, lastname):
    results = []
    for student in students:
        if student['StLastName'] == lastname:
            results.append(
                f"{student['StLastName']} {student['StFirstName']}, Classroom: {student['Classroom']}, Teacher: {student['TFirstName']} {student['TLastName']}")
    return results

# Search for the bus route by student's last name
def search_student_bus_by_lastname(students, lastname):
    results = []
    for student in students:
        if student['StLastName'] == lastname:
            results.append(f"{student['StLastName']} {student['StFirstName']}, Bus: {student['Bus']}")
    return results

# Search for students by teacher's last name
def search_students_by_teacher(students, teacher_lastname):
    results = []
    for student in students:
        if student['TLastName'] == teacher_lastname:
            results.append(f"{student['StLastName']} {student['StFirstName']}")
    return results

# Search for students by classroom number
def search_students_by_classroom(students, classroom):
    results = []
    for student in students:
        if student['Classroom'] == classroom:
            results.append(f"{student['StLastName']} {student['StFirstName']}")
    return results

# Search for students by bus number
def search_students_by_bus(students, bus_number):
    results = []
    for student in students:
        if student['Bus'] == bus_number:
            results.append(
                f"{student['StLastName']} {student['StFirstName']}, Grade: {student['Grade']}, Classroom: {student['Classroom']}")
    return results

# Function to display search time
def print_search_results(results, start_time):
    for result in results:
        print(result)
    elapsed_time = time.time() - start_time
    print(f"Search time: {elapsed_time:.4f} seconds")

# Main function to handle user commands
def main():
    filename = 'students.txt'
    if not os.path.exists(filename):
        print(f"File {filename} not found. Exiting the program.")
        return

    students = read_students_file(filename)

    while True:
        try:
            # Convert the input to uppercase for case-insensitive matching
            command = input(
                "Enter a command (S[tudent] <lastname>, S[tudent] <lastname> B[us], T[eacher] <lastname>, C[lassroom] <number>, B[us] <number>, Q[uit]): ").strip().upper()

            if command.startswith('S '):
                parts = command.split()

                # Check for S <lastname> B (bus route search)
                if len(parts) == 3 and parts[2] == 'B':
                    lastname = parts[1]
                    start_time = time.time()
                    results = search_student_bus_by_lastname(students, lastname)
                    print_search_results(results, start_time)

                # Check for S <lastname> (general student info search)
                elif len(parts) == 2:
                    lastname = parts[1]
                    start_time = time.time()
                    results = search_student_by_lastname(students, lastname)
                    print_search_results(results, start_time)

                else:
                    print("Invalid command format for S <lastname> or S <lastname> B.")

            elif command.startswith('T '):
                _, teacher_lastname = command.split(' ', 1)
                start_time = time.time()
                results = search_students_by_teacher(students, teacher_lastname)
                print_search_results(results, start_time)

            elif command.startswith('C '):
                _, classroom = command.split(' ', 1)
                start_time = time.time()
                results = search_students_by_classroom(students, int(classroom))
                print_search_results(results, start_time)

            elif command.startswith('B '):
                _, bus_number = command.split(' ', 1)
                start_time = time.time()
                results = search_students_by_bus(students, int(bus_number))
                print_search_results(results, start_time)

            elif command == 'Q':
                print("Exiting the program.")
                break

            else:
                print("Unknown command. Please try again.")

        except ValueError:
            print("Invalid input. Please ensure that numbers are entered where required.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()