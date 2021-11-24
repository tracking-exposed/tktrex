import argparse
import pandas as pd
import json 
from lxml import html

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')
args = parser.parse_args()


def get_user_from_link(link):
    idx_start = link.find('@')
    link_tmp = link[idx_start:]
    idx_end = link_tmp.find('/')
    return link_tmp[:idx_end]

#print(args)
with open(args.input, 'r') as f:
    lines = f.readlines()

df = pd.DataFrame(columns=["user", 
                            "video_link",
                            "tags",
                            "text"])

for line in lines:
    data = json.loads(line)    
    source = data['html']
    
    tree = html.fromstring(source)  
    
    video_link = tree.xpath('.//@href')[0]
    user = get_user_from_link(video_link)
    text = tree.xpath('.//img/@alt')[0]
    tags = tree.xpath('.//strong[starts-with(text(),"#")]/text()')
#    print(search_link,video_link,user,text,tags,end='\n\n')

    df = df.append({
          "user": user,
          "video_link": video_link,
          "tags": tags,
          "text": text}, ignore_index=True)
print(df)

df.to_csv(args.output)