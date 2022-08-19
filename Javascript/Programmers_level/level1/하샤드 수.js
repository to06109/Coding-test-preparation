function solution(x) {
  let s = 0 // 각 자릿수의 합
  for (let i of x.toString()) {
    // Number()보다 parseInt로 형변환 하는게 더 안정적임
    s += parseInt(i)
  }
  return x % s === 0 ? true : false
}
