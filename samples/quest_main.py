import quest_making,quest_solving,quest_scoring


list_quiz=quest_making.quizmaking()                                                          # 입력 받은 list를 list_quiz로 지정  
list_user_answer = quest_solving.answermaking(list_quiz)                                   # 참여자의 이름과 답안지를 입력받아 list_user_answer 작성
list_sum = quest_scoring.calculating(list_user_answer,list_quiz)                               # 참여자의 점수를 list_sum에 작성
quest_scoring.averazing(list_sum,list_user_answer)                                             # 참여자의 점수와 과목 평균 출력4
