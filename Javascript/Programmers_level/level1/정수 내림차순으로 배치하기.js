function solution(n) {
  let answer = 0
  const a = n.toString().split('')
  let arr = a.map((e) => parseInt(e))
  arr.sort()
  arr.reverse()
  answer = parseInt(arr.join(''))
  return answer
}
