f = open("yesterday.txt", 'r')
yesterday_lyric = f.readlines()
f.close()

num = 0
for s in yesterday_lyric :
    ss = s.lower()
    num += ss.count("yesterday")

print("Number of a Word 'Yesterday' ", num)
