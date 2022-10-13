
urls = ['business-standard.com', 'ft.com']
fullurl = ''
for url in urls:
    fullurl += " OR site:"+ url.lower() 
    
print(fullurl.replace(" OR ",'',1))