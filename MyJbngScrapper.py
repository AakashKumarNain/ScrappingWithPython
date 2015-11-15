import requests
from bs4 import BeautifulSoup

cnt=0;

url = "http://www.jabong.com/shoes/Adidas/?tt=&rank=0&qc=adidas%20shoes"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find_all("section",{"class":"row search-product animate-products"})[0]
##cnt=1;
for items in g_data:
    try:
        img_url = items.contents[0].find_all("img")[0].get("src")
    except:
        pass
    try:
        name = items.contents[0].find_all("div",{"class":"h4"})[0].text
    except:
        pass
    try:
        price = items.contents[0].find_all("span",{"class":"standard-price"})[0].text
    except:
        pass
    try:
        sizes = items.contents[0].find_all("div",{"class":"avail-size"})[0]
        avail_sizes =[]
        for s in sizes:
            if(s.text!="Sizes"):
                avail_sizes.append(s.text)
    except:
        pass
    
    print("Image = " +img_url)
    print("Product Name : " +name)
    print("Price : " +price)
    print("Available Sizes : " +str(avail_sizes))
    print("\n\n")
    cnt=cnt+1;
print(cnt)    

    
