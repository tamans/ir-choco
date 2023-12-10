<template>
  <div class="columns">
    <div class="buttons">
      <button
        @click="selectView('cluster')"
        :class="{ active: selectedView === 'cluster' }"
      >
        Cluster
      </button>
      <button
        @click="selectView('normal')"
        :class="{ active: selectedView === 'normal' }"
      >
        Normal
      </button>
    </div>
    <div class="results-column">
      <ul class="results">
        <li v-for="(item, index) in displayData" :key="index">
          <div class="result-box">
            <h3>{{ item.title }}</h3>
            <p>Price: {{ item.price }}</p>
            <p>Ingredients: {{ item.ingredients.split(',').slice(0, 5).join(', ') }}</p>
          </div>
        </li>
      </ul>
    </div>
    <div
      class="rec-column"
      v-if="selectedView === 'cluster' && clusters.length"
    >
      <h3>Clustered Items</h3>
      <!-- Display clustered items here -->
      <ul>
        <li v-for="(cluster, clusterIndex) in clusters" :key="clusterIndex">
          <div
            class="result-box"
            v-for="(item, index) in cluster.items"
            :key="index"
          >
            <h3>{{ item.title }}</h3>
            <p>Price: {{ item.price }}</p>
            <p>Ingredients: {{ item.ingredients }}</p>
          </div>
        </li>
      </ul>
    </div>
    <div class="rec-column">
      <h3>Recommended</h3>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import kmeans from "kmeans-js";

