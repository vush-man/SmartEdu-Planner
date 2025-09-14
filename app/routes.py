from flask import Blueprint, render_template, redirect, url_for, flash, request, make_response
from flask_login import login_required, current_user
from .models import Lecture, Teacher, db
from .services import find_and_assign_substitute, generate_timetable_pdf, generate_timetable_excel
from sqlalchemy import case

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@login_required
def dashboard():
    """
    Renders the appropriate dashboard based on the user's role.
    Sorts the timetable by a custom day order.
    """
    day_order = case(
        {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7,
        },
        value=Lecture.day,
    )

    if current_user.role == 'admin':
        lectures = Lecture.query.order_by(day_order, Lecture.time_slot).all()
        teachers = Teacher.query.all()
        return render_template("admin_dashboard.html", lectures=lectures, teachers=teachers)
    
    if current_user.role == 'student':
        lectures = Lecture.query.filter_by(section=current_user.section).order_by(day_order, Lecture.time_slot).all()
        return render_template("student_dashboard.html", lectures=lectures)

    return "Invalid user role.", 403

@main_bp.route("/add_lecture", methods=["POST"])
@login_required
def add_lecture():
    if current_user.role != 'admin':
        flash("You do not have permission to perform this action.", "flash-error")
        return redirect(url_for('main.dashboard'))

    day = request.form.get("day")
    section = request.form.get("section")
    subject = request.form.get("subject")
    time_slot = request.form.get("time_slot")
    teacher_id = request.form.get("teacher_id")

    new_lecture = Lecture(
        day=day,
        section=section,
        subject=subject,
        time_slot=time_slot,
        teacher_id=teacher_id
    )
    db.session.add(new_lecture)
    db.session.commit()
    flash("Lecture added successfully!", "flash-success")
    return redirect(url_for("main.dashboard"))

@main_bp.route("/lectures/<int:lecture_id>/delete", methods=["POST"])
@login_required
def delete_lecture(lecture_id):
    if current_user.role != 'admin':
        flash("You do not have permission to perform this action.", "flash-error")
        return redirect(url_for('main.dashboard'))

    lecture = Lecture.query.get_or_404(lecture_id)
    db.session.delete(lecture)
    db.session.commit()
    flash("Lecture deleted successfully.", "flash-info")
    return redirect(url_for("main.dashboard"))

@main_bp.route("/lectures/<int:lecture_id>/add_substitute", methods=["POST"])
@login_required
def add_substitute(lecture_id):
    if current_user.role != 'admin':
        flash("You do not have permission to perform this action.", "flash-error")
        return redirect(url_for('main.dashboard'))
        
    _, message = find_and_assign_substitute(lecture_id)
    flash(message, "flash-info")
    return redirect(url_for("main.dashboard"))

@main_bp.route("/download_timetable_pdf")
@login_required
def download_timetable_pdf():
    if current_user.role != 'student':
        flash("Only students can download timetables.", "flash-error")
        return redirect(url_for('main.dashboard'))

    pdf_buffer = generate_timetable_pdf(current_user)
    
    response = make_response(pdf_buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=timetable_section_{current_user.section}.pdf'
    return response


@main_bp.route("/download_timetable_excel")
@login_required
def download_timetable_excel():
    if current_user.role != 'student':
        flash("Only students can download timetables.", "flash-error")
        return redirect(url_for('main.dashboard'))

    excel_buffer = generate_timetable_excel(current_user)
    
    response = make_response(excel_buffer)
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = f'attachment; filename=timetable_section_{current_user.section}.xlsx'
    return response