<template>
  <div class="search-container">
    <form action= ""  class="search-bar">
      <input
        v-model="searchQuery"
        type="search"
        id="query"
        name="q"
        placeholder="Search..."
        aria-label="Search through site content"
      />
      <button type="submit">
        <i class="fa fa-search" style="font-size: 18px"> </i>
      </button>
    </form>
  </div>
</template>

// role="search"

<script>
import { defineComponent} from "vue";

export default defineComponent({
  name: "SearchView",
  data() {
    return {
      searchQuery: "", // Add a data property to store the search query
    };
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
}

.topnav {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.search-container{
  width: 100%;
  background-position: center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-bar{
    width: 100%;
    max-width: 70vh;
    background: rgba(255,255,255,0.2);
    display: flex;
    align-items: center;
    border-radius: 10vh;
    padding: 2vh 3vh;
}

.search-bar input{
    background: transparent;
    flex: 1;
    border: 0;
    outline: none;
    padding: 0.3vh 0.2vh;
    font-size: 20px;
    color: #fa9ebc;
}

button{
  background-color: transparent;
  border: 1px solid transparent;
}

</style>