odoo.define('point_of_sale.PrintReceipt', function (require) {
    'use strict';

    const OrderReceipt = require('point_of_sale.OrderReceipt');
    const Registries = require('point_of_sale.Registries');

    class PrintReceipt extends OrderReceipt {
        constructor() {
            super(...arguments);
        }
    }

    PrintReceipt.template = 'PrintReceipt';

    Registries.Component.add(PrintReceipt);

    return PrintReceipt;
});
