/* 문제 제한조건: 2 <= n <= 100,000
47번째 피보나치 수는 2,971,215,073이고 
이 수는 32비트 정수(int) 범위를 넘어서 오버플로우 발생

-> 모든 단계에서 1234567로 나눈 나머지를 구하기
   나머지 연산 특징: (a + b) % m = ((a % m) + (b % m)) % m
*/
function solution(n) {
  let arr = new Array(n)
  arr[0] = 0
  arr[1] = 1
  for (let i = 2; i <= n; i++) {
    arr[i] = ((arr[i - 1] % 1234567) + (arr[i - 2] % 1234567)) % 1234567
  }
  return arr[n] % 1234567
}
