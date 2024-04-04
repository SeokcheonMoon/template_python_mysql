# 나중에 지울것
# list_quiz=[
#     {'question': '1. Python의 창시자는 누구인가?', 'choice': ['Guido van Rossum', 'James Gosling', 'Dennis Ritchie', 'Brendan Eich'], 'answer': '1', 'score': 5},
#     {'question': '2. Python에서 리스트의 길이를 반환하는 내장 함수는?', 'choice': ['sum', 'len', 'list', 'Str'], 'answer': '2', 'score': 5},
#     {'question': '3. 주문 테이블에서 2023년에 이루어진 주문 수를 구하는 쿼리를 작성하시오.', 'choice': ["SELECT COUNT(1) SELECT COUNT(*) FROM orders WHERE order_date >= '2023-01-01' AND order_date < '2024-01-01';", "SELECT COUNT(*) FROM orders WHERE order_date = '2023-01-01';", "SELECT COUNT(*) FROM orders WHERE order_date = '2023-12-31';", "SELECT COUNT(*) FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';"], 'answer': '1', 'score': 5}
# ]
# list_user_answer = [{'user_name': '문석천', 'user_answer': ['1', '2', '1']}]




def calculating(list_user_answer,list_quiz):
    list_sum = []
    for x in range(len(list_user_answer)) :  #------------------------------------------------------------------------------------list_quiz 내용만큼 숫자 받아 for구문 돌리기
        sum = 0
        for y in range(len(list_quiz)) :
            if list_quiz[y]["answer"] == list_user_answer[x]["user_answer"][y] :
                sum = sum + list_quiz[x]["score"]  #-------------------------------------------------------------------------------------------------한사람의 점수 합계구하기
                pass
            pass
        pass
        list_sum.append(sum) #-------------------------------------------------------------------------------------------------------list_sum에 위에서 받는 sum 값을 리스트로 배열
        pass
    return list_sum

# calculating(list_user_answer,list_quiz)


def averazing(list_sum,list_user_answer):               
    total_score = 0
    for i in range(len(list_sum)):
        total_score = total_score + list_sum[i] #-------------------------------------------------------------------------------list_sum 내 값들을 순서대로 더해 점수 총합을 구하기
        pass
    pass
    average = total_score/len(list_user_answer)  #--------------------------------------------------------------------------------------total score를 user수 만큼 나눠 평균 구하기
    pass
    print("응시자별 채점결과:")
    for number in range(len(list_user_answer)) :
        print("{}:{}점".format(list_user_answer[number]["user_name"],list_sum[number])) #----------------------------list answer에 해당하는 순서의 참여자 이름과 참여자의 총점 구하기
    print("과목 평균 점수: {}".format(average))
    return  average

# averazing(list_sum,list_user_answer)


if __name__ == "__main__":
    apple = calculating(list_user_answer,list_quiz)
    averazing(apple,list_user_answer)
