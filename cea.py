# the general hypothesis

G = [ ('?', '?', '?', '?','?','?','?') ]

# the specific hypothesis

S = [('0', '0', '0', '0','0','0','0')]

# attributes:
AV = (['sunny', 'rainy'], ['cool', 'warm'], ['normal', 'high'], ['light', 'strong'],['warm', 'cold'],['same', 'change'],['yes','no'])

# training examples:
D = [

    {'sample': ('sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes' ), 'positive': True },
    {'sample': ('sunny', 'warm', 'high', 'strong', 'warm', 'same', 'no' ), 'positive': False },
    {'sample': ('rainy', 'cool', 'high', 'strong', 'warm', 'change', 'no'), 'positive': False},
    {'sample': ('sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes'), 'positive': True}
  
]


def consistent(hypothesis, sample):
    return all([hypothesis[i] == sample[i] or hypothesis[i] == '?' for i in range(len(hypothesis))])


def more_general(a, b):
    result = False
    if a == '0' and b != '0':
        result = True
    elif a != '?' and b == '?':
        result = True
    return result


def more_specific(a, b):
    result = False
    if a == '?' and b != '?':
        result = True
    elif a != '0' and b == '0':
        result = True
        return result


for d in D:

    if d['positive']:
        G = [g for g in G if consistent(g, d['sample'])]
        for s in S:
            if not consistent(s, d['sample']):
                S.remove(s)
                dd = d['sample'] 
                if s == 0:
                    h = dd[s]
                else:
                    h = '?'  
                if consistent(h, d['sample']) and any([more_general(g, h) for g in G]):
                    S.append(h)
                '''S.remove(s)

                # Adding to S all minimal generalizations of s by h:
                dd = d['sample'] 
                if s == 0:
                    h = dd[s]
                else:
                    h = '?'  


                if consistent(h, d['sample']) and any([more_general(g, h) for g in G]):
                    S.append(h)'''

                #Removing from S any hypothesis that is more general than     another hypothesis in S
                for s2 in S:
                    if any([more_general(s2, s3) and not s2 == s3 for s3 in S]):
                        S.remove(s2)

    else:
        S = [s for s in S if not consistent(s, d['sample'])]
        for g in G:
            if consistent(g, d['sample']):
                G.remove(g)

               # Add to G all minimal specializations h of g
                for ai in range(len(AV)):
                    if g[ai] == '?':
                        h = list(g)
                        h[ai] = AV[ai][1 - AV[ai].index(d['sample'][ai])]
                        h = tuple(h)
                        if not consistent(h, d['sample']) and any([more_specific(s, h) for s in S]):
                            G.append(h)




    print('Sample: {} {}\nG: {}\nS: {}\n'.format('+' if d['positive'] else '-', d['sample'], G, S))
