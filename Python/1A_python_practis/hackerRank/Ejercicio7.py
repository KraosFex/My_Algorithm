from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])
    
    def handle_endtag(self, tag):
        print("End  :", tag)
    
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)

    #def handle_data(self, data):
    #    print("Empty  :", data)

read = int(input())
if read > 0 and read < 100:
    # codeHtml = ""
    for i in range(read):
        print(i + 1)
