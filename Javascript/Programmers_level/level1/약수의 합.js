// 이 방법이 속도 훨씬 빠름
function solution(n) {
  let answer = 0
  let arr = []
  // 약수 찾기
  for (let i = 1; i < Math.sqrt(n) + 1; i++) {
    if (n % i === 0) {
      arr.push(i, n / i)
    }
  }
  let set = new Set([...arr])
  set.forEach((a) => (answer += a))
  return answer
}

// function solution(n) {
//     let answer = 0;
//     // 약수 찾기
//     for (let i  = 1; i < parseInt(Math.sqrt(n)) + 1; i++) {
//         if (n % i === 0) {
//             console.log(i, n / i)
//             answer += i
//             if (i === n / i) {
//                 continue
//             }
//             answer += n / i
//         }
//     }
//     return answer;
// }
