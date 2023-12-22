"""
# import urllib
# user urllib.request to get data from the url
# write a function that takes a url and returns a response
"""
from urllib import request



def main(url): 
    print('Checking connectivity status...')
    response = request.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was: {response.code}")



print("This is a site connectivity checker. ")
input_url = input("Input the url of the site you want to check:  ")
main(input_url)