def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurence_array = [0] * 26
    for char in string:
        arr_index = ord('char') - ord('a')
        alphabet_occurence_array[arr_index] += 1

    for num in alphabet_occurence_array:


    return "a"


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))