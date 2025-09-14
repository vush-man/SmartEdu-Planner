from app import create_app
from app.extensions import db
from app.models import User, Teacher, Lecture

def seed_data():
    """Clears existing data and populates the database with sample data."""
    app = create_app()
    with app.app_context():
        print("Clearing existing database tables...")
        Lecture.query.delete()
        Teacher.query.delete()
        User.query.delete()
        
        print("Adding new sample data...")
        
        print("Adding users...")
        admin = User(username='admin', role='admin')
        admin.set_password('admin')

        student_a = User(username='studentA', role='student', section='A')
        student_a.set_password('student')

        student_b = User(username='studentB', role='student', section='B')
        student_b.set_password('student')
        
        db.session.add_all([admin, student_a, student_b])
        db.session.commit()

        print("Adding teachers...")
        t1 = Teacher(name="Prof. Sharma", subject="Physics")
        t2 = Teacher(name="Prof. Gupta", subject="Physics")
        t3 = Teacher(name="Prof. Verma", subject="Math")
        t4 = Teacher(name="Prof. Singh", subject="Chemistry")
        t5 = Teacher(name="Prof. Iyer", subject="Biology")
        db.session.add_all([t1, t2, t3, t4, t5])
        db.session.commit()

        print("Adding lectures...")
        lectures_to_add = [
            Lecture(section="A", day="Monday", time_slot="09:00 AM", subject="Physics", teacher_id=t1.id),
            Lecture(section="A", day="Monday", time_slot="11:00 AM", subject="Math", teacher_id=t3.id),
            Lecture(section="A", day="Tuesday", time_slot="10:00 AM", subject="Chemistry", teacher_id=t4.id),
            Lecture(section="A", day="Wednesday", time_slot="09:00 AM", subject="Biology", teacher_id=t5.id),
            Lecture(section="A", day="Friday", time_slot="01:00 PM", subject="Physics", teacher_id=t1.id),
            
            Lecture(section="B", day="Monday", time_slot="10:00 AM", subject="Math", teacher_id=t3.id),
            Lecture(section="B", day="Tuesday", time_slot="11:00 AM", subject="Physics", teacher_id=t2.id),
            Lecture(section="B", day="Wednesday", time_slot="01:00 PM", subject="Chemistry", teacher_id=t4.id),
            Lecture(section="B", day="Thursday", time_slot="09:00 AM", subject="Biology", teacher_id=t5.id),
            Lecture(section="B", day="Friday", time_slot="11:00 AM", subject="Physics", teacher_id=t2.id),
        ]
        db.session.add_all(lectures_to_add)
        db.session.commit()

        print("✅ Database has been populated successfully!")

if __name__ == '__main__':

    seed_data()
