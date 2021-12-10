import requests, json
import os
import pandas as pd
import random
def API_PARAPHRAZING(URL,text):
        PARAMS = {'text':text}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()['new_sentence'].lower()
        return data
def API_TEXT(URL,top_k,text):
        PARAMS = {'top_k':",".join(top_k),'text':text}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()['resultant_class'].lower()
        return data

def print_json(obj):
    """Print the object as json"""
    print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))
def API_IMAGE(BASE_URI,imagePath):
        file = {'image' : ("filename.jpg", open(imagePath, 'rb'))}
        try:
            response = requests.post(BASE_URI, files=file)
            response.raise_for_status()
        except:
            return "FAILURE"
        count=0
        ans=[]
        for i in response.json()['predictions']:
            ans.append(i['disease_name'])
            count+=1
            if count==5:
                break
        return ans
def system_tests(URL1,URL,BASE_URI,path):
        df=pd.read_csv("C:\\Users\\SHIVANSH\\Desktop\\text\\6th Sem\\Capstone 1\\1.csv")
        count1=0
        symptoms=dict()
        for i in range(len(df)):
                if df['Name'][i].lower() in symptoms:
                        symptoms[df['Name'][i].lower()].append(df['Symptoms'][i])
                else:
                        symptoms[df['Name'][i].lower()]=[df['Symptoms'][i]]
        accuracies=dict()
        for x in os.listdir(path):
                total_count=0
                correct_count=0
                print("class ",x," is being tested Now")
                for y in os.listdir(path+"\\"+x):
                    imagePath=path+"\\"+x+"\\"+y
                    top_k=API_IMAGE(BASE_URI,imagePath)
                    if top_k=="FAILURE":
                            continue
                    for i in range(len(top_k)):
                            top_k[i]=top_k[i].lower()
                    text=random.choice(symptoms[x.lower()])
                    text=API_PARAPHRAZING(URL1,text)
                    result=API_TEXT(URL,top_k,text)
                    total_count+=1
                    if result.lower()==x.lower():
                            correct_count+=1
                    print(total_count)
                    if total_count==10:
                            break
                accuracies[x.lower()]=[correct_count,total_count]
        return accuracies
def print_results(accuracies):
        for i in accuracies:
                print(i)
                print("correct result = ",accuracies[i][0]," total test cases = ",accuracies[i][1])

URL1="http://f41b-35-237-53-80.ngrok.io/get"#copyofparrot.py
URL = "http://1c0d-34-74-177-192.ngrok.io/get"#final_app.py
BASE_URI = "http://c064-35-231-138-180.ngrok.io/predict"#untitled.py
path="C:\\Users\\SHIVANSH\\Desktop\\text\\6th Sem\\Capstone 1\\Data_17-25\\"

accuracies=system_tests(URL1,URL,BASE_URI,path)
print_results(accuracies)
