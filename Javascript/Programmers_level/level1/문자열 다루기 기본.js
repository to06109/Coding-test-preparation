function solution(s) {
  // 1. forEach 비동기 문제 -> 문자열을 검색해서 false를 반환하기 전에 무조건 for문 밖의 true를 반환해버림
  // 2. 그냥 isNaN(s)로 하면 s가 "1e22" 의 지수 형식이나 "0x2FA3"의 16진수 형식이면
  // 숫자로 인식해서 false를 반환해버린다!!
  let len = s.length;
  if (len === 4 || len === 6) {
    for (item of [...s]) {
      if (isNaN(parseInt(item))) return false;
    }
    return true;
  }
  return false;
}
