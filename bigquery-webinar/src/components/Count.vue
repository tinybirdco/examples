<template>
  <div class="mt-6">
    <div class="title">
      <div class="Loader" style="width: 12px; height: 12px" v-if="loading">
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
      </div>
      <h2 class="as-font--medium as-color--tuna mb-1">
        {{title}}
      </h2>
      <number
        class="as-font--huge as-color--secondary"
        ref="number"
        :to="amount"
        :format="theFormat"
        :duration="0.5"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'List',
  props: ['pipe', 'title', 'keys'],
  data: function (){
    return {
      loading: true,
      amount: 0
    }
  },
  methods: {
    theFormat(number) {
      return number.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
    },
    fetchData () {
      this.loading = true
      this.tinyb.pipe(this.pipe).json().then(r => {
        if (!r.error) {
          this.amount = r.data[0].round
          setTimeout(this.fetchData, 5000)
        } else {
          this.amount = 0
        }

        this.$refs.number.play()
        this.loading = false
      })
    }
  },
  mounted() {
    this.tinyb = window.tinybird(process.env.VUE_APP_TOKEN || '')
    this.fetchData()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title {
  position: relative;
}
.title .Loader {
  position: absolute;
  top: 9px;
  left: -35px;
}
</style>