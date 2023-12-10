<template>
 <div class="columns">
      <div class="results-column">
        <ul class="results">
          <li>
            <div class="result-box">
              <router-link to="/" class="link">Result 1</router-link>
            </div>
          </li>
          <li>
            <div class="result-box">
              <router-link to="/" class="link">Result 2</router-link>
            </div>
          </li>
        </ul>
      </div>
      <div class="rec-column"></div>
    </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ResView",
 
});
</script>

<style scoped>
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

.link {
  color: #3e043e;
  justify-content: space-between;
  text-decoration: none;
  margin-left: 3vh;
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

/* Menu {
  list-style: none;
  display: flex;
  margin-left: auto;
  padding-bottom: 20vh;
} */

.columns {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding-top: 0.5vh;
}

.rec-column {
  flex: 1;
  height: 100vh;
  width: 50vh;
  margin-bottom: 5vh;
  background-color: rgba(255, 255, 255, 0.2);
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 10px;
  padding-top: 30vh;
}

.results {
  padding-left: 5vh;
  padding-right: 3vh;
}

.result-box {
  height: 20vh;
  width: 90vh;
  margin-bottom: 5vh;
  background-color: rgba(255, 255, 255, 0.2);
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 10px;
}

.result-box li {
  text-decoration: none;
}

.results-column {
  flex: 1;
  flex-direction: row;
}

.details-column {
  flex: 2;
}
</style>
