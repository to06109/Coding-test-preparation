function solution(n, m) {
  var answer = []
  let a = n,
    b = m
  // 최대공약수
  while (a % b !== 0) {
    let temp = a
    a = b
    b = temp % b
  }
  answer.push(b)

  // 최소공배수
  answer.push(parseInt((m * n) / b))
  return answer
}
