<template>
  <div class="chart mt-5">
    <div class="Loader" style="width: 12px; height: 12px" v-if="loading">
      <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
      <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
      <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
      <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
    </div>
    <highcharts class="hc" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
export default {
  name: 'Chart',
  props: ['pipe', 'title', 'keys'],
  data() {
    return {
      loading: false,
      chartOptions: {
        title: {
          align: 'left',
          text: this.title,
          margin: 20
        },
        xAxis: {
          type: 'datetime',
          labels: {
            format: '{value:%b-%e}'
          },
          title: {
            text: ''
          },
          gridLineWidth: 1
        },
        yAxis: {
          title: {
            text: ''
          },
          min: 0
        },
        series: [
          {
            name: '',
            data: [],
            color: '#1FCC83'
          }
        ],
        chart: {
          plotBackgroundColor: 'rgba(255,255,255,0)'
        },
        pane: {
          background: [{
            backgroundColor: 'red'
          }]
        },
        legend: {
          enabled: false
        }
      }
    };
  },
  methods: {
    fetchData () {
      this.loading = true
      this.tinyb.pipe(this.pipe).json().then(r => {
        if (!r.error) {
          this.chartOptions.series[0].data = r.data.map(item => 
            ([
              Date.UTC(item.x_date.split('-')[0], item.x_date.split('-')[1] - 1, item.x_date.split('-')[2]),
              item.b_payed
            ])
          );
          setTimeout(this.fetchData, 5000)
        } else {
          this.chartOptions.series[0].data = [];
        }

        this.loading = false
      })
    }
  },
  mounted() {
    this.tinyb = window.tinybird(process.env.VUE_APP_TOKEN || '')
    this.fetchData()
  }
};
</script>
<style>
.hc { margin-left: -10px }
.highcharts-title { fill: var(--tuna-color)!important }
.highcharts-credits { display: none }
.highcharts-background { fill: transparent }
.chart { position: relative }
.chart .Loader {
  position: absolute;
  top: 12px;
  left: -31px;
}
</style>
