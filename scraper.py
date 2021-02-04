#Get the first page to extract page numbers
import requests, re
from bs4 import BeautifulSoup


tags = ["a",
"abbr",
"acronym",
"address",
"applet",
"area",
"article",
"aside",
"audio",
"b",
"base",
"basefont",
"bdi",
"bdo",
"bgsound",
"big",
"blink",
"blockquote", 
"br",
"button",
"canvas",
"caption",
"center",
"cite",
"code",
"col",
"colgroup",
"content",
"data",
"datalist",
"dd",
"decorator",
"del",
"details",
"dfn",
"dir", 
"dl",
"dt",
"element",
"em",
"embed",
"fieldset",
"figcaption",
"figure",
"font",
"footer",
"form",
"frame",
"frameset",
"h1",
"h2",
"h3",
"h4",
"h5",
"h6",
"head",
"header",
"hgroup",
"hr",
# "html",
"i",
"iframe",
"img",
"input",
"ins",
"isindex",
"kbd",
"keygen",
"label",
"legend",
"li",
"link",
"listing",
"main",
"map",
"mark",
"marquee",
"menu",
"menuitem",
"meta",
"meter",
"nav",
"nobr",
"noframes",
"noscript",
"object",
"ol",
"optgroup",
"option",
"output",
"p",
"param",
"plaintext",
"pre",
"progress",
"q",
"rp",
"rt",
"ruby",
"s",
"samp",
"script",
"section",
"select",
"shadow",
"small",
"source",
"spacer",
"span",
"strike",
"strong",
"style",
"sub",
"summary",
"sup",
# "table",
"tbody",
# "td",
"template",
"textarea",
"tfoot",
"th",
"thead",
"time",
"title",
"tr",
"track",
"tt",
"u",
"ul",
"var",
"video",
"wbr",
"xmp"]

def scrapUrl(url):
    demo_url= "http://toscrape.com/"
    r=requests.get(url) 
    c=r.content
    soup=BeautifulSoup(c,"html.parser") 
    
    # following code will create tag plus data list
    tag_data_list=[] 
    for item in tags:
        i = item
        itemTags=[] 
        item = soup.find_all(item) 
        if item: 
            itemTags.append(i)
            itemTags.append(item)
            tag_data_list.append(itemTags)
            


    # list of tag 
    scrapTags=[]

    for item in tag_data_list:
        scrapTags.append(item[0])


  
    
 
    #follow
    data_dictionary=[]
    for item in tag_data_list:
        dic=[]
        textList=[]
        tag = item[0]
        for i in item[1]:
            if i.getText():
                textList.append(i.getText().replace('\n',''))
            
        dic.append(tag)
        dic.append(textList) 
        data_dictionary.append(dic) 

    
    finalList=[]
    for item in data_dictionary:
        tag=item[0]
        data=item[1]
        dic={}
        for i in data: 
            finalList.append({tag:i})
    
    return finalList      
    

 