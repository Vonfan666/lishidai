
for  a  in  range(2):
    import requests

    url = "http://192.168.2.9:88/api/workOrder/approve"

    payload = {"id":149,"opearteLocation":"2","opearteType":"1",}
    headers = {
        'accept': "application/json, text/plain, */*",
        'origin': "http://192.168.2.9:88",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'token': "eyJhbGciOiJIUzI1NiJ9.eyJsb2dpbk5hbWUiOiJhZG1pbiIsInJpZ2h0cyI6IjQ3ODkwNDg1NjUyMDgwODA0ODk1MTgxMjg0NjYwMTA4ODE3OTcwODQyNTMwMDgxOTMxMjY2IiwicmVmcmVzaFRpbWUiOjE1NjMzNTg0ODgsImlzcyI6Im1hbmFnZSIsImV4cCI6MTU2MzM2NTY4OCwidXNlcklkIjoxfQ.nnqI3ZVEsFmxQ8oYpmvHdKwIR-nIXnzBgp3I4k3rGDM",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "72ea5ad5-f760-e973-2c1e-658e8083d10d"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)