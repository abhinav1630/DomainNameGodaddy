import requests
import time
import json

api_key = "e532npLvjUiV_NtGT4xJYjEDWGqVFCJU2og"
secret_key="B89T6wo8tYsdAAYaaVH6zr"

headers = {"Authorization" : "sso-key {}:{}".format(api_key, secret_key)}

url = "https://api.godaddy.com/v1/domains/available"

pre=[]
suff=[]
hoho=500

#print("Enter 1 for prefix")
#print("Enter 2 for suffix")
#user_selection= int(input())
#if(user_selection==1):
def write_to_file(data_list, file_name):
    with open(file_name, 'w') as f:
        for item in data_list:
            f.write("%s\n" % item)


print("Enter the keyword")
name_pre= input()
print("Enter the filename")
name_country= input()
with open("%s"%name_country, "r")as f:
    for domainname in f.read().splitlines():
        pre.append(name_pre+domainname+'.com')

def split_fn(array, size):
   for i in range(0, len(array), size):
      yield array[i:i + size]

domain_split = list(split_fn(pre, hoho))
#domain_list = list(domain)
available_domains_prefix = []
not_available_domains_prefix= []
available_domains_suffix = []
not_available_domains_suffix= []
for domains in domain_split:
   availability_res = requests.post(url, json=domains, headers=headers)
   for aa in json.loads(availability_res.text)["domains"]:
       if aa["available"]:
           available_domains_prefix.append(aa['domain'])
           write_to_file(available_domains_prefix, 'available_prefix.txt')

       else:
           not_available_domains_prefix.append(aa['domain'])
           write_to_file(not_available_domains_prefix, 'not_available_prefix.txt')



with open("%s"%name_country, "r")as f:
    for domainname in f.read().splitlines():
        suff.append(domainname+name_pre+'.com')


domain_split = list(split_fn(suff, hoho))
#domain_list = list(domain)

for domains in domain_split:
   availability_res = requests.post(url, json=domains, headers=headers)
   for aa in json.loads(availability_res.text)["domains"]:
       if aa["available"]:
           available_domains_suffix.append(aa['domain'])
           write_to_file(available_domains_suffix, 'available_suffix.txt')

       else:
           not_available_domains_suffix.append(aa['domain'])
           write_to_file(not_available_domains_suffix, 'not_available_suffix.txt')
