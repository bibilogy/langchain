from graph import app

response = app.invoke({"name": "", "attempts": 0, "guesses": [], "l_bound": 0, "u_bound": 20, "result": ""})
# result = response["result"]
# guesses = response["guesses"]
#
# print(f"Result: {result}\nGuesses: {guesses}")