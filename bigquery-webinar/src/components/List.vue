<template>
  <div class="mt-6">
    <div class="title">
      <div class="Loader" style="width: 12px; height: 12px" v-if="loading">
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
        <div style="border-color: var(--tuna-color) transparent transparent transparent; border-width: 1px"></div>
      </div>
      <h2 class="as-font--medium as-color--tuna pb-1">
        {{title}}
      </h2>
    </div>
    <ul>
      <li v-for="(item, i) in items.slice(0, 10)" :key="item[keys[1]]">
        <span class="item-number as-font--small">#{{i + 1}}</span>
        <div class="flex-between-center overflow">
          <span class="overflow as-font--small" v-bind:title="item[keys[1]]">{{item[keys[1]]}}</span>
          <span class="overflow as-font--small" v-bind:title="item[keys[1]]">{{item[keys[2]] | formatNumber}}</span>
        </div>
      </li>
    </ul>
    <div v-if="!items.length">
      <p class="as-font--small as-color--tuna">No data available</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'List',
  props: ['pipe', 'title', 'keys'],
  data: function (){
    return {
      polling: null,
      loading: true,
      items: []
    }
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
          this.items = r.data
        } else {
          this.items = []
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
.item {
  position: relative;
  display: flex;
  align-items: center;
  height: 48px;
  color: #000;
  text-decoration: none;
}
.item-number {
  position: absolute;
  left: -20px;
  top: 50%;
  transform: translateY(-50%) translateX(-16px);
  color: #D1D1D6;
  cursor: default;
}
</style>