"""
📚 PROJECT: Student Record System - OOP Practice
🎯 OBJECTIVE: Practice OOP concepts with a student management system
📖 DIFFICULTY: Beginner
🔧 CONCEPTS: Classes, Methods, Lists of Objects, Object State Management

This project reinforces OOP concepts by building a student record system
where you can manage students, grades, and calculate statistics.
"""

class Student:
    """
    👨‍🎓 Student Class
    
    Represents a student with grades and personal information.
    
    LEARNING: Object State Management
    - Each object maintains its own state (grades, personal info)
    - Methods can modify and query this state
    """
    
    # Class variable for grade scale
    grade_scale = {
        'A+': (97, 100), 'A': (93, 96), 'A-': (90, 92),
        'B+': (87, 89), 'B': (83, 86), 'B-': (80, 82),
        'C+': (77, 79), 'C': (73, 76), 'C-': (70, 72),
        'D+': (67, 69), 'D': (63, 66), 'D-': (60, 62),
        'F': (0, 59)
    }
    
    total_students = 0
    
    def __init__(self, student_id, name, age, major):
        """
        🔧 Constructor
        
        Initializes a student with personal information.
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.grades = {}  # Dictionary: subject -> list of grades
        self.attendance = []  # List of attendance records
        
        Student.total_students += 1
    
    def add_grade(self, subject, grade):
        """
        ✅ Add Grade Method
        
        Adds a grade for a specific subject.
        
        LEARNING: Working with Dictionaries as Attributes
        - Attributes can be complex data structures
        - Methods can manage these structures
        """
        if not 0 <= grade <= 100:
            print(f"❌ Invalid grade! Must be between 0 and 100.")
            return False
        
        if subject not in self.grades:
            self.grades[subject] = []
        
        self.grades[subject].append(grade)
        print(f"✅ Added grade {grade} for {subject} to {self.name}'s record")
        return True
    
    def get_subject_average(self, subject):
        """
        📊 Calculate Subject Average
        
        Returns average grade for a specific subject.
        """
        if subject not in self.grades or not self.grades[subject]:
            return None
        
        return sum(self.grades[subject]) / len(self.grades[subject])
    
    def get_gpa(self):
        """
        🎓 Calculate GPA
        
        Returns overall GPA (0.0 - 4.0 scale).
        
        LEARNING: Iterating Over Object Data
        - Methods can process all stored data
        - Demonstrates encapsulation: internal calculation
        """
        if not self.grades:
            return 0.0
        
        total_points = 0
        total_grades = 0
        
        for subject, grade_list in self.grades.items():
            for grade in grade_list:
                total_points += self._grade_to_gpa(grade)
                total_grades += 1
        
        return round(total_points / total_grades, 2) if total_grades > 0 else 0.0
    
    def _grade_to_gpa(self, grade):
        """
        🔢 Private Helper Method
        
        Converts numeric grade to GPA scale.
        """
        if grade >= 93:
            return 4.0
        elif grade >= 90:
            return 3.7
        elif grade >= 87:
            return 3.3
        elif grade >= 83:
            return 3.0
        elif grade >= 80:
            return 2.7
        elif grade >= 77:
            return 2.3
        elif grade >= 73:
            return 2.0
        elif grade >= 70:
            return 1.7
        elif grade >= 67:
            return 1.3
        elif grade >= 65:
            return 1.0
        else:
            return 0.0
    
    def get_letter_grade(self, numeric_grade):
        """
        📝 Convert to Letter Grade
        
        Converts numeric grade to letter grade.
        """
        for letter, (min_grade, max_grade) in Student.grade_scale.items():
            if min_grade <= numeric_grade <= max_grade:
                return letter
        return 'F'
    
    def get_overall_letter_grade(self):
        """
        📊 Get Overall Letter Grade
        
        Returns letter grade based on overall average.
        """
        gpa = self.get_gpa()
        avg_numeric = (gpa / 4.0) * 100
        return self.get_letter_grade(avg_numeric)
    
    def mark_attendance(self, date, status):
        """
        ✅ Record Attendance
        
        Records attendance for a specific date.
        
        LEARNING: Working with Lists of Dictionaries
        - Complex data structures for tracking information
        """
        record = {'date': date, 'status': status}
        self.attendance.append(record)
        print(f"✅ Attendance recorded for {self.name} on {date}: {status}")
    
    def get_attendance_rate(self):
        """
        📈 Calculate Attendance Rate
        
        Returns percentage of days present.
        """
        if not self.attendance:
            return 0.0
        
        present_count = sum(1 for record in self.attendance if record['status'] == 'Present')
        return round((present_count / len(self.attendance)) * 100, 2)
    
    def get_grade_report(self):
        """
        📊 Generate Grade Report
        
        Returns comprehensive grade information.
        """
        report = f"\n{'='*60}\n"
        report += f"📋 GRADE REPORT - {self.name}\n"
        report += f"{'='*60}\n"
        report += f"Student ID: {self.student_id}\n"
        report += f"Major: {self.major}\n"
        report += f"Age: {self.age}\n"
        report += f"\n📚 GRADES BY SUBJECT:\n"
        report += f"{'-'*60}\n"
        
        if not self.grades:
            report += "No grades recorded yet.\n"
        else:
            for subject, grade_list in self.grades.items():
                avg = self.get_subject_average(subject)
                letter = self.get_letter_grade(avg)
                report += f"\n{subject}:\n"
                report += f"  Grades: {', '.join(map(str, grade_list))}\n"
                report += f"  Average: {avg:.2f} ({letter})\n"
        
        report += f"\n{'='*60}\n"
        report += f"📊 OVERALL STATISTICS:\n"
        report += f"{'-'*60}\n"
        report += f"GPA: {self.get_gpa():.2f} / 4.0\n"
        report += f"Overall Grade: {self.get_overall_letter_grade()}\n"
        report += f"Attendance Rate: {self.get_attendance_rate():.1f}%\n"
        report += f"{'='*60}\n"
        
        return report
    
    def __str__(self):
        """String representation for printing"""
        gpa = self.get_gpa()
        return f"Student({self.name}, ID: {self.student_id}, GPA: {gpa:.2f})"
    
    def __repr__(self):
        """Developer representation"""
        return f"Student('{self.student_id}', '{self.name}', {self.age}, '{self.major}')"
    
    def __lt__(self, other):
        """
        🔢 Less Than Comparison
        
        Allows sorting students by GPA.
        
        LEARNING: Operator Overloading
        - Magic methods allow custom comparison behavior
        - Enables sorting and comparing objects
        """
        return self.get_gpa() < other.get_gpa()


class StudentDatabase:
    """
    🗄️ StudentDatabase Class
    
    Manages a collection of students.
    
    LEARNING: Composition and Object Collections
    - A class that contains and manages multiple objects
    - Demonstrates separation of concerns
    """
    
    def __init__(self, school_name):
        """Initialize the database"""
        self.school_name = school_name
        self.students = []  # List of Student objects
    
    def add_student(self, student):
        """
        ➕ Add Student
        
        Adds a student to the database.
        
        LEARNING: Managing Collections of Objects
        - Lists can store objects
        - Methods can operate on entire collections
        """
        if any(s.student_id == student.student_id for s in self.students):
            print(f"❌ Student with ID {student.student_id} already exists!")
            return False
        
        self.students.append(student)
        print(f"✅ Added {student.name} to the database")
        return True
    
    def remove_student(self, student_id):
        """Remove a student by ID"""
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"✅ Removed student {student_id}")
                return True
        
        print(f"❌ Student {student_id} not found!")
        return False
    
    def find_student(self, student_id):
        """
        🔍 Find Student
        
        Returns student object by ID.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def get_honor_students(self, gpa_threshold=3.5):
        """
        🏆 Get Honor Students
        
        Returns students with GPA above threshold.
        
        LEARNING: Filtering Collections
        - Using list comprehensions to filter objects
        - Calling methods on objects in collections
        """
        return [s for s in self.students if s.get_gpa() >= gpa_threshold]
    
    def get_top_students(self, n=5):
        """
        ⭐ Get Top Students
        
        Returns top N students by GPA.
        
        LEARNING: Sorting Objects
        - Using sorted() with custom comparison
        - Demonstrates __lt__ magic method usage
        """
        return sorted(self.students, reverse=True)[:n]
    
    def get_class_average(self):
        """
        📊 Calculate Class Average GPA
        
        Returns average GPA of all students.
        """
        if not self.students:
            return 0.0
        
        total_gpa = sum(s.get_gpa() for s in self.students)
        return round(total_gpa / len(self.students), 2)
    
    def generate_class_report(self):
        """
        📋 Generate Class Report
        
        Comprehensive report of all students.
        """
        report = f"\n{'='*60}\n"
        report += f"🏫 CLASS REPORT - {self.school_name}\n"
        report += f"{'='*60}\n"
        report += f"Total Students: {len(self.students)}\n"
        report += f"Class Average GPA: {self.get_class_average():.2f}\n\n"
        
        if self.students:
            report += f"{'Name':<20} {'ID':<10} {'Major':<15} {'GPA':>6}\n"
            report += f"{'-'*60}\n"
            for student in sorted(self.students, reverse=True):
                report += f"{student.name:<20} {student.student_id:<10} {student.major:<15} {student.get_gpa():>6.2f}\n"
        
        return report


