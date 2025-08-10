from graph import app

result = app.invoke({"numbers": [2, 5, 1, 8], "result": 0})
print(f"Final result: {result["result"]}")