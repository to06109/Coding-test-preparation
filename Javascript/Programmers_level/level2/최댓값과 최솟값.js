function solution(s) {
  let arr = s.split(" ");
  arr = arr.map((item) => parseInt(item));

  var answer = "";
  answer = Math.min(...arr) + " " + Math.max(...arr);

  return answer;
}
