from simpleapp import app
from flask import render_template, flash, redirect, url_for
from simpleapp.services.viewservice import viewdata
from simpleapp.services.formservice import registration

viewdata = viewdata()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/registration", methods=['GET', 'POST'])
def form():
    form = registration()
    if form.validate_on_submit():
        with open("C:\\Users\\pdebnath\\PycharmProjects\\SimpleApplication\\datafile.txt", 'w') as fw:
            fw.writelines(form.username.data)
            fw.writelines('\n')
            fw.writelines(str(form.age.data))
            fw.writelines('\n')
            fw.writelines(form.place.data)
            fw.writelines('\n')
        return redirect(url_for('view'))
    return render_template('form.html', form=form)

@app.route("/view")
def view():
    return render_template('view.html', posts=viewdata.viewdata())