function linearSearch(A, key){
    for(let i = 0; i < A.length; i++){
        if(A[i]===key){
            return i;
        }
    }
    return "Not Found";
}

console.log(linearSearch([1,2,3,4,5],3));
