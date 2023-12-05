import { createStore } from 'vuex'

export default createStore({
    id: "chocolate",
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
                const response = await fetch(`http://127.0.0.1:8000/api/chocolate/get-choco/${query}/`);
                const data = await response.json();
                commit('SET_CHOCOLATE', data.documents);
            } catch (error) {
                console.error('Error fetching chocolates:', error);
            }
        },
    },

    async fetchRecs({ commit }, array) {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api//chocolate/choco/get-recs/`, {
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
    getters: {
        getChocolate: state => state.chocolate,
        getRecs: state => state.recs,
    },
});

// const store = createStore({
//     state,
//     mutations,
//     actions,
//     getters,
// });

