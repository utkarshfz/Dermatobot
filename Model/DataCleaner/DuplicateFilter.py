import hashlib 
import os


duplicates =[]
hash_keys=set()

for disease in os.listdir('../Data/'):
    flag=True
    for images in os.listdir('../Data/'+disease):
        if(flag):
            print("Cleaning: "+disease)
            flag=False
        f=open('../Data/'+disease+'/'+images,'rb')
        filehash=hashlib.md5(f.read()).hexdigest()
        if(filehash in hash_keys):
            os.remove('../Data/'+disease+'/'+images)
        else:
            hash_keys.add(filehash)




