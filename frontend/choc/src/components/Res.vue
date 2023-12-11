<template>
  <div>
    <div class="but">
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
    <div class="columns">
      <div class="filter-column" v-if="selectedView === 'normal'">
        <div class="price-filter-container">
          <p>Price</p>
          <input
            type="number"
            class="price-input"
            v-model="minPrice"
            step="0.01"
            placeholder="Min Price"
          />
          <input
            type="number"
            class="price-input"
            v-model="maxPrice"
            step="0.01"
            placeholder="Max Price"
          />
          <button @click="filter(minPrice, maxPrice)">Filter</button>
        </div>
        <div class="brand-filter-container">
          <p>Brand</p>
          <button @click="filterBrand('laderach')">Laderach</button>
          <button @click="filterBrand('spruengli')">Sprunli</button>
          <button @click="filterBrand('maxchocolatier')">Max</button>
        </div>
        <div class="choco-filter-container">
          <p>Type</p>
          <button @click="filterByChocolateType('white')">White</button>
          <button @click="filterByChocolateType('dark')">Dark</button>
          <button @click="filterByChocolateType('milk')">Milk</button>
        </div>
      </div>
      <div class="results-column" v-if="selectedView === 'normal'">
        <ul class="results" v-show="selectedView === 'normal'">
          <li v-for="(item, index) in regularResults" :key="index">
            <div class="result-box">
              <h3>
                <a :href="item.site" target="_blank">{{ item.title }}</a>
              </h3>
              <p>Price: {{ item.price }}</p>
              <p>
                Ingredients:
                {{ item.ingredients.split(",").slice(0, 5).join(", ") }}
              </p>
            </div>
          </li>
        </ul>
      </div>
      
      <div class="cluster-results" v-if="selectedView === 'cluster' && Object.keys(clusteredData).length">
          <div  class="results" v-for="(cluster, brand) in clusteredData" :key="brand" >
            <h2>{{ brand }}</h2>
            <ul class="results">
              <li v-for="(item, index) in cluster" :key="index" >
                <div class="clusters-box">
                  <h3>
                    <a :href="item.site" target="_blank">{{ item.title }}</a>
                  </h3>
                  <p>Price: {{ item.price }}</p>
                  <p>
                    Ingredients:
                    {{ item.ingredients.split(",").slice(0, 5).join(", ") }}
                  </p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
// import kmeans from "kmeans-js";

