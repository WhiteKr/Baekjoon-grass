"""
13073. Sums

작성자: xCrypt0r
언어: Python 3
사용 메모리: 29,380 KB
소요 시간: 920 ms
해결 날짜: 2020년 9월 19일
"""

def main():
    for _ in range(int(input())):
        N = int(input())

        print(f'{N * (N + 1) // 2} {N ** 2} {N * (N + 1)}')

if __name__ == '__main__':
    main()
