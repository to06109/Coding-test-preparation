function solution(A, B) {
  let result = 0
  A.sort((a, b) => a - b)
  B.sort((a, b) => b - a)

  result = A.reduce((acc, n, idx) => {
    return (acc += n * B[idx])
  }, 0)

  return result
}
