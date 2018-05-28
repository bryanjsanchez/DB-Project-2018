
google.charts.load('current', {'packages': ['corechart']});


google.charts.setOnLoadCallback(drawChart);

function reformatData(jsonData){
    var temp= jsonData.Trending_Hashtag;
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
         console.log(row.hid);
        dataElement.push(row.hid );
        dataElement.push(row.hits);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/ChatApp/dash/Trending",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Hash');
    data.addColumn('number', 'Hits');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Trending HashTags',
        chartArea: { width: '50%', height: '50%'},

        hAxis: {
            title: 'Total ',
            minValue: 0,


        },
        vAxis: {
            title: 'Hash',
            gridlines: {count: -1},
            textPosition : 'none'
            //textstyle: {color: 'black',fontSize: 8},
             //ticks: [5,10,15,20]
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

    chart.draw(data, options);

}


//google.charts.load('current', {packages: ['corechart', 'bar']});
//google.charts.setOnLoadCallback(drawChart);


