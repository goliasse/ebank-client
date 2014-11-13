(function(window, undefined) {
    'use strict';

    angular.module('ebank-client', [
        'ngAnimate',
        'ngCookies',
        'ui.bootstrap',
        'ui.router',
        'aa.formExtensions',
        'toaster',
        'directives',
        'filters',
    ]).config(['$interpolateProvider', '$httpProvider',
        function($interpolateProvider, $httpProvider) {
            $httpProvider.interceptors.push('unauthenticatedInterceptor');
    }]).run(['$rootScope', '$http', '$window', '$state', '$stateParams', 'customEvents', 'localizationService', 'userInfoService',
        function($rootScope, $http, $window, $state, $stateParams, customEvents, localizationService, userInfoService) {
            $rootScope.localizationService = localizationService;

            $rootScope.$on(customEvents.general.sessionExpired, function() {
                $state.go('login');
            });

            $rootScope.$on(customEvents.general.logIn, function() {
                $state.go('main.authenticated.currency');
            });

            $rootScope.$on(customEvents.general.notAnonymousUser, function() {
                $state.go('main.authenticated.currency');
            });

            $rootScope.$on('$stateChangeSuccess', function() {
                $rootScope.$emit(customEvents.leftMenu.closeLeftMenu);
            });

            $rootScope.$on(customEvents.general.logOut, function() {
                if (!$state.current.abstract) {
                    $state.transitionTo($state.current, $stateParams, {
                        reload: true,
                        inherit: true,
                        notify: true
                    });
                }
            });
        }]);
 })(window);