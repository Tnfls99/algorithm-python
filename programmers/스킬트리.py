def solution(skill, skill_trees):
    cnt = 0
    sd = {s:i for i, s in enumerate(skill)}
    for s in skill_trees:
        tree = [sd[i] for i in s if i in skill]
        if [i for i in range(len(tree))] == tree:
            cnt += 1
    return cnt


    """
    def solution(skill, skill_trees):
    cnt = 0

    for sk in skill_trees:
        skill_list = list(skill)

        for s in sk:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            cnt += 1
    return cnt
    """