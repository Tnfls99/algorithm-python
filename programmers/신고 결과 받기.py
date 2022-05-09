def solution(id_list, report, k):
    d = {name: [i, []] for i, name in enumerate(id_list)}
    for r in report:
        r1, r2 = r.split(' ')
        if r1 not in d[r2][1]:
            d[r2][1].append(r1)
    
    result = [0 for _ in range(len(id_list))]
    
    for key in d.keys():
        if len(d[key][1]) >= k:
            for j in d[key][1]:
                result[d[j][0]] += 1
    return result