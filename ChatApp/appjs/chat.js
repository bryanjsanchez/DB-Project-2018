angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope','$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;

        this.messageList = [];
       
        this.newText = "";
        this.chatName="";
        this.cgid = "";
        this.uid = "";

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            this.cgid = $routeParams.cgid
            $http.get('http://127.0.0.1:5000/ChatApp/chat/' + this.cgid + '/messages').then(function(response) {
                if (!('Error' in response.data)) {
                    thisCtrl.messageList = response.data.Messages;
                }

            });
            $http.get('http://127.0.0.1:5000/ChatApp/chat/' + this.cgid).then(function(response) {
                thisCtrl.chatName = response.data.Chat[0].cgname;
                console.log(response);
            });

            $http.get("http://127.0.0.1:5000/ChatApp/user").then(function(response){
                thisCtrl.uid = response.data.User.uid;
            });
            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var cgid =thisCtrl.cgid;
            var uid =thisCtrl.uid;
            var data = {};
            data.mtext = thisCtrl.newText

            //These two need will be given after login
            data.uid = uid;
            data.cgid = cgid;
            
         
            data.mrepliedmid = 0;
         

            var date = new Date();
            var d = date.getFullYear().toString() + "-" + date.getMonth().toString()+ "-" + date.getDate().toString()+" " +date.getHours().toString()+":"+date.getMinutes().toString()+":"+date.getSeconds().toString();
            data.mtimestamp = d;

            
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
                    location.reload();
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
            
           
            $location.url('/chat/'+cgid);        
        };

        this.likeMessage = function(mid){
            var uid =thisCtrl.uid;
            var cgid = thisCtrl.cgid;
            var data = {};
            data["uid"] = uid;
            data["mid"] = mid;
            var date = new Date();
            var d = date.getFullYear().toString() + "-" + date.getMonth().toString()+ "-" + date.getDate().toString()+" " +date.getHours().toString()+":"+date.getMinutes().toString()+":"+date.getSeconds().toString();
            data["mrtimestamp"] = d;


            var reqURL = "http://localhost:5000/ChatApp/messages/"+mid+"/likes";
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
                    alert("Liked message added with id: " + response.data.Like.mrlike);
                    $location.url('/chat/'+thisCtrl.cgid);
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
            
            $location.url('/chat/'+thisCtrl.cgid);
            
        };

        this.dislikeMessage = function(mid){
            var uid =thisCtrl.uid;
            var cgid =thisCtrl.cgid;
            var data = {};
            data["uid"] = uid;
            data["mid"] = mid;

            var date = new Date();
            var d = date.getFullYear().toString() + "-" + date.getMonth().toString()+ "-" + date.getDate().toString()+" " +date.getHours().toString()+":"+date.getMinutes().toString()+":"+date.getSeconds().toString();
            data["mrtimestamp"] = d;   

            var reqURL = "http://localhost:5000/ChatApp/messages/"+mid+"/dislikes";
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
                    alert("Disliked message successfully: " + response.data.Dislike.mrlike);
                    $location.url('/chat/'+thisCtrl.cgid);
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
            
            $location.url('/chat/'+thisCtrl.cgid);            
        };

        this.messageLikeUsers= function (mid) {
            $location.url('/message/' + mid + "/likes");
        };

        this.messageDislikeUsers= function (mid) {
            $location.url('/message/' + mid + "/dislikes");
        };

        this.replyToMessage = function(mid){
            $location.url('/message/'+ mid +"/reply");

        };

        this.newChat= function () {
            $location.url('/newchat');
        };

        this.addContact= function () {
            $location.url('/addcontact');
        };

        this.joinChat= function () {
            $location.url('/joinchat');
        };

        this.loadMessages();
    }]);