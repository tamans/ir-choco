<template>
  <div id="app">
    <div class="topnav">
      <div class="logo-container">
        <router-link to="/" class="link">
          <img class="home" src="@/assets/choco.png" alt="choco" />
        </router-link>
      </div>
      <div class="search-container">
        <form role="search" class= "search-bar" id="form">
        <input type="search" id="query" name="q" placeholder="Search..." aria-label="Search through site content">
          <button>
            <img src="@/assets/icons8-search.gif" alt="search">
          </button>
          </form>
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

  mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    console.log('Query:', query);

    fetch(`http://127.0.0.1:8000/get-chocolates/?q=${query}`)
    .then(response => response.json())
    .then(data => {
      
      console.log('Backend response:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });

  }
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

form {
  display: flex;
  align-items: center;
}

input {
  width: 50vh;
  height: 5vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  border: 1px solid #fa9ebc;
  background-color: #ffdbd1;
  color: #fa9ebc;
}

input:focus {
  background-color: #fa9ebc;
  color: #ffdbd1;
}

.home {
  width: 50.5vh;
  height: 40.5vh;
  transform: rotate(-45deg);
  padding: 10vh;
}

button {
  all: unset;
  cursor: pointer;
  width: 44px;
  height: 44px;
}
</style>