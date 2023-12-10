<template>
  <div class="menu-container">
    <!-- Image on the top left -->
    <div class="image-container">
      <router-link to="/" class="link">
        <img class="choco" src="@/assets/choco.png" alt="choco" />
      </router-link>
    </div>

    <div class="bar-container">
      <Bar />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Bar from "@/components/Bar.vue";

export default defineComponent({
  name: "MenuView",
  components: {
    Bar,
  },
});
</script>

<style scoped>
.menu-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: transparent;
  margin-top: 4vh;
}

.choco {
  width: 20vh;
  height: 15.5vh;
  transform: rotate(-45deg);
  margin-right: 115vh;
}
</style>
