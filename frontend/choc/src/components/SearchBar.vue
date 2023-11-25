<template>
  <div class="topnav">
    <div class="search-container">
      <input type="text" placeholder="Search.." class="search-bar"/>
      <a href="#">
        <i class="fas fa-search"></i>
      </a>
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
* {
  margin: 0;
  padding: 0;
}

.topnav {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center;
  height: 100vh; /* Set height to full viewport height */
}

.search-container {
  display: flex;
  align-items: center;
}

.search-bar {
  width: 50vh; 
  height: 5vh; /* Adjust height as needed */
  border-radius: 15px; 
  padding: 5px 10px; 
  font-size: 16px; 
  border: 1px solid #ccc; 
}
</style>
