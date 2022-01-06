//console.log('Point of Sale JavaScript loaded');
odoo.define('pos_demo.custom',function (require) {
"use strict";

var screens = require('point_of_sale.models');
var rpc = require('web.rpc');
const Registries = require('point_of_sale.Registries');
//Modifying the POS screen UI
var pos_model = require('point_of_sale.models');
pos_model.load_fields("product.product",["qty_available","show_qty_on_hand","show_neg","can_still_sold_neg"]); //load standard_price field in js
//making business logic
const ProductScreen = require('point_of_sale.ProductScreen');

const UpdatedProductScreen = ProductScreen =>
    class extends ProductScreen {
        _clickProduct(event) {

            const qty_product = event.detail
            if (qty_product.qty_available >0){
                super._clickProduct(event);
            }
            else if (qty_product.qty_available < 1){
                if (qty_product.can_still_sold_neg){
                    super._clickProduct(event);
                }
                else{
                        this.showPopup('ErrorPopup', { title:
                                    'Warning', body: 'Product is not available.' });
                    }
            }

        }
    };
    Registries.Component.extend(ProductScreen,UpdatedProductScreen);




});