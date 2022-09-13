function solution(s) {
  var answer = []

  let zero = 0
  let num = 0
  let input = s

  // 이진변환 함수
  const transform = (s) => {
    zero += s.split('0').length - 1 // 지울 0개수 세기
    const s1 = s.replace(/0/g, '') // 0 제거
    const l = s1.length
    return l.toString(2) // 이진수로 변환
  }

  while (true) {
    if (input === '1') break
    input = transform(input)
    num += 1
  }
  answer.push(num)
  answer.push(zero)

  return answer
}
