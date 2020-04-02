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

    var cur_x = Hours + "시"+ Minutes +"분" + Seconds+"초";
    var cur_x2 = Hours + ":"+ Minutes +":" + Seconds;


    if(Number(param1) > 0.7){
        pieChartSet[0] += 1;
        var append_log = document.getElementById("warning_data_view")
        var append_string =  cur_x + "<br>";
        append_log.insertAdjacentHTML("beforeend" ,append_string);
   } else if( Number(param1) > 0.5  || Number(param1) < 0) {
        pieChartSet[1] += 1;
        var append_log = document.getElementById("caution_data_view")
        var append_string =  cur_x + "<br>";
        append_log.insertAdjacentHTML("beforeend" ,append_string);
   } else {
    pieChartSet[2] += 1;
   }

    dataArray.push(now_prec);
    xGroup.push(cur_x2);

    if (xGroup.length % 80 == 0) {
        xGroup.length = 0;
    }


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
                        min: -2,
                        max:2,
                        stepSize: 0.5,
                        fontSize: 12,
                    },
                    gridLines: {
                        color: 'rgb(166, 201, 226)',
                        lineWidth: 3
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

                            if (data >= 0.5) {

                                data = "경고";

                            } else if ((data >0.4) || (data < 0)) {
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


function section2() {
    var ctx = document.getElementById("myChart2").getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["경고", "정상", "주의"],
            datasets: [{
                label: '# of Votes',
                data: pieChartSet,
                backgroundColor: [
                    'rgb(219, 15, 38,0.5)',
                    'rgb(68, 219, 111,0.5)',
                    'rgb(255, 255, 0,0.5)'
                ],
                borderColor: [
                    'rgba(0, 0, 0, 0.5)'
                ],
                borderWidth: 1
            }]
        },
        options: {

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

                section01(result)
            }
        }
        xhr.open("Post", "./predict", true);
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	    xhr.send("predict=","1");

}, 1500);

setInterval(function() {
    section2();
}, 6000);