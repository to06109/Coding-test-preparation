function solution(a, b) {
  let answer = 0;
  if (a > b) {
    let temp;
    temp = b;
    b = a;
    a = temp;
  }
  for (let i = a; i < b + 1; i++) {
    answer += i;
  }
  return answer;
}
