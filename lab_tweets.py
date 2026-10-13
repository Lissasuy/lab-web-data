# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt
tweets = []
for year in range(2009, 2019):
    with open(f'master_{year}.json') as f:
        tweets.extend(json.load(f))
print(len(tweets))
print(tweets[0].keys())

def get_message(tweet):
    if 'full_text' in tweet:
        return tweet['full_text']
    return tweet['text']

phrases = ['obama', 'trump', 'mexico', 'russia', 'fake news', 'wall', 'daca', 'mainstream media']

counts = {}
for phrase in phrases:
    counts[phrase] = 0
    for tweet in tweets:
        if phrase in get_message(tweet).lower():
            counts[phrase] += 1
    print(phrase, counts[phrase])

total = len(tweets)
width = max(len(p) for p in phrases)
lines = []
lines.append(f"| {'phrase' :>{width}} | percent of tweets |")
lines.append(f"| {'-' * width} | {'-' * 15 } |")
for phrase in sorted(phrases):
    percent = counts[phrase] / total * 100
    lines.append(f"| {phrase :>{width}} | {percent:05.2f} |")

print('\n'.join(lines))
with open('table.md', 'w') as f:
    f.write('\n'.join(lines))


names = sorted(phrases)
percents = [counts[p] / total * 100 for p in names]

plt.figure(figsize=(10, 6))
plt.barh(names, percents)
plt.xlabel('Percentage of Tweets')
plt.title('Frequency of Keywords in Tweets, 2009-2018')
plt.tight_layout()
plt.savefig('tweets.png')

