function solution(n) {
  var answer = 0
  for (let i = 1; i <= n; i++) {
    let cur = n
    let temp = i

    while (cur > 0) {
      cur -= temp
      temp += 1
      if (cur === 0) answer += 1 // n이 만들어지는 경우
    }
  }
  return answer
}
