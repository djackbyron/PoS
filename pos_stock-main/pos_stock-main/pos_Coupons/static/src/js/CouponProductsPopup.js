odoo.define('pos_Coupons.CouponProductsPopup', function(require) {
   'use strict';
   const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
   const Registries = require('point_of_sale.Registries');
   const PosComponent = require('point_of_sale.PosComponent');
   const ControlButtonsMixin = require('point_of_sale.ControlButtonsMixin');
   const NumberBuffer = require('point_of_sale.NumberBuffer');
   const { useListener } = require('web.custom_hooks');
   var pos_model = require('point_of_sale.models');
   pos_model.load_fields("product.product",["product_popup"]); //load standard_price field in js
   const { onChangeOrder, useBarcodeReader } = require('point_of_sale.custom_hooks');
   const { useState } = owl.hooks;
   class CouponProductsPopup extends AbstractAwaitablePopup {
    constructor() {
    super(...arguments);
    useListener('click-product', this._clickProduct);
    }
    get selectedCouponId() {
        if (this.env.pos.config.category_id[0]){
            return this.env.pos.config.category_id[0]
        }
        else{
            return 0
        }

    }
   //To get coupon products category
    get productsToDisplay() {
        const prod_array = [];
        var products = this.env.pos.db.get_product_by_category(this.selectedCouponId);
        for (let i=0;i<products.length;i++){
            if (products[i].product_popup){
                prod_array.push(products[i])
            }
        }
        return prod_array
    }
     get currentOrder() {
           return this.env.pos.get_order();
       }
//      get products details in orderlines when clicking on popup product
     async _clickProduct(event) {
           if (!this.currentOrder) {
               this.env.pos.add_new_order();
           }
           console.log("bbb")
           const product = event.detail;
           let price_extra = 0.0;
           let description, packLotLinesToEdit;
           // Add the product after having the extra information.
           this.currentOrder.add_product(product, {
               description: description,
           });
       }
    }

    //Create products popup
   CouponProductsPopup.template = 'CouponProductsPopup';
   CouponProductsPopup.defaultProps = {
       confirmText: 'Close',
       cancelText: 'Cancel',
       title: 'Do you want to add these Products',
       body: '',
   };
   Registries.Component.add(CouponProductsPopup);
   return CouponProductsPopup;
});