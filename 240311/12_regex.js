let regex = /[a-z]0-9{6,10}/g; //g는 전역설정
let user_id = 'asdfRT099'
console.log(regex.exec(user_id)) //조건에 가장 부합하는 첫번쨰 결과
console.log(regex.test(user_id))
console.log(user_id.match(regex))  //조건에 가장 부합하는 첫번쨰 결과
console.log(user_id.search(regex)) // //조건에 가장 부합하는 가장첫 인덱스 반환

if (regex.test(usesr_id)) {
    console.log('아이디 사용가능');
}else {
    console.error('아이디사용간으')
}

let msg = '안녕하세요. hi 반갑습니다. nice'
let msg_regex = /[a-zA-Z]+/
// msg = msg.replace(msg_regex,'')
// console.log(msg)
