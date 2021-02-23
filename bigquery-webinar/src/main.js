import Vue from "vue";
import App from "./App.vue";
import numeral from "numeral";

Vue.config.productionTip = false;

Vue.filter("formatNumber", function (value) {
  return numeral(value).format("0,0");
});

new Vue({
  render: (h) => h(App),
}).$mount("#app");
