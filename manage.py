import os 
from app.main import create_app
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)