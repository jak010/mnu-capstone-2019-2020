var dataArray = new Array();
var xGroup = new Array();
var totalSet = [0, 0, 0];

// [0] 경고
// [1] 주의
// [2] 정상

function async_text(param_lanked_data ,time_data, flag) {

    var danger_log_dyn_html = "<li class='timeline-item'>"
    danger_log_dyn_html += "  <div class='timeline-badge danger'><i class='glyphicon glyphicon-check'></i></div>"
    danger_log_dyn_html += "   <div class='timeline-panel'>"
    danger_log_dyn_html += "       <div class='timeline-heading'>"
    danger_log_dyn_html += "           <h4 class='timeline-title'> "+time_data+" </h4>"
    danger_log_dyn_html += "       </div>"
    danger_log_dyn_html += "       <div class='timeline-body'>"
    danger_log_dyn_html += "           <p>"+param_lanked_data+"</p>"
    danger_log_dyn_html += "       </div>"
    danger_log_dyn_html += "   </div>"
    danger_log_dyn_html += "</li>"


    var warning_log_dyn_html = "<li class='timeline-item'>"
    warning_log_dyn_html += "  <div class='timeline-badge warning'><i class='glyphicon glyphicon-check'></i></div>"
    warning_log_dyn_html += "   <div class='timeline-panel'>"
    warning_log_dyn_html += "       <div class='timeline-heading'>"
    warning_log_dyn_html += "           <h4 class='timeline-title'> "+param_lanked_data+" </h4>"
    warning_log_dyn_html += "       </div>"
    warning_log_dyn_html += "       <div class='timeline-body'>"
    warning_log_dyn_html += "           <p> Caution </p>"
    warning_log_dyn_html += "       </div>"
    warning_log_dyn_html += "   </div>"
    warning_log_dyn_html += "</li>"

    var green_log_dyn_html = "<li class='timeline-item'>"
    green_log_dyn_html += "  <div class='timeline-badge primary'><i class='glyphicon glyphicon-check'></i></div>"
    green_log_dyn_html += "   <div class='timeline-panel'>"
    green_log_dyn_html += "       <div class='timeline-heading'>"
    green_log_dyn_html += "           <h4 class='timeline-title'> "+time_data+" </h4>"
    green_log_dyn_html += "       </div>"
    green_log_dyn_html += "       <div class='timeline-body'>"
    green_log_dyn_html += "           <p> Normal </p>"
    green_log_dyn_html += "       </div>"
    green_log_dyn_html += "   </div>"
    green_log_dyn_html += "</li>"


   var doc = document.getElementsByClassName("timeline timeline-horizontal");
   var doc_list = doc[0].getElementsByTagName("li");

   if( flag > 1.2) {
        doc[0].insertAdjacentHTML('beforeend',danger_log_dyn_html);
   } else if ((Number(flag) > 0.8) && (Number(flag) < 1.2)) {
        doc[0].insertAdjacentHTML('beforeend',warning_log_dyn_html);
    } else {
        doc[0].insertAdjacentHTML('beforeend',green_log_dyn_html);
    }

   if(doc_list.length > 15) {
        for( var i = doc_list.length-1; i >= 0; i--) {
//            doc_list[0].getElementsByTagName("li")[i].remove();
            doc_list[i].remove();
        }
   }

}

