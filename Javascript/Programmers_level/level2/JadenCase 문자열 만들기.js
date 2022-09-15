function solution(s) {
  var answer = []
  let arr = s.split(' ')
  arr.forEach((word) => {
    word = word.toLowerCase() // 단어 전체 소문자로 변환

    let wordArr = word.split('')
    if (typeof wordArr[0] === 'string') {
      wordArr[0] = wordArr[0].toUpperCase() // 단어 첫글자 대문자로 변환
    }
    answer.push(wordArr.join(''))
  })
  return answer.join(' ')
}

// 다른 사람의 풀이
// 이런 식으로 단어를 조합하는 방법도 있음(charAt(), slice() 사용)
result += String[i].charAt(0).toUpperCase() + String[i].slice(1)
