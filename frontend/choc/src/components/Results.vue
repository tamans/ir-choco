<template>
  <div>
    <div class="topnav">
      <ul class="menu">
        <li><router-link to="/" class="link">Home</router-link></li>
        <li>
          <router-link to="/recs" class="link">Recommendations</router-link>
        </li>
        <li><router-link to="/history" class="link">History</router-link></li>
      </ul>
      <div class="search-container">
        <input type="text" placeholder="Search.." class="search-bar" />
        <a href="#">
          <i class="fas fa-search"></i>
        </a>
      </div>
    </div>

    <div class="results-column">
      <ul class="results">
        <li>
          <div class="result-box">
            <router-link to="/" class="link">Result 1</router-link>
          </div>
        </li>
        <li>
          <div class="result-box">
            <router-link to="/recs" class="link">Result 2</router-link>
          </div>
        </li>
      </ul>
    </div>
    <div class="details-column">
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ResultsView",
  setup() {
    const router = useRouter();
    const isSearchRoute = computed(
      () => router.currentRoute.value.path === "/"
    );

    const navigateToItemSearch = () => {
      router.push({ name: "ItemSearch" });
    };

    return {
      isSearchRoute,
      navigateToItemSearch,
    };
  },
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.topnav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.search-container {
  display: flex;
  align-items: center;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.menu {
  list-style: none;
  display: flex;
}

.menu li {
  margin-left: 15px;
  cursor: pointer;
}

.menu a {
  text-decoration: none; 
  color: black; 
}

.results {
    padding-left: 10vh;
    padding-right: 5vh;
    padding-top: 10vh;
}

.result-box{
    height: 10vh;
    width: 65vh;
    margin-bottom: 5vh;
}

.result-box li{
    text-decoration: none;
}

.search-bar {
  width: 50vh;
  height: 3vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  border: 1px solid #ccc;
}

.results-column {
  flex: 1; 
  flex-direction: row;
}

.details-column {
  flex: 2; 
}

.result-box {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 10px;
  background-color: #f9f9f9;
}
</style>
