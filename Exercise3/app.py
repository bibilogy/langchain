from graph import app

response = app.invoke({"name": "Charlie", "age" : "21", "skills": ["Programming", "Math"], "result": ""})
result = response["result"]

print(result)
