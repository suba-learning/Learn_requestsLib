#Import requests library
import requests

#1. Send get all resources
# https://jsonplaceholder.typicode.com/todos
get_response = requests.get("https://jsonplaceholder.typicode.com/todos")
print("GET ALL: ",get_response.status_code)
#print(help(get_response))
#print(get_response.text)
print(get_response.json())

#2. Getting a single resource
resource_id ="3"
get_response = requests.get("https://jsonplaceholder.typicode.com/todos/"+resource_id)
print("GET: ",get_response.status_code)
#print(help(get_response))
#print(get_response.text)
print(get_response.json())


#3. Requests with parameters in url
todo_id={
    'userId': '5'}
get_response = requests.get("https://jsonplaceholder.typicode.com/todos", params=todo_id)
print("GET PARAM: ",get_response.status_code)
print(get_response.json())

#4. Send post request: Creating a resource
post_body={
  'userId': 1,
  'title': 'New title:learn_requests.py',
  'completed': False
}

post_headers= {
    'Content-type': 'application/json'
}

post_response = requests.post("https://jsonplaceholder.typicode.com/todos", json=post_body, headers=post_headers,)
print("POST: ",post_response.status_code)
print(post_response.json())
if post_response.ok:
    print("Creation Success")
else:
    print("Creation failed")


#5. Send Put request: Updating a resource
put_body={
  'userId': 1,
  'id': 1,
  'title': 'foo',
  'completed': False
}

put_headers= {
    'Content-type': 'application/json'
}

put_response = requests.put("https://jsonplaceholder.typicode.com/todos/1/", json=put_body, headers=put_headers)
print("PUT: ",put_response.status_code)
print(put_response.json())


#6. Send Patch request: Updating a resource
patch_body={
  'title': 'test'
}

patch_headers= {
    'Content-type': 'application/json'
}

patch_response = requests.patch("https://jsonplaceholder.typicode.com/todos/1/", json=patch_body, headers=patch_headers)
print("PATCH: ",patch_response.status_code)
print(patch_response.json())


#7.Send Delete request: Deleting a resource
del_response = requests.delete("https://jsonplaceholder.typicode.com/todos/3/")
print("DELETE: ",del_response.status_code)
