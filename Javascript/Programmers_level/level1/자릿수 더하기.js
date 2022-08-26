function solution(n) {
  let answer = 0
  const sample = n.toString().split('')
  sample.forEach((num) => (answer += parseInt(num)))
  return answer
}
