function solution(A, B) {
  let result = 0
  // 정렬할 때 그냥 sort() 쓰면 안됨!!
  A.sort((a, b) => a - b)
  B.sort((a, b) => b - a)

  result = A.reduce((acc, n, idx) => {
    return (acc += n * B[idx])
  }, 0)

  return result
}
