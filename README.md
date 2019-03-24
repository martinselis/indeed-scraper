# indeed-scraper

**Overview:**

I keep hearing about X programming language being more popular than Y. Or A framework being more used than B. To settle debate, created this script, which scrapes indeed.co.uk job listings in the city and job title that you choose. Then second script will show how many job listings mention certain technology.

**How to use:**

```
python3 code.py #(in terminal)
```
You'll be prompted to enter city and job title.
This will then scrape the data and save it to data.json. Once data is scraped:

```
python3 working_with_data.py
```

Now type what you want to see. For example, entering 'java' will return X amount of jobs containing word java, one or more times.

**What I'd improve on next time:**

1. Definitely introduce a database. Currently data is saved to one file and overwrites it, whenever you scrape new searches. 
2. Use OOP. It's a mess right now.
3. Split functions into smaller ones.
4. Not create global variables.
5. Make code more DRY. There's some repetition in working_with_data.py.
6. Categorize data differently. Right now it saves data in hash with count next to each word i.e. {'a': 10, 'nodejs': 20} etc. You can't see word combinations like 'Amazon Web Services'. You can just search for one word, like 'amazon' or 'aws'.
