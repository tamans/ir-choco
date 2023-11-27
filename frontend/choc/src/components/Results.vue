<template>
  <div>
    <div class="topnav">
      <ul class="menu">
        <li>
            <router-link to="/" class="link">
            <img class="home" src="@/assets/choco.png" alt="choco" />
            </router-link>
        </li>
        <li>
          <router-link to="/recs" class="link" style="color:#fa9ebc">Recommendations</router-link>
        </li>
        <li><router-link to="/history" class="link" style="color:#fa9ebc">History</router-link></li>
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

div {
    font-family: "Lucida Console", Courier, monospace;
}
* {
  margin: 0;
  padding: 0;
}



.link {
  color: #6b1f2d; 
  text-decoration: none; 
  margin-left: 3vh;
}

.topnav {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
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
  align-items: flex-end;
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
  height: 5vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  border: 1px solid #fa9ebc;
  background-color: #ffdbd1;
  color: #fa9ebc;
}

.search-bar:focus {
  background-color: #fa9ebc;
  color: #ffdbd1;
}

.results-column {
  flex: 1; 
  flex-direction: row;
}

.details-column {
  flex: 2; 
}

.result-box {
  border: 1px solid #fa9ebc;
  padding: 10px;
  border-radius: 10px;
  background-color: #ffdbd1;
}

.home {
  width: 8vh;
  height: 6vh;
  transform: rotate(-45deg); 
}
</style>
