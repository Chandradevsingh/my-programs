import ast

# data = "[1,2,3]"
# data = "{'name': 'Dev'}"
data = "('Hello', 'World')"

list = ast.literal_eval(data)

print(list)
print(type(list))