export default defineComponent({
  name: "ResView",
  data() {
    return {
      priceRange: 5,
      minPrice: 3,
      maxPrice: 10,
      brand: "",
      type: "",
      selectedView: "normal",
      regularResults: [],
      clusteredData: {},
      data_filtered: [],
      data: [
        {
          docno: "d1",
          title: "Christmas Pralines assorted 72pcs per box",
          site: "https://laderach.com/ch-en/10008296-pralines-assortiert-weihnachten-72er-packung",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "A selection of 72 beautifully crafted Christmas pralin\u00e9s for an unforgettable indulgence. This box contains a selection of L\u00e4derach pralin\u00e9s and truffles from the classic L\u00e4derach range and several seasonal varieties, all alcohol-free. It's an ideal size to share during a Christmas get-together or any other festive occasion. (800g)",
          ingredients:
            "sugar, cocoa butter, cocoa paste, whole powder, , , glucose, butter ( ), vegetable oils (palm kernel, palm, sunflower, coconut, rapeseed), skimmed powder, humectant (E420, E1103), , , dried coconut flakes, cream ( ), flour, invert sugar syrup, Chopped , , clarified butter ( ), caramel, emulsifier ( lecithin, sunflower lecithin), honey, vegetable fats (sunflower, rapeseed, illipe, shea, palm kernel, palm, coconut), , natural flavour, glucose syrup, fructose, coffee, cocoa beans kernels, maltodextrin, flavouring, natural flavouring substances, dextrose, salt, thickening agent (E414), protein, coating agent (E904), skim , ground cinnamon, anise, cocoa powder, coriander, malt, raising agent (E500), antioxidant (E306), fennel seeds, colouring (E100, E160b(ii)), cloves, Radish juice concentrate, Apple juice concentrate, black currant juice concentrate. milk milk wheat almond soya barley",
          allergens: "May contain egg, other nuts.",
          price: "CHF 10.10",
        },
        {
          docno: "d2",
          title: "FrischSchoggi Star Hazelnut dark",
          site: "https://laderach.com/ch-en/10083900-frischschoggitm-stern-haselnuss-dunkel",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "A L\u00e4derach FrischSchoggi Star makes an ideal gift for Advent. It is made from melt-in-your-mouth dark chocolate, freshly produced by the Swiss chocolatier. Caramelised hazelnuts from Piedmont add a fabulous crunch. (200g)",
          ingredients:
            "33%, sugar, cocoa paste, cocoa butter, vegetable oils (rapeseed), emulsifier ( lecithin, sunflower lecithin), natural flavouring substances. soya",
          allergens: "May contain egg, gluten (incl. wheat), milk, other nuts.",
          price: "CHF 4.10",
        },
        {
          docno: "d3",
          title: "FrischSchoggi Sticks Christmasbox dark mini",
          site: "https://laderach.com/ch-en/frischschoggi-sticks-packung-weihnachten-dunkel-mini",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "We hope your Christmas is as colourful and sweet as this selection of fresh chocolate from L\u00e4derach chocolatier suisse: We combined our most popular FrischSchoggi varieties in an attractive, transparent packaging. Give this surprise to your loved ones, and sweeten their holidays. (95g)",
          ingredients:
            "cocoa paste, sugar, cocoa butter, , , orange juice from concentrate, emulsifier ( lecithin, sunflower lecithin), fructose, lemon juice from concentrate, vegetable oils (rapeseed), blackberry juice, pineapple fibres, gelling agent (E440), natural flavouring substances, flavouring, acidifier (E330), cocoa powder. soya",
          allergens: "May contain egg, gluten (incl. wheat), milk, other nuts.",
          price: "CHF 25.10",
        },
        {
          docno: "d4",
          title: "Pralines Christmas assorted 72 pieces per woodbox",
          site: "https://laderach.com/ch-en/10083911-pralines-weihnachten-72er-holzbox-assortiert",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "This selection of 72 exquisite Christmas pralin\u00e9s created by L\u00e4derach chocolatier suisse is an unforgettable experience during Advent. We\u2019ve combined a selection of alcohol-free pralin\u00e9s and truffles from our classic L\u00e4derach range with several Christmas-themed seasonal varieties. Presented in a wooden box, these pralin\u00e9s are an eye-catcher at any holiday gathering. (800 g)",
          ingredients:
            "sugar, cocoa butter, cocoa paste, , whole powder, glucose, butter ( ), , vegetable oils (palm kernel, palm, sunflower, coconut), humectant (E420), , skimmed powder, , dried coconut flakes, invert sugar syrup, Chopped , , clarified butter ( ), honey, flour, cream ( ), emulsifier ( lecithin, sunflower lecithin), caramel, , fructose, cocoa beans kernels, vegetable fats (sunflower, rapeseed, shea, illipe, palm kernel, palm, coconut), maltodextrin, glucose syrup, natural flavour, dextrose, flavouring, natural flavouring substances, thickening agent (E414), salt, coating agent (E904), protein, cocoa powder, antioxidant (E306), raising agent (E500), malt, colouring (E100). milk almond wheat milk soya barley",
          allergens: "May contain egg, other nuts.",
          price: "CHF 5.10",
        },
        {
          docno: "d5",
          title: "Pralin\u00e9s assorted Stars 5pcs box",
          site: "https://laderach.com/ch-en/10087790-pralines-assortiert-sterne-5er-packung",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "A fine selection of five exquisite Christmas pralin\u00e9s from L\u00e4derach chocolatier suisse. Indulge yourself this Advent season with these star pralin\u00e9s: white chocolate with orange marzipan, milk chocolate with mixed nut gianduja, white chocolate with almond gianduja, milk chocolate with butter foam and honey caramel, and dark chocolate with coconut gianduja, all alcohol-free. (60g)",
          ingredients:
            "sugar, cocoa butter, whole powder, cocoa paste, , dried coconut flakes, skimmed powder, butter ( ), vegetable oils (palm kernel, sunflower, coconut, palm), , , honey, cream ( ), glucose, , emulsifier ( lecithin, sunflower lecithin), humectant (E420), dextrose, caramel, vegetable fats (shea, illipe, palm kernel, palm, coconut), natural flavour, clarified butter ( ), ground cinnamon, thickening agent (E414), anise, natural flavouring substances, coriander, cocoa powder, glucose syrup, fennel seeds, maltodextrin, cloves, colouring (E100, E160b(ii)), Radish juice concentrate, Apple juice concentrate, black currant juice concentrate. milk milk soya",
          allergens: "May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d6",
          title: "FrischSchoggi Pecans-Whisky Caramel milk",
          site: "https://laderach.com/ch-en/frischschoggi-pecannuss-whisky-caramel-milch",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "For this Limited Edition, whiskey-steeped pecans are gently caramelised and covered in Swiss milk chocolate and white chocolate with caramel and processed in our traditional chocolatier craft to the highest quality. Our L\u00e4derach chocolatier suisse FrischSchoggi is available as quarter, half or whole chocolate slabs. To experience the fresh aroma, break and enjoy within two to three weeks.",
          ingredients:
            "sugar, 22%, cocoa butter, whole powder, cocoa paste, , skimmed powder, Whisky 2%, vegetable oils (rapeseed, coconut), glucose syrup, maltodextrin, emulsifier ( lecithin, sunflower lecithin), natural flavour, , butter ( ), thickening agent (E414), natural flavouring substances, cocoa powder. soya milk",
          allergens: "May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d7",
          title: "FrischSchoggi Sticks Box",
          site: "https://laderach.com/ch-en/10095226-frischschoggitm-sticks-box",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "We hope your Christmas is as colourful and sweet as this selection of fresh chocolate from L\u00e4derach chocolatier suisse: We combined our most popular FrischSchoggi varieties in an attractive, transparent packaging. Give this surprise to your loved ones, and sweeten their holidays. (210g)",
          ingredients:
            "sugar, cocoa butter, , whole powder, cocoa paste, , skimmed powder, , , fructose, vegetable oils (rapeseed), blackberry juice, emulsifier ( lecithin, sunflower lecithin), natural flavour, raspberry juice, raspberry puree, acidifier (E330), flavouring, natural flavouring substances, cocoa powder. soya",
          allergens: "May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d8",
          title: "Christmas Pralines 54 pce box",
          site: "https://laderach.com/ch-en/10008030-pralines-assortiert-weihnachten-54er-packung",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "A selectionof 54 beautifully crafted Christmas pralin\u00e9s for an unforgettable indulgence.This box contains a selection of pralin\u00e9s and truffles from the classicL\u00e4derach range and several seasonal varieties, all alcohol-free. It's an idealsize to share during a Christmas get-together. (600g)",
          ingredients:
            "sugar, cocoa butter, cocoa paste, whole powder, , , butter ( ), glucose, vegetable oils (palm kernel, palm, sunflower, coconut, rapeseed), humectant (E420, E1103), skimmed powder, , , cream ( ), honey, invert sugar syrup, , Chopped , dried coconut flakes, clarified butter ( ), caramel, emulsifier ( lecithin, sunflower lecithin), flour, , fructose, natural flavour, coffee, cocoa beans kernels, maltodextrin, vegetable fats (sunflower, rapeseed, shea, illipe, palm kernel, palm, coconut), glucose syrup, dextrose, natural flavouring substances, flavouring, thickening agent (E414), salt, coating agent (E904), ground cinnamon, protein, cocoa powder, anise, coriander, malt, raising agent (E500), antioxidant (E306), colouring (E100), fennel seeds, cloves. milk milk almond soya wheat barley",
          allergens: "May contain egg, other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d9",
          title: "Pralines Star mixed",
          site: "https://laderach.com/ch-en/10097681-pralines-giandujasterne-assortiert",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "This Christmas-inspired mix ensures an unforgettable L\u00e4derach chocolate pleasure during the Advent season. The mix contains pralin\u00e9 stars in the traditional varieties of cinnamon and plum gianduja with white chocolate as well as orange and honey gianduja with milk chocolate. These freshly made treats are a definite wintertime favourite. (200g)",
          ingredients:
            "sugar, cocoa butter, whole powder, , , vegetable fats (palm kernel, coconut, palm), skimmed powder, cocoa paste, , honey, plum juice, humectant (E420), orange juice, caramel, ground cinnamon, natural flavouring substances, emulsifier ( lecithin, sunflower lecithin), natural flavour. soya",
          allergens: "May contain egg, gluten (incl. wheat), other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d10",
          title: "Praline Christmas 144 pce Woodbox",
          site: "https://laderach.com/ch-en/10092929-pralines-assortiert-144er-holzbox-weihnachten",
          img_link: [
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092888_Pralin_s_assortiert_32er_Weihnachts_Holzbox_360g_3_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10092577_10097036_10098654_10005057_10098654_FrischSchoggiSchiffligross-01.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10097585_FrischSchoggi_Sticks_Weihnachten_max_380g_1_1.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/0/10007194_Pralin_s_assortiert_Special_Edition_16er_Packung_2.jpg",
            "https://laderach.com/media/catalog/product/cache/ab58ae1874a621b7b023cbcffac729e3/1/_/1_10100519_FrischSchoggi_Sticks_Packung_Weihnachten_dunkel_max_1_1.jpg",
          ],
          description:
            "This selection of 144 exquisite Christmas pralin\u00e9s created by L\u00e4derach chocolatier suisse is an unforgettable experience during Advent. We\u2019ve combined a selection of alcohol-free pralin\u00e9s and truffles from our classic L\u00e4derach range with several Christmas-themed seasonal varieties. Presented in a wooden box, these pralin\u00e9s are an eye-catcher at any holiday gathering. (1680g)",
          ingredients:
            "sugar, cocoa butter, cocoa paste, whole powder, , , glucose, butter ( ), vegetable oils (palm kernel, palm, sunflower, coconut, rapeseed), skimmed powder, humectant (E420, E1103), , , dried coconut flakes, cream ( ), flour, invert sugar syrup, Chopped , , clarified butter ( ), caramel, emulsifier ( lecithin, sunflower lecithin), honey, vegetable fats (sunflower, rapeseed, shea, illipe, palm kernel, palm, coconut), , natural flavour, glucose syrup, fructose, coffee, cocoa beans kernels, maltodextrin, flavouring, natural flavouring substances, dextrose, salt, thickening agent (E414), protein, coating agent (E904), skim , ground cinnamon, anise, cocoa powder, coriander, raising agent (E500), antioxidant (E306), malt, fennel seeds, colouring (E100, E160b(ii)), cloves, Radish juice concentrate, Apple juice concentrate, black currant juice concentrate. milk milk wheat almond soya barley",
          allergens: "May contain egg, other nuts.",
          price: "CHF 21.10",
        },
        {
          docno: "d664",
          title: 'Teddy bear "Madagascar 68%"',
          site: "https://en.maxchocolatier.com/product/teddybar-madagascar-68",
          img_link:
            "https://assets-global.website-files.com/615c12c88abae398ef9edd6a/631079ffce33ed695f00f8f5_BearMadagascar.png",
          description:
            'Handmade Teddy bear made of "Madagascar 68%" Grand Cru chocolate. We love to look around the world for beautiful antique chocolate molds. We fell in love with this cute teddy bear at first sight. Our chocolatiers cast in from dark and milky Grand Cru chocolate and use their brushes to give him his bear face at the end.',
          ingredients:
            "Cocoa nibs, almonds , sugar, powdered sugar, cocoa butter, whole milk powder, skimmed milk powder , vanilla Madagascar, cream powder , sunflower lecithin \u200d",
          allergens: "",
          price: "13.90",
        },
        {
          docno: "d665",
          title: 'chocolate bar "Bolivia 45%" with apple',
          site: "https://en.maxchocolatier.com/product/tafel-bolivia-45-mit-apfel",
          img_link:
            "https://assets-global.website-files.com/615c12c88abae398ef9edd6a/6482c69475a1f930d2307add_Rio_mandeln.png",
          description:
            "Wild Grand Cru milk chocolate from the province of Beni in Bolivia with apple. Originating from the Bolivian Amazon, this wild cocoa offers an unforgettable and wonderfully long-lasting finish. It features rich and harmonious cocoa notes and a bouquet of lemon, plum and grapefruit aromas.",
          ingredients:
            "sugar, cocoa butter, whole milk powder , fruit crisp blood orange 11% (sugar, blood orange juice, citric acid, flavor natural, beet), sunflower lecithin \u200d",
          allergens: "",
          price: "12.85",
        },

        {
          docno: "d451",
          title: "Praline Rocher milk",
          site: "https://www.spruengli.ch/en/shop/mix-and-match-pralines-truffles/praline-rocher-milk-en.html",
          img_link:
            "https://www.spruengli.ch/components/com_mijoshop/opencart/image/cache/catalog/Artikel2023/16470-590x590.jpg",
          description:
            "Roasted almond slivers, covered with the finest milk chocolate.In the Confiserie Spr\u00fcngli online shop you will find matching gift ideas made from the finest chocolate, classy gift packages, personalisable cakes and birthday presents for your loved ones or business partners.",
          ingredients:
            "Ingredients: Almonds 49%, sugar, cocoa butter , milk powder, cocoa mass, butter fat, emulsifier ( soy lecithin ), Bourbon vanilla. May contain hazel nuts . Storage K\u00fchl und trocken aufbewahren. Material designation Frische Pralin\u00e9s.",
          allergens: "",
          price: "CHF 14.70 per 100g",
        },
        {
          docno: "d452",
          title: "Praline Sp\u00e9ciale",
          site: "https://www.spruengli.ch/en/shop/mix-and-match-pralines-truffles/praline-speciale-en.html",
          img_link:
            "https://www.spruengli.ch/components/com_mijoshop/opencart/image/cache/catalog/Artikel2023/15822-590x590.jpg",
          description:
            "Milk chocolate fresh cream ganache with flaked walnuts, coated in premium milk chocolate and decorated with half a walnut.In the Confiserie Spr\u00fcngli online shop you will find matching gift ideas made from the finest chocolate, classy gift packages, personalisable cakes and birthday presents for your loved ones or business partners.",
          ingredients:
            "Ingredients: Sugar, wal nuts , cocoa butter , cream , cocoa mass, milk powder, humectant (sorbitol), butter fat, emulsifier ( soy lecithin ), Bourbon vanilla. May contain almonds , hazel nuts . Storage K\u00fchl und trocken aufbewahren. Material designation Frische Pralin\u00e9s.",
          allergens: "",
          price: "CHF 14.70 per 100g",
        },
        {
          docno: "d453",
          title: "Praline Mandola",
          site: "https://www.spruengli.ch/en/shop/mix-and-match-pralines-truffles/praline-mandola-en.html",
          img_link:
            "https://www.spruengli.ch/components/com_mijoshop/opencart/image/cache/catalog/Artikel2023/15874-590x590.jpg",
          description:
            "White almond gianduja with almond pieces, covered with white and dark chocolate.In the Confiserie Spr\u00fcngli online shop you will find matching gift ideas made from the finest chocolate, classy gift packages, personalisable cakes and birthday presents for your loved ones or business partners.",
          ingredients:
            "Ingredients: Sugar, almonds , cocoa butter , milk powder, cocoa mass, coconut fat, emulsifier ( soy lecithin ), Bourbon vanilla, vanilla extract, vanillin. May contain hazel nuts . Storage K\u00fchl und trocken aufbewahren. Material designation Frische Pralin\u00e9s.",
          allergens: "",
          price: "CHF 14.70 per 100g",
        },
        {
          docno: "d454",
          title: "Praline Gianduja",
          site: "https://www.spruengli.ch/en/shop/mix-and-match-pralines-truffles/praline-gianduja-en.html",
          img_link:
            "https://www.spruengli.ch/components/com_mijoshop/opencart/image/cache/catalog/Artikel2023/15870-590x590.jpg",
          description:
            "A combination of milk almond gianduja and dark hazelnut gianduja, dipped in smooth dark chocolate.In the Confiserie Spr\u00fcngli online shop you will find matching gift ideas made from the finest chocolate, classy gift packages, personalisable cakes and birthday presents for your loved ones or business partners.",
          ingredients:
            "Ingredients: Sugar, almonds , cocoa butter , hazel nuts , cocoa mass, milk powder, emulsifier ( soy lecithin ), natural flavor, Bourbon vanilla. Storage K\u00fchl und trocken aufbewahren. Material designation Frische Pralin\u00e9s.",
          allergens: "",
          price: "CHF 14.70 per 100g",
        },
      ],
    };
  },
  mounted() {
    this.data_filtered = this.data;
  },
  computed: {
    displayData() {
      let filteredData =
        this.selectedView === "normal" ? this.data : this.flattenClusters();

      if (this.selectedView === "priceFilter") {
        filteredData = this.filterByPrice(
          filteredData,
          this.minPrice,
          this.maxPrice
        );
      }
      console.log(filteredData);
      return filteredData;
    },
  },

  methods: {
    selectView(view) {
      if (view === "cluster") {
        this.filterCLusters(["laderach", "spruengli", "maxchocolatier"]);
      } else {
        this.clusters = [];
      }
      this.selectedView = view;
    },

    //function to filter the results shown based on a max and min price set by the user
    filter(minPrice, maxPrice) {
      console.log(maxPrice);
      this.data_filtered = this.data;
      const filtered_results = this.data_filtered.filter((product) => {
        const productPrice = parseFloat(product.price.replace(/[^\d.]/g, ""));
        return productPrice >= minPrice && productPrice <= maxPrice;
      });

      console.log(filtered_results);
      this.data_filtered = filtered_results;
      this.regularResults = filtered_results;
    },

    filterBrand(selectedBrand) {
      this.data_filtered = this.data;
      let filtered_results;

      filtered_results = this.data_filtered.filter((product) => {
        const url = product.site.toLowerCase();
        switch (selectedBrand.toLowerCase()) {
          case "laderach":
            return url.includes("laderach");
          case "spruengli":
            return url.includes("spruengli");
          case "maxchocolatier":
            return url.includes("maxchocolatier");

          default:
            return true;
        }
      });

      const clusters = {
        laderach: filtered_results.filter((product) =>
          product.site.toLowerCase().includes("laderach")
        ),
        spruengli: filtered_results.filter((product) =>
          product.site.toLowerCase().includes("spruengli")
        ),
        maxchocolatier: filtered_results.filter((product) =>
          product.site.toLowerCase().includes("maxchocolatier")
        ),
      };
      console.log("clusters:", clusters);
      this.clusteredData = clusters;

      console.log(filtered_results);
      this.data_filtered = filtered_results;
      this.regularResults = filtered_results;
    },

    filterCLusters(selectedBrands) {
      this.data_filtered = this.data;
      let filtered_results;

      filtered_results = this.data_filtered.filter((product) => {
        const url = product.site.toLowerCase();
        return selectedBrands.some((brand) =>
          url.includes(brand.toLowerCase())
        );
      });

      const clusters = {};
      selectedBrands.forEach((brand) => {
        clusters[brand.toLowerCase()] = filtered_results.filter((product) =>
          product.site.toLowerCase().includes(brand.toLowerCase())
        );
      });

      console.log("clusters:", clusters);
      this.clusteredData = clusters;

      console.log(filtered_results);
      this.data_filtered = filtered_results;
      this.regularResults = filtered_results;
    },

    filterByChocolateType(chocolateType) {
      this.data_filtered = this.data;
      const filtered_results = this.data_filtered.filter((product) => {
        const description = product.description.toLowerCase();
        switch (chocolateType.toLowerCase()) {
          case "milk":
            return description.includes("milk chocolate");
          case "dark":
            return description.includes("dark chocolate");
          case "white":
            return description.includes("white chocolate");
          case "praline":
            return description.includes("praline");
          default:
            return true;
        }
      });
      this.data_filtered = filtered_results;
      this.regularResults = filtered_results;
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

/* .but {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
} */

.columns {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 0.5vh;
}

.filter-column {
  background-color: rgba(255, 255, 255, 0.2);
  border: 1px solid transparent;
  border-radius: 10px;
  padding: 3vh;
}

/* .results {
  padding-left: 5vh;
  
} */

input {
  width: 6vh;
  height: 2vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  background-color: #ffdbd1;
  border: 1px solid transparent;
  color: #fa9ebc;
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

.clusters-box {
  height: 20vh;
  width: 100vh;
  margin-bottom: 5vh;
  background-color: rgba(255, 255, 255, 0.2);
  border: 1px solid transparent;
  padding: 10px;
  border-radius: 10px;
  position: relative;

  @media (max-width: 768px) {
   
    /* Styles for mobile view */
    flex-direction: column;
    padding: 10px;
    align-items: center;
    
  }

}

.result-box li {
  text-decoration: none;
}

.results-column {
  flex: 1;
  flex-direction: row;
}

.cluster-column {
  flex-wrap: wrap;
  width: 70vh;
}

.details-column {
  flex: 2;
}

button {
  color: white;
  padding: 2vh;
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  border: none;
  border-radius: 3vh;
  cursor: pointer;
  margin: 2vh;
}

.active {
  color: white;
  padding: 2vh;
  background-color: rgb(241, 168, 188);
  color: white;
  border: none;
  border-radius: 3vh;
  cursor: pointer;
  margin: 2vh;
}

.price-filter-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: flex-start;
}

.price-filter-container input {
  width: 6vh;
  height: 3vh;
  margin-left: 2vh;
}

.price-filter-container button {
  margin-right: 2vh;
}

.brand-filter-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: flex-start;
}

.brand-filter-container input {
  margin-right: 2vh;
  margin-left: 2vh;
  width: 10vh;
  height: 3vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  background-color: #ffdbd1;
  border: 1px solid transparent;
  color: #fa9ebc;
}

.brand-filter-container button {
  margin-right: 0.5vh;
  margin-left: 0.5vh;
}

.choco-filter-container button {
  margin-right: 0.5vh;
  margin-left: 1.5vh;
  width: 10vh;
  height: 6vh;
}

.choco-filter-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: flex-start;
}

.choco-filter-container input {
  margin-right: 4vh;
  margin-left: 4vh;
  width: 10vh;
  height: 3vh;
  border-radius: 15px;
  padding: 5px 10px;
  font-size: 16px;
  background-color: #ffdbd1;
  border: 1px solid transparent;
  color: #fa9ebc;
}

.cluster-results {
  display: flex;
  justify-content: space-around;
  list-style-type: none;
  flex-wrap: wrap;
  /* width: 100vh; */
  padding: 0;
}

.cluster {
  text-align: center;
  cursor: pointer;
  margin: 20px;
  transition: transform 0.3s ease-in-out;
}

.cluster:hover {
  transform: scale(1.1);
}
.cluster-box {
  width: 15vh;
  height: 15vh;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  margin: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 8px;
}

.choco-filter-container button .active {
  background-color: rgb(241, 168, 188);
}

h3 {
  color: rgb(207, 118, 142);
}
a{
  text-decoration: none;
  color: rgb(207, 118, 142);
}

p {
  color: rgb(255, 255, 255);
}

@media (max-width: 768px) {
    .container {
      /* Styles for mobile view */
      flex-direction: column;
      padding: 10px;
      align-items: center;
    }
  }
</style>
