from os import environ
from b_end import app
if __name__ == '__main__':
    HOST = '192.168.0.171'
    try:
        PORT = int(environ.get('SERVER_PORT','8001'))
    except ValueError:
        PORT = 8000
app.run(HOST,PORT, debug=True)