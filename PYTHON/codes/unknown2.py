words = "a b b a b c b d b a b d b d b a b a b a b c b c b a b"
uniques = set(words.split())
print(uniques)
count=0
for i in uniques:
    count=count+1

print(count)
    #freqs = [(item, words.split.count(item)) for item in uniques]
#print(freqs)
