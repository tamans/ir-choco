import { createStore } from 'vuex'

export default createStore({

    state: {
        chocolate: []
    },

    actions: {
        async fetchChoco({ query: string }) {
            try {
                const response = await fetch(`http://localhost:8000/api/choco/get-choco/${query}/`); 
                this.chocolate = response.data.chocolate;
            } catch (error) {
                console.error('Error fetching chocolates:', error);
                throw error;
            }
        },
    },
});
