function solution(price, money, count) {
  let totalMoney = 0
  for (let i = 1; i < count + 1; i++) {
    totalMoney += price * i
  }
  const result = totalMoney - money
  return result > 0 ? result : 0
}
