odoo.define('pos_Coupons.pos_models',function (require) {
"use strict";

    var models = require('point_of_sale.models');
    var orderline_super = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        get_full_product_name: function () {
            if(this.product.product_popup){
                var full_name = ' +'+this.product.display_name;
                return full_name;
            }
            else{
                return orderline_super.get_full_product_name.apply(this);
            }
        }
    });
});