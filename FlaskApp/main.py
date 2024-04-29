from Website import create_app

app = create_app()

#runs server if main is run, debug = true means that it reruns flask website everytime code is changed
if __name__ == '__main__':
    app.run(port=8000,debug=True)