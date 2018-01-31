#USAGE
#this script converts a txt file of links from http://image-net.org 
#to an array of links that python downloads. To use, go to image-net.org and download
#a set of image links (e.g. http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02766534) 
#as a .txt file
#then in terminal, cd to wherever you have this file stored and use a command like the following to 
#download images:
# $ python scrape.py image_name_prefix path_to_links.txt
# downloaded images will be output to the 'downloaded_images' folder and named whatever you entered for 'image_name_prefix'


import urllib.request
import socket
import os
import sys
links = []
#even though i'm checking for errors below, lots were still coming up. flickr reliably returns
#images or placeholders without error, so i am parsing anything that doesn't come from 
#flickr (there should usually be enough flickr links from image-net to satisfy training requirements
flickr = "flickr" 
file_path = "downloaded_images/"
directory = os.path.dirname(file_path)

if not os.path.exists(directory):
    os.makedirs(directory)

try:
	data_file = sys.argv[2]
except IndexError:
	print("expecting image name and path to links file. sample command: $ python scrape.py baggage imagenet.synset.luggage.txt")
	exit()

try:
    with open(data_file) as data:
        for each_line in data:
            try:
                link = each_line.replace("\n", "").strip()
                if flickr in link:
                	links.append(link)

            except ValueError:
                pass
except:
    pass

counter = 0

try:
	name = sys.argv[1]
except IndexError:
	print("expecting image name and path to links file. sample command: $ python scrape.py baggage imagenet.synset.luggage.txt")
	exit()


for link in links:
	try:
		urllib.request.urlretrieve(link, directory+"/"+name+"_image"+str(counter)+".jpg")
		counter=counter+1
	except urllib.error.HTTPError as err:
		print(link)
	except ConnectionResetError as conErr:
		print(link)
		continue
	except socket.gaierror as sError:
		print(link)
		continue
	except urllib.error.URLError as urlErr:
		print(link)
		continue
	except ValueError as valErr:
		print(link)
		continue


print("complete")
exit()