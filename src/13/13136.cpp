/**
 * 13136. Do Not Touch Anything
 * 
 * 작성자: xCrypt0r
 * 언어: C++14
 * 사용 메모리: 1,984 KB
 * 소요 시간: 0 ms
 * 해결 날짜: 2020년 9월 12일
 */

#include <iostream>

using namespace std;

int main()
{
    long long R, C, N;

    cin >> R >> C >> N;
    cout << (R / N + (R % N ? 1 : 0)) * (C / N + (C % N ? 1 : 0));
}