import json

with open('data.json', 'r') as file:
    data = json.load(file)

#{company: company, job_title: job_title, text: text}
companies = {}

for advert in data:
    try:
        companies[advert["company"]]["postings"] += 1
    except:
        companies[advert["company"]] = {}
        companies[advert["company"]]["postings"] = 1

def duplicateVerification(item):
    addition = item["text"]
    try:
        for check in companies[item["company"]]["job_advert"]:
            if check == addition:
                print('match. cant add')
                return False #cant add
        return True #can add
    except:
        return True #can add

for item in data:
    addition = item["text"]
    try:
        if (duplicateVerification(item)):
            companies[item["company"]]["job_advert"].append(addition)
    except:
        if (duplicateVerification(item)):
            companies[item["company"]]["job_advert"] = []
            companies[item["company"]]["job_advert"].append(addition)

def duplicateVerification(item):
    addition = item["text"]
    try:
        for check in companies[item["company"]]["job_advert"]:
            if check == addition:
                print('match. cant add')
                return False #cant add
        return True #can add
    except:
        return True #can add

raw_text = []
for k in companies:
    for listing in companies[k]["job_advert"]:
        raw_text.append(listing)

res = {}

for num, listing in enumerate(raw_text):
    listing = listing.lower()
    listing = listing.replace("\n", " ").replace(".", " ").replace("node js", "nodejs")
    listing = listing.replace("(", " ").replace(")", " ").replace(",", " ")
    listing = listing.replace("-", " ").replace("/", " ").replace("\\", " ")
    listing = listing.replace("angular 2", "angular").replace("angular 3", "angular")
    listing = listing.replace("js", "javascript")
    raw_text[num] = listing

for listing in raw_text:
    listing = listing.split(" ")
    listing = set(listing)
    for item in listing:
        try:
            res[item] += 1
        except:
            res[item] = 0
            res[item] += 1

print ('Enter Q to quit')
while True:
    print ('Enter keyword to look up: ')
    keyword = input()
    if keyword == 'Q':
        break
    try:
        print ('There are {} job applications that mention {}'.format(res[keyword], keyword))
    except:
        print ('There are no mentions of {}'.format(keyword))
