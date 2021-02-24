<template>
  <div class="chart mt-5">
    <highcharts class="hc" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
export default {
  name: 'Chart',
  props: ['pipe', 'title', 'keys'],
  data() {
    return {
      chartOptions: {
        title: {
          align: 'left',
          text: this.title,
          margin: 50
        },
        xAxis: {
          type: 'datetime',
          labels: {
            format: '{value:%b-%e}'
          },
          title: {
            text: ''
          }
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
    pollData () {
      this.polling = setInterval(() => {
        this.fetchData()
      }, 5000)
    },
    fetchData () {
      this.loading = true
      this.tinyb.pipe(this.pipe).json().then(r => {
        if (!r.error) {
          this.chartOptions.series[0].data = r.data.map(item => 
            ([
              Date.UTC(item.x_date.split('-')[0], item.x_date.split('-')[1], item.x_date.split('-')[2]),
              item.b_payed
            ])
          );
        } else {
          this.chartOptions.series[0].data = [];
        }

        this.loading = false
      })
    }
  },
  created() {
    this.pollData()
  },
  mounted() {
    this.tinyb = window.tinybird(process.env.VUE_APP_TOKEN || '')
    this.fetchData()
  },
  beforeDestroy () {
    clearInterval(this.polling)
  }
};
</script>
<style>
.hc { margin-left: -10px }
.highcharts-title { fill: var(--tuna-color)!important }
.highcharts-credits { display: none }
.highcharts-background { fill: transparent }
</style>
