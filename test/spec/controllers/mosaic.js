'use strict';

describe('Controller: MosaicCtrl', function () {

  // load the controller's module
  beforeEach(module('instamozApp'));

  var MosaicCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    MosaicCtrl = $controller('MosaicCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
