# Import the app variable from the init
from homework_2 import app

# Import specific packages from flask
from flask import render_template,request

# Import Our Form(s)
from homework_2.forms import UserInfoForm

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/avengers')
def testRoute():
    names = ['Flash','Thor','Black Widow','Maria Hill']
    return render_template('avengers.html',list_names = names)


# GET == Gathering Info
# POST == Sending Info
@app.route('/avengeregister', methods = ['GET','POST'])
def avengeregister():
    # Init our Form
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        #Print the data to the server that comes from the form
        print(name,phone,email,password)

    return render_template('avengeregister.html',user_form = form)