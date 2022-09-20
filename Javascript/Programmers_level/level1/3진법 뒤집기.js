function solution(n) {
  let a = n.toString(3).split('').reverse().join('') // 10진법을 3진법으로 변환
  return parseInt(a, 3) // 3진법을 10진법으로 변환
}
