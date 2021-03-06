(function(window, undefined) {
    'use strict';

    angular.module('ebank-client')
        .factory('unauthenticatedInterceptor', ['$q', '$rootScope', 'customEvents',
            function ($q, $rootScope, customEvents) {
                return {
                    /* Handle session timeout and not authenticated errors */
                    responseError: function(rejection) {
                        if (rejection != null && rejection.status === 401) {
                            $rootScope.$emit(customEvents.general.userNotAuthenticated);
                        }

                        return $q.reject(rejection);
                    }
                };
            }]);
})(window);