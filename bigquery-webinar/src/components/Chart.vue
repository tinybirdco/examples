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
          text: this.title,
          margin: 50
        },
        xAxis: {
          type: 'datetime',
          labels: {
            format: '{value:%b-%e}'
          },
          title: {
            text: 'Date'
          }
        },
        yAxis: {
          title: {
            text: 'Payed'
          },
          min: 0
        },
        series: [
          {
            data: []
          }
        ],
        chart: {
          plotBackgroundColor: 'rgba(255,255,255,0)'
        },
        pane: {
          background: [{
            backgroundColor: 'red'
          }]
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
.highcharts-credits { display: none }
</style>
