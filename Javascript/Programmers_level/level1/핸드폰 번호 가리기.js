// 1차 풀이
// function solution(phone_number) {
//     var answer = '';
    
//     let len = phone_number.length
//     // 뒤에 4개 뺀 개수만큼 별찍기
//     for (let i = len; i > 4; i--) {
//         answer += "*"
//     }
//     // 뒤에 네 글자 잘라서 붙여주기
//     answer += phone_number.slice(len - 4, len + 1)

//     return answer;
// }

// 2차 풀이
function solution(phone_number) {
    var answer = '';
    const d = phone_number.slice(-4)
    answer = "*".repeat(phone_number.length - 4) + d
    return answer;
}