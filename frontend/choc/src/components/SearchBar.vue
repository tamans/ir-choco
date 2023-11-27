<template>
  <div id="app">
    <div class="topnav">
      <div class="logo-container">
        <router-link to="/" class="link">
          <img class="home" src="@/assets/choco.png" alt="choco" />
        </router-link>
      </div>
      <div class="search-container">
        <input type="text" placeholder="Search.." class="search-bar" />
        <a href="#">
          <i class="fas fa-search"></i>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "SearchView",
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

.topnav {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo-container {
  margin-bottom: 10px; /* Add margin as needed */
}

.search-container {
  display: flex;
  align-items: center;
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

.home {
  width: 50.5vh;
  height: 40.5vh;
  transform: rotate(-45deg);
  padding: 10vh;
}
</style>
