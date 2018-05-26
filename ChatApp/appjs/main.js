(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'logingCtrl'
        }).when('/signup', {
            templateUrl: 'pages/signup.html',
            controller: 'SignUpController',
            controllerAs : 'signupCtrl'
        }).when('/homepage', {
            templateUrl: 'pages/homepage.html',
            controller: 'HPController',
            controllerAs : 'hpCtrl'
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
        }).when('/message/:mid/reply',{
            templateUrl: 'pages/reply.html',
            controller: 'ReplyController',
            controllerAs : 'replyCtrl'
        }).when('/newchat',{
            templateUrl: 'pages/newchat.html',
            controller: 'NewChatController',
            controllerAs : 'newChatCtrl'
        }).when('/addcontact',{
            templateUrl: 'pages/addcontact.html',
            controller: 'AddContactController',
            controllerAs : 'addContactCtrl'
        }).when('/joinchat',{
            templateUrl: 'pages/joinchat.html',
            controller: 'JoinChatController',
            controllerAs : 'joinChatCtrl'
        }).otherwise({
            redirectTo: '/homepage'
        });
    }]);

})();
