import sys
import os

sys.path.insert(0,'/var/www/html/triviapractice')

activate_this ='/home/rich2/.local/share/virtualenvs/triviapractice-MbtZD7Cg/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(),dict(__file__=activate_this))

def application(environ, start_response):
    # explicitly set environment variables from the WSGI-supplied ones
    ENVIRONMENT_VARIABLES = [
        'db_user',
        'db_password',
        'db_name',
        'db_host',
        'db_port'
    ]
    for key in ENVIRONMENT_VARIABLES:
        os.environ[key] = environ.get(key)
 
    from triviasite import app
 
    return app(environ, start_response)


