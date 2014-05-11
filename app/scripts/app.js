'use strict';

angular
  .module('instamozApp', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/mosaic', {
        templateUrl: 'views/mosaic/index.html',
        controller: 'MainCtrl'
      })
      .when('/mosaic/:mosaicId', {
        templateUrl: 'views/mosaic/show.html',
        controller: 'MosaicShowCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
