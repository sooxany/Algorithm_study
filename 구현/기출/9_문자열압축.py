#함수만 짠 코드

def solution(s):
    answer = len(s)
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for i in range(1, int(len(s)/2) + 1 ): # 문자열 길이의 절반까지는 가야함
        pos = 0 # 어느 위치에서 처리하고 있는지 표현하는 변수
        length = len(s) # 우선 문자열 길이로 초기화

        while pos + i <= len(s): # 다음 문자열
            unit = s[pos:pos+i]
            pos += i

            cnt = 0
            while pos + i <= len(s):
                if unit == s[pos:pos+i]:
                    cnt += 1
                    pos += i
                else:
                    break

            if cnt > 0:
                length -= i * cnt

                if cnt < 9:
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4

        answer = min(answer, length)

    return answer



