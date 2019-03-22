from flask import Flask, render_template, redirect
from collections import OrderedDict
app = Flask(__name__)

@app.route('/about-me')
def about_me():
    intro = {
        'Name': 'Bang',
        'Work': 'Student',
        'School': 'Techkid Coding School',
        'Hobbies': 'Football',
    }
    return render_template('about_me.html', intro = intro)

@app.route('/school')
def school():
      return redirect ('https://techkids.vn/')

if __name__ == '__main__':
  app.run(debug=True)
 