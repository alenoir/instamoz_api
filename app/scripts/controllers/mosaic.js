'use strict';

angular.module('instamozApp')
  .controller('MosaicCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  })
  .controller('MosaicShowCtrl', function ($scope, $http) {
    $http.get('http://instamoz.alenoir.com/mosaics/13/').success(function(data) {
      $scope.mosaic = data;
    });
  });