def main():
    """Main function demonstrating Student Record System"""
    
    print("=" * 60)
    print("📚 STUDENT RECORD SYSTEM - OOP PRACTICE")
    print("=" * 60)
    
    # Create student database
    db = StudentDatabase("Python University")
    
    # Create students
    print("\n👨‍🎓 Creating Students...")
    alice = Student("S001", "Alice Johnson", 20, "Computer Science")
    bob = Student("S002", "Bob Smith", 21, "Mathematics")
    charlie = Student("S003", "Charlie Brown", 19, "Physics")
    diana = Student("S004", "Diana Prince", 22, "Engineering")
    
    # Add to database
    db.add_student(alice)
    db.add_student(bob)
    db.add_student(charlie)
    db.add_student(diana)
    
    # Add grades
    print(f"\n{'='*60}")
    print("📝 ADDING GRADES")
    print(f"{'='*60}")
    
    # Alice's grades
    alice.add_grade("Python Programming", 95)
    alice.add_grade("Python Programming", 92)
    alice.add_grade("Data Structures", 88)
    alice.add_grade("Algorithms", 90)
    
    # Bob's grades
    bob.add_grade("Calculus", 78)
    bob.add_grade("Linear Algebra", 85)
    bob.add_grade("Statistics", 82)
    
    # Charlie's grades
    charlie.add_grade("Physics I", 92)
    charlie.add_grade("Physics II", 95)
    charlie.add_grade("Lab Work", 88)
    
    # Diana's grades
    diana.add_grade("Engineering Design", 98)
    diana.add_grade("Mechanics", 96)
    diana.add_grade("Thermodynamics", 94)
    
    # Mark attendance
    print(f"\n{'='*60}")
    print("✅ MARKING ATTENDANCE")
    print(f"{'='*60}")
    
    dates = ["2025-01-05", "2025-01-06", "2025-01-07"]
    for date in dates:
        alice.mark_attendance(date, "Present")
        bob.mark_attendance(date, "Present")
        charlie.mark_attendance(date, "Absent" if date == "2025-01-06" else "Present")
        diana.mark_attendance(date, "Present")
    
    # Display individual reports
    print(alice.get_grade_report())
    print(bob.get_grade_report())
    
    # Display class report
    print(db.generate_class_report())
    
    # Show honor students
    print(f"\n🏆 HONOR STUDENTS (GPA >= 3.5):")
    print(f"{'-'*60}")
    for student in db.get_honor_students():
        print(f"   {student}")
    
    # Interactive menu
    print(f"\n{'='*60}")
    print("🎮 INTERACTIVE MODE")
    print(f"{'='*60}")
    
    while True:
        print("\n1. View Student Report")
        print("2. Add Grade to Student")
        print("3. View Class Report")
        print("4. View Honor Students")
        print("5. View Top Students")
        print("6. Search Student")
        print("7. Exit")
        
        choice = input("\n👉 Enter your choice (1-7): ").strip()
        
        if choice == '1':
            student_id = input("Enter student ID: ").strip()
            student = db.find_student(student_id)
            if student:
                print(student.get_grade_report())
            else:
                print(f"❌ Student {student_id} not found!")
        
        elif choice == '2':
            student_id = input("Enter student ID: ").strip()
            student = db.find_student(student_id)
            if student:
                subject = input("Enter subject: ").strip()
                try:
                    grade = float(input("Enter grade (0-100): "))
                    student.add_grade(subject, grade)
                except ValueError:
                    print("❌ Invalid grade!")
            else:
                print(f"❌ Student {student_id} not found!")
        
        elif choice == '3':
            print(db.generate_class_report())
        
        elif choice == '4':
            honor_students = db.get_honor_students()
            if honor_students:
                print(f"\n🏆 HONOR STUDENTS:")
                for student in honor_students:
                    print(f"   {student}")
            else:
                print("No honor students found.")
        
        elif choice == '5':
            top = db.get_top_students(3)
            if top:
                print(f"\n⭐ TOP 3 STUDENTS:")
                for i, student in enumerate(top, 1):
                    print(f"   {i}. {student}")
            else:
                print("No students found.")
        
        elif choice == '6':
            student_id = input("Enter student ID: ").strip()
            student = db.find_student(student_id)
            if student:
                print(f"\n✅ Found: {student}")
                print(f"   Name: {student.name}")
                print(f"   Major: {student.major}")
                print(f"   GPA: {student.get_gpa():.2f}")
            else:
                print(f"❌ Student {student_id} not found!")
        
        elif choice == '7':
            print("\n👋 Thank you for using the Student Record System!")
            print(f"📊 Total Students: {Student.total_students}")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\n⏸️  Press Enter to continue...")


if __name__ == "__main__":
    main()

