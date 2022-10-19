function solution(a, b) {
  // 윤년 -> 2월 29일까지
  // 2016년 1월 1일 금요일
  // 1, 3, 5, 7, 8, 10, 12 -> 31일
  // 4, 6, 9, 11 -> 30일
  // 2 -> 29일

  const th31 = [1, 3, 5, 7, 8, 10, 12];
  const th30 = [4, 6, 9, 11];
  const s = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];

  let day = 0;
  for (let i = 1; i < a; i++) {
    if (th31.includes(i)) day += 31;
    else if (th30.includes(i)) day += 30;
    else day += 29;
  }
  day += b;
  let answer = s[day % 7];

  return answer;
}
