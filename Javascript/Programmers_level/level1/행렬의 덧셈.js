function solution(arr1, arr2) {
  const l1 = arr1.length
  const l2 = arr1[0].length
  let answer = []
  for (let i = 0; i < l1; i++) {
    let temp = []
    for (let j = 0; j < l2; j++) {
      temp.push(arr1[i][j] + arr2[i][j])
    }
    answer.push(temp)
  }
  return answer
}
