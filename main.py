from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditor, CKEditorField
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)

# Configuration settings for Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "no0739566@gmail.com"
app.config["MAIL_PASSWORD"] = "wijk jveh ypet nbpk"
app.config["MAIL_DEFAULT_SENDER"] = ("Basti", "no0739566@gmail.com")

mail = Mail(app)


class CreatePostForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    # subject = StringField("Subject (Optional)")
    body = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = CreatePostForm()

    if form.validate_on_submit():
        print(form.name.data)
        msg = Message(
            subject=f"Contact form submission from {form.name.data}",
            recipients=["no0739566@gmail.com"],
            body=f"""
               Name: {form.name.data}
               Email: {form.email.data}
               Message: {form.body.data}
               """
        )
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)