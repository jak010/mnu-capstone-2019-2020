var ctx = document.getElementById("myChart1")
var myChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        datasets: [{

                //  # 0 minute data
                label: "0 minute data",
                data: MinuteZero,
                borderColor: "#3e95cd",
                fill: false,

            }, {
                // 10 minute data
                data: MinuteOne,
                label: "10 minute data",
                borderColor: "#8e5ea2",
                fill: false
            }, {
                // 20 minute data
                data: MinuteTwo,
                label: "20 minute data",
                borderColor: "#3cba9f",
                fill: false
            }, {
                //  30 minute data
                data: MinuteThree,
                label: "30 minute data",
                borderColor: "#e8c3b9",
                fill: false
            }, {
                // 40 minute data
                data: MinuteFour,
                label: "40 minute data",
                borderColor: "#c45850",
                fill: false
            }, {
                // 50 minute data
                data: MinuteFive,
                label: "50 minute data",
                borderColor: "#cff201",
                fill: false
            }

        ]
    },
    options: {

        title: {
            display: true,
            text: 'Train Data Statical Graph'
        },

        xAxes: [{
            ticks: {
                fontColor: 'rgb(0, 0, 0, 1)',
                fontSize: 20
            },
        }],

        legend: {
            display: true,
            labels: {
                fontColor: 'rgb(0, 0, 0, 0.4)',
            }
        },

        yAxes: [{
            ticks: {
                min: 0,
                max: 100,
                stepSize: 10,
                fontSize: 14,
                fontColor: 'rgb(0, 0 0, 0.6)'
            },

        }],

        layout: {
            padding: {
                left: 10,
                right: 25,
                top: 10,
                bottom: 10
            }
        },
    }
});

