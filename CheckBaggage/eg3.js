// Returns sum of elements in l that are multiples of a or b
function listEuler1Sum(a1, b1, l) {
    return l.filter(x => x % a1 === 0 || x % b1 === 0).reduce((sum, x) => sum + x, 0);
}

// Returns sum of elements in l that are multiples of any value in array a ( 2 values in aList )
function listEuler2Sum(aList, mList) { 
    return mList.filter(x => aList.some(y => x % y === 0)).reduce((sum, x) => sum + x, 0);
}

// Returns sum of elements in l that are multiples of any value in array a (Multiple values in aList)
function listEuler3Sum(aList, mList) {
    return mList.filter(x => aList.some(y => x % y === 0)).reduce((sum, x) => sum + x, 0);
}


function listEuler1() {
    let a = document.getElementById('a1').value;
    let b = document.getElementById('b1').value;
    let l = document.getElementById('l').value.split(" ").map(x => parseInt(x));
    let result = listEuler1Sum(a, b, l);
    alert('Sum is '  + result);
}

function listEuler2() {
    let aList = document.getElementById('aList').value.split(" ").map(x => parseInt(x));
    let mList = document.getElementById('mList').value.split(" ").map(x => parseInt(x));
    let result = listEuler2Sum(aList, mList);
    alert(' sum of the values is ' + result);
}

function listEuler3() {
    let aList = document.getElementById('aList').value.split(" ").map(x => parseInt(x));
    let mList = document.getElementById('mList').value.split(" ").map(x => parseInt(x));
    let result = listEuler3Sum(aList, mList);
    alert('SUm of the multiple of Values is ' + result);
}