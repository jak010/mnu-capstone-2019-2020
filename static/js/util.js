var dataArray = new Array();
var xGroup = new Array();
var totalSet = [0, 0, 0];

// [0] 경고
// [1] 주의
// [2] 정상

function section01(param1) {

    now_prec = Number(param1);

    var ctx = document.getElementById("myChart");

    // 일시 데이터 정의
    var dateobj = new Date();

    Current_Year = dateobj.getFullYear();
    Current_month_ = dateobj.getMonth() + 1 + "월";
    Current_Date = dateobj.getDate() + "일";
    Current_Hour = dateobj.getHours() + "시";
    Current_Minutes = dateobj.getMinutes() + "분";
    Current_Seconds = dateobj.getSeconds() + "초";

    // 현재 시간
    var cur_x = Current_Hour + " " + Current_Minutes + " " + Current_Seconds;
    var time_log = Current_month_ + " " + Current_Date + " " + Current_Hour + " " + Current_Minutes + " " + Current_Seconds + " ";

    // 경고
    if(Number(param1) > 1.2){
        totalSet[0] += 1;
          var obj = document.getElementById("warningLog");
        obj.getElementsByClassName("Logtext")[0].innerText = totalSet[0];
        var text_obj = document.getElementById("w_time_log_text");
        text_obj.innerHTML += time_log + "<hr>";
        text_obj.scrollTop = text_obj.scrollHeight;

    // 주의
   } else if( Number(param1) > 0.8) {
        totalSet[1] += 1;
        var obj = document.getElementById("CautionLog");
        obj.getElementsByClassName("Logtext")[0].innerText = totalSet[1];

        var text_obj = document.getElementById("c_time_log_text");
        text_obj.innerHTML += time_log + "<hr>";
        text_obj.scrollTop = text_obj.scrollHeight;

   // 정상
   } else {
    totalSet[2] += 1;
     var obj = document.getElementById("NoticeLog");
      obj.getElementsByClassName("Logtext")[0].innerText = totalSet[2];
        var text_obj = document.getElementById("g_time_log_text");
        text_obj.innerHTML += time_log + "<hr>";
        text_obj.scrollTop = text_obj.scrollHeight;
   }

    dataArray.push(now_prec);
    xGroup.push(cur_x);

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
                        min: -0.5,
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

                            if (data > 1.2) {

                                data = "경고";

                            } else if (data >0.8) {
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
        xhr.open("GET", "http://127.0.0.1:5000/predict?request=1");
        xhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
	    xhr.send();

}, 1500);

} catch(e) {
    console.log(" ");
}

