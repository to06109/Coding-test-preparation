function solution(s) {
  var answer = true
  let left = 0
  let right = 0
  for (let letter of s) {
    if (letter === '(') left += 1
    else right += 1

    if (right > left) {
      answer = false
      break
    }
  }

  if (right !== left) answer = false

  return answer
}

// 다른 사람의 풀이
function solution(s) {
  let cnt = 0
  // 마지막이 "(" 이거나 처음이 ")" 인 경우 예외처리
  if (s[s.length - 1] === '(' || s[0] === ')') return false

  for (let i = 0; i < s.length; i++) {
    s[i] === '(' ? cnt++ : cnt--
    if (cnt < 0) break
  }

  return cnt === 0 ? true : false
}
