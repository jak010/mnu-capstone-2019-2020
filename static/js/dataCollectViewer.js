
totalSet = [0, 0, 0, 0, 0, 0]

function doughnut_chart() {
    var ctx = document.getElementById("myChart").getContext('2d');
    ctx.canvas.width = 400;
    ctx.canvas.height = 100;


    var text_ = document.getElementById("data_live_variable");


    var myChart2 = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["0min", "10min", "20min","30min","40min","50min"],
            datasets: [{
                label: '# of Votes',
                data: totalSet,
                backgroundColor: [
                    'rgb(27, 108,168)',
                    'rgb(10, 151, 176)',
                    'rgb(225, 211,225)',
                    'rgb(152, 232,213)',
                    'rgb(45, 21,77)'

                ],

                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    fontColor: 'rgb(0,0,0,0.8)'
                }

            },

            cutoutPercentage: 60,
        }
    });
    myChart2.update();
}


try {
    console.log("Hello Welcome to Dashboard")

    setInterval(function() {
    var result;
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4 && xhr.status ==200) {
                var predict_data = xhr.responseText
                result = predict_data;
                console.log(result)
                if (result == 0) {
                    totalSet[0] += 1

                } else if (result == 1) {
                    totalSet[1] += 1

                } else if (result == 2) {
                    totalSet[2] += 1

                } else if (result == 3) {
                    totalSet[3] += 1

                }   else if (result == 4) {
                    totalSet[4] +=1

                }   else if (result == 5) {
                    totalSet[5] +=1
                }

                doughnut_chart()

            }
        }
        xhr.open("GET", "http://127.0.0.1:5000/dataCollectValue?flag=true");
        xhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
	    xhr.send();

}, 1000);
} catch(e) {
    console.log(" ");
}
