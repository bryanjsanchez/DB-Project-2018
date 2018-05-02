(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'logingCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/message/:mid/likes',{
            templateUrl: 'pages/likes.html',
            controller: 'LikesController',
            controllerAs : 'likesCtrl'
        }).when('/message/:mid/dislikes',{
            templateUrl: 'pages/dislikes.html',
            controller: 'DislikesController',
            controllerAs : 'dislikesCtrl'
        }).otherwise({
            redirectTo: '/chat'
        });
    }]);

})();
