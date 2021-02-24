<template>
  <div id="app">
    <aside>
      <div>
        <h1>
          <a href="https://tinybird.co">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" viewBox="0 0 40 40" fill="none">
              <path fill="#25283D" d="M40 3.425L27.513 0l-4.394 9.818L40 3.425zM28.257 27.528l-11.38-4.619L9.907 40l18.349-12.472z" opacity=".6"/>
              <path fill="#25283D" d="M0 17.594l28.059 10.042L32.66 6.182 0 17.594z"/>
            </svg>
          </a>
        </h1>
        <p class="as-font--small as-color--secondary mt-3">
          This sample application shows top github users and repositories for each type of event and based on +50M rows, all by making use of the <a href="https://docs.tinybird.co/api-reference/datasource-api.html" class="Link underline as-color--main">Tinybird API</a> and with no backend involved.
        </p>
        <p class="as-font--caption as-color--secondary mt-1">Last query was performed in {{time}}ms**</p>
      </div>
      <div>
        <div class="as-font--caption as-color--tuna">
          <p>Take a look at the <a href="https://www.gharchive.org/" class="Link underline as-color--tuna">original datasets</a></p>
          <p class="mt-1">**No intermediate caches involved</p>
        </div>
        <div style="display: inline-block">
          <a href="https://blog.tinybird.co/2020/03/11/create-analytic-static-applications" class="Button as-bkg--secondary mt-2">
            <span class="as-font--caption-bold as-color--light">LEARN MORE</span>
          </a>
        </div>
      </div>
    </aside>
    <main>
      <h2 class="as-font--huge as-color--secondary">
        {{event_count}}
      </h2>
      <List title="Top 10 rank for agents" pipe="dataflow__top_agents" :keys="['position', 'agent', 'total']"></List>
      <List title="Top 10 rank for clients" pipe="dataflow__top_clients" :keys="['company_country', 'company_name', 'total']"></List>
      <List title="Top 10 rank for recipients" pipe="dataflow__top_recipients" :keys="['country', 'recipient_code', 'total']"></List>
      <Chart title="Evolution of payments" pipe="dataflow__payments_status__v1"></Chart>
    </main>
  </div>
</template>

<script>
import List from './components/List.vue'
import Chart from "./components/Chart";

export default {
  name: 'app',
  components: {
    List,
    Chart
  },
  data: function() {
    return {
      selected: '',
      options: [],
      top_users: [],
      top_repos: [],
      time: 0,
      loading: true,
      event_count: 0
    }
  }
}
</script>

<style>
#app {
  display: flex;
  height: 100vh;
}
aside {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 336px;
  min-width: 336px;
  height: 100vh;
  padding: 40px;
  box-sizing: border-box;
}
main {
  width: 100%;
  padding: 84px 130px;
  overflow: auto;
  box-sizing: border-box;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.02) 0%, rgba(0, 0, 0, 0.02) 100%);
}
h2 {
  margin: 0;
}
ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
li {
  position: relative;
  width: 320px;
  padding: 0;
  border-bottom: 1px solid #E0E1E4;
}
li:last-child { border: none }

@media only screen and (max-width: 780px) {
  #app {
    position: relative;
    height: 100vh;
    flex-direction: column;
    overflow: auto;
    background: linear-gradient(to right, rgba(0, 0, 0, 0.02) 0%, rgba(0, 0, 0, 0.02) 100%);
  }
  aside {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width: 100%;
    max-width: 380px;
    height: auto;
    padding: 20px;
    background: none;
  }
  main {
    width: 100%;
    padding: 20px;
    overflow: initial;
    box-sizing: border-box;
    background: none;
  }
  h2 {
    padding-bottom: 8px;
  }
}
</style>