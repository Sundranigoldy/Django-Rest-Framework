
Generate Token
1. using admin panel
2. using cmd by
python manage.py drf_create_token username

3.token generated by client directly 
here for testing we ussing httpie model 

from another terminal
http POST http://127.0.0.1:8000/gettoken/  username="user1" password="Goldy123@

after this u will get below response
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 09 Feb 2023 04:33:56 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.8.2
Vary: Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "token": "f2a2b933d0e5b9ce2096676f57b7c30483eb2e9f"
}


(DjangoDRF) PS D:\MICROSOFT PROJECT -COPY\Django\DjangoDRF> http POST http://127.0.0.1:8000/gettoken/  username="user1" password="Goldy123@"
HTTP/1.1 200 OK

{
    "token": "f2a2b933d0e5b9ce2096676f57b7c30483eb2e9f"
}

we can also customize the reponse instead of just getting token we can some more fields
by creating one new file say auth.py


4. using signals