function solution(n) {
  var answer = "";
  const even = "수박";
  const odd = "수";
  if (n % 2 === 0) answer += even.repeat(n / 2);
  else answer += even.repeat(n / 2) + odd;

  return answer;
}
