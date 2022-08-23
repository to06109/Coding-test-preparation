function solution(arr) {
  const d = Math.min(...arr)
  let answer = arr.filter((num) => num !== d)
  if (answer.length === 0) {
    answer.push(-1)
  }
  return answer
}

/* 
다른 사람의 풀이
function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)),1);
    if(arr.length<1)return[-1];
    return arr;
} 
*/
