from app.app import app


from app.database import init

init()

app.run(debug=True)