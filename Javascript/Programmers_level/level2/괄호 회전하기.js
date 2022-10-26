// 14 테케 실패
// "[{]}"의  경우 정답은 0이어야 하는데 1이 나옴
// 괄호의 개수가 맞는지만 확인하고 괄호가 맞는 형식인지 체크하지 않음

function solution(s) {
  const hash = {
    ']': '[',
    '}': '{',
    ')': '(',
  }

  // 문자열 회전 함수
  const rotate = (text, noOfChars = 0) => {
    const first = text.slice(noOfChars)
    const second = text.slice(0, noOfChars)
    return first + second
  }

  // 괄호문자열 판별 함수
  const isRight = (text) => {
    const count = {
      '[': 0,
      '{': 0,
      '(': 0,
    }
    const arr = [...text]
    const values = Object.values(hash)
    for (let letter of arr) {
      if (values.includes(letter)) {
        count[letter] += 1
      } else {
        count[hash[letter]] -= 1
        if (count[hash[letter]] < 0) return false
      }
    }

    const count_values = Object.values(count)
    const num_no = count_values.filter((item) => item !== 0)
    if (num_no.length > 0) return false
    return true
  }

  let result = 0
  for (let i = 0; i < s.length; i++) {
    const s_rotated = rotate(s, i)
    if (isRight(s_rotated)) result += 1
  }

  return result
}