export default defineComponent({
  name: "ResView",
  data() {
    return {
      selectedView: "normal",
      clusters: [],
      data: [
        {
          docno: "d1",
          site: "FrischSchoggi",
          title: "Hazelnut Milk",
          description:
            "This FrischSchoggi made of fine milk chocolate is blended with large roasted and caramelized hazelnuts from Piedmont. This gourmet Swiss chocolate, made by Läderach chocolatier suisse, is produced at the highest quality using our chocolatier’s traditional craftsmanship. To best experience the aroma of the fresh chocolate, break and enjoy within 2-3 weeks.",
          ingredients:
            "31%, sugar, cocoa butter, whole powder, cocoa paste, , skimmed powder, vegetable oils (rapeseed), emulsifier ( lecithin, sunflower lecithin), natural flavour, natural flavouring substances, cocoa powder.",
          allergens: "soya	May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d2",
          site: "FrischSchoggi",
          title: "Sticks Box",
          description:
            "We hope your Christmas is as colourful and sweet as this selection of fresh chocolate from Läderach chocolatier suisse: We combined our most popular FrischSchoggi varieties in an attractive, transparent packaging. Give this surprise to your loved ones, and sweeten their holidays.",
          ingredients:
            "(210g)	sugar, cocoa butter, , whole powder, cocoa paste, , skimmed powder, , , fructose, vegetable oils (rapeseed), blackberry juice, emulsifier ( lecithin, sunflower lecithin), natural flavour, raspberry juice, raspberry puree, acidifier (E330), flavouring, natural flavouring substances, cocoa powder.",
          allergens: "soya	May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d3",
          site: "FrischSchoggi",
          title: "Sticks Christmasbox dark mini",
          description:
            "	We hope your Christmas is as colourful and sweet as this selection of fresh chocolate from Läderach chocolatier suisse: We combined our most popular FrischSchoggi varieties in an attractive, transparent packaging. Give this surprise to your loved ones, and sweeten their holidays.",
          ingredients:
            "(95g)	cocoa paste, sugar, cocoa butter, , , orange juice from concentrate, emulsifier ( lecithin, sunflower lecithin), fructose, lemon juice from concentrate, vegetable oils (rapeseed), blackberry juice, pineapple fibres, gelling agent (E440), natural flavouring substances, flavouring, acidifier (E330), cocoa powder.",
          allergens:
            "soya	May contain egg, gluten (incl. wheat), milk, other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d4",
          site: "FrischSchoggi",
          title: "Sticks Christmasbox mini",
          description:
            "We hope your Christmas is as colourful and sweet as this selection of fresh chocolate from Läderach chocolatier suisse: We combined our most popular FrischSchoggi varieties in an attractive, transparent packaging. Give this surprise to your loved ones, and sweeten their holidays.",
          ingredients:
            "(95g)	sugar, cocoa butter, , whole powder, cocoa paste, , skimmed powder, , , fructose, vegetable oils (rapeseed), blackberry juice, emulsifier ( lecithin, sunflower lecithin), raspberry puree, raspberry juice, natural flavour, acidifier (E330), flavouring, natural flavouring substances, cocoa powder.",
          allergens: "soya	May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d5",
          site: "Christmas",
          title: "Pralines assorted 72pcs per box",
          description:
            "A selection of 72 beautifully crafted Christmas pralinés for an unforgettable indulgence. This box contains a selection of Läderach pralinés and truffles from the classic Läderach range and several seasonal varieties, all alcohol-free. It's an ideal size to share during a Christmas get-together or any other festive occasion.",
          ingredients:
            "(800g)	sugar, cocoa butter, cocoa paste, whole powder, , , glucose, butter ( ), vegetable oils (palm kernel, palm, sunflower, coconut, rapeseed), skimmed powder, humectant (E420, E1103), , , dried coconut flakes, cream ( ), flour, invert sugar syrup, Chopped , , clarified butter ( ), caramel, emulsifier ( lecithin, sunflower lecithin), honey, vegetable fats (sunflower, rapeseed, illipe, shea, palm kernel, palm, coconut), , natural flavour, glucose syrup, fructose, coffee, cocoa beans kernels, maltodextrin, flavouring, natural flavouring substances, dextrose, salt, thickening agent (E414), protein, coating agent (E904), skim , ground cinnamon, anise, cocoa powder, coriander, antioxidant (E306), raising agent (E500), malt, fennel seeds, colouring (E100, E160b(ii)), cloves, Radish juice concentrate, Apple juice concentrate, black currant juice concentrate.",
          allergens:
            "milk milk wheat almond soya barley	May contain egg, other nuts",
          price: "CHF 21.10",
        },

        {
          docno: "d6",
          site: "FrischSchoggi ",
          title: "Sticks Christmasbox max",
          description:
            "We hope your Christmas is as colourful and sweet as this selection of fresh chocolate from Läderach chocolatier suisse: We combined our most popular FrischSchoggi varieties in an attractive, transparent packaging. Give this surprise to your loved ones, and sweeten their holidays.",
          ingredients:
            "(380g)	sugar, cocoa butter, , whole powder, cocoa paste, , skimmed powder, , , fructose, vegetable oils (rapeseed), blackberry juice, emulsifier ( lecithin, sunflower lecithin), natural flavour, raspberry juice, raspberry puree, acidifier (E330), flavouring, natural flavouring substances, cocoa powder.",
          allergens: "soya	May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d7",
          site: "Pralines",
          title: "Christmas assorted 72 pieces per woodbox",
          description:
            "This selection of 72 exquisite Christmas pralinés created by Läderach chocolatier suisse is an unforgettable experience during Advent. We’ve combined a selection of alcohol-free pralinés and truffles from our classic Läderach range with several Christmas-themed seasonal varieties. Presented in a wooden box, these pralinés are an eye-catcher at any holiday gathering.",
          ingredients:
            "(800 g)	sugar, cocoa butter, cocoa paste, , whole powder, glucose, butter ( ), , vegetable oils (palm kernel, palm, sunflower, coconut), humectant (E420), , skimmed powder, , dried coconut flakes, invert sugar syrup, Chopped , , clarified butter ( ), honey, flour, cream ( ), emulsifier ( lecithin, sunflower lecithin), caramel, , fructose, cocoa beans kernels, vegetable fats (sunflower, rapeseed, shea, illipe, palm kernel, palm, coconut), maltodextrin, glucose syrup, natural flavour, dextrose, flavouring, natural flavouring substances, thickening agent (E414), salt, coating agent (E904), protein, cocoa powder, malt, raising agent (E500), antioxidant (E306), colouring (E100).",
          allergens:
            "milk almond wheat milk soya barley	May contain egg, other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d8",
          site: "Pralines",
          title: "Pralines assorted 32 pieces Christmas Woodbox",
          description:
            "A selection of 32 beautiful Christmas pralinés for an unforgettable experience during the Advent season. Carefully packaged in a luxurious wooden box, a variety of alcohol-free Christmas pralinés and classic favourites await discovery. Ideal for gifting among friends and family.",
          ingredients:
            "(360g)	sugar, cocoa butter, cocoa paste, , whole powder, vegetable oils (palm kernel, palm, sunflower, coconut, rapeseed), glucose, butter ( ), , , skimmed powder, humectant (E420), cream ( ), dried coconut flakes, honey, caramel, flour, Chopped , , emulsifier ( lecithin, sunflower lecithin), invert sugar syrup, cocoa beans kernels, vegetable fats (sunflower, rapeseed, shea, illipe), natural flavour, glucose syrup, clarified butter ( ), dextrose, flavouring, natural flavouring substances, salt (fleur de sel), coating agent (E904), salt, protein, thickening agent (E414), malt, raising agent (E500), antioxidant (E306), ground vanilla, colouring (E100).",
          allergens:
            "milk milk wheat almond soya barley	May contain egg, other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d9",
          site: "laderach",
          title: "Advent Calendar Dark Chocolat Sujet 2023",
          description:
            "Let the Läderach table calendar help you get into the Christmas spirit! Our Advent calendar contains 24 alcohol-free Christmas pralines. There is something for every chocolate-lover from milk chocolate with gianduja, white chocolate with orange marzipan to Grand Cru dark chocolate with gold decorations.",
          ingredients:
            "(295g)	sugar, cocoa paste, cocoa butter, glucose, butter ( ), humectant (E420), , cream ( ), vegetable oils (palm kernel, sunflower, palm, coconut), , dried coconut flakes, , clarified butter ( ), whole powder, honey, emulsifier ( lecithin, sunflower lecithin), yuzu purée, passion fruit juice, skimmed powder, , fructose, cocoa beans kernels, invert sugar syrup, caramel, natural flavouring substances, vegetable fats (illipe, shea), salt (fleur de sel), glucose syrup, malt, cocoa powder, spirulinaextract, natural flavour, ground vanilla, colouring (E100), thickening agent (E414).",
          allergens: "milk milk soya barley	May contain egg, other nuts.",
          price: "CHF 21.10",
        },

        {
          docno: "d10",
          site: "",
          title: "Praline Christmas 144 pce Woodbox",
          description:
            "This selection of 144 exquisite Christmas pralinés created by Läderach chocolatier suisse is an unforgettable experience during Advent. We’ve combined a selection of alcohol-free pralinés and truffles from our classic Läderach range with several Christmas-themed seasonal varieties. Presented in a wooden box, these pralinés are an eye-catcher at any holiday gathering.",
          ingredients:
            "(1680g)	sugar, cocoa butter, cocoa paste, whole powder, , , glucose, butter ( ), vegetable oils (palm kernel, palm, sunflower, coconut, rapeseed), skimmed powder, humectant (E420, E1103), , , dried coconut flakes, cream ( ), flour, invert sugar syrup, Chopped , , clarified butter ( ), caramel, emulsifier ( lecithin, sunflower lecithin), honey, vegetable fats (sunflower, rapeseed, shea, illipe, palm kernel, palm, coconut), , natural flavour, glucose syrup, fructose, coffee, cocoa beans kernels, maltodextrin, flavouring, natural flavouring substances, dextrose, salt, thickening agent (E414), protein, coating agent (E904), skim , ground cinnamon, anise, cocoa powder, coriander, raising agent (E500), antioxidant (E306), malt, fennel seeds, colouring (E100, E160b(ii)), cloves, Radish juice concentrate, black currant juice concentrate, Apple juice concentrate.",
          allergens:
            "milk milk wheat almond soya barley	May contain egg, other nuts.",
          price: "CHF 21.10",
        },
      ],
    };
  },
  computed: {
    displayData() {
      return this.selectedView === "normal"
        ? this.data
        : this.flattenClusters();
    },
  },

  methods: {
    selectView(view) {
      if (view === "cluster") {
        this.clusterData();
      } else {
        this.clusters = [];
      }
      this.selectedView = view;
    },

    clusterData() {
      // Extract ingredients from the data
      const ingredientsData = this.data.map((item) => item.ingredients);

      // Convert ingredients data to a format suitable for k-means
      const vectorizedData = ingredientsData.map((ingredients) =>
        ingredients
          .split(",")
          .map((ingredient) => {
            const numericValue = parseFloat(ingredient.trim());
            return isNaN(numericValue) ? 0 : numericValue;
          })
      );
      console.log("Vectorized Data:", vectorizedData);


      // try {
        // Use kmeans-js to cluster the data
        const { clusters } = kmeans(vectorizedData, 3); // You can adjust the number of clusters

        // Assign clusters to the original data
        this.clusters = clusters.map((cluster, index) => ({
          clusterIndex: index,
          items: this.data.filter((_, i) => cluster[i] === 1),
        }));
      // } catch (error) {
      //   console.error("Error during clustering:", error);
      //   // Handle the error as needed
      // }
    },

    flattenClusters() {
      // Flatten clusters to a single array for display
      return this.clusters.reduce(
        (result, cluster) => [...result, ...cluster.items],
        []
      );
    },
  },
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

.buttons {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

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

button {
  color: white;
  writing-mode: vertical-lr;
  text-orientation: mixed;
  padding: 3vh;
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  border: none;
  border-radius: 3vh;
  cursor: pointer;
  margin: 2vh;
}

.active {
  color: white;
  writing-mode: vertical-lr;
  text-orientation: mixed;
  padding: 3vh;
  background-color: rgb(241, 168, 188);
  color: white;
  border: none;
  border-radius: 3vh;
  cursor: pointer;
  margin: 2vh;
}

h3 {
  color: rgb(207, 118, 142);
}

p {
  color: rgb(255, 255, 255);
}
</style>
