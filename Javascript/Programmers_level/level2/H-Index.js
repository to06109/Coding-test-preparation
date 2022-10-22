function solution(citations) {
  citations.sort((a, b) => {
    return a - b
  })

  for (let h = citations[citations.length - 1]; h > -1; h--) {
    // h번 인용된 논문이 h편 이상인지 확인
    let temp = citations.filter((item) => item >= h)
    if (temp.length >= h) {
      return h
    }
  }
}
