#importing create_app function from init.py inside website folder
from website import create_app

app = create_app()

# To run the flask server ( checks if the current script is the main program that is being executed)
if __name__ == '__main__':
    app.run(debug=True) #debug=True means whenever we will make changes server will restart
    