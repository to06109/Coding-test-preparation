function solution(s) {
  var answer = "";
  let str = s.split("");
  // sort() 함수는 배열 정렬 함수
  str.sort().reverse();
  answer = str.join("");
  return answer;
}
