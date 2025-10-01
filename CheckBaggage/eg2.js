//redefine these - ex1 should output the solution to project Euler Q1
//ex2 should output the sum of all multiples of a or b less than n



	// Project Euler Q1: Find the sum of all multiples of 3 or 5 below 1000
let euler1 = () => {
	let sum = 0;
	for (let i = 0; i < 1000; i++) {
		if (i % 3 === 0 || i % 5 === 0) {
			sum += i;
		}
	}
	alert('Sum of all multiples of 3 or 5 below 1000 is: ' + sum );
};

// Sum of all multiples of a or b below n ( Custom Input )
let eulerCustom = () => {
	let sum = 0;
    let n = parseInt(document.getElementById('n').value);  
    let a = parseInt(document.getElementById('a').value);
    let b = parseInt(document.getElementById('b').value);
	for (let i = 0; i < n; i++) {
		if (i % a === 0 || i % b === 0) {
			sum += i;
		}
	}
	alert('Sum of all multiples of ' + a + ' or ' + b + ' below ' + n + ' is: ' + sum  );
}
