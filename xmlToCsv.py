from urllib.request import urlopen
from xml.etree.ElementTree import parse
import pandas as pd


def xmlToCsv(url,item,filename):
    var_url = urlopen('https://www.europarl.europa.eu/rss/doc/top-stories/en.xml')
    xmldoc = parse(var_url)

    data = []
    cols = []
    for item in xmldoc.iterfind('channel/item'):
        cols=[subchild.tag for subchild in item.getiterator()][1:]
        data.append([subchild.text for subchild in item.getiterator()][1:])

    df = pd.DataFrame(data)  # Write in DF and transpose it
    df.columns = cols  # Update column names
    df.to_csv(filename,index=False)


# define parameters
url = 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml' # declare url
item = 'channel/item'  #declare XMl item
filename = 'channel_Data.csv' # csv filename

#calling function
xmlToCsv(url,item,filename)
