from graph import app

result = app.invoke({"message": "Bob"})
print(result["message"])