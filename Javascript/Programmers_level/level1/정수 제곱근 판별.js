// function solution(n) {
//     var answer = 0;
//     let i = 1
//     for (i; i < n + 1; i++) {
//         if (i**2 === n) {
//             break
//         }
//     }
//     if (i === n + 1) answer = -1
//     else answer = (i+1) ** 2
//     return answer;
// }

// 50ms 시간단축
function solution(n) {
  var answer = 0
  let i = 1
  const temp = parseInt(Math.sqrt(n) + 1)
  for (i; i < temp; i++) {
    if (i ** 2 === n) {
      break
    }
  }
  if (i === temp) answer = -1
  else answer = (i + 1) ** 2
  return answer
}
