/* 
1. ? : 문 많이 이용하기
2. JS에서는 64 < Ascii < 91 이런 조건문 작동안함
*/

// 내 풀이
function solution(s, n) {
  let answer = ''
  for (let i = 0; i < s.length; i++) {
    if (s[i] != ' ') {
      const Ascii = s.charCodeAt(i)
      let changedAscii = Ascii + n
      // 대문자
      if (64 < Ascii && 91 > Ascii && 90 < changedAscii) {
        changedAscii = 64 + changedAscii - 90
        // 소문자
      } else if (96 < Ascii && 123 > Ascii && 122 < changedAscii) {
        changedAscii = 96 + changedAscii - 122
      }
      answer += String.fromCharCode(changedAscii)
    } else answer += ' '
  }
  return answer
}

// 아스키코드 안쓰는 방법
function solution(s, n) {
  var upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  var lower = 'abcdefghijklmnopqrstuvwxyz'
  var answer = ''

  for (var i = 0; i < s.length; i++) {
    var text = s[i]
    if (text == ' ') {
      answer += ' '
      continue
    }
    var textArr = upper.includes(text) ? upper : lower
    var index = textArr.indexOf(text) + n
    if (index >= textArr.length) index -= textArr.length
    answer += textArr[index]
  }
  return answer
}
