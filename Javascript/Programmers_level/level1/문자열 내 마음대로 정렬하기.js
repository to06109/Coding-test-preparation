function solution(strings, n) {
  strings.sort((a, b) => {
    let first = a[n];
    let second = b[n];
    // n번째 문자가 같을 경우
    if (first === second) {
      // 참이면 1, 거짓이면 -1 반환
      return (a > b) - (a < b);
    } else {
      return (first > second) - (first < second);
    }
  });

  return strings;
}

/*
function(a,b) < 0 이면 a를 b보다 작은 인덱스로 정렬한다.
function(a,b) == 0 이면 a와 b의 순서를 바꾸지 않는다.
function(a,b) > 0 이면 b를 a보다 작은 인덱스로 정렬한다.
*/
