import { createStore } from 'vuex'

export default createStore({

    state: {
        chocolate: [],
        recs: [],
    },
    mutations: {
        SET_CHOCOLATE(state, chocolate) {
            state.chocolate = chocolate;
        },
        SET_RECS(state, recs) {
            state.recs = recs;
        }
    },


    actions: {
        async fetchChoco({ commit }, query) {
            try {
                const response = await fetch(`http://localhost:8080/api/choco/get-choco/${query}/`);
                const data = await response.json();
                commit('SET_CHOCOLATE', data.chocolates);
            } catch (error) {
                console.error('Error fetching chocolates:', error);
                throw error;
            }
        },

        async fetchRecs({ commit }, array) {
            try {
                const response = await fetch(`http://localhost:8080/api/choco/get-recs/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ array }),
                });
                const data = await response.json();
                commit('SET_RECS', data.recs); 
            } catch (error) {
                console.error('Error fetching recs:', error);
                throw error;
            }
        },
    },

    getters: {
        getChocolate: state => state.chocolate,
        getRecs: state => state.recs,
    },
});
