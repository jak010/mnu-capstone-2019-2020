var dataArray = new Array();
var xGroup = new Array();

function section01(param1) {
    now_prec = Number(param1);

    var ctx = document.getElementById("myChart");

    var dateobj = new Date();

    Minutes = dateobj.getMinutes();
    Seconds = dateobj.getSeconds();

    var cur_x = Minutes + ":" + Seconds+"초";

    dataArray.push(now_prec);
    xGroup.push(cur_x);

    if (xGroup.length % 15 == 0) {
        xGroup.length = 0;

    }
    console.log(now_prec);

    var myChart = new Chart(ctx, {

        type: 'line',

        data: {
            labels: xGroup,
            datasets: [{
                label: "Live View",
                data: dataArray,

                fill: false,
                borderColor: 'rgb(240,128,128)',

                lineTension: 0.5
            }]
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        fontColor: 'rgba(12, 13, 13, 1)',
                        fontSize: 14
                    },
                    gridLines: {
                        display: false,
                        color: "rgba(87, 152, 23, 1)",
                        lineWidth: 3
                    }
                }],

                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        min: -4.5,
                        max: 4.5,
                        stepSize: 0.5,
                        fontSize: 12,
                    },
                    gridLines: {
                        color: 'rgb(166, 201, 226)',
                        lineWidth: 3
                    },

                }],


            }
        }
    });

}
setInterval(function() {
    var result;
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4 && xhr.status ==200) {
                var predict_data = xhr.responseText
                result = predict_data;

//                var obj = document.getElementById("getPredictData");
//
//                obj.insertAdjacentHTML("beforeend",'<br>'+predict_data+'</br>');
//                obj.scrollTop = obj.scrollHeight;
                section01(result)
            }
        }
        xhr.open("Post", "./predict", true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	    xhr.send("predict=","1");


}, 2000);