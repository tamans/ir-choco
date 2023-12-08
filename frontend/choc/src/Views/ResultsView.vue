<template>
  <div class="res">
    <!-- <div class="topnav">
      <ul class="menu">
        <li @click="toggleBlock" :class="{ 'menu-open': isBlockVisible }">
          <img class="home" src="@/assets/choco.png" alt="choco" />
        </li>
        <ul class="recs-menu">
          <router-link to="/recs" class="link" style="color:#3e043e">Recommendations</router-link>
        </ul>
      </ul>
    </div> -->
    <Menu />

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
import Menu from "@/components/Menu.vue";


export default defineComponent({
  name: "ResultsView",
  components: {
    Menu,
    },
  setup() {
    const router = useRouter();
    const isBlockVisible = computed(() => router.currentRoute.value.path === "/");

    const toggleBlock = () => {
      isBlockVisible.value = !isBlockVisible.value;
    };

    //const searchQuery = ref("");
   // const searchResults = ref([]);

    const isSearchRoute = computed(
      () => router.currentRoute.value.path === "/"
    );

    const navigateToItemSearch = () => {
      router.push({ name: "ItemSearch" });
    };

    // const peformSearch = () => {
    //   searchResults.value = fetchSearchResults(searchQuery.value);
    // }
    return {
      // searchQuery,
      // searchResults,
      // peformSearch,
      toggleBlock,
      isBlockVisible: false,
      isSearchRoute,
      navigateToItemSearch,
    };
  },
//    methods: {
//     toggleBlock() {
//       this.isBlockVisible = !this.isBlockVisible;
//     },
//   },
});
</script>

<style scoped>

div {
  font-family: "Verdana", Courier, monospace;
}
* {
  margin: 0;
  padding: 0;
}

.res {
  width: 100%;
  height: 100vh; 
  background-image: linear-gradient(#ffdbd1, #fa9ebc);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}


.link {
  color: #3e043e; 
  justify-content: space-between;

  text-decoration: none; 
  margin-left: 3vh;
}

.topnav {
  display: flex;
  justify-content: flex-start; 
  /* align-items: flex-end; */
  padding: 10vh;
  
}

.menu-open ul {
  /* Adjust the styles to make the "Recs" menu appear to the left */
  position: absolute;
  left: -120px; /* Adjust the value based on your layout */
  top: 0;
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
  /* align-items: flex-end; */
  margin-left: auto;
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
    padding-left: 5vh;
    padding-right: 3vh;
    padding-top: 10vh;
}

.result-box{
    height: 20vh;
    width: 90vh;
    margin-bottom: 5vh;
}

.result-box li{
    text-decoration: none;
}


.results-column {
  flex: 1; 
  flex-direction: row;
}

.details-column {
  flex: 2; 
}

.result-box {
  background-color:  rgba(255,255,255,0.2);
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 10px;
}

.home {
  width: 15vh;
  height: 11.5vh;
  transform: rotate(-45deg); 
}
</style>
