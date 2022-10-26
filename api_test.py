import requests
r = requests.get(url = "http://localhost:5000/")
print(r.text)
r = requests.post(url = "http://localhost:5000/emotions" , files = {'image': open("C:/Users/gtx25/Downloads/OIP.jfif" , "rb")})
print(r.text)



#curl -X POST -F 'image=@<location>' http://localhost:5000/emotions