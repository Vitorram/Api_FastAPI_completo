import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZV9jcmlwdG9AZ21haWwuY29tIiwiZXhwIjoxNzc1MDYzODgwfQ.WU1aw7gH3g0zEf4WrsJJ3n0TJNlP6nJ2_-nfBJxcOYw"
}

requisicao = requests.get("http://localhost:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.text)