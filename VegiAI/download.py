from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

key =""
secret = "f2e682da42af9181"
wait_time = 0.5

vegitable_name= sys.argv[1]
savedir ="./"+ vegitable_name

flickr=FlickrAPI(key,secret,format="parsed-json")
result =flickr.photos.search(
    text =vegitable_name,
    per_page =400,
    media="photos",
    sort = "relevance",
    safe_search = 1,
    extras="url_q, licence"
)

photos =result["photos"]
#pprint(photos)

for i,photo in enumerate(photos["photo"]):
    url_q=photo["url_q"]
    filepath=savedir + '/' + photo['id'] +'.jpg'
    if os.path.exists(filepath):continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
