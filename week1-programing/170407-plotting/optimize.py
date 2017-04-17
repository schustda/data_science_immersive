p1 = 0
p2 = 0
p3 = 0

from itertools import combinations
d = all2001
x = range(len(d))
c = (list(combinations(x,3)))
avg_obp = .36386867712807924
best_players = (0,0,0)
m = 0
for i in c:
    if (d.loc[i[0]]['salary'] + d.loc[i[1]]['salary']+ d.loc[i[2]]['salary']) > 15000000:
        pass

    else:
        obp = (d.loc[i[0]]['OBP'] + d.loc[i[1]]['OBP']+ d.loc[i[2]]['OBP'])/3
        if obp > m:
            best_players = (i[0],i[1],i[2])
            m = obp
return best_players
