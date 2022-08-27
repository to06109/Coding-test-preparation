function solution(n) {
  let answer = 0
  let arr = []
  for (let i = 1; i < Math.sqrt(n) + 1; i++) {
    if (n % i === 0) {
      arr.push(i, n / i)
    }
  }
  let set = new Set([...arr])
  set.forEach((a) => (answer += a))
  return answer
}

// 조건문으로 약수중복 처리
// function solution(n) {
//     let answer = 0;
//     for (let i  = 1; i < parseInt(Math.sqrt(n)) + 1; i++) {
//         if (n % i === 0) {
//             answer += i
//             if (i === n / i) {
//                 continue
//             }
//             answer += n / i
//         }
//     }
//     return answer;
// }
