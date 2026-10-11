from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>DANISH COMPANY - Cyber Security Store</h1>
    <p>Rawalpindi, Pakistan | 03701591836</p>
    <h2>My 7 Tools:</h2>
    <ul>
    <li>Tool 1 - 500 Rs</li>
    <li>Tool 2 - 1000 Rs</li>
    <li>Tool 3 - 1500 Rs</li>
    </ul>
    <a href="https://wa.me/923701591836">Buy on WhatsApp</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
