import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':65, 'Gender':0, 'Total_Bilirubin':0.7, 'Alamine_Aminotransferase':16, 'Total_Protiens':6.8,'Albumin':3.3,'Albumin_and_Globulin_Ratio':0.9})

print(r.json())
