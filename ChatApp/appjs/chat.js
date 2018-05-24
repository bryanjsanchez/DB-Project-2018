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
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "text" : msg, "username" : author, "likes" : 0, "dislikes" : 0});
            thisCtrl.newText = "";            
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