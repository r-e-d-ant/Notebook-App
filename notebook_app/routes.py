
from notebook_app import app, db, bcrypt
from notebook_app.models import User, Notes, Feedbacks, Subjects
from notebook_app.forms import RegistrationForm, LoginForm, UpdateAccountForm, UpdateNoteForm, NewSubjectForm

from flask import render_template, redirect, url_for, request, abort, flash
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime


# ====================================================== NOTES PART =============================
def a_current_user():
    superuser =  User.query.filter_by(username='superuser').first()
    return superuser

@app.route('/', methods=['GET', 'POST'])
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if (email and password):
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(url_for(next_page)) if next_page else redirect(url_for('home'))

            else:
                flash('Login unsuccessfull, Please check email and password', 'danger')
    return render_template('signin.html', title="Sign In", form=form)

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = NewSubjectForm()
    user_notes = User.query.get(current_user.id)
    notes = user_notes.notes
    users_subjects = user_notes.subjects

    for note in notes:
        print(note.date_saved)

    if request.method == 'POST':
        subject_data = request.form['subject']
        notes_data = request.form['notes']

        if subject_data and notes_data:
            note = Notes(subjects=subject_data, notes=notes_data, author=current_user)
            db.session.add(note)
            db.session.commit()

            return redirect(url_for('home'))

    return render_template('home.html', notes=notes, users_subjects=users_subjects, form=form, superuser=a_current_user(), title='Summary-Notebook')

@app.route('/update/<int:note_id>', methods=['GET', 'POST'])
@login_required
def update(note_id):
    note = Notes.query.get(note_id)

    if note.author != current_user:
        flash("Mind your business", "warning")
        return redirect(url_for('home'))
        abort(403)

    form = UpdateNoteForm()

    if form.validate_on_submit():
        subjects = form.subject.data
        notes = form.notes.data

        if (subjects and notes):
            note.subjects = form.subject.data
            note.notes = form.notes.data

            db.session.commit()
            flash("Note updated successfull", "success")
            return redirect(url_for('home'))
        
    elif request.method == 'GET':
        form.subject.data = note.subjects
        form.notes.data = note.notes
        
    return render_template('update.html', note=note, title="Update", form=form)

@app.route('/note/<int:note_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_note(note_id):
    note = Notes.query.get_or_404(note_id)

    if note.author != current_user:
        flash("Mind your business", "warning")
        abort(403)
        

    db.session.delete(note)
    db.session.commit()

    flash("Your note have been deleted", "success")
    
    return redirect(url_for('home'))

# ====================================================== SUBJECTS =============================

@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    form = NewSubjectForm()

    if form.validate_on_submit():
        new_subject_data = form.subjects_name.data

        if new_subject_data:
            subject = Subjects(subjects_name=new_subject_data, subject_author=current_user)
            db.session.add(subject)
            db.session.commit()
            flash("New subject added", "success")
            return redirect(url_for('home'))

@app.route('/delete_subject/<int:subject_id>', methods=['GET', 'POST'])
def delete_subject(subject_id):
    user_subj = Subjects.query.get_or_404(subject_id)
    if user_subj.subject_author != current_user:
        flash("Mind your business", "waring")
        abort(403)

    db.session.delete(user_subj)
    db.session.commit()

    flash("Subject deleted successfully", "success")
    return redirect(url_for('home'))
# ====================================================== ••••••••••• =============================

# ====================================================== USER PART =============================    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        password = form.password.data

        if (username and email and password):
            # Hash inputed password then assign it to hashed password variable
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=hashed_password)

            db.session.add(user)
            db.session.commit()

            flash("Welcome. Now you can login", "success")

        return redirect(url_for('signin'))

    return render_template('signup.html', title="Sign Up", form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signin'))

@app.route('/account/<int:user_id>', methods=['GET', 'POST'])
@login_required
def account(user_id):

    user = User.query.get(user_id)

    form = UpdateAccountForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        if username:
            user.username = username
            user.email = email
            db.session.commit()
            flash("Your account has been update", "success")
            return redirect(url_for('account', user_id=user.id))

        if email:
            user.username = username
            user.email = email
            db.session.commit()
            flash("Your account has been update", "success")
            return redirect(url_for('account', user_id=user.id))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title="Account", form=form)



# ====================================================== ••••••••••• =============================

# ====================================================== ADMIN PART ===============================
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name_data = request.form['name']
        email_data = request.form['email']
        subject_data = request.form['subject']
        message_data = request.form['message']

        if (name_data and email_data and subject_data and message_data):
            feedback = Feedbacks(name=name_data, email=email_data, subject=subject_data, message=message_data)
            db.session.add(feedback)
            db.session.commit()
            flash("Thank you for the feedback", "success")
        else:
            flash("Something went wrong, Verify your name and email")
            return redirect(url_for(contact))

    return render_template('contact.html', title="Feedback")

@app.route('/feedback')
@login_required
def feedback():
    if current_user == a_current_user():
        feedbacks = Feedbacks.query.order_by(Feedbacks.date_submited.desc()) # query feedback by submited date.
        return render_template('feedback.html', feedbacks=feedbacks)
    else:
        abort(403)

@app.route('/<int:feed_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_feedback(feed_id):
    feed = Feedbacks.query.get_or_404(feed_id)
    if current_user == a_current_user():
        db.session.delete(feed)
        db.session.commit()
        flash("Your feed have been deleted", "success")
        return redirect(url_for('feedback'))
    else:
        abort(403)

# ====================================================== ••••••••••• =============================








