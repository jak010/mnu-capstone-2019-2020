var dataArray = new Array();
var xGroup = new Array();


// [0] 경고
// [1] 주의
// [2] 정상
var pieChartSet = [0, 0, 0];

function section01(param1) {
    console.log(pieChartSet[0],pieChartSet[1],pieChartSet[2]);
    console.log(param1);

    now_prec = Number(param1);

    var ctx = document.getElementById("myChart");

    var dateobj = new Date();
    Hours = dateobj.getHours();
    Minutes = dateobj.getMinutes();
    Seconds = dateobj.getSeconds();

    var curret_date = Hours + ":"+ Minutes +":" + Seconds;

    // 경고
    if(Number(param1) > 1.3){
        pieChartSet[0] += 1;

    // 주의
   } else if( Number(param1) > 0.9  || Number(param1) < 0) {
        pieChartSet[1] += 1;

   // 정상
   } else {
    pieChartSet[2] += 1;
   }

    dataArray.push(now_prec);
    xGroup.push(curret_date);

    if (xGroup.length % 70 == 0) {
        xGroup.length = 0;
    }


    var myChart = new Chart(ctx, {

        type: 'line',

        data: {
            labels: xGroup,
            datasets: [{
                label: "Live Predict Grpah",
                data: dataArray,

                backgroundColor: 'rgb(255, 192, 203, 1)',
                // backgroundColor: 'rgb(0, 0, 0)',
                fill: false,

                borderColor: [
                    'rgb(255, 192, 203,0.6)',
                ],
                borderWidth: 2,
                lineTension: 0.2,


            }]


        },
        options: {

            maintainAspectRatio: false,

            legend: {
                display: true,

                labels: {
                    fontColor: 'rgb(255,255,255)',
                }
            },

            scales: {

                xAxes: [{

                    ticks: {
                        fontColor: 'rgb(255, 255, 255,1)',
                        fontSize: 14
                    },
                    gridLines: {
                        display: false,
                        color: "rgb(0, 0, 0,0.4)",
                        lineWidth: 0,
                    }
                }],

                yAxes: [{
                    ticks: {
                        min: -1,
                        max: 2,
                        stepSize: 0.5,
                        fontSize: 12,
                        fontColor: 'rgb(255, 255, 255,0.7)'
                    },
                    gridLines: {
                        color: 'rgba(255, 255, 255,0.7)',
                        lineWidth: 0.5
                    },

                }],


            },
            animation: {
                duration: 1,
                onComplete: function() {
                    var chartInstance = this.chart,
                        ctx = chartInstance.ctx;
                    ctx.font = Chart.helpers.fontString(Chart.defaults.global.defaultFontSize, Chart.defaults.global.defaultFontStyle, Chart.defaults.global.defaultFontFamily);
                    ctx.fillStyle = 'purple';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'bottom';

                    this.data.datasets.forEach(function(dataset, i) {
                        var meta = chartInstance.controller.getDatasetMeta(i);
                        meta.data.forEach(function(bar, index) {
                            var data = dataset.data[index];

                            if (data > 0.7) {

                                data = "경고";

                            } else if ((data >0.6) || (data < 0)) {
                                data = "주의";

                            }else {
                                data = "정상";
                            }

                            ctx.fillText(data, bar._model.x, bar._model.y - 5);
                        });
                    });
                }
            }
        }
    });

}



function waring_alaram_chart() {
    var ctx = document.getElementById("warning_alarm_chart").getContext('2d');

    totalValue = pieChartSet[0] + pieChartSet[1] + pieChartSet[2];
    warningValue = pieChartSet[0];

    var warning_data_set = [warningValue, totalValue];

    var warning_alarm_text_update = document.getElementById("warning_alarm_text_set");
    warning_alarm_text_update.innerHTML = "Warning : " + warningValue;

    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["경고", "전체"],
            datasets: [{
                label: '# of Votes',
                data: warning_data_set,
                backgroundColor: [
                    'rgb(219, 15, 38,0.5)',
                ],
                borderColor: [
                    'rgba(0, 0, 0, 0.4)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    fontColor: 'rgb(255,255,255,0.8)'
                }
            }
        }
    });
}

function caution_alaram_chart() {
    var ctx = document.getElementById("caution_alarm_chart").getContext('2d');

    totalValue = pieChartSet[0] + pieChartSet[1] + pieChartSet[2];
    cautionValue = pieChartSet[1];

    var caution_data_set = [cautionValue, totalValue];
    var warning_alarm_text_update = document.getElementById("caution_alarm_text_set");
    warning_alarm_text_update.innerHTML = "Caution : " + cautionValue;

    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["주의", "전체"],
            datasets: [{
                label: '# of Votes',
                data: caution_data_set,
                backgroundColor: [
                    'rgb(255, 255, 0,0.5)',
                ],
                borderColor: [
                    'rgba(0, 0, 0, 0.4)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    fontColor: 'rgb(255,255,255,0.8)'
                }
            }
        }
    });
}



function green_alaram_chart() {
    var ctx = document.getElementById("green_alarm_chart").getContext('2d');

    totalValue = pieChartSet[0] + pieChartSet[1] + pieChartSet[2];
    greenValue = pieChartSet[2];

    var green_data_set = [greenValue, totalValue];

    var green_alarm_text_update = document.getElementById("green_alarm_text_set");
    green_alarm_text_update.innerHTML = "Notice : " + greenValue;

    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["정상", "전체"],
            datasets: [{
                label: '# of Votes',
                data: green_data_set,
                backgroundColor: [
                    'rgb(124, 252, 0,0.5)',
                ],
                borderColor: [
                    'rgba(0, 0, 0, 0.4)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    fontColor: 'rgb(255,255,255,0.8)'
                }
            }
        }
    });
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

                section01(result)
            }
        }
        xhr.open("Post", "./predict", true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	    xhr.send("predict=","1");

}, 1500);

setInterval(function() {

    waring_alaram_chart();
    caution_alaram_chart();
    green_alaram_chart();

}, 6000);


} catch(e) {
    console.log(" ");
}

