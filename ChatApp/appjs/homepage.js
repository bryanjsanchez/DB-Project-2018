angular.module('AppChat').controller('HPController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope,$location) {
        var thisCtrl = this;

        this.messageList = [];
       
        this.uid = "";//Will be replaced with correct uid.

        this.createChat= function (uid) {
            $location.url('/newchat');
        };

        this.addContact= function (uid) {
            $location.url('/addcontact');
        };

        this.joinChat= function (uid) {
            $location.url('/joinchat');
        };

        this.logOut = function(uid){
           $location.url('/login');  
        };

      
    }]);