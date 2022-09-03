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
