var pgSearchApp = angular.module('pgSearch', []);

pgSearchApp.factory('SearchService', function($http) {
    return {
        search: function(search_term, version, callback) {
            $http(
            {
                url : '/search/',
                params: {term: search_term, v: version},
                method : "GET"
            }).success(function(data)
            {
                callback(data);
            }).error(function(data, status)
            {
                console.log(data);
            });
        }
    }
    
});

pgSearchApp.directive('ngEnter', function() {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$eval(attrs.ngEnter);
                event.preventDefault();
            }
        });
    };
});

/**
 * Search controller that submits the search term and updates the search results
 */
pgSearchApp.controller('SearchController', function($scope, SearchService) {
    $scope.search_mgr = {
            term: '',
            results: [],
            status: 'Ready',
            search: function(version) {
                $scope.search_mgr.results = [];
                $scope.search_mgr.status = 'Waiting';
                SearchService.search(this.term, version, function(data) {
                    $scope.search_mgr.status = 'Got results. Rendering';
                    $scope.search_mgr.results = data.results;
                    $scope.search_mgr.status = 'Done';
                })
            },
            init: function() {
                
            }
    }
})