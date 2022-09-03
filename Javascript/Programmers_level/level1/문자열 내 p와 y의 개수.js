function solution(s) {
  let p = 0
  let y = 0
  for (item of s.toLowerCase()) {
    if (item === 'p') p += 1
    else if (item === 'y') y += 1
  }

  if (p === y) return true
  else if (p === 0 && y === 0) return true
  else return false
}

// 다른 코드 참고
function numPY(s) {
  return s.toUpperCase().split('P').length === s.toUpperCase().split('Y').length
}
