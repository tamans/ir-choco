<template>
  <div id="app">
    <div class="topnav">
      <div class="logo-container">
        <router-link to="/" class="link">
          <img class="home" src="@/assets/choco.png" alt="choco" />
        </router-link>
      </div>
      <div class="search-container">
        <div class="search-bar" id="form">
          <input
            type="search"
            id="query"
            name="q"
            v-model="query"
            placeholder="Search..."
            aria-label="Search through site content"
          />
          <button type="submit" @click="fetchData">
            <i class="fa fa-search" style="font-size: 18px"> </i>
          </button>
        </div>
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

  data() {
    return {
      query,
    }
  },

  methods: {

    async fetchData() {
      try {
        console.log("Here")
        console.log("Query:", this.query);
        const search = await this.$store.dispatch("fetchChoco", this.query);
        this.chocolates = search;
        console.log("chocolates", this.chocolates);
        console.log("what is happening");
      } catch (error) {
        console.error("Error loading chocolates:", error);
      }
    },

    // async fetchData() {
    //   console.log("Here")
    //   console.log("Query:", this.query);

    //   try {
    //     await this.$store.dispatch("fetchChoco", query);
    //     console.log("here");
    //     const chocolates = this.$store.getters.getChocolate;
    //     console.log("Chocolates:", chocolates);

    //     // await this.$store.dispatch('fetchRecs', this.array);
    //     // const recs = this.$store.getters.getRecs;
    //     // console.log('Recs:', recs);
    //   } catch (error) {
    //     console.error("Error fetching data:", error);
    //   }
    // },
  },

  mounted() {
    console.log("mounting???");
    this.fetchData();
    console.log("mounted");
  },
});
</script>

<style scoped>
div {
  font-family: "Lucida Console", Courier, monospace;
}

body, html {
  margin: 0;
  padding: 0;
  overflow: hidden; /* Disable scroll */
  background-image: linear-gradient(rgba(230, 182, 229, 0.9), rgba(234, 127, 228, 0.9));
  background-position: center;
  background-size: cover;
}

.topnav {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 3vh;
}

.search-container{
  width: 100%;
  min-height: 100vh;
  padding: 5%;
  background-image: linear-gradient(rgba(230, 182, 229, 0.9), rgba(234, 127, 228, 0.9));
  background-position: center;
  background-size: cover;
}

form {
  display: flex;
  align-items: center;
}

form{

  width: 50vh;
  height: 5vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  border: 1px solid #fa9ebc;
  background-color: #ffdbd1;
}

input {
  width: 50vh;
  height: 5vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  background-color: #ffdbd1;
  border: 1px solid transparent;
  color: #fa9ebc;
}

form:focus {
  background-color: #fa9ebc;
  color: #ffdbd1;
}

.home {
  width: 50.5vh;
  height: 40.5vh;
  transform: rotate(-45deg);
  padding: 0vh;
}

button{
  background-color: #ffdbd1;
  border: 1px solid transparent;
}

</style>