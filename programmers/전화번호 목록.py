def solution(phone_book):
    
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book)-1):
        num = phone_book[i]
        if num == phone_book[i+1][:len(num)]:
            return False
    return True