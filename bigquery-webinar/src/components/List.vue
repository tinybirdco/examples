<template>
  <div class="mt-6">
    <h2 class="as-fontel as-color--tuna pb-1">{{title}}</h2>
    <ul>
      <li v-for="(item, index) in items" :key="item">
        <span class="item-number">#{{index + 1}}</span>
        <a class="item overflow" v-bind:href="'https://github.com/' + item">
          <span v-if="avatar" class="avatar mr-1">
            <img
              class="avatar-image"
              v-bind:src="'https://github.com/' + item + '.png'"
              v-bind:title="item"
              v-bind:alt="item"
              width="24"
              onerror="this.style.display='none'"
            />
          </span>
          <span class="overflow" v-bind:title="item">{{item}}</span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'List',
  props: ['items', 'avatar', 'title']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>