(function() {
  'use strict';
  // Sidenav
  angular
    .module('app.layout')
    .directive('appSidenav', layoutSidenavDirective);

  /* @ngInject */
  function layoutSidenavDirective() {
    var directive = {
      bindToController: true,
      controller:       layoutSidenavController,
      controllerAs:     'vm',
      restrict:         'E',
      templateUrl:      'app/layout/sidenav/layoutSidenav.html'
    };
    return directive;
  }

  /* @ngInject */
  function layoutSidenavController($scope) {
    var vm = this;

    vm.openMenu = openMenu;
    vm.navLinks = navLinks;

    function openMenu($mdOpenMenu, $event) {
      $mdOpenMenu($event);
    }

    function navLinks() {
      return [
        {
          data: {
            route:     'pubmed.list',
            icon:      'home',
            label:     'Home',
            condition: function() {return true;}
          }
        },
        {
          data: {
            route:     'pubmed.list',
            icon:      'crop',
            label:     'Pubmed',
            condition: function() {return true;}
          }
        },
        {
          data: {
            route:     'users.list',
            icon:      'people',
            label:     'Users',
            condition: $scope.userCtrl.isAuthenticated
          }
        }
      ];
    }

  }

})();

