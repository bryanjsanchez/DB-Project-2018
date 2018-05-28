
google.charts.load('current', {'packages': ['corechart']});


google.charts.setOnLoadCallback(drawHashChart);

google.charts.setOnLoadCallback(drawMessageDayChart);

google.charts.setOnLoadCallback(drawRepliesDayChart);

google.charts.setOnLoadCallback(drawLikesDayChart);

google.charts.setOnLoadCallback(drawDislikesDayChart);

google.charts.setOnLoadCallback(drawActiveUsersChart);

function reformatData(jsonData){ //Need to Redo this one per DrawChart
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

function reformatHashData(jsonData){ //Need to Redo this one per DrawChart
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



function drawHashChart() {
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
    data.addRows(reformatHashData(JSON.parse(jsonData)));

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

function reformatMessageData(jsonData){ //Need to Redo this one per DrawChart
    var temp= jsonData.Messages_Per_Day;
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
         //console.log(row.hid);
        dataElement.push(row.Day );
        dataElement.push(row.Count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawMessageDayChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/ChatApp/dash/MessagesPerDay",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Day');
    data.addColumn('number', 'Total');
    data.addRows(reformatMessageData(JSON.parse(jsonData)));

    var options = {
        title: 'Total Messages Per Day',
        chartArea: { width: '50%', height: '50%'},

        hAxis: {
            title: 'Total ',
            minValue: 0,


        },
        vAxis: {
            title: 'Day',
            gridlines: {count: -1},
            textPosition : 'none'
            //textstyle: {color: 'black',fontSize: 8},
             //ticks: [5,10,15,20]
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart2_div'));

    chart.draw(data, options);

}

function reformatRepliesData(jsonData){ //Need to Redo this one per DrawChart
    var temp= jsonData.Replies_Per_Day;
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
         //console.log(row.hid);
        dataElement.push(row.Day );
        dataElement.push(row.Count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawRepliesDayChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/ChatApp/dash/RepliesPerDay",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Day');
    data.addColumn('number', 'Total');
    data.addRows(reformatRepliesData(JSON.parse(jsonData)));

    var options = {
        title: 'Total Replies Per Day',
        chartArea: { width: '50%', height: '50%'},

        hAxis: {
            title: 'Total ',
            minValue: 0,


        },
        vAxis: {
            title: 'Day',
            gridlines: {count: -1},
            textPosition : 'none'
            //textstyle: {color: 'black',fontSize: 8},
             //ticks: [5,10,15,20]
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart3_div'));

    chart.draw(data, options);

}


function reformatLikesData(jsonData){ //Need to Redo this one per DrawChart
    var temp= jsonData.Likes_Per_Day;
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
         console.log(row.hid);
        dataElement.push(row.Day );
        dataElement.push(row.Count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


function drawLikesDayChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/ChatApp/dash/LikesPerDay",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Day');
    data.addColumn('number', 'Total');
    data.addRows(reformatLikesData(JSON.parse(jsonData)));

    var options = {
        title: 'Total Likes Per Day',
        chartArea: { width: '50%', height: '50%'},

        hAxis: {
            title: 'Total ',
            minValue: 0,


        },
        vAxis: {
            title: 'Day',
            gridlines: {count: -1},
            textPosition : 'none'
            //textstyle: {color: 'black',fontSize: 8},
             //ticks: [5,10,15,20]
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart4_div'));

    chart.draw(data, options);

}


function reformatDislikesData(jsonData){ //Need to Redo this one per DrawChart
    var temp= jsonData.Dislikes_Per_Day;
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
         console.log(row.hid);
        dataElement.push(row.Day );
        dataElement.push(row.Count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


function drawDislikesDayChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/ChatApp/dash/DislikesPerDay",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Day');
    data.addColumn('number', 'Total');
    data.addRows(reformatDislikesData(JSON.parse(jsonData)));

    var options = {
        title: 'Total Dislikes Per Day',
        chartArea: { width: '50%', height: '50%'},

        hAxis: {
            title: 'Total ',
            minValue: 0,


        },
        vAxis: {
            title: 'Day',
            gridlines: {count: -1},
            textPosition : 'none'
            //textstyle: {color: 'black',fontSize: 8},
             //ticks: [5,10,15,20]
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart5_div'));

    chart.draw(data, options);

}

function reformatActiveUsersData(jsonData){ //Need to Redo this one per DrawChart
    var temp= jsonData.Top_Users;
    console.log("temp: " + JSON.stringify(temp));

    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
         console.log(row.hid);
        dataElement.push(row.uusername + " : "+ row.day );
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawActiveUsersChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/ChatApp/dash/TopUsers",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date and Name');
    data.addColumn('number', 'Total Messages');
    data.addRows(reformatActiveUsersData(JSON.parse(jsonData)));

    var options = {
        title: 'Top Users for last 10 days',
        chartArea: { width: '50%', height: '50%'},

        hAxis: {
            title: 'Total ',
            minValue: 0,


        },
        vAxis: {
            title: 'Day and User',
            gridlines: {count: -1},
            textPosition : 'none'
            //textstyle: {color: 'black',fontSize: 8},
             //ticks: [5,10,15,20]
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart6_div'));

    chart.draw(data, options);

}


//google.charts.load('current', {packages: ['corechart', 'bar']});
//google.charts.setOnLoadCallback(drawChart);


