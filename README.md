# Dermatobot


Please add /API/weight/(the weight file) manually


Run:
1) Download the models and save it at API/weight/(model file name.md)
2) Run the image classification API present inside API --> this will start running the server and output you an url (lets say x.com)
3) Symptoms based classification is too heavy to be run on your local machine
4) Open colab or any remote execution env with enough resources.
5) Upload the 1.csv present inside API/symptoms to colab.
6) Upload the symptoms classifier API present in API/ to colab and run --> this will start running the server and output you an url(lets say y.com)
7) Take the urls x.com and y.com and make corresoponding changes to ./chatui/src/chat.js 
8) Now navigate to ./chatui directory open terminal and run npm install (Note: Further development please dont install packages manually rather just edit packages.json and add your package ; then run npm start you will have your package installed .This will enable consistency)
9) Finally run npm start
10) Your local development server should be up and running and should be accessible via your browser.
