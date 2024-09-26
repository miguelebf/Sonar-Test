import requests
import json

def test_requests():
    var = False
    url = "http://localhost:5000/operator/clasification"
    req = requests.get(url, verify=var)
    print(req.json())


def sum(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def printre():
    re_ = re.compile(r'\d+')
    return re_.findall('test')

def main():
    printre()

if __name__ == '__main__':
    main()
