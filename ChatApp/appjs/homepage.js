angular.module('AppChat').controller('HPController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope,$location) {
        var thisCtrl = this;

        this.chatList = [];
       
        this.uid = "";


        this.loadChats = function(){
            var reqURL ="http://localhost:5000/ChatApp/chat/loggeduser";
          
            $http.get(reqURL).then(function(response) {
                thisCtrl.chatList  = response.data.ChatGroups;
                console.log(response);
            })

            $log.error("ChatGroups Loaded: ", JSON.stringify(thisCtrl.chatList));
            
        };

        this.goToChat = function(cgid){
            $location.url('/chat/'+cgid);
        }

        this.createChat= function () {
            $location.url('/newchat');
        };

        this.addContact= function () {
            $location.url('/addcontact');
        };

        this.joinChat= function () {
            $location.url('/joinchat');
        };

        this.logOut = function(){
           $location.url('/login');  
        };
        
        this.loadChats();

      
    }]);