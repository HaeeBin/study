def sort_key(t) :
    return t[1]


from collections import OrderedDict
from collections import defaultdict

text = """A press release is the quickest and easiest way to get free publicity. If well written, 
a press release can result in multiple published articles about your firm and its products. 
And that can mean new prospects contacting you asking you to sell to them.""".lower().split()

d = defaultdict(lambda : 0)
for k in text :
    d[k] += 1


for k, v in OrderedDict(sorted(d.items(), key = sort_key)).items() :
    print(k, v)

