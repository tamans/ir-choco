<template>
  <div class="home">
    <div class="logo-container">
      <router-link to="/" class="link">
        <img class="choco" src="@/assets/choco.png" alt="choco" />
      </router-link>
    </div>
    <Bar  style="margin-top: -60px;"/>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useRouter } from "vue-router";
import Bar from "@/components/Bar.vue";


export default defineComponent({
  name: "SearchView",
  components: {
    Bar,
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

body {
  margin: 0;
  padding: 0;
}

.home {
  width: 100%;
  height: 130vh; 
  background-image: linear-gradient(#ffdbd1, #fa9ebc);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.choco {
  width: 50.5vh;
  height: 40.5vh;
  transform: rotate(-45deg);
  margin-top: 0.5vh;
  margin-bottom: 20vh;
}



</style>