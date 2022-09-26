function solution(numbers) {
    let arr = new Set()
    
    idx = 0
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            arr.add(numbers[i] + numbers[j])
        }
    }
    
    // set을 배열로 바꾸기: Array.from(set)
    const result = Array.from(arr).sort((a, b) => {
        return a - b
    })
    
    return result
    
}

/* 다른 사람의 풀이
// 이렇게도 set을 list로 변환할 수 있음
const answer = [...new Set(temp)]

return answer.sort((a, b) => a - b)
*/