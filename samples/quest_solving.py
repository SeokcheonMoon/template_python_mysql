import pymysql
# import quest_making
# list_quiz=quest_making.quizmaking()


# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='127.0.0.1',  # 컨테이너 이름 또는 IP
    port= 3306,
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4'
)

# # quest_making에서 가져온 임의값 - 나중에 지울것
# list_quiz=[
#     {'question': '1. Python의 창시자는 누구인가?', 'choice': ['Guido van Rossum', 'James Gosling', 'Dennis Ritchie', 'Brendan Eich'], 'answer': '1', 'score': 5},
#     {'question': '2. Python에서 리스트의 길이를 반환하는 내장 함수는?', 'choice': ['sum', 'len', 'list', 'Str'], 'answer': '2', 'score': 5},
#     {'question': '3. 주문 테이블에서 2023년에 이루어진 주문 수를 구하는 쿼리를 작성하시오.', 'choice': ["SELECT COUNT(1) SELECT COUNT(*) FROM orders WHERE order_date >= '2023-01-01' AND order_date < '2024-01-01';", "SELECT COUNT(*) FROM orders WHERE order_date = '2023-01-01';", "SELECT COUNT(*) FROM orders WHERE order_date = '2023-12-31';", "SELECT COUNT(*) FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';"], 'answer': '1', 'score': 5}
# ]

# 사용자의 답안을 기록하는 함수
def answermaking(list_quiz):  
    # 사용자의 답안을 저장할 리스트 초기화
    list_user_answer = []  

    while True:  # 무한 루프 시작
        # 각 사용자의 답안을 저장할 리스트 초기화
        list_answer = []  
        str_username = input("응시자의 이름을 입력하세요: ")  # 사용자 이름 입력
        
        # 문제 리스트의 길이만큼 반복
        for i in range(len(list_quiz)):  
            quizs = list_quiz[i]["question"]  # 문제를 추출
            print("문항{}: {}".format(i+1, quizs))  # 문제 번호와 문제 출력
            choices = list_quiz[i]["choice"]  # 선택지 추출
            print("선택지")  # "선택지" 출력
            for j in range(len(choices)):  # 선택지의 갯수만큼 반복
                print("{}. {}".format(j+1, choices[j]))  # 선택지 번호와 선택지 출력
            user_answer = input("답: ")  # 사용자 답안 입력
            list_answer.append(user_answer)  # 사용자 답안을 리스트에 추가
            print("--------------") 

        # 사용자의 이름과 답안을 저장할 딕셔너리 초기화    
        dic_user = {}  
        # 사용자 이름 딕셔너리에 저장
        dic_user['user_name'] = str_username  
        # 사용자 답안 딕셔너리에 저장
        dic_user['user_answer'] = list_answer  
        
        ## mysql에 입력
        with conn.cursor() as cursor:
        # USER 테이블에 값 넣기 
            for x in range(len(list_user_answer)):
                sql = "INSERT INTO USER (USER_ID,USER_NAME) VALUES (%s, %s)"
                cursor.execute(sql, (f'USER_{x+1}',list_user_answer[x]['user_name']))
                conn.commit()

                # ANSWER 테이블에 값 넣기
                for y in range(len(list_user_answer[x]['user_answer'])):
                    sql = "INSERT INTO ANSWER (ANSWER_ID, OPTION_ID, QUES_ID, USER_ID) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (f'ANSWER_{y+1}',f'OPTION_{list_user_answer[x]["user_answer"][y]}', f'QUES_{y+1}',f'USER_{x+1}'))
                    conn.commit()
            # Read
            sql = "SELECT * FROM TableName"
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:
                print(row)  # 각 행 출력
        



        # 사용자 이름과 답안이 저장된 딕셔너리를 리스트에 추가
        list_user_answer.append(dic_user)  
        quit_input = input("다음 응시자가 있나요? (계속: c, 종료: x): ").lower()
        if quit_input == 'x':                  # 'x'를 입력하면
            print("프로그램이 종료되었습니다.")  # 종료 메시지 출력 후
            conn.close()
            return list_user_answer            # 사용자 답안 리스트 반환
        elif quit_input == 'c':  # 'c'를 입력하면
            continue  # 다음 사용자를 위해 루프 계속

        