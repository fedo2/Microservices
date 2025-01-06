2025-01-06

Vytvořen app.py a otestována funkčnost api Flask
curl http://localhost:5000/hello
OK

přidán endpoint /text a otestovány GET i POST metody
GET:  curl http://localhost:5000/text
POST: curl -F "file=@sample.txt" http://localhost:5000/text
OK
