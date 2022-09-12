function solution(numbers) {
    let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let answer = 0;
    
    numbers.forEach((item) => {
        const index = arr.indexOf(item)
        arr[index] = 0
    })
             
    arr.forEach((a) => {
        answer += a
    })
    
    return answer;
}