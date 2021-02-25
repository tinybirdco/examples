import Vue from "vue";
import App from "./App.vue";
import numeral from "numeral";
import HighchartsVue from "highcharts-vue";
import VueNumber from "vue-number-animation";

Vue.config.productionTip = false;

Vue.filter("formatNumber", function(value) {
  return numeral(value).format("0,0");
});

Vue.use(HighchartsVue);
Vue.use(VueNumber);

new Vue({
  render: (h) => h(App),
}).$mount("#app");
