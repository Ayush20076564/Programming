
function resultStr() {
    let strList = document.getElementById('strList').value;
    let [factorsStr, multiplesStr] = strList.split(':').map(s => s.trim());
    let factors = factorsStr.split(' ').map(Number);
    let multiples = multiplesStr.split(' ').map(Number);
    let sum = multiples.filter(n => factors.some(m => n % m === 0)).reduce((a, b) => a + b, 0);
    let result = `${sum} : ${factors.join(' ')} : ${multiples.join(' ')}`;
    alert('The result of this problem is ' +result);
}


///////Create a function to read a string of the form:
// factors : multiples
//and output a string:
// result : factors : multiples

//where factors and multiples are space separated lists of integers

// Example Input : 
// 3 5 : 1 2 3 4 5 6 7 8 9

// Example Output : 
// 23 : 3 5 : 1 2 3 4 5 6 7 8 9

//keep code DRY (Don't repeat yourself)