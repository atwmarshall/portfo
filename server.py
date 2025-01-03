from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(form_data):
    '''
    appends form_data to database.csv

    expected format of form_data is dictionary with the keys: email, subject, message
    '''
    with open('database.csv', mode='a', encoding='utf-8', newline='') as database:
        email = form_data['email']
        subject = form_data['subject']
        message = form_data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Something went wrong, did not save to database.'
    else:
        return 'Something went wrong. Please try again.'
