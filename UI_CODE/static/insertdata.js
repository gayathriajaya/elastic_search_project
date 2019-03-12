var app = angular.module('app', ['ngTouch']);
 
app.controller('insertdata', ['$scope', 'factory', '$http', function ($scope, factory, $http) {
    
    $scope.submit = function() {


        api = 'pushdata/'
        
        data = {
            path: $scope.path,
            index: $scope.index,
            
            }

        factory.getData(api,data);        
        //$scope.clear();   
    };

     $scope.clear = function() {
        $scope.path = '';
        $scope.index = '';
    };

}]);

app.factory('factory', ['$http','$q', function($http, $q) {
    var factory = {}
    factory.getData = function(api,param) {
        var d = $q.defer();

        console.log(api)

        $http({
            method:'GET',
            url: api,
            params : param           
        }).success(function(result) {
            d.resolve(result)
            alert("Success");
        }).error(function(result) {
            console.log("Error Occurred:")
            d.resolve(result)
            alert("Failure");
        });
        return d.promise;
    };

    
    return factory;
}]);