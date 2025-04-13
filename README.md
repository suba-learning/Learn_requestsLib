# Learn_requestsLib


# 🐍 Python Requests Library Examples

This repository demonstrates how to use Python's `requests` library to interact with RESTful APIs. All examples use the public [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API.

## 📦 Prerequisites

Make sure you have Python installed. Then install the `requests` library:

```bash
pip install requests
```

---

## 🧪 API Examples Covered

### 1. 📥 GET All Resources
Fetches all TODOs from the placeholder API.

```python
get_response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(get_response.status_code)
print(get_response.json())
```

---

### 2. 📥 GET Single Resource
Fetches a TODO item by ID.

```python
resource_id = "3"
get_response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{resource_id}")
print(get_response.status_code)
print(get_response.json())
```

---

### 3. 🔍 GET with Query Parameters
Fetches TODOs filtered by a query parameter (`userId=5`).

```python
params = {'userId': '5'}
get_response = requests.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(get_response.status_code)
print(get_response.json())
```

---

### 4. ➕ POST: Create a New Resource
Creates a new TODO item.

```python
post_body = {
  'userId': 1,
  'title': 'New title:learn_requests.py',
  'completed': False
}

headers = {'Content-type': 'application/json'}

post_response = requests.post("https://jsonplaceholder.typicode.com/todos", json=post_body, headers=headers)
print(post_response.status_code)
print(post_response.json())
```

---

### 5. 📝 PUT: Full Update of a Resource
Fully updates an existing TODO item (ID = 1).

```python
put_body = {
  'userId': 1,
  'id': 1,
  'title': 'foo',
  'completed': False
}

put_response = requests.put("https://jsonplaceholder.typicode.com/todos/1", json=put_body, headers=headers)
print(put_response.status_code)
print(put_response.json())
```

---

### 6. 🔧 PATCH: Partial Update of a Resource
Partially updates a TODO's title.

```python
patch_body = {'title': 'test'}

patch_response = requests.patch("https://jsonplaceholder.typicode.com/todos/1", json=patch_body, headers=headers)
print(patch_response.status_code)
print(patch_response.json())
```

---

### 7. ❌ DELETE: Remove a Resource
Deletes a TODO item (ID = 3).

```python
del_response = requests.delete("https://jsonplaceholder.typicode.com/todos/3")
print(del_response.status_code)
```

---

## 📚 References

- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [JSONPlaceholder Fake API](https://jsonplaceholder.typicode.com/)

---

## 🙌 Contributing

Feel free to fork, improve, and submit pull requests!

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
```
