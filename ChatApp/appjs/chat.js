angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope,$location) {
        var thisCtrl = this;

        this.messageList = [];
        this.counter;
        this.newText = "";
        this.chatName=""

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            $http.get('http://127.0.0.1:5000/ChatApp/chat/1/messages').then(function(response) {
                thisCtrl.messageList = response.data.Messages;
                thisCtrl.chatName = thisCtrl.messageList[0]['chatName'];

                var msg  = thisCtrl.messageList[0];
                thisCtrl.chatName = msg["chatname"];
                counter = thisCtrl.messageList.length;
            });
            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
           
            // Need to figure out who I am
            var author = "jocasio";
            var data = {};
            data.mtext = thisCtrl.newText
            data.uid = 1;
            data.cgid = 1;
            
            var nextId = thisCtrl.counter++;
            data.mrepliedmid = 0;
            data.mtimestamp = "2018-01-08 04:05:06";
            
            //thisCtrl.messageList.unshift({"uid": nextId, "mtext" : msg, "uid" : uid, "mtimestamp" : mtimestamp, "mrepliedmid" : mrepliedmid});
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
            alert("Created new message succesfully");
            
            
            
            thisCtrl.newText = "";    
            $location.url('/chat');        
        };

        this.messageLikeUsers= function (mid) {
            $location.url('/message/' + mid+ "/likes");
        };

        this.messageDislikeUsers= function (mid) {
            $location.url('/message/' + mid+ "/dislikes");
        };

        this.replyToMessage = function(mid){
            $location.url('/message/'+ mid+"/reply");

        };

        this.newChat= function (mid) {
            $location.url('/newchat');
        };

        this.addContact= function (mid) {
            $location.url('/addcontact');
        };

        this.joinChat= function (mid) {
            $location.url('/joinchat');
        };

        this.loadMessages();
    }]);