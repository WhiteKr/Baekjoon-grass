"""
16189. Repetitive Palindrome

작성자: xCrypt0r
언어: Python 3
사용 메모리: 29,872 KB
소요 시간: 68 ms
해결 날짜: 2020년 9월 20일
"""

def main():
    s = input()

    input()
    print('YES' if s == s[::-1] else 'NO')

if __name__ == '__main__':
    main()
