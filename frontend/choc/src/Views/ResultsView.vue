<template>
  <div class="res">
    <div class="content">
      <Menu class="menu"/>
      <Res class="results"/>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useRouter } from "vue-router";
import Menu from "@/components/Menu.vue";
import Res from "@/components/Res.vue";


export default defineComponent({
  name: "ResultsView",
  components: {
    Menu,
    Res,
  },
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
    console.log("mounting???");
    console.log("mounted");
  },
});
</script>

<style scoped>
div {
  font-family: "Verdana", Courier, monospace;
}
* {
  margin: 0;
  padding: 0;
  overflow-y: auto;
}

.content{
  margin-bottom: 20vh;
}

.res {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(#ffdbd1, #fa9ebc);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow-y: auto;
}

.menu {
  
  margin-bottom: 10vh;
}
/* .link {
  color: #3e043e;
  justify-content: space-between;
  text-decoration: none;
  margin-left: 3vh;
} */

.search-container {
  display: flex;
  align-items: center;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.home {
  width: 15vh;
  height: 11.5vh;
  transform: rotate(-45deg);
}
</style>
