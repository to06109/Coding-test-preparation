function solution(a, b) {
  var answer = 0
  for (let i = 0; i < a.length; i++) {
    answer += a[i] * b[i]
  }
  return answer
}

// 다른 사람의 풀이 -> reduce는 누산기가 포함되어있어 누적값을 구할 때 용이
function solution(a, b) {
  var answer = a.reduce((acc, cur, idx) => (acc += cur * b[idx]), 0)
  return answer
}
