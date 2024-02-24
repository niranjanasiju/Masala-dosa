import requests

url = "https://braille.p.rapidapi.com/braille/image"

querystring = {"text":"Hi, I am from Mars and I speak Braille."}

headers = {
	"X-RapidAPI-Key": "0b1081a701mshdb1026dffc18e9ep1994b3jsnc6214c8d93b3",
	"X-RapidAPI-Host": "braille.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())