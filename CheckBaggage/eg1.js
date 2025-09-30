const allowedWeight = 15;
            let currentWeight = 0;
            let check = () => {
                currentWeight = parseInt(document.getElementById('weight').value) || 0;
                if (currentWeight > allowedWeight) {
                    document.getElementById('removed').style.display = 'block';
                    document.getElementById('remB').style.display = 'block';
                    alert('Baggage overweight,you have to remove some weight.');
                } else {
                    document.getElementById('removed').style.display = 'none';
                    document.getElementById('remB').style.display = 'none';
                    alert('You are good to go!');
                }
            }

            let remove = () => {
                let removeWeight = parseInt(document.getElementById('removed').value) || 0;
                currentWeight -= removeWeight;
                document.getElementById('weight').value = currentWeight;
                if (currentWeight > allowedWeight) {
                    alert('Still overweight! Current weight: ' + currentWeight + 'kg');
                } else {
                    document.getElementById('removed').style.display = 'none';
                    document.getElementById('remB').style.display = 'none';
                    alert('Weight is now acceptable. You are good to go: ' + currentWeight + 'kg');
                }
            }