function section01(param1) {

    now_prec = Number(param1);

    if (dataArray.length % 10 == 0) {
        dataArray = new Array();
        xGroup = new Array();
    }

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

    // total Value
    var arraySum = totalSet[0] + totalSet[1] + totalSet[2];

    // 경고
    if(Number(param1) > 1.2){

        var obj = document.getElementById("green_log_text");
        obj.innerHTML = "SYSTEM " + "<br> NORMAL " + totalSet[2] + "<br>TOTAL " + arraySum;

        var obj = document.getElementById("warning_log_text");
        obj.innerHTML = "SYSTEM WARNING" + "<br>WARNING " + totalSet[0] + "<br>TOTAL " + arraySum;

        var obj = document.getElementById("caution_log_text");
        arrayCaution = ((totalSet[1] / arraySum) * 100);
        obj.innerHTML = "SYSTEM CAUTION" + "<br>WARNING " + totalSet[1] + "<br>TOTAL " + arraySum;

        totalSet[0] = totalSet[0] + 1;

        // data Top Lanked call
        var tempxhr = new XMLHttpRequest();

        tempxhr.onreadystatechange = function() {
        if(tempxhr.readyState == 4 && tempxhr.status ==200) {
            var lanked_data = tempxhr.responseText;
            console.log(lanked_data)
             async_text(lanked_data ,time_log, Number(param1));
            }
        }
        tempxhr.open("GET", "http://127.0.0.1:5000/dataLanked");
        tempxhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
	    tempxhr.send();

    // 주의
   } else if ((Number(param1) > 0.8) && (Number(param1) < 1.2)) {

        var obj = document.getElementById("green_log_text");
        obj.innerHTML = "SYSTEM " + "<br> NORMAL " + totalSet[2] + "<br>TOTAL " + arraySum;

        var obj = document.getElementById("warning_log_text");
        obj.innerHTML = "SYSTEM WARNING" + "<br>WARNING " + totalSet[0] + "<br>TOTAL " + arraySum;

        var obj = document.getElementById("caution_log_text");
        arrayCaution = ((totalSet[1] / arraySum) * 100);
        obj.innerHTML = "SYSTEM CAUTION" + "<br>WARNING " + totalSet[1] + "<br>TOTAL " + arraySum;

        totalSet[1] = totalSet[1] + 1;

        // data Top Lanked call
        var tempxhr = new XMLHttpRequest();

        tempxhr.onreadystatechange = function() {
        if(tempxhr.readyState == 4 && tempxhr.status ==200) {
            var lanked_data = tempxhr.responseText;
            console.log(lanked_data)
             async_text(lanked_data ,time_log, Number(param1));
            }
        }
        tempxhr.open("GET", "http://127.0.0.1:5000/dataLanked");
        tempxhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
	    tempxhr.send();

   // 정상
   } else {

        var obj = document.getElementById("green_log_text");
        obj.innerHTML = "SYSTEM " + "<br> NORMAL " + totalSet[2] + "<br>TOTAL " + arraySum;

        var obj = document.getElementById("warning_log_text");
        obj.innerHTML = "SYSTEM WARNING" + "<br>WARNING " + totalSet[0] + "<br>TOTAL " + arraySum;

        var obj = document.getElementById("caution_log_text");
        arrayCaution = ((totalSet[1] / arraySum) * 100);
        obj.innerHTML = "SYSTEM CAUTION" + "<br>WARNING " + totalSet[1] + "<br>TOTAL " + arraySum;

        async_text("Stability" ,time_log, Number(param1));
        totalSet[2] = totalSet[2] + 1;
   }

    dataArray.push(now_prec);
    xGroup.push(cur_x);

    if (xGroup.length % 20 == 0) {
        xGroup.length = 0;
    }

    var myChart1 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xGroup,
            datasets: [{
                label: "실시간 예측",
                data: dataArray,

                backgroundColor: 'rgb(0, 0, 0, 0.4)',

                fill: false,

                borderColor: [
                      'rgb(135, 206, 236)',
                ],
                borderWidth: 2,
                lineTension: 0.2,
            }]
        },
        options: {
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 20,
                    right: 100,
                    top: 10,
                    bottom: 70
                }
            },

            legend: {
                display: true,
                labels: {
                    fontColor: 'rgb(0, 0, 0, 0.4)',
                }
            },

            scales: {

                xAxes: [{
                    ticks: {
                        fontColor: 'rgb(0, 0, 0, 1)',
                        fontSize: 14
                    },
                    gridLines: {
                        display: false,
                        color: "rgb(0, 0, 0, 0.4)",
                        lineWidth: 0,
                    }
                }],

                yAxes: [{
                    ticks: {
                        min: -0.5,
                        max: 3,
                        stepSize: 0.5,
                        fontSize: 12,
                        fontColor: 'rgb(0, 0 0, 0.6)'
                    },
                    gridLines: {
                        color: 'rgb(0, 0, 0, 0.3)',
                        lineWidth: 0.5,
                        display : false,
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
    myChart1.update();

}

function doughnut_chart() {
    var ctx = document.getElementById("myChart2").getContext('2d');
    ctx.canvas.width = 400;
    ctx.canvas.height = 350;
    var myChart2 = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["경고", "주의","정상"],
            datasets: [{
                label: '# of Votes',
                data: totalSet,
                backgroundColor: [
                   'rgb(219, 15, 38,0.5)',
                    'rgb(255, 255, 0,0.5)',
                    'rgb(0, 216, 255,0.5)'

                ],
                borderColor: [
                    'rgba(0, 0, 0, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            legend: {
                labels: {
                    // This more specific font property overrides the global property
                    fontColor: 'rgb(0,0,0,0.8)'
                }

            },




            cutoutPercentage: 80,
        }
    });
    myChart2.update();
}

function printTime() {
    var clock = document.getElementById("clock"); // 출력할 장소 선택
    var now = new Date(); // 현재시간
    var nowTime = now.getFullYear() + "년&nbsp;" + (now.getMonth() + 1) + "월&nbsp;" + now.getDate() + "일&nbsp;" + now.getHours() + "시&nbsp;" + now.getMinutes() + "분&nbsp;" + now.getSeconds() + "초";

    clock.innerHTML = nowTime; // 현재시간을 출력
    setTimeout("printTime()", 1000); // setTimeout(“실행할함수”,시간) 시간은1초의 경우 1000
}

window.onload = function() { // 페이지가 로딩되면 실행
    printTime();
}

function startPredict() {
    test();
    timerId = setInterval(test, 2000);
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
                section01(result);

                doughnut_chart();
            }
        }
        xhr.open("GET", "http://127.0.0.1:5000/predict?request=1");
        xhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
	    xhr.send();


}, 1900);

} catch(e) {
    console.log(" ");
}


