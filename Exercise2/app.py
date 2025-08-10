from graph import app

response = app.invoke({"name": "Susan", "values": [1,2,3,4], "operator": "/"})
result = response["result"]

print(result)