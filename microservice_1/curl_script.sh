curl -X 'POST' 'http://127.0.0.1:8000/upload' \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=@data.xlsx'