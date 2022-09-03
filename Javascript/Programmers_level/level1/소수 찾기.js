function solution(n) {
  var answer = 0;
  const isPrime = (n) => {
    if (n === 2) return true;
    else if (n === 3) return true;
    else {
      for (let i = 2; i < Math.sqrt(n) + 1; i++) {
        if (n % i === 0) return false;
      }
      return true;
    }
  };

  for (let j = 2; j < n + 1; j++) {
    if (isPrime(j)) {
      answer += 1;
    }
  }

  return answer;
}
