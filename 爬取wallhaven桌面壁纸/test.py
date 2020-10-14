from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)
for i in range(1, 50):
    headers = {
        'User-Agent': ua.random,
    }
print(headers)