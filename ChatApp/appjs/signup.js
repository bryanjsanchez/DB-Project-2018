angular.module('AppChat').controller('SignUpController', ['$http', '$log', '$scope','$location','$window',
    function($http, $log, $scope,$location) {
        var thisCtrl = this;
      
     

        this.firstName = "";
        this.lastName = "";
        this.phone = "";
        this.email = "";
        this.username = "";
        this.password = "";

        this.usersList =[];

        this.loadUsers = function(){
            // Get the messages from the server through the rest api
            $http.get('http://127.0.0.1:5000/ChatApp/users').then(function(response) {
                thisCtrl.usersList = response.data.Users;            
            });
            $log.error("Users Loaded: ", JSON.stringify(thisCtrl.usersList));
        };

        this.signUp = function(){
            
        
            var data = {};
            data["firstname"] = thisCtrl.firstName;
            data["lastname"] = thisCtrl.lastName;
            data["phone"] = thisCtrl.phone;
            data["email"] = thisCtrl.email;
            data["username"] = thisCtrl.username;
            data["password"] = thisCtrl.password;     
            
        

            
            var reqURL = "http://localhost:5000/ChatApp/users";
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
                    alert("New  user added with id: " + response.data.User.uid);
                    thisCtrl.firstName = "";
                    thisCtrl.lastName = "";
                    thisCtrl.phone = "";
                    thisCtrl.email = "";
                    thisCtrl.username = "";
                    thisCtrl.password = "";
                    var url = "/login";
                    $location.url(url);
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
            
           
           
        };

       

        
        this.loadUsers();
    }]);