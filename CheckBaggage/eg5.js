
function resulsetStr() {
  try {
    let stList = document.getElementById('stList').value.trim();
    let result = '';
    if (!stList.includes(':')) {
      throw new Error('corrupt');
    }
    let [factorsStr, multiplesStr] = stList.split(':').map(s => s.trim());
    let factors = factorsStr.split(' ')
      .map(s => parseInt(s, 10))
      .filter(n => !isNaN(n));
    let multiples = multiplesStr.split(' ')
      .map(s => parseInt(s, 10))
      .filter(n => !isNaN(n));
    if (factors.length === 0 || multiples.length === 0) {
      throw new Error('corrupt');
    }
    let sum = multiples
      .filter(n => factors.some(m => n % m === 0))
      .reduce((a, b) => a + b, 0);
    result = `${sum} : ${factorsStr} : ${multiplesStr}`;
    alert('The result of this problem is ' + result);

  } catch (e) {
   
    let stList = document.getElementById('stList').value.trim();
    alert('The result of this problem is corrupt : ' + stList);
  }
}
