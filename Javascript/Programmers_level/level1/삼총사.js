// 완탐으로 풀어보기
function solution(number) {
  var answer = 0;
  number.sort();
  len = number.length;
  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      for (let m = j + 1; m < len; m++) {
        if (number[i] + number[j] + number[m] === 0) {
          answer += 1;
        }
      }
    }
  }

  return answer;
}
