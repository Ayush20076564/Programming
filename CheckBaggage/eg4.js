
function parseNumbers(str) {
    return str.split(' ').map(Number).filter(n => !isNaN(n));
}

function showResult(result) {
    alert('The result of this problem is ' + result);
}

function resultStr() {
    let strList = document.getElementById('strList').value;
    let result;
    try {
        let [factorsStr, multiplesStr] = strList.split(':').map(s => s.trim());
        let factors = parseNumbers(factorsStr);
        let multiples = parseNumbers(multiplesStr);
        let sum = multiples.filter(n => factors.some(m => m !== 0 && n % m === 0)).reduce((a, b) => a + b, 0);
        if (isNaN(sum)) sum = 0;
        result = `${sum} : ${factors.join(' ')} : ${multiples.join(' ')}`;
    } catch (e) {
        result = '0 : Invalid input';
    }
    showResult(result);
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