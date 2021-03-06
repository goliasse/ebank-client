angular.module('services')
    .factory('paymentsService', ['paymentsProvider',
        function(paymentsProvider) {
            'use strict';

            var self = {
                getEripTree: function() {
                    return paymentsProvider.getEripTree();
                },
                getEripPayments: function() {
                    return paymentsProvider.getEripPayments();
                },
                getEripPaymentById: function(id) {
                    return paymentsProvider.getEripPaymentById(id);
                },
                payEripPayment: function(paymentData) {
                    return paymentsProvider.payEripPayment(paymentData);
                },
                payGenericPayment: function(paymentData) {
                    return paymentsProvider.payGenericPayment(paymentData);
                }
            };

            return self;
        }]);