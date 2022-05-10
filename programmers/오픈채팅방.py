def solution(record):
    answer = []
    m = {"Enter": "님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    user = {}
    record = [r.split(" ") for r in record]
    for r in record:
        if r[0] != "Leave":
            user[r[1]] = r[2]
    for r in record:
        if r[0] == "Enter":
            answer.append(user[r[1]]+m[r[0]])
        elif r[0] == "Leave":
            answer.append(user[r[1]]+m[r[0]])
    return answer