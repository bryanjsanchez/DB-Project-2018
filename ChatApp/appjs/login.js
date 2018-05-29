angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope','$location',
    function($http, $log, $scope,$location) {
        var thisCtrl = this;
      
     

        this.username ="";
        this.password ="";

       

        
        this.login = function(){
            
            var username = thisCtrl.username;
            var password = thisCtrl.password; 
        
            var data = {};
            data["username"] = username;
            data["password"] = password;       

            
            var reqURL = "http://localhost:5000/ChatApp/login";
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
                                   
                    thisCtrl.username = "";
                    thisCtrl.password = "";

                    $location.url('/homepage')
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
                        $location.url('/login')
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                        $location.url('/login')
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                        $location.url('/login')
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                        $location.url('/login')
                    }
                    else {
                        alert("Error interno del sistema.");
                    }

                }
            );            
            
           
                
        };


        this.signUp = function(){
            $location.url('/signup');
        };      

        
       
    }]);