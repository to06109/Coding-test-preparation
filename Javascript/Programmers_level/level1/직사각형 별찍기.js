process.stdin.setEncoding('utf8')
process.stdin.on('data', (data) => {
  // 입력 받아서
  const n = data.split(' ')
  // 상수로 변환
  const a = Number(n[0]),
    b = Number(n[1])

  const row = '*'.repeat(a)

  for (let i = 0; i < b; i++) {
    console.log(row)
  }
})
