function linearSearch(A, key){
    let i = 0, n = A.length;
    A[n] = key;
    while(A[i] !== key){
        i++;
    }
    if(i === n){
        return "Not Found";
    }
    return i;
}

console.log(linearSearch([1,2,3,4,5],3));
