from Geoguesser import create_app

app = create_app()

if __name__ == '__main__':

    app.run(host='127.0.8.1', port='5050')


