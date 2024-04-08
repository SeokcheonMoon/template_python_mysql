import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='127.0.0.1',  # 컨테이너 이름 또는 IP
    port= 3306,
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4'
)


def quizmaking():
    list_quiz = [] # 리스트화
    question_type = int(input("보기 수를 입력하세요. 숫자만 입력하세요."))  # 문제생성1
    num_questions = int(input("문항 수를 입력하세요."))                     # 문제생성2
    print("문제와 선택지를 입력하세요.")
    for quiz in range(num_questions):        # 문항 수 만큼 
        dict_quizlist = {}                   # 딕셔너리화
        dict_quizlist["question"] = input("문항 : ")     # question, choice, answer, score 받기
        dict_quizlist["choice"] = []
        for choice in range(question_type) : 
            dict_quizlist["choice"].append(input("보기 : "))
        dict_quizlist["answer"] = input("정답 : ")
        dict_quizlist["score"] = int(input("배점 : "))
        list_quiz.append(dict_quizlist)

    with conn.cursor() as cursor:
    # QUEST 테이블에 값 넣기

        for i in range(len(list_quiz)):
            pk_quest = f'QUES_{i+1}'
            sql = "INSERT INTO QUEST (PK_QUEST, QUESTION, SCORE, `FK_QUEST`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (pk_quest, list_quiz[i]['question'], list_quiz[i]["score"], pk_quest))
            conn.commit()
            # OPTION 테이블에 값 넣기
            for x in range(min(question_type, len(list_quiz[i]['choice']))):
                sql = "INSERT INTO `QUEST` (`NUMBER`, `OPTION`) VALUES (%s, %s) "
                cursor.execute(sql, (x+1, list_quiz[i]['choice'][x]))

        # for i in range(len(list_quiz)):
        #     pk_quest = f'QUES_{i+1}'
        #     sql = "INSERT INTO QUEST (PK_QUEST, QUESTION, SCORE, `FK_QUEST`) VALUES (%s, %s, %s, %s)"
        #     cursor.execute(sql, (pk_quest, list_quiz[i]['question'], list_quiz[i]["score"], pk_quest))
        #     conn.commit()
        #     # OPTION 테이블에 값 넣기
        #     for x in range(min(question_type, len(list_quiz[i]['choice']))):
        #         sql = "INSERT INTO `QUEST` (`NUMBER`, `OPTION`, `FK_QUEST`) VALUES (%s, %s, %s) "
        #         cursor.execute(sql, (x+1, list_quiz[i]['choice'][x], pk_quest))
        #         conn.commit()


        # for i in range(len(list_quiz)):

        #     pk_quest = f'QUES_{i+1}'
        #     sql = "INSERT INTO QUEST (PK_QUEST,QUESTION, SCORE,`FK_QUEST` ) VALUES (%s, %s, %s, %s)"
        #     cursor.execute(sql, (pk_quest, list_quiz[i]['question'], list_quiz[i]["score"],""))
        #     conn.commit()
        #     # OPTION 테이블에 값 넣기
        #     for x in range(min(question_type, len(list_quiz[i]['choice']))):
        #     #    sql = "SELECT COUNT(OPTION) FROM `QUEST`"
        #         # cursor.execute(sql)
        #         # number = cursor.fetchall()
        #         # number = int(number[0][0])

        #         sql = "INSERT INTO `QUEST` (`NUMBER`,`OPTION`) VALUES (%s, %s) "
        #         cursor.execute(sql, (x+1 ,list_quiz[i]['choice'][x]))
        #         
        # Read
        sql = "SELECT * FROM TableName"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)  # 각 행 출력     
    conn.close()             
    return list_quiz

# try:
#     list_quiz,question_type = quizmaking()
    
#     with conn.cursor() as cursor:
#        # QUEST 테이블에 값 넣기
#         for i in range(len(list_quiz)):
#             sql = "INSERT INTO QUEST (QUES_ID,QUESTION, SCORE) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (f'QUES_{i+1}', list_quiz[i]['question'], list_quiz[i]["score"]))
#             conn.commit()
#             # OPTION 테이블에 값 넣기
#             for x in range(question_type):
#                 sql = "INSERT INTO `OPTION` (`OPTION_ID`,`QUES_ID`,`NUMBER`,`OPTION`,`ANSWER`) VALUES (%s, %s, %s, %s, %s) "
#                 cursor.execute(sql, (f'OPTION_{x+1}', f'QUES_{i+1}', x+1 ,list_quiz[i]['choice'][x], list_quiz[i]["answer"]))
#                 conn.commit()

#         # Read
#         sql = "SELECT * FROM TableName"
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         for row in data:
#             print(row)  # 각 행 출력

        # # Update
        # sql = "UPDATE QUEST SET column1=%s WHERE pk_id=%s"
        # cursor.execute(sql, ('newvalue1', 1))
        # conn.commit()

        # # Delete
        # sql = "DELETE FROM TableName WHERE pk_id=%s"
        # cursor.execute(sql, (1,))
        # conn.commit()
# finally:
#     conn.close()

# def quizmaking():
#     list_quiz = [] # 리스트화
#     question_type = int(input("보기 수를 입력하세요. 숫자만 입력하세요."))  # 문제생성1
#     num_questions = int(input("문항 수를 입력하세요."))                     # 문제생성2
#     print("문제와 선택지를 입력하세요.")
#     for quiz in range(num_questions):        # 문항 수 만큼 
#         dict_quizlist = {}                   # 딕셔너리화
#         dict_quizlist["question"] = input("문항 : ")     # question, choice, answer, score 받기
#         dict_quizlist["choice"] = []
#         for choice in range(question_type) : 
#             dict_quizlist["choice"].append(input("보기 : "))
#         dict_quizlist["answer"] = input("정답 : ")
#         dict_quizlist["score"] = int(input("배점 : "))
#         list_quiz.append(dict_quizlist)                  
#     return list_quiz, question_type


# try:
#     list_quiz,question_type = quizmaking()
    
#     with conn.cursor() as cursor:
#        # QUEST 테이블에 값 넣기
#         for i in range(len(list_quiz)):
#             sql = "INSERT INTO QUEST (QUES_ID,QUESTION, SCORE) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (f'QUES_{i+1}', list_quiz[i]['question'], list_quiz[i]["score"]))
#             conn.commit()
#             # OPTION 테이블에 값 넣기
#             for x in range(question_type):
#                 sql = "INSERT INTO `OPTION` (`OPTION_ID`,`QUES_ID`,`NUMBER`,`OPTION`,`ANSWER`) VALUES (%s, %s, %s, %s, %s) "
#                 cursor.execute(sql, (f'OPTION_{x+1}', f'QUES_{i+1}', x+1 ,list_quiz[i]['choice'][x], list_quiz[i]["answer"]))
#                 conn.commit()

#         # Read
#         sql = "SELECT * FROM TableName"
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         for row in data:
#             print(row)  # 각 행 출력
