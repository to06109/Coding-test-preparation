function solution(n) {
  let answer = n.toString().split('')
  answer = answer.map((e) => parseInt(e))
  answer.reverse()
  return answer
}
