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


with open(args.input, 'r') as f:
    data = json.load(f)
    source = data['html']

tree = html.fromstring(source)  

video_link = tree.xpath('./a/@href')[0]
user = get_user_from_link(video_link)

#print(video_link,user)


df = pd.DataFrame(columns=["user", 
                           "video_link"])

df = df.append({
    "user": user,
    "video_link": video_link}, ignore_index=True)
print(df)

df.to_csv(args.output)