from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/')
def index():
    return {'Mamma mia marcello!': 'What are you doing here?'}


@app.route('/about_me')
def about_us():
    my_text = '''
    Hi there, I'm Bahman and I'm a developer based in Istanbul. I was born on February 2nd, 1990 in Tabriz and I started programming at the young age of 13. Since then, I've developed a strong passion for programming and have gained experience in various programming languages and frameworks.
    <br><br>
    I'm skilled in PHP, JavaScript, and Python, and have extensive knowledge in HTML/CSS markup language. I have worked with various PHP frameworks such as Laravel, Symfony, Codeigniter, and FatFREE, and also have experience working with JS frameworks and libraries such as JQuery, VueJS, Express, Cordova, and ElectronJS.
    <br><br>
    In addition,I'm familiar with Python frameworks like Django, Flask, and FastAPI, and have worked with CSS frameworks like Bootsrap, Zurb Foundation, and Semantic UI. I'm comfortable working with APIs and have experience in RESTful, JSON, XML, SOAP, and cURL.
    <br><br>
    When it comes to databases, I have experience with MySQL, MariaDB, MongoDB, and SQLite.I'm also familiar with caching and message brokers such as Redis, RabitMQL, and Kafka. And for version control, I use Git and have experience with package managers such as NPM, Yarn, Composer, and PIP.
    <br><br>
    Overall, I'm a well-rounded developer with a passion for creating high-quality, efficient, and user-friendly software applications.
    '''
    return {'content': my_text}


@app.route('/skills')
def skills():
    skills_array = [
        {'title': 'Programming Language', 'list': 'PHP, JavaScript, Python'},
        {'title': 'Markup Language', 'list': 'HTML/CSS'},
        {'title': 'PHP Frameworks', 'list': 'Laravel, Symfony, Codeigniter, FatFREE'},
        {'title': 'JS Frameworks and libraries', 'list': 'JQuery, VueJS, Express, Cordova, ElectronJS'},
        {'title': 'Python Frameworks', 'list': 'Django, Flask, FastAPI'},
        {'title': 'CSS Frameworks', 'list': 'Bootsrap, Zurb Foundation, Semantic UI'},
        {'title': 'Working with APIs', 'list': 'RESTful, JSON, XML, SOAP, cURL'},
        {'title': 'Database', 'list': 'MySQL, MariaDB, MongoDB, SQLite'},
        {'title': 'Caching & Message Brokers', 'list': 'Redis, RabitMQL, Kafka'},
        {'title': 'Version Control System', 'list': 'Git'},
        {'title': 'Package Managers', 'list': 'NPM, Yarn, Composer, PIP'},
    ]
    return skills_array


@app.route('/experience')
def experience():
    experience_array = [
        {'company': 'Freelancer World', 'position': 'Full Stack Developer', 'start': '2020', 'end': 'present'},
        {'company': 'Raxin Digital', 'position': 'Chief Technology Officer', 'start': '2018', 'end': '2020'},
        {'company': 'Qonqa Online Taxi', 'position': 'Chief Technology Officer', 'start': '2016', 'end': '2018'},
        {'company': 'Azarin Nov Avaran', 'position': 'Senior Back End Developer', 'start': '2015', 'end': '2016'},
        {'company': 'Gostaresh Foolad Tabriz FC', 'position': 'Senior Web Developer', 'start': '2013', 'end': '2015'},
        {'company': 'Qume Maad Designers', 'position': 'Senior Web Developer', 'start': '2009', 'end': '2013'},
    ]
    return experience_array


@app.route('/projects')
def projects():
    projects_array = [
        {'title': 'TeoriKORT online traffic exam', 'link': 'https://teorikort.se'},
        {'title': 'TeoriKORT Mobile APP', 'link': 'https://play.google.com/store/apps/developer?id=Teorikort'},
        {'title': 'JÄRFÄLLA TRAFIKSKOLA Website', 'link': 'https://jarfallatrafikskola.se'},
        {'title': 'Ruka CRM system', 'link': 'https://crm.ruka.ir'},
        {'title': 'Ruka company Website', 'link': 'https://ruka.ir'},
        {'title': 'Qonqa Online Taxi platform', 'link': 'https://www.qonqa.ir'},
        {'title': 'Hamnava News Agency website', 'link': 'https://hamnava.ir'},
        {'title': 'TabrizFORI News Agency website', 'link': 'https://tabrizfori.ir'},
    ]
    return projects_array


@app.route('/certificates')
def certificates():
    certificates_array = [
        {'title': 'Responsive Web Design Certificate', 'link': 'https://www.freecodecamp.org/certification/shahmarasy/responsive-web-design'},
        {'title': 'JS Algorithms and Data Structures Certificate', 'link': 'https://www.freecodecamp.org/certification/shahmarasy/javascript-algorithms-and-data-structures'},
        {'title': 'Back End Development and APIs Certificate', 'link': 'https://www.freecodecamp.org/certification/shahmarasy/back-end-development-and-apis'},
        {'title': 'CSS Certificate', 'link': 'https://www.hackerrank.com/certificates/87a1c65adcda'},
        {'title': 'Python Django Certificate', 'link': 'https://www.udemy.com/certificate/UC-cbaba320-823a-4e5d-b03a-503fd7f78b1e/'},
        {'title': 'Problem solving Certificate', 'link': 'https://www.hackerrank.com/certificates/a1e104bb7466'}
    ]
    return certificates_array


@app.route('/contact')
def contact():
    contact_array = [
        {'title': 'Email', 'content': 'shahmarasy@gmail.com'},
        {'title': 'linkedin', 'content': 'https://www.linkedin.com/in/shahmarasy/'},
        {'title': 'Github', 'content': 'https://github.com/shahmarasy'},
    ]
    return contact_array


if __name__ == '__main__':
    app.run()
