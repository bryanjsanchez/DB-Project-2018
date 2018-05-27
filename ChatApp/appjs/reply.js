angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;

        // This variable hold the information on the part
        // as read from the REST API
        var orgMessage = "";
        var replyMessage = "";
        var messageData ="";

        var uid = "";
        var cgid ="";

        this.loadMessage = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var mid = $routeParams.mid;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/ChatApp/messages/" + mid;
            console.log("reqURL: " + reqURL);
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    var msg = response.data.Message;
                    thisCtrl.messageData = msg;
                    thisCtrl.orgMessage = msg["mtext"];
                    thisCtrl.cgid = msg["cgid"]
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    //console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );

            $http.get("http://127.0.0.1:5000/ChatApp/user").then(function(response){
                thisCtrl.uid = response.data.User.uid;
            });
        };

        this.postReply = function(){
            var oldMsg = thisCtrl.orgMessage;
            var msg = thisCtrl.replyMessage;
            // Need to figure out who I am

            var data = {};

            var uid = thisCtrl.uid;
            var cgid = thisCtrl.cgid;
            
            data.uid = uid;
            data.cgid = cgid;
           
            var date = new Date();
            var d = date.getFullYear().toString() + "-" + date.getMonth().toString()+ "-" + date.getDate().toString()+" " +date.getHours().toString()+":"+date.getMinutes().toString()+":"+date.getSeconds().toString();
            data.mtimestamp = d;
            
          
            data.mrepliedmid = thisCtrl.messageData["mid"];            
            
            data.mtext = "RE:"+"\""+oldMsg+"\""+msg;

            var reqURL = "http://localhost:5000/ChatApp/messages";
            console.log("reqURL: " + reqURL);

            // configuration headers for HTTP request
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                    //'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'

                }

            }
            $http.post(reqURL, data, config).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // tira un mensaje en un alert
                    alert("New reply message added with id: " + response.data.Message.mid);
                    $location.url('/chat');
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    //console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
            alert("Created reply message succesfully");
            
          
                     
        };

        this.loadMessage();
}]);