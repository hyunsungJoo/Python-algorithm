def find_max_occurred_alphabet(string):
    # 알파벳 발생 횟수를 저장하는 배열
    alphabet_occurence_array = [0] * 26

    # 문자열 순회하며 알파벳 빈도 계산
    for char in string.lower():  # 소문자로 변환
        if char.isalpha():  # 알파벳인지 확인
            arr_index = ord(char) - ord('a')
            alphabet_occurence_array[arr_index] += 1

    # 최대 빈도와 해당 알파벳을 찾음
    max_occurence = 0
    max_index = 0

    for index in range(len(alphabet_occurence_array)):
        if alphabet_occurence_array[index] > max_occurence:
            max_occurence = alphabet_occurence_array[index]
            max_index = index

    # 최대 빈도의 알파벳 반환
    max_occurence_alphabet = chr(max_index + ord('a'))
    return max_occurence_alphabet


# 테스트
print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))
