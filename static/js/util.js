var dataArray = new Array();
var xGroup = new Array();

function section01(param1) {
    now_prec = Number(param1);

    var ctx = document.getElementById("myChart");

    var dateobj = new Date();
    Hours = dateobj.getHours();
    Minutes = dateobj.getMinutes();
    Seconds = dateobj.getSeconds();

    var cur_x = Hours + "시"+ Minutes +"분" + Seconds+"초";
    var cur_x2 = Hours + ":"+ Minutes +":" + Seconds;


    if( Number(param1) > 1 ||  Number(param1) < -1) {
        var append_log = document.getElementById("article_section_01_3_dataView")
        var append_string =  cur_x + "<br>";
        append_log.insertAdjacentHTML("beforeend" ,append_string);
   } else if( Number(param1) > 0.5  || Number(param1) > -0.5){
        var append_log = document.getElementById("article_section_01_2_dataView")
        var append_string =  cur_x + "<br>";
        append_log.insertAdjacentHTML("beforeend" ,append_string);
   }

    dataArray.push(now_prec);
    xGroup.push(cur_x2);

    if (xGroup.length % 25 == 0) {
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


}, 